#!/usr/bin/env python3
"""
Split a markdown document into sections based on hierarchical header structure.
Handles cases where parent and child sections both use ## (two # marks).
"""

import re
import os

def parse_headers(content):
    """Parse markdown headers and their line numbers."""
    headers = []
    lines = content.split('\n')
    for i, line in enumerate(lines):
        match = re.match(r'^(#{1,3})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            headers.append({
                'line': i,
                'level': level,
                'title': title
            })
    return headers

def is_roman_numeral(title):
    """Check if title starts with a Roman numeral pattern like 'I.', 'II.', 'III.', 'IV.'"""
    # Match only common Roman numerals: I, II, III, IV, V, VI, VII, VIII, IX, X, XI, XII
    pattern = r'^(I{1,3}|IV|V|VI{0,3}|IX|X|XI|XII)\.\s*'
    return bool(re.match(pattern, title))

def get_section_prefix(title):
    """Extract section prefix like 'A.', 'B.', '1.', '2.', 'III.' from title"""
    match = re.match(r'^([IVXLC]+|[A-Z]|\d+)\.\s*(.*)$', title)
    if match:
        prefix = match.group(1)
        rest = match.group(2) if match.group(2) else ""
        return prefix, rest
    return "", title

def sanitize_filename(text):
    """Convert text to a safe filename."""
    text = re.sub(r'[^a-zA-Z0-9\s]', '_', text)
    text = re.sub(r'\s+', '_', text.strip())
    text = re.sub(r'_+', '_', text)
    return text

def should_remove_section(title):
    """Check if section should be removed (acknowledgments, appendix, etc.)"""
    title_lower = title.lower()
    remove_patterns = ['acknowledg', 'appendix', 'pacs']
    for pattern in remove_patterns:
        if pattern in title_lower:
            return True
    return False

def split_document(input_file, output_dir):
    """Split the document into sections."""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    headers = parse_headers(content)
    
    # Build section tree
    # Roman sections (I, II, III, IV) are top-level
    # Letter sections (A, B, C, D) under a Roman section
    # Number sections (1, 2) under a letter section
    
    section_tree = {}  # title -> {content, children, parent}
    
    current_roman = None
    current_letter = None
    
    for i, h in enumerate(headers):
        if h['level'] != 2:
            continue
        
        title = h['title']
        
        if should_remove_section(title):
            continue
        
        # Find end of this section
        end_line = len(lines)
        for j in range(i + 1, len(headers)):
            if headers[j]['level'] == 2:
                end_line = headers[j]['line']
                break
        
        section_content = '\n'.join(lines[h['line']:end_line])
        
        # Clean up PACS numbers from Abstract
        if 'abstract' in title.lower():
            section_content = re.sub(r'PACS numbers:.*$', '', section_content, flags=re.MULTILINE)
        
        prefix, rest = get_section_prefix(title)
        
        # Determine hierarchy level
        if is_roman_numeral(title):
            current_roman = title
            current_letter = None
            section_tree[title] = {
                'content': section_content,
                'children': {},
                'parent': None,
                'prefix': prefix,
                'rest': rest
            }
        elif prefix.isalpha() and prefix.isupper() and len(prefix) == 1:
            # Letter section (A, B, C, D)
            current_letter = prefix
            if current_roman and current_roman in section_tree:
                section_tree[current_roman]['children'][prefix] = {
                    'content': section_content,
                    'title': rest,
                    'parent': current_roman,
                    'prefix': prefix,
                    'rest': rest
                }
        elif prefix.isdigit():
            # Number section (1, 2)
            if current_letter and current_roman and current_roman in section_tree:
                parent_letter = section_tree[current_roman]['children'].get(current_letter, {})
                if 'children' not in parent_letter:
                    section_tree[current_roman]['children'][current_letter]['children'] = {}
                section_tree[current_roman]['children'][current_letter]['children'][prefix] = {
                    'content': section_content,
                    'title': rest,
                    'parent': current_letter,
                    'prefix': prefix,
                    'rest': rest
                }
        else:
            # Non-Roman top-level section like Abstract, etc.
            # Store as a top-level section without parent
            section_tree[title] = {
                'content': section_content,
                'children': {},
                'parent': None,
                'prefix': '',
                'rest': title
            }
    
    # Generate output files
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    os.makedirs(output_dir, exist_ok=True)
    
    created_files = []
    
    def write_file(base_path, content):
        filepath = os.path.join(output_dir, base_path + '.md')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        created_files.append(base_path + '.md')
    
    def make_filename(parts):
        """Build filename from parts, filtering empty strings"""
        return '.'.join(filter(None, parts))
    
    # Write top-level sections and their letter subsections as combined or separate
    for roman_title, roman_data in section_tree.items():
        # Write main roman section with all its content (including subsections)
        # Use rest if available, otherwise use prefix (for cases like III without text after)
        safe_roman = sanitize_filename(roman_data['rest']) if roman_data['rest'] else sanitize_filename(roman_data['prefix'])
        filename = make_filename([base_name, roman_data['prefix'], safe_roman])
        write_file(filename, roman_data['content'])
        
        # Write individual letter subsections
        for letter_prefix, letter_data in roman_data['children'].items():
            safe_rest = sanitize_filename(letter_data['rest']) if letter_data['rest'] else sanitize_filename(letter_data['title'])
            filename = make_filename([base_name, roman_data['prefix'], safe_roman, letter_prefix, safe_rest])
            write_file(filename, letter_data['content'])
            
            # Write number subsections
            # NOTE: We do NOT create separate files for number subsections (1., 2.)
            # They remain as part of their parent letter section content
            if False:  # Disabled - numbers are not split into separate files
                for num_prefix, num_data in letter_data['children'].items():
                    safe_num_rest = sanitize_filename(num_data['rest']) if num_data['rest'] else sanitize_filename(num_data['title'])
                    filename = make_filename([base_name, roman_data['prefix'], safe_roman, letter_prefix, safe_rest, num_prefix, safe_num_rest])
                    write_file(filename, num_data['content'])
    
    return created_files

if __name__ == '__main__':
    input_file = r'c:\Users\admin\MinerU\1405.pdf-4ef2c801-fd49-466a-b93d-fbd00e0be1c7\full.md'
    output_dir = r'c:\Users\admin\MinerU\1405.pdf-4ef2c801-fd49-466a-b93d-fbd00e0be1c7\sections'
    
    files = split_document(input_file, output_dir)
    print(f"Created {len(files)} files:")
    for f in sorted(files):
        print(f"  - {f}")
