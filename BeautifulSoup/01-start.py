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

# 获取head标签
print(soup.head) 
print(soup.title)
# 获取<body>标签中的第一个<b>标签
print(soup.body.b)
# 获得当前名字的第一个tag
print(soup.a)
# 所有的<a>标签
print(soup.find_all("a"))


# tag的 .contents 属性可以将tag的子节点以列表的方式输出
head_tag = soup.head
print(head_tag)
print(head_tag.contents)

title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)

# BeautifulSoup 对象本身一定会包含子节点,也就是说<html>标签也是 BeautifulSoup 对象的子节点:
print(len(soup.contents))
print(soup.contents[0].name)

# text = title_tag.contents[0]
# print(text.contents)

# 通过tag的 .children 生成器,可以对tag的子节点进行循环
for child in title_tag.children:
    print(child)

# .descendants 属性可以对所有tag的子孙节点进行递归循环 
for child in head_tag.descendants:
    print(child)

print(len(list(soup.children)))
print(len(list(soup.descendants)))

print(title_tag.string)
print(head_tag.string)

# 如果tag中包含多个字符串,可以使用 .strings 来循环获取，但是会输出很多空格或空行
for string in soup.strings:
    print(repr(string))

# 使用 .stripped_strings 可以去除多余空白内容
for string in soup.stripped_strings:
    print(repr(string))