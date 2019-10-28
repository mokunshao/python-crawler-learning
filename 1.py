import requests

url = 'https://www.baidu.com/'

data = requests.get(url)

data.encoding = 'utf8'

print(data.text)
