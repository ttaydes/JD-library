import requests
import json
import get_userinfo


url = "http://xxxxx/api.php/spaces/这里写座位号/book"

header = {
    "Host": "xxxxx",
    "Content-Length": "94",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5315 MMWEBSDK/20231202 MMWEBID/6867 MicroMessenger/8.0.47.2560(0x28002F36) WeChat/arm64 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "http://www.skalibrary.com",
    "X-Requested-With": "com.tencent.mm",
    "Referer": "http://www.skalibrary.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close"
}


def bookmain():
    with open("log.txt", 'a+', encoding='utf-8') as f:   #创建每次记录的日志文件

        try:
            act = get_userinfo.get_access_token()  # 获取accesstoken
            segement = get_userinfo.segement
            userid, pwd = get_userinfo.getunpwd()
            bookinfo = get_userinfo.bookstatus()

            datas = {

                "access_token": f"{act}",
                "userid": f"{userid}",
                "type": 1,
                "id": xxx,  #这里需要自定义座位号
                "segment": f"{segement}"

            }
            if bookinfo == "空闲":
                sessions = requests.session()  # 每次创建一个session

                contents = sessions.post(url=url, data=datas, headers=header).text
                print("预约成功！")
                sessions.close()
                f.write(f"{get_userinfo.dates} ：成功预约!" + '\n')

            else:
                f.write(f"{get_userinfo.dates}：预约失败 被占用或已经预约！" + '\n')

        except Exception as e:
                f.write(f"{get_userinfo.dates}： 异常事件{e}")

if __name__ == '__main__':
    bookmain()
