import requests
from bs4 import BeautifulSoup

# Request for temperature in Arcos city.
r = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/1079/arcos-mg')
html_code = r.content

soup = BeautifulSoup(html_code, 'html.parser')

temp_min = soup.find(id="min-temp-1")
temp_max = soup.find(id="max-temp-1")

print(f"Today the minimum temperature in Arcos/MG can reach up to: {temp_min.text} and its maximum of up to: {temp_max.text}")

# Request for dolar quote today.
s = requests.get('https://dolarhoje.com')
html_code1 = s.content

soup1 = BeautifulSoup(html_code1, 'html.parser')

dolar = soup1.find(id="nacional")
print(f"The current value of the american dollar in brazilian real is: {dolar['value']}")