from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(open("6-12-1-source.html"))

links = soup.find_all('a')

for link in links:
    print(link.get('href'))
