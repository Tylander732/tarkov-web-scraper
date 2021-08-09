import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://escapefromtarkov.fandom.com/wiki/Weapon_mods",)

soup = BeautifulSoup(response.content, 'lxml')

#Finds every item under wikitable sortables, grabs the name of the item and outputs it
for wikitableSortable in soup.find_all('table', class_='wikitable sortable'):
	itemTbody = wikitableSortable.find('tbody')
	for aElement in itemTbody.find_all('a'):
		if aElement.text != "":
			print(aElement.text)



#This grabs everything underneath the tabber wds-tabber div
#itemTabber = soup.find('div', class_='tabber wds-tabber')

# for itemTable in itemTabber.find_all('div', class_='wds-tab__content'):
# 	for itemValues in itemTable.find_all('table', class_='wikitable sortable'):
# 		itemName = itemValues.tbody.tr.th.text
# 		print(itemName)