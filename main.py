'''
定时自定义
2 8,12,19 * * * main.py
new Env('微信读书时长');
'''# 
#  微信读书
#  
     
import random
import requests
import json
import time
import hashlib
import urllib.parse
import pprint

# 如果登录过期，更新下面的cookies和heads部分即可
cookies = {
    'pgv_pvid': '5940625535',
    'ptcz': '1e0f97fd22d3d1e3f650330bddd5b24faf5b89dd151bc6f19fd3adfe3aa2113a',
    'iip': '0',
    'o_cookie': '47710',
    'fqm_pvqid': 'ac8effec-4a17-40b1-8c02-2a2daa50d869',
    '_qimei_q36': '',
    'logTrackKey': 'fd9872e902d84550b7fbabbcc0f51fcb',
    'pac_uid': '0_i0c18kshYiepD',
    '_qimei_fingerprint': '5b899aa6b1cfec6e2cb676b662dc0603',
    '_clck': '8umwyt|1|fpf|0',
    'suid': 'user_0_i0c18kshYiepD',
    '_qimei_h38': 'fded99030d59215a937aea4d02000004d1791a',
    'wr_vid': '281755137',
    'wr_rt': 'web%40cnNC6deyOvH2CBhwQyz_AL',
    'wr_localvid': '4d832b60810cb3e014d8cdd',
    'wr_name': '%E9%A9%AC%E5%86%9B',
    'wr_gender': '1',
    'wr_avatar': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FPiajxSqBRaEIicG7grpicolv3saJO36e36r9UNU7WrBR3Xw4pTbFwfY9moHGGnRuFibp43Bicv6p81ZfFe1LSkbqj7ib1VKH5icC6cyVD9iaoFUBSweBEO6La9hcAA%2F132',
    'wr_pf': 'NaN',
    'qq_domain_video_guid_verify': 'be15878d6d10c167',
    'RK': 'vJl0RuyjHf',
    'wr_skey': '1pRTGWfb',
    'wr_gid': '209791202',
    'wr_fp': '2007578777',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'baggage': 'sentry-environment=production,sentry-release=dev-1730698697208,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=54851df4c8ad468ab96e7aa79d4f9717',
    'cache-control': 'no-cache',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'pgv_pvid=5940625535; ptcz=1e0f97fd22d3d1e3f650330bddd5b24faf5b89dd151bc6f19fd3adfe3aa2113a; iip=0; o_cookie=47710; fqm_pvqid=ac8effec-4a17-40b1-8c02-2a2daa50d869; _qimei_q36=; logTrackKey=fd9872e902d84550b7fbabbcc0f51fcb; pac_uid=0_i0c18kshYiepD; _qimei_fingerprint=5b899aa6b1cfec6e2cb676b662dc0603; _clck=8umwyt|1|fpf|0; suid=user_0_i0c18kshYiepD; _qimei_h38=fded99030d59215a937aea4d02000004d1791a; wr_vid=281755137; wr_rt=web%40cnNC6deyOvH2CBhwQyz_AL; wr_localvid=4d832b60810cb3e014d8cdd; wr_name=%E9%A9%AC%E5%86%9B; wr_gender=1; wr_avatar=https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FPiajxSqBRaEIicG7grpicolv3saJO36e36r9UNU7WrBR3Xw4pTbFwfY9moHGGnRuFibp43Bicv6p81ZfFe1LSkbqj7ib1VKH5icC6cyVD9iaoFUBSweBEO6La9hcAA%2F132; wr_pf=NaN; qq_domain_video_guid_verify=be15878d6d10c167; RK=vJl0RuyjHf; wr_skey=1pRTGWfb; wr_gid=209791202; wr_fp=2007578777',
    'dnt': '1',
    'origin': 'https://weread.qq.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://weread.qq.com/web/reader/037427a3643425f447132334e6d334b6532764136716d36703436387233554331a',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '54851df4c8ad468ab96e7aa79d4f9717-9b1ac3d06f4512dd',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

# 这是读的书籍信息，挑一本你读过的书
data = {
    'appId': 'wb182564874663h1736463455',
    'b': '037427a3643425f447132334e6d334b6532764136716d36703436387233554331a',
    'c': '6f4322302126f4922f45dec',
    'ci': 18,
    'co': 362,
    'sm': '火车伊要开往叨位「火车它要开到哪里」我生',
    'pr': 100,
    'rt': 22,
    'ts': 1730159166185,
    'rn': 966,
    'sg': '357f4c0875562b4d77ebdb99219e3e3aaa1fc8ed249f191d18eb622a00eb1cae',
    'ct': 1730159166,
    'ps': '77f32f907a500369g016d66',
    'pc': 'a96326707a500369g0187b4',
    's': '9c263c22',
}

def get_wr_skey():
    url = "https://weread.qq.com/web/login/renewal"
    data = {
        "rq": "%2Fweb%2Fbook%2Fread"
    }
    data = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    # print(response.text)
    cookie_str = response.headers['Set-Cookie']
    # print(cookie_str)
    wr_key = ""
    for cookie in cookie_str.split(';'):
        if cookie.__contains__("wr_skey"):
            wr_skey = cookie[-8:]
            print("数据初始化成功！")
            return wr_skey
             
def encode_data(data, keys_to_include=None):
    sorted_keys = sorted(data.keys())
    query_string = ''

    for key in sorted_keys:
        if keys_to_include is None or key in keys_to_include:
            value = data[key]
            encoded_value = urllib.parse.quote(str(value), safe='')
            query_string += f'{key}={encoded_value}&'

    if query_string.endswith('&'):
        query_string = query_string[:-1]

    return query_string


def cal_hash(input_string):
    _7032f5 = 0x15051505
    _cc1055 = _7032f5
    length = len(input_string)
    _19094e = length - 1

    while _19094e > 0:
        _7032f5 = 0x7fffffff & (_7032f5 ^ ord(input_string[_19094e]) << (length - _19094e) % 30)
        _cc1055 = 0x7fffffff & (_cc1055 ^ ord(input_string[_19094e - 1]) << _19094e % 30)
        _19094e -= 2

    return hex(_7032f5 + _cc1055)[2:].lower()


url = "https://weread.qq.com/web/book/read"


# 加密盐
key = "3c5c8717f3daf09iop3423zafeqoi"
num = 1
errnum = 0
t = 0
ss =0

while True:
    # 处理数据
    print(f"-------------------第{num}次，共阅读{ss/60}分钟-------------------")
    data['ct'] = int(time.time())
    data['ts'] = int(time.time() * 1000)
    data['rn'] = random.randint(0, 1000)  # 1000以内的随机整数值
    data['sg'] = hashlib.sha256(("" + str(data['ts']) + str(data['rn']) + key).encode()).hexdigest()
    print(f"sg:{data['sg']}")
    data['s'] = cal_hash(encode_data(data))
    print(f"s:{data['s']}")

    sendData = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=sendData)
    resData = response.json()
    print(response.json())



    if 'succ' in resData:
        print("数据格式正确，阅读进度有效！")
        # 确认无s字段
        num += 1
        t = random.randint(100, 200)
        ss= ss +t
        time.sleep(t)
    else:
        print("数据格式问题,异常退出！")
        cookies['wr_skey'] = get_wr_skey()
        errnum += 1
        num -= 1

    if num == 50:
        print("阅读脚本运行已完成！")
        QLAPI.notify("微信阅读",f"阅读脚本运行已完成！共阅读{ss/60}分钟")
        break
    elif errnum >3:
        print("阅读脚本运行未正常完成！")
        QLAPI.notify("微信阅读",f"阅读脚本运行未正常完成！共阅读{ss/60}分钟")
        
        break    

    data.pop('s')
