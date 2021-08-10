import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://escapefromtarkov.fandom.com/wiki/Harris_HBR_Bipod",)

soup = BeautifulSoup(response.content, 'lxml')

infoBox = soup.find('table', id='va-infobox0')

itemName = infoBox.find('div', class_='va-infobox-title-main')

print(itemName.text)