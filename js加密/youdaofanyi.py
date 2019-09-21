import requests
import time
import hashlib
import random


url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
 'Connection': 'keep-alive',
 'Content-Length': '290',
 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
 'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=189463627.20703408; '
           'OUTFOX_SEARCH_USER_ID="1029809263@10.168.11.69"; '
           'JSESSIONID=aaayLTJb9vHomavhFDe0w; '
           '___rl__test__cookies=1567738852283',
 'Host': 'fanyi.youdao.com',
 'Origin': 'http://fanyi.youdao.com',
 'Referer': 'http://fanyi.youdao.com/',
 'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) '
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 '
               'Mobile Safari/537.36',
 'X-Requested-With': 'XMLHttpRequest'
}


def get_ts():
    ts = int(time.time()*1000)
    return ts

def get_bv():
    appVersion = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Mobile Safari/537.36'
    m = hashlib.md5()
    m.update(appVersion.encode('utf-8'))
    bv = m.hexdigest()
    return bv

def get_salt(ts):
    num = int(random.random()*10)
    salt = str(ts) + str(num)
    return salt

def get_sign(salt,i):
    a = 'fanyideskweb'
    b = str(i)
    c = salt
    d = '@6f#X3=cCuncYssPsuRUE'

    str_data = a + b + str(c) + d

    m = hashlib.md5()
    m.update(str_data.encode('utf-8'))
    sign = m.hexdigest()

    return sign


def get_form_data(i):
    ts = get_ts()
    bv = get_bv()
    salt = get_salt(ts)
    sign = get_sign(salt,i)

    form_data = {
        'action': 'FY_BY_CLICKBUTTION',
        'bv': str(bv),
        'client': 'fanyideskweb',
        'doctype': 'json',
        'from': 'AUTO',
        'i': str(i),
        'keyfrom': 'fanyi.web',
        'salt': str(salt),
        'sign': str(sign),
        'smartresult': 'dict',
        'to': 'AUTO',
        'ts': str(ts),
        'version': '2.1'
    }

    return form_data

if __name__ == '__main__':
    i = "小帅b"
    formdata = get_form_data(i)

    response = requests.post(url,data=formdata,headers = headers)
    print(response.text)