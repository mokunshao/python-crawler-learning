import requests
from lxml import etree

url = 'https://movie.douban.com/subject/27166976/'

text = requests.get(url).text

html = etree.HTML(text)

name = html.xpath('//*[@id="content"]/h1/span[1]/text()')
score = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
stars = html.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
votes = html.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/div/div[2]/a/span/text()')

print('电影名称', name)
print('评分', score)
print('演员', stars)
print('评价人数', votes)

print(stars[0])

print(stars[0:3])