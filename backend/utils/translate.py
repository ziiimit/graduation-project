import requests
import hashlib

# https://fanyi-api.baidu.com/doc
URL = "https://fanyi-api.baidu.com/api/trans/vip/translate"
APP_ID = '20240130001954694'
KEY = 'B3y1ogKE5dbHRk6_kLUy'
salt = "sakjdffjhcoadsasdfasgsf" # 随机数，随便敲的

#  MD5(appid+q+salt+密钥)
def getSign(q):
    str = APP_ID + q + salt + KEY
    md = hashlib.md5()
    md.update(str.encode('utf-8'))
    return md.hexdigest()

def toChinese(queryString):
    params = {
        'q':queryString,
        'from':'auto',
        'to':"zh",
        'appid':APP_ID,
        'salt':salt,
        'sign':getSign(queryString)
    }

    res = requests.get(URL, params=params).json()
    return res['trans_result'][0]['dst']

    
def toEnglish(queryString):
    params = {
        'q':queryString,
        'from':'auto',
        'to':"en",
        'appid':APP_ID,
        'salt':salt,
        'sign':getSign(queryString)
    }

    res = requests.get(URL, params=params).json()
    return res['trans_result'][0]['dst']



