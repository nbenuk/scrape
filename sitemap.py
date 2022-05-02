import csv
from bs4 import BeautifulSoup
import requests

def sitemap():
    source = requests.get('http://example.python-scraping.com/sitemap.xml').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('urlset.csv', 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['url'])

    table = soup.find('urlset')
    for url in table.find_all('url'):
        csv_writer.writerow([url.text])
        # print(url.text)
        # print()
    csv_file.close
