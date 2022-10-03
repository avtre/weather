from bs4 import BeautifulSoup as bs
import os

output = open("db.txt", 'a')

for root, dirs, files, in os.walk('.'):
	for filename in files:
		if filename.find('html') != -1 and filename != 'page.html':
			print(filename)	
			f = open("db/" + filename, "r")
			page = ""
			qwe = f.readlines()
			for it in qwe:
				page += it

			#print(page)
			soup = bs(page, 'html.parser')
			hrefs = soup.find_all('a', class_="link place-list__item-name i-bem")
			for it in hrefs:
				href_h = it['href']
				for i in it.text.lower().split(', '):
					output.write('\'' + i + '\': \'' + href_h[href_h.rfind('/') + 1:href_h.find('?')].lower() + '\', ')


	