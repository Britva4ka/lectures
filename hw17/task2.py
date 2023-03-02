import requests
from lxml import html
from bs4 import BeautifulSoup

page = requests.get(" /")

body = html.fromstring(page.content)
# Взяти рік фільма і вивести парою
print(*body.xpath('//table[@class = "chart full-width"]/tbody/tr/td[@class = "titleColumn"]/a/text()'), sep='\n')