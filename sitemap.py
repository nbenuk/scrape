import csv
from bs4 import BeautifulSoup
import requests
import time
def sitemap():
    source = requests.get('http://example.python-scraping.com/sitemap.xml').text

    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('urlset.csv', 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['url'])

    table = soup.find('urlset')
    for url in table.find_all('url'):
        csv_writer.writerow([url.text])
    csv_file.close
pages = []

# Crawl strarting from site: url
def crawl(url):
    print('*** Crawling Site Pages ***')

    if url[0] != 'h':
        url = 'http://example.python-scraping.com' + url

    # GET Page data
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    print('Sleeping for 5 seconds...')
    time.sleep(5)
    # Find link and add to list
    href = soup.find_all(href=True)

    for url in href:
        if url['href'] != '#':
            if url['href'][0] != 'h':
                url = 'http://example.python-scraping.com' + url['href']
            pages.append(url)
            print('Found '+ url)

    # Find next page
    next_page=soup.find(id='pagination')
    next_page=next_page.find_all('a', href=True)
    for link in href:
        string=link.string
        if string is not None:
            if 'Next' in (link.string):
                url = (link['href'])
                if url[0] != 'h':
                    url = 'http://example.python-scraping.com' + url
                # crawl next page
                crawl((url))


    # Save list of URLs found
    csv_file = open('URLS.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['url'])
    for country in pages:
        csv_writer.writerow([country])
    csv_file.close
    print('*** Crawl Successful ***')

# for testing
# crawl('http://example.python-scraping.com/')
