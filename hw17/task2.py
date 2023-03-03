import requests
from lxml import html
from bs4 import BeautifulSoup

page = requests.get("https://www.imdb.com/chart/top/")

body = html.fromstring(page.content)
# Взяти рік фільма і вивести парою
names = body.xpath('//table[@class = "chart full-width"]/tbody/tr/td[@class = "titleColumn"]/a/text()')
years = body.xpath('//table[@class="chart full-width"]/tbody/tr/td[@class="titleColumn"]/span[@class="secondaryInfo"]/text()')
for x, y in zip(names, years):
    print(f"{x}, {y}")