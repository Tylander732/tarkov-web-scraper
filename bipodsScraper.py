from weaponModInfoClass import WeaponModInfo
import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://escapefromtarkov.fandom.com/wiki/Harris_HBR_Bipod",)

soup = BeautifulSoup(response.content, 'lxml')

infoBox = soup.find('table', id='va-infobox0')

itemName = infoBox.find('div', class_='va-infobox-title-main')

recoilChildTag = infoBox.find('a', text="Recoil")
recoilParentTrTag = recoilChildTag.find_parent('tr')
recoilValue = recoilParentTrTag.find('td', class_='va-infobox-content')

ergoChildTag = infoBox.find('a', text="Ergonomics")
ergoParentTrTag = ergoChildTag.find_parent('tr')
ergoValue = ergoParentTrTag.find('td', class_='va-infobox-content')

weapMod = WeaponModInfo(itemName.text, recoilValue.text, ergoValue.text)

print(weapMod.getName())
print(weapMod.getRecoil())
print(weapMod.getErgo())