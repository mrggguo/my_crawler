from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html =etree.HTML(text)
result= etree.tostring(html)
print(result.decode ('utf-8'))
# //选取节点
result=html.xpath("//li")
print(result)
# /选取直接子节点
result=html.xpath("//li/a")
print(result)
# //选取所有子孙节点
result=html.xpath("//ul//a")
print(result)
# @实现属性匹配过滤，获取父节点
result=html.xpath('//a[@href="link4.html"]/../@class')
print(result)
result=html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
# text()获取文本
result=html.xpath('//li[@class="item-0"]/a/text()')
print(result)
# @获取属性
result=html.xpath('//li/a/@href')
print(result)