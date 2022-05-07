import csv
from bs4 import BeautifulSoup
import requests
import time


def build():
    csv_file = open('country.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['country'])

    with open('URLs.csv', mode='r') as csv_file:
        print('*** Downloading Data ***')
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        # read URL from crawl data
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\tDownloading {row["url"]}.')
            line_count += 1

            # Get page data 
            source = requests.get(row["url"]).text
            soup = BeautifulSoup(source, 'lxml')
            table = soup.find('table')
            data = ''
            # download relevant data to file
            if table is not None:
                for elem in table.find_all('tr'):
                    data = data + (elem.text) + ' '
                csv_writer.writerow([data,row["url"]])
            csv_file.close
            print('Sleeping for 5 seconds...')
            time.sleep(5)

        print(f'Processed {line_count} lines.')
        print('*** Download Successful ***')

            
# for testing
# build()