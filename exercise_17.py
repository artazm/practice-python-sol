import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

for h2 in soup.find_all('h2'):
    print(h2.text)
