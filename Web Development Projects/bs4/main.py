from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.a.string)
# print(soup.p)
# print(soup.p.string)
# print(soup.li)
# print(soup.li.string)
# print(soup.find_all(name="li"))
