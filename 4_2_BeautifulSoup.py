html ="""
<html><head><title>The Dormouse's story</title></head>
<body>
<title class="title" name="dromouse"><b>The Dormouse's story</b></title>
<p class="story">Once upon a time there were three little sisters; and their names were 
<a href="http://example.com/elsie" class="sister" id="linkl"><span>Elsie</span></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a> ;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.title.string)
print(soup.p.string)
print(soup.p.attrs)
print(soup.p['class'])
# 直接子节点
print(soup.p.contents)
print(soup.p.children)
# 所有子孙节点
print(soup.p.descendants)
# 父节点
print(soup.p.parent)
# 所有祖先节点
print(soup.p.parents)
# 兄弟节点
print(soup.a.next_siblings)