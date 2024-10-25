# 
#  微信读书
#  
     
import random
import requests
import json
import time
import hashlib
import urllib.parse

from config import headers,cookies
from cookie import get_wr_skey


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
