# 2follow.py

import requests as req
from bs4 import BeautifulSoup as bs
from parse100 import *

url = 'https://www.forbes.com/sites/alapshah/2017/11/16/the-100-best-twitter-accounts-for-finance/#271ce0fb7ea0'
filename = 'top100.txt'
newline = '\n'

def getContent(url):
	page = req.get(url)
	return page.content

def getSoup(url):
	return bs(getContent(url), 'html.parser')

soup = getSoup(url)
extract = soup.find(class_='table-wrapper')
text = str(extract)
start = text.find('https://twitter.com/')
top100 = []
while start:
	text = text[start:]
	end = 0
	FOUND = False
	for a in range(len(text)):
		end = a
		if text[a] == '"':
			FOUND = True
			break
	if FOUND:
		top100.append(text[start:end])
		text = text[end:]
		start = text.find('https://twitter.com/')
	if end==len(text)-1:
		break

with open(filename, 'w+') as f:
	for a in top100:
		if not a.strip()=='':
			f.write(a + newline)

parse(filename)

# print(str(extract)[568:600])