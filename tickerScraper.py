from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import csv

with open('companies.csv', 'w', newline='') as csvfile:
    fieldnames = ['Company Name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    request = requests.get(url)
    only_table = SoupStrainer("table", id="constituents")
    soup = BeautifulSoup(request.text, 'lxml', parse_only=only_table)
    for tag in soup.find_all("tr"):
        print(tag.a.contents[0])
        if tag.a.contents[0] != "Symbol":
            writer.writerow({'Company Name': tag.a.contents[0]})