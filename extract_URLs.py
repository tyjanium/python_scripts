# This script will extract URLs from a webpage create a txt file containing 
# the URLs

import csv, requests
from bs4 import BeautifulSoup

url = input("Enter URL: ")
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

# Open a text file in write mode. Note: bes sure to use .txt file extension
# for a plain text file. 
f = open(input("Enter filename for list of links: "), "w")

# Find links in html
for link in soup.find_all("a", href=True):
    data = link.get("href")
    f.write(data)
    f.write("\n")

f.close()