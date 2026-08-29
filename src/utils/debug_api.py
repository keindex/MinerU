import requests
import json

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
 'cookie':'captcha_session_v2=2|1:0|10:1786556545|18:captcha_session_v2|88:clo4NkYrbDcyL3UyUTh2eDM0Y2t1eDQ0b0hQL1diWkIycjJRU1RjWDV1ZXhUZmg2RllSNVNjM3lpVlQzN0pkTQ==|87cbc214a4b985ec1e502850142138895d35b47ce4b9b0fe9c2b4845e3254263; _zap=029ea90a-ebe6-43fb-903b-c644b08b9914; d_c0=BvNXVdC4vxyPTlM_l0RTnvop14BLqRzv15w=|1786682578; q_c1=50e987aacced4cd29d23bf42476df39c|1786959087000|1786959087000; __zse_ck=005_nCZDa6jv=XccCHDtKsrBwEufbZF5Kh=WN6S0zS5ovKikyh5yQD7Dh7BrpyV=ZX2ehAUf5tFlFt9m4qQ9j7rZc2R62lvDJ52elhWFzR/K=e=29hx=VZpYReyhP0A=RDHb-RX468gg1WIru48ydzm9fkfC1/Tr5qjHD96YnLR6Ha4V335GtHfEtG4LW3euN4Xnpo//2qwejAAY52C299nB4J9yfBEc+SdlDvtf8iPE1+Z05s2JzulynPXy/480jnQoZ; z_c0=2|1:0|10:1787106696|4:z_c0|92:Mi4xcEtMU05RQUFBQUFVbEJPYnN2LTdHaVlBQUFCZ0FsVk5tdjVwYXdBTV9ad0xzV2RXeDBkZ1FpeHZvSktFTkp6a1d3|1c97129304c886576cb72cf9151adca2fc2785524f5aa8668ca506fb019a03ef; _xsrf=3700036d-9a74-469f-9a68-f4a8ab58e02c; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1786959090,1787037010,1787106679,1787200752; HMACCOUNT=F4A2E54A8E7E8BA6; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1787207651; BEC=6bca8f185b99e85d761c7a0d8d692864'}

response = requests.get('https://www.zhihu.com/api/v3/moments/yjk-59-34/activities?limit=5&desktop=true&ws_qiangzhisafe=0', headers=headers)
data = response.json()
print(json.dumps(data, ensure_ascii=False, indent=2))