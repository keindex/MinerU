import requests

headers = {
 'pragma':'no-cache',
 'cache-control':'no-cache',
 'sec-ch-ua-platform':'"Windows"',
 'sec-ch-ua':'"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
 'x-api-version':'3.0.40',
 'x-zse-96':'2.0_7ittm16eYkWdxCAAlQ/TD8xoRgRtvMgbVUuvgucX/BDUa7xwBqFHapDzLH1koFXe',
 'sec-ch-ua-mobile':'?0',
 'x-requested-with':'fetch',
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
 'x-zst-81':'3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZmLY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFHF0quFmobXC28X9HqN_792MWCSm6M3L3JxGTvX9rBH8zqcppBc9sHgMSDrTvRYxTwoMsqYf6Xx0bMt8tq2mRwH9_9xGcGYsZuVfpTSGODU_ICLGPCHmuGCf6Q9MA921oCLy49LmJXSfbutsWrHMfLCyfqxYkBVsNwVLFUxf6i9_CCexOqfzdGYMSACO9qYpSR2qThC_ZbxMJLO8VwOOy9p1NJVZPGe1tuVZ4BoYXhS_hh3YuGoLf_cGEJV1nqe8qBe_GrSVkXOMbXcKkGX1kwL_zbL1eTYYQXXC1QNC',
 'x-zse-93':'101_3_3.0',
 'accept':'*/*',
 'sec-fetch-site':'same-origin',
 'sec-fetch-mode':'cors',
 'sec-fetch-dest':'empty',
 'referer':'https://www.zhihu.com/people/yjk-59-34',
 'accept-encoding':'gzip, deflate, br, zstd',
 'accept-language':'zh-CN,zh;q=0.9',
 'priority':'u=1, i',
 'cookie':'z_c0=2|1:0|10:1788511705|4:z_c0|92:Mi4xcEtMU05RQUFBQUJGeFJrNExyclRIQ1lBQUFCZ0FsVk4yZE9IYXdCdHRJVE1nZFB2SmFmUWNfWUU4VjdPZEQ3N1FR|2600bffb992bdbf5780fd9b143b7c70868a22da84a3727143bf0261f0368a3cb;__zse_ck=005_4vIbXwufkAfY8ETDMKXkyV8YJoi8Ec5G9anErLOg1vA/pt=SWXXnnqWxglFIxhVARpgXlvBJkAElwDbJsPA19LgsETV0RtfxShiGRFt8Wqd2D=BqYW4PEFK1pfwUdg9K-3aPXnKVpYr0DVQtKUzKBTHAx2ZPVLkL04qXbiNE3datF5DRFVCZzXUqsQq1IviMVAaY/Bl5Hytj8u+oxnbOVaZx7Bb/lIHJSdf/HRH97UhhsZ+6R7jSFhISqM3lV/L+p'}
payload=None

response0 = requests.request("GET", "https://www.zhihu.com/api/v3/moments/yjk-59-34/activities?limit=5&desktop=true&ws_qiangzhisafe=0", headers=headers, data=payload)
print(f"Response 0 Status Code: {response0.status_code}")
print(f"Response 0 Text Preview: {response0.text[:200]}...")

headers = {
 'pragma':'no-cache',
 'cache-control':'no-cache',
 'sec-ch-ua-platform':'"Windows"',
 'sec-ch-ua':'"Not=A?Brand";v="99", "Google Chrome";v="151", "Chromium";v="151"',
 'x-api-version':'3.0.40',
 'x-zse-96':'2.0_7ittm16eYkWdxCAAlQ/TD8xoRgRtvMgbVUuvgucX/BDUa7xwBqFHapDzLH1koFXe',
 'sec-ch-ua-mobile':'?0',
 'x-requested-with':'fetch',
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36',
 'x-zst-81':'3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZmLY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFHF0quFmobXC28X9HqN_792MWCSm6M3L3JxGTvX9rBH8zqcppBc9sHgMSDrTvRYxTwoMsqYf6Xx0bMt8tq2mRwH9_9xGcGYsZuVfpTSGODU_ICLGPCHmuGCf6Q9MA921oCLy49LmJXSfbutsWrHMfLCyfqxYkBVsNwVLFUxf6i9_CCexOqfzdGYMSACO9qYpSR2qThC_ZbxMJLO8VwOOy9p1NJVZPGe1tuVZ4BoYXhS_hh3YuGoLf_cGEJV1nqe8qBe_GrSVkXOMbXcKkGX1kwL_zbL1eTYYQXXC1QNC',
 'x-zse-93':'101_3_3.0',
 'accept':'*/*',
 'sec-fetch-site':'same-origin',
 'sec-fetch-mode':'cors',
 'sec-fetch-dest':'empty',
 'referer':'https://www.zhihu.com/people/yjk-59-34',
 'accept-encoding':'gzip, deflate, br, zstd',
 'accept-language':'zh-CN,zh;q=0.9',
 'priority':'u=1, i',
 'cookie':'z_c0=2|1:0|10:1788511705|4:z_c0|92:Mi4xcEtMU05RQUFBQUJGeFJrNExyclRIQ1lBQUFCZ0FsVk4yZE9IYXdCdHRJVE1nZFB2SmFmUWNfWUU4VjdPZEQ3N1FR|2600bffb992bdbf5780fd9b143b7c70868a22da84a3727143bf0261f0368a3cb;__zse_ck=005_4vIbXwufkAfY8ETDMKXkyV8YJoi8Ec5G9anErLOg1vA/pt=SWXXnnqWxglFIxhVARpgXlvBJkAElwDbJsPA19LgsETV0RtfxShiGRFt8Wqd2D=BqYW4PEFK1pfwUdg9K-3aPXnKVpYr0DVQtKUzKBTHAx2ZPVLkL04qXbiNE3datF5DRFVCZzXUqsQq1IviMVAaY/Bl5Hytj8u+oxnbOVaZx7Bb/lIHJSdf/HRH97UhhsZ+6R7jSFhISqM3lV/L+p'}
payload=None

response1 = requests.request("GET", "https://www.zhihu.com/api/v3/moments/yjk-59-34/activities?offset=1787121034418&page_num=1", headers=headers, data=payload)
print(f"Response 1 Status Code: {response1.status_code}")
print(f"Response 1 Text Preview: {response1.text[:200]}...")

