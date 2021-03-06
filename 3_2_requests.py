import requests

# url='https://www.baidu.com'
# r=requests.get(url)
# print(type(r))
# print(r. status_code)
# print(type(r. text))
# print(r. text)
# print(r.cookies)

# data = {
# 'name': 'jack',
# 'age': 22
# }
# r = requests.get("http://httpbin.org/get",params=data)
# print(r.text)

# url='https://www.jianshu.com'
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
# }
# r=requests.get(url,headers=headers)
# print(type(r.status_code),r.status_code)
# print(type(r.headers),r.headers)
# print(type(r.cookies),r.cookies)
# print(type(r.url),r.url)
# print(type(r.history),r.history)
# print(r.text)

# Session
# s=requests.Session()
# s.get('http://httpbin.org/cookies/set/number/12345678')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)

r=requests.get('https://www.12306.cn',verify=False)
print(r.status_code)
print(r.text)