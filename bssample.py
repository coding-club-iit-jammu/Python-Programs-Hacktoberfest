import requests
from bs4 import BeautifulSoup
def res_spider():
	url='https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=shoes'
	srcode=requests.get(url)
	plain=srcode.text
	soup=BeautifulSoup(plain)#object
	for link in soup.findAll('h2',{'class':'a-size-base s-inline  s-access-title  a-text-normal'}):
		name=link.string
		print(name)

res_spider()
