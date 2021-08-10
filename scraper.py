import requests
from bs4 import BeautifulSoup

wikiUrlBase = "https://escapefromtarkov.fandom.com"

response = requests.get(url="https://escapefromtarkov.fandom.com/wiki/Weapon_mods",)

soup = BeautifulSoup(response.content, 'lxml')

wikiUrlsFile = open("wikiUrlsFile.txt", "w")

#Finds every item under wikitable sortables, grabs the href of the item and writes it to a text file
for wikitableSortable in soup.find_all('table', class_='wikitable sortable'):
	itemTbody = wikitableSortable.find('tbody')
	for thElement in itemTbody.find_all('th'):
		for aElement in thElement.find_all('a'):
			#find element within tag by using dictionary syntax. Example: aElement['href']
			href = aElement['href']
			wikiUrlsFile.write(href + "\n")

wikiUrlsFile.close()