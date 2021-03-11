html = '''
<div id='wrap'>
<div id='container'>
<ul class='list'>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class='bold'>third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
from pyquery import PyQuery as pq
doc=pq(html)
print(doc('li'))
print(doc('#container .list li'))
item=doc('.list')
lis=item.find('li')
print(lis)
li=doc('.item-0.active')
print(li.text())
print(li.html())
print(li)
li.remove_class('active')
print(li)
li.add_class('active')
print(li)