import requests
import ddddocr
import random
from urllib import parse
import json
import execjs

# proxies = {
#     'http': 'http://192.168.1.5:8888',
#     'https': 'http://192.168.1.5:8888'
# }
proxies = None
url = 'https://cn.fawmx.com'
session = requests.session()


def get_verifycode():
    params = {
        'x': random.random()
    }
    path = '/service/verifycode'
    get_verifycode_url = parse.urljoin(url, path)
    if proxies:
        response = session.get(get_verifycode_url, params=params, proxies=proxies, verify=False)
    else:
        response = session.get(get_verifycode_url, params=params)
    return response.content


def get_vpkey():
    path = '/service/vpkey'
    get_vpkey_url = parse.urljoin(url, path)
    if proxies:
        response = session.get(get_vpkey_url, proxies=proxies, verify=False)
    else:
        response = session.get(get_vpkey_url)
    return json.loads(response.content.decode())


def loginverification():
    path = '/ee/loginverification'
    loginverification_url = parse.urljoin(url, path)
    data = {
        "eeblackbox": "0002MDAwN0xTVE9LRU4wMDI0NGYxZDVjNTktMmZmYy00NmMxLWEwZjYtNjkyYWM1ODIwNzVhMDAwNklOVExPQzAwMWZodHRwczovL2NuLmZhd214LmNvbS9ob21lL2luZGV4MDAwN1BSSVZBVEUwMDA1ZmFsc2UwMDA1SkVOQkwwMDAxMTAwMDVKU1NSQzAwMjBodHRwczovL3d3dy5mNGJ6eXJ6OTJ1czMuY29tL0UyLzAwMDRVQUdUMDA2Zk1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMDQuMC4wLjAgU2FmYXJpLzUzNy4zNjAwMDdKU1RPS0VOMDAyNDRmMWQ1YzU5LTJmZmMtNDZjMS1hMGY2LTY5MmFjNTgyMDc1YTAwMDdIQUNDTE5HMDAwZXpoLUNOLHpoO3E9MC45MDAwN0hBQ0NDSFIwMDBmVW5pY29kZSAoVVRGLTgpMDAwNUpTVkVSMDAwMzIuMDAwMDRUWk9OMDAwNC00ODAwMDA2SlNUSU1FMDAxNzIwMjIvMDgvMjYgMjE6MDI6NDIuNzE1MDAwN1NWUlRJTUUwMDE0OC8yNi8yMDIyIDk6MDI6NDIgUE0wMDA1SkJSTk0wMDA2Q2hyb21lMDAwNUpCUlZSMDAwOTEwNC4wLjAuMDAwMDVKQlJPUzAwMGZXaW5kb3dzIE5UIDEwLjAwMDA1SkJSQ00wMDFkV2luNjQ7IHg2NDsgS0hUTUwsIGxpa2UgR2Vja28wMDA1SkxBTkcwMDA1emgtQ04wMDA0SlJFUzAwMDkxMDgweDE5MjAwMDA2SlBMR05TMDA2NGludGVybmFsLXBkZi12aWV3ZXI7aW50ZXJuYWwtcGRmLXZpZXdlcjtpbnRlcm5hbC1wZGYtdmlld2VyO2ludGVybmFsLXBkZi12aWV3ZXI7aW50ZXJuYWwtcGRmLXZpZXdlcjswMDA2SlJFRlJSMDAxZmh0dHBzOi8vY24uZmF3bXguY29tL2hvbWUvaW5kZXgwMDA0SUdHWTAwMmNBQUxjbWo5ZkVyYm5TZXgrT01MdnFLc2tPMFFFR0dweUh2a3laV2NtL1B3PTAwMDVBUFZFUjAwNjc1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNC4wLjAuMCBTYWZhcmkvNTM3LjM2MDAwNUFQTkFNMDAwOE5ldHNjYXBlMDAwNU5QTEFUMDAwNVdpbjMyMDAwMk1WMDAyMDEzN0Q4NTI3NjNERUVBRjU1MTQ4QjBERUY1ODBGRjQ5MDAwM0VUVDAwNThBU0tPamlDd3Q5QTNSb0djV1hSQTlLNndZVWJBWWtoVWd4RVBLR2xpMkhJOWVKM1VISXhMSlUxOTEycDVJd0FjdU92eTZYR0R1Rzg2eHQ1eWZIZ1MwQT09MDAwNEVUUFQwMDU4MGRXaWI2YnhpdFhQTmhnVVo0M2JqL3gxZW9KUmVmc3Q4UzFISEswdGpIMzl1N2tPeGhNZjBmOGkxS2ZwZmFFTHZWOGIwUFdIYWQ5U1FVTDJ1Q01yZEE9PTAwMDhXREJUT0tFTjAwMjQ0ZjFkNWM1OS0yZmZjLTQ2YzEtYTBmNi02OTJhYzU4MjA3NWEwMDA4V0VCUlRDSVAwMDBjMTEyLjQyLjM4LjI4MDAwNkNUT0tFTjAwMjQ0ZjFkNWM1OS0yZmZjLTQ2YzEtYTBmNi02OTJhYzU4MjA3NWE=",
        "fkey": "0",
        "info": "haohao9527",
        "p": ""
    }
    if proxies:
        response = session.post(loginverification_url, data=data, proxies=proxies, verify=False)
    else:
        response = session.post(loginverification_url, data=data)
    return json.loads(response.content.decode())


def loginAdvance(resp, verifycode, enPassword):
    path = '/kz/member/loginAdvance'
    loginAdvance_url = parse.urljoin(url, path)
    params = {
        'r': random.random()
    }
    data = {
        "loginpwd": enPassword,
        "loginame": 'haohao9527',
        "verifycode": verifycode,
        "fkey": resp['response'],
        "captchaMethod": 0,
        "captchaToken": '',
        "loginMethod": 0,
    }
    if proxies:
        response = session.post(loginAdvance_url, params=params, data=data, proxies=proxies, verify=False)
    else:
        response = session.post(loginAdvance_url, params=params, data=data)
    print(response.content.decode())

def logincheck():
    path = '/home/register'
    logincheck_url = parse.urljoin(url, path)
    if proxies:
        response = session.get(logincheck_url, proxies=proxies, verify=False)
    else:
        response = session.get(logincheck_url)
    print(response.content.decode())


if __name__ == '__main__':
    headers = {
        "Connection": "keep-alive",
        "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"Windows\"",
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Dest": "image",
        "Referer": "https://cn.fawmx.com/home/register",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    session.headers = headers
    verifycodeB = get_verifycode()
    with open('login.js', 'r') as f:
        js_code = f.read()
    with open('verifycode.jpg', 'wb') as f:
        f.write(verifycodeB)
    ocr = ddddocr.DdddOcr(show_ad=False)
    res = ocr.classification(verifycodeB)
    print(res.strip())
    vpkey_resp = get_vpkey()
    js = execjs.compile(js_code)
    enPassword = js.call('get_enPassword', vpkey_resp)
    resp = loginverification()
    verifycode = res.lower().strip()
    loginAdvance(resp, verifycode, enPassword)
    logincheck()
