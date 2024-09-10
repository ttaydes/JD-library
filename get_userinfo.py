import json
import requests
from datetime import datetime, timedelta

day = datetime.now() + timedelta(days=1)
dates = day.date()  # 获取当天的第二天日期

url0 = f"http://xxxxx/api.php/space_time_buckets?area=21&day={dates}"

headers = {
    "headers_1": {
        "Host": "xxxxx",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5315 MMWEBSDK/20231202 MMWEBID/6867 MicroMessenger/8.0.47.2560(0x28002F36) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
        "Origin": "http://www.skalibrary.com",
        "X-Requested-With": "com.tencent.mm",
        "Referer": "http://www.skalibrary.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive"
    },

    "headers_2": {
        "Host": "xxxx",
        "Content-Length": "74",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5315 MMWEBSDK/20231202 MMWEBID/6867 MicroMessenger/8.0.47.2560(0x28002F36) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "http://www.skalibrary.com",
        "X-Requested-With": "com.tencent.mm",
        "Referer": "http://www.skalibrary.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive"
    },

    "headers_3": {
        "Host": "www.skalibrary.com",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5315 MMWEBSDK/20231202 MMWEBID/6867 MicroMessenger/8.0.47.2560(0x28002F36) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
        "X-Requested-With": "com.tencent.mm",
        "Referer": "http://www.skalibrary.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": "connect.sid=xxxxxxxx",
        "Connection": "keep-alive"
    }

}

segement = json.loads(requests.get(url=url0, headers=headers["headers_1"]).text)['data']['list'][0]['id']


url1 = "http://www.skalibrary.com/getUser?openid=xxxxxxx"  # 通过openid 登入
url2 = "http://xxxxxxxxxx/api.php/login"  # 登入
url3 = f"http://xxxxxxxxx/api.php/spaces_old?area=21&day={dates}&endTime=23:20&segment={segement}&startTime=07:00"

# area 21指的是电子阅览室


def bookstatus():
    try:
        a = requests.get(url=url3, headers=headers["headers_1"]).text
        transcode = a.encode('utf-8').decode("unicode_escape")
        transjson = json.loads(transcode)
        lists = transjson['data']['list']
        for dicts in lists:
            if dicts['id'] == 4058:
                return dicts['status_name']

    except Exception as e:
        print(f"{e} bookstatus 异常！！！")


def getunpwd():
    try:
        gets1 = requests.get(url=url1, headers=headers["headers_3"])

        username = json.loads(gets1.text)['username']
        password = json.loads(gets1.text)['password']

        return username, password

    except Exception as e:
        print(f"getunpwd {e}异常")


def get_access_token():
    uname, pwd = getunpwd()
    data1 = {
        "username": f"{uname}",
        "password": f"{pwd}",
        "from": "mobile"
    }
    try:
        post1 = requests.post(url=url2, headers=headers["headers_2"], data=data1)

        content_json = json.loads(post1.text)
        access_token = content_json['data']['_hash_']['access_token']
        return access_token

    except Exception as e:
        print(f"get_access_token{e}异常")


