## 本脚本基于“ https://github.com/findmover/wxread ”项目，只是把这个项目修改了一下，可以直接挂在青龙平台下面，首先感谢原作者！

## 序

开发这个脚本主要是为了挑战赛刷时长以及天数，。只需要一次部署，长时间挂机。

## 脚本介绍

针对微信读书阅读挑战赛编写的脚本：

1. 能进行刷阅读时长，且时长默认计入排行榜、挑战赛等。（指定200分钟）
2. 可以在部署青龙平台，每天定时运行脚本并推送。
3. 一次抓包，长时间使用。对于Cookie更新问题给出了自动获取Cookie更新值的解决方案。

## 操作步骤

1、先在青龙面板中拉取任务：
```
ql repo https://github.com/midpoint/weread.git "jd_" "" "cookie|config" "main"
```

2、脚本逻辑还是比较简单的，运行`main.py`即可，依赖自行安装。大部分代码不需要改动。

先自行获取heads和cookies信息，更新config.py中的信息：
在微信阅读官网 [微信读书 (qq.com)](https://weread.qq.com/) 搜索【三体】点开阅读点击下一页进行抓包，抓到`read`接口 `https://weread.qq.com/web/book/read`，如果返回格式正常（如：

```
json复制代码{
  "succ": 1,
  "synckey": 564589834
}
```

右键复制为Curl(Bash)格式，然后到这里 [Convert curl commands to Python (curlconverter.com)](https://curlconverter.com/python/) 把网络请求相关信息转化为Python数据格式，只复制前面的Header与Cookie字段替换到`main.py`即可。对于`renew`（`https://weread.qq.com/web/login/renewal`）自动更新Cookie的接口，可以沿用`main.py`中的大部分字段，或者自己抓取，需要一段时间才能抓到更新cookie的值（大于一小时）。

## 截图展示

#### 1、运行结果

![image-20241004115421978](pic/image-20241004115421978.png)

#### 2、接口抓取

![image-20241004115513846](pic/image-20241004115513846.png)

#### 3、JS逆向

![image-20241004115545324](pic/image-20241004115545324.png)

#### 3、显示成效(测试8天全部正常运行)

![352c71c4cdd2e16e84cb9239499573a1](pic/352c71c4cdd2e16e84cb9239499573a1.jpg)

#### 4、服务器自动运行指令

![image-20241004120026766](pic/image-20241004120026766.png)

#### 5、完成推送


![5ed32774727aadb47aeb32ca21db8342](pic/5ed32774727aadb47aeb32ca21db8342.jpg)


### 字段解释

- `appId`: `"wbxxxxxxxxxxxxxxxxxxxxxxxx"` ✔
  - 应用的唯一标识符。

- `b`: `"ce032b305a9bc1ce0b0dd2a"` ✔
  - 书籍或章节的唯一标识符。

- `c`: `"0723244023c072b030ba601"` ✔
  - 内容的唯一标识符，可能是页面或具体段落。

- `ci`: `60` ✔
  - 章节或部分的索引。

- `co`: `336` ✔
  - 内容的具体位置或页码。

- `sm`: `"[插图]威慑纪元61年，执剑人在一棵巨树"` ✔
  - 当前阅读的内容描述或摘要。

- `pr`: `65` ✔
  - 页码或段落索引。

- `rt`: `88` ✔
  - 阅读时长或阅读进度。

- `ts`: `1727580815581` ✔
  - 时间戳，表示请求发送的具体时间（毫秒级）。

- `rn`: `114`
  - 随机数或请求编号，用于标识唯一的请求。

- `sg`: `"bfdf7de2fe1673546ca079e2f02b79b937901ef789ed5ae16e7b43fb9e22e724"`
  - 安全签名，用于验证请求的合法性和完整性。

- `ct`: `1727580815` ✔
  - 时间戳，表示请求发送的具体时间（秒级）。

- `ps`: `"xxxxxxxxxxxxxxxxxxxxxxxx"` ✔
  - 用户标识符或会话标识符，用于追踪用户或会话。

- `pc`: `"xxxxxxxxxxxxxxxxxxxxxxxx"` ✔
  - 设备标识符或客户端标识符，用于标识用户的设备或客户端。

- `s`: `"fadcb9de"`
  - 校验和或哈希值，用于验证请求数据的完整性。
