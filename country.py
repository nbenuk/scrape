import csv
from bs4 import BeautifulSoup
import requests
csv_file = open('country.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['country'])

def build():
    with open('urlset.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["url"]}.')
            line_count += 1

            # add url to list

            source = requests.get(row["url"]).text
            soup = BeautifulSoup(source, 'lxml')
            table = soup.find('table')

            for elem in table.find_all('tr'):
                csv_writer.writerow([elem.text])
                print(elem.text)
                print()
            csv_file.close
        print(f'Processed {line_count} lines.')


