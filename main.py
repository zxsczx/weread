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
    'qq_domain_video_guid_verify': '506b2532a6aa5826',
    'o_cookie': '47710',
    'fqm_pvqid': 'ac8effec-4a17-40b1-8c02-2a2daa50d869',
    'eas_sid': '21T6C9U9H8G5J633o2G9P1i211',
    '_qimei_uuid42': '17b16071e0410024f298f5541a884a490cd9a3ae65',
    '_qimei_q36': '',
    'logTrackKey': 'fd9872e902d84550b7fbabbcc0f51fcb',
    'pac_uid': '0_i0c18kshYiepD',
    '_qimei_fingerprint': '5b899aa6b1cfec6e2cb676b662dc0603',
    '_clck': '8umwyt|1|fpf|0',
    'suid': 'user_0_i0c18kshYiepD',
    '_qimei_h38': 'fded99030d59215a937aea4d02000004d1791a',
    'uin': 'o47710',
    '_qpsvr_localtk': '0.6640695549387141',
    'wr_gid': '249875501',
    'wr_vid': '281755137',
    'wr_rt': 'web%40cnNC6deyOvH2CBhwQyz_AL',
    'wr_localvid': '4d832b60810cb3e014d8cdd',
    'wr_name': '%E9%A9%AC%E5%86%9B',
    'wr_gender': '1',
    'wr_fp': '37437988',
    'wr_avatar': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FPiajxSqBRaEIicG7grpicolv3saJO36e36r9UNU7WrBR3Xw4pTbFwfY9moHGGnRuFibp43Bicv6p81ZfFe1LSkbqj7ib1VKH5icC6cyVD9iaoFUBSweBEO6La9hcAA%2F132',
    'wr_pf': 'undefined',
    'wr_skey': '8_qN3Le5',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'pgv_pvid=5940625535; ptcz=1e0f97fd22d3d1e3f650330bddd5b24faf5b89dd151bc6f19fd3adfe3aa2113a; iip=0; qq_domain_video_guid_verify=506b2532a6aa5826; o_cookie=47710; fqm_pvqid=ac8effec-4a17-40b1-8c02-2a2daa50d869; eas_sid=21T6C9U9H8G5J633o2G9P1i211; _qimei_uuid42=17b16071e0410024f298f5541a884a490cd9a3ae65; _qimei_q36=; logTrackKey=fd9872e902d84550b7fbabbcc0f51fcb; pac_uid=0_i0c18kshYiepD; _qimei_fingerprint=5b899aa6b1cfec6e2cb676b662dc0603; _clck=8umwyt|1|fpf|0; suid=user_0_i0c18kshYiepD; _qimei_h38=fded99030d59215a937aea4d02000004d1791a; uin=o47710; _qpsvr_localtk=0.6640695549387141; wr_gid=249875501; wr_vid=281755137; wr_rt=web%40cnNC6deyOvH2CBhwQyz_AL; wr_localvid=4d832b60810cb3e014d8cdd; wr_name=%E9%A9%AC%E5%86%9B; wr_gender=1; wr_fp=37437988; wr_avatar=https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FPiajxSqBRaEIicG7grpicolv3saJO36e36r9UNU7WrBR3Xw4pTbFwfY9moHGGnRuFibp43Bicv6p81ZfFe1LSkbqj7ib1VKH5icC6cyVD9iaoFUBSweBEO6La9hcAA%2F132; wr_pf=undefined; wr_skey=8_qN3Le5',
    'DNT': '1',
    'Origin': 'https://weread.qq.com',
    'Pragma': 'no-cache',
    'Referer': 'https://weread.qq.com/web/reader/609427c3643425f425a36314a4531484244764f36726936744436416b3158691e4kecc32f3013eccbc87e4b62e',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'baggage': 'sentry-environment=production,sentry-release=dev-1729770851188,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=76c3d75d61254263bfbb7bf38e361345',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sentry-trace': '76c3d75d61254263bfbb7bf38e361345-ae7835662d87d403',
}

# 这是读的书籍信息，挑一本你读过的书
data = {
    "appId": "wb182564874663h1736463455",
    "b": "609427c3643425f425a36314a4531484244764f36726936744436416b3158691e4",
    "c": "c81322c012c81e728d9d180",
    "ci": 2,
    "co": 643,
    "sm": "图书在版编目（CIP）数据我与地坛／史铁",
    "pr": 0,
    "rt": 9,
    "ts": 1729840344377,
    "rn": 902,
    "sg": "10a63e47c3a337c129375854161f639d89f50f98999bdfcdd78d72b2807a5cdf",
    "ct": 1729840344,
    "ps": "f8732c107a4f86e1g013d29",
    "pc": "25a324107a4f86e1g014dd4",
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

while True:
    # 处理数据
    print(f"-------------------第{num}次，共阅读{num * 0.5}分钟-------------------")
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
        time.sleep(30)
    else:
        print("数据格式问题,异常退出！")
        cookies['wr_skey'] = get_wr_skey()
        errnum += 1
        num -= 1

    if num == 200:
        print("阅读脚本运行已完成！")
        QLAPI.notify("微信阅读",f"阅读脚本运行已完成！共阅读{num * 0.5}分钟")
        break
    elif errnum >3:
        print("阅读脚本运行未正常完成！")
        QLAPI.notify("微信阅读","阅读脚本运行未正常完成！共阅读{num * 0.5}分钟")
        
        break    

    data.pop('s')
