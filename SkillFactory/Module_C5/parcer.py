import requests
import lxml.html
from lxml import etree


# html = requests.get('https://www.python.org/').content
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())
ul = tree.findall('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/')

for li in ul:
    a = li.find('a')
    print(a.text)
