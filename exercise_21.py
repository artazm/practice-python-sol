# Write to a File
import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

with open('file to save.txt', 'w') as open_file:
    for h2 in soup.find_all('h2'):
        open_file.write(h2.text + '\n')

