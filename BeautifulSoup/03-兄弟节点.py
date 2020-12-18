from bs4 import BeautifulSoup
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", "html.parser")
print(sibling_soup.prettify())



