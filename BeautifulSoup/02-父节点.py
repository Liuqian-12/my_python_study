html_doc = """
<html><head><title>The Dormouse's story</title></head>
    <body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

title_tag = soup.title
# 通过 .parent 属性来获取某个元素的父节点.
# <head>标签是<title>标签的父节点:
print(title_tag.parent)
print(title_tag.string.parent)

# 文档的顶层节点比如<html>的父节点是 BeautifulSoup 对象:
html_tag = soup.html
print(type(html_tag.parent))

# 通过元素的 .parents 属性可以递归得到元素的所有父辈节点,下面的例子使用了 .parents 方法遍历了<a>标签到根节点的所有节点
link = soup.a
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)


