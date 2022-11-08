import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.climatempo.com.br')

html_code = r.content
print(html_code)