import re
html ='''<div id="songs-list"> 
<h2 class="title">经典老歌</h2> 
<p class="introduction"> 经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐泰">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li> 
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li> 
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

# 匹配齐秦往事随风
result=re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result.group(1),result.group(2))

#匹配所有文件，歌手与歌曲名称
result=re.findall('<a href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
for i in result:
    print(i[0],i[1],i[2])

# 匹配所有歌曲名称
html=re.sub('<a.*?>|</a>','',html)
result=re.findall('<li.*?>(.*?)</li>',html,re.S)
for i in result:
    print(i.strip())
