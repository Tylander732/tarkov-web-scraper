import requests
from bs4 import BeautifulSoup

response = requests.get(
		url="https://escapefromtarkov.fandom.com/wiki/Weapon_mods",
	)

soup = BeautifulSoup(response.content, 'lxml')

itemTabber = soup.find('div', class_='tabber wds-tabber')

for itemTable in itemTabber.find_all('div', class_='wds-tab__content'):
	for itemValues in itemTable.find_all('table', class_='wikitable sortable'):
		itemName = itemValues.tbody.tr.th.text
		print(itemName)




