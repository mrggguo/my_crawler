# 当urllib.urlopen一个https的时候会验证一次SSL证书,当目标使用的是自签名的证书时就会爆出该错误消息
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

# 普通用法
# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.read().decode('utf8'))


# 使用Request带headers
# from urllib import request, parse
# url='http://httpbin.org/post'
# headers={
#     'User-Agent':'Mozilla/4.0 (compatible; MSIE S.S; Windows NT)',
#
# }
# dict={
#     'name':'Jack'
# }
# data=bytes(parse.urlencode(dict),encoding='utf8')
# req=request.Request(url=url,headers=headers,data=data,method='POST')
# response=request.urlopen(req)
# print(response.read().decode('utf8'))

# 带cookies
# 首先,声明一个 CookieJar对象;接下来，利用 HTTPCookieProcessor来构建一个Handler,
# 最后利用 build_opener()方法构建出 Opener，执行 open()函数即可 。
import http.cookiejar, urllib.request
cookie=http.cookiejar.CookieJar()
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name+':'+item.value)
print(response.read().decode('utf8'))