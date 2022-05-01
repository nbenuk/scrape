import csv
from bs4 import BeautifulSoup
import requests

source = requests.get('http://example.python-scraping.com/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['country'])

table = soup.find('table')
for country in table.find_all('div'):
    csv_writer.writerow([country.text])
    print(country.text)
    print()
csv_file.close
