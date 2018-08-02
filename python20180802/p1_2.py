import urllib.request
import urllib.parse

import json

url = "http://fanyi.youdao.com/translate?keyfrom=plugin&amp;smartresult=dict&amp;smartresult=rule"

content = input("请输入需要翻译的内容：")

head = {}
head['Referer'] = 'http://fanyi.youdao.com'
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
data = {}
#data['from'] = 'AUTO'
#data['to'] = 'AUTO'
#data['smartresult'] = 'dict'
#data['client'] = 'fanyideskweb'
#data['salt'] = f
#data['sign'] = sign
data['i'] = content
data['doctype'] =  'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
#data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(url, data, head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
html = json.loads(html)
html = html['translateResult'][0][0]['tgt']
print("翻译结果：%s " % html)
