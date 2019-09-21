import time
import hashlib
import random

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

def get_sign(salt):
    a = 'fanyideskweb'
    b = '小帅b'
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
    sign = get_sign(salt)

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
    i = input('qingshuru:')
    print(get_form_data(i))