import execjs
import requests
import time
"""
des 加密
"""

def getpassword(account, password):
    with open('login.js', 'r') as f:
        jscode = f.read()
        password = execjs.compile(jscode).call('getpassword', account, password)
        return password


def login(account, password):
    headers = {
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "x-riskdevicesign": "6c43d10ffd1901984c1ab15517e770b9",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://m.ctyun.cn/wap/main/auth/login",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "Hm_lvt_4b4ce93f1c92033213556e55cb65769f=1660662408; mvid=3ab6e7fe-5bde-4968-bf25-f2ce3d8942b1; JSESSIONID=98DFBB0D717FDD7DB1BDBF05CE1104CD; sid1=1661354671634-6D6E572AA68EBE75AD5218E4100F7701; sid2=1661354671634-6D6E572AA68EBE75AD5218E4100F7701; Hm_lpvt_4b4ce93f1c92033213556e55cb65769f=1661355255; pvid=4"
    }
    session = requests.session()
    session.headers = headers
    params = {
        "userName": account,
        "password": getpassword(account, password),
        "referrer": "wap",
        "mainVersion": "300031500",
        "comParam_curTime": str(int(time.time() * 1000)),
        "comParam_seqCode": "DB47E525D579032F9E9A0FBDB410920A",
        "comParam_signature": "ab0fd945dccc3f452a8a2becca7e4b71",
        "isCheck": "true",
        "locale": "zh-cn"
    }
    response = session.get("http://m.ctyun.cn/account/login", params=params)
    print(response.content.decode())
    print(session.cookies)



if __name__ == '__main__':
    password = '~haohao9527'
    account = "1205095339@qq.com"
    login(account, password)
