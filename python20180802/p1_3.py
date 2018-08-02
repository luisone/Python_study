import urllib.request

url = 'http://www.whatismyip.com.tw/'

#代理http://www.data5u.com/free/gwpt/index.shtml
proxy_support = urllib.request.ProxyHandler({'http':'46.242.1.182:8081'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
