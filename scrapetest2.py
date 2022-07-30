from urllib.request import urlopen
from bs4 import BeautifulSoup

html =  urlopen("https://github.com/snowrlax")


soup = BeautifulSoup(html.read(), 'html.parser')

print(soup.prettify())