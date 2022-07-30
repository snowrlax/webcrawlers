from urllib.request import urlopen  
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
 html = urlopen('https://www.pythonscraping.com/pages/page1.html')
 
#  The server error is handled ht HTTPError
except HTTPError as e:
 print(e)

# The URL error are handled by URLError
except URLError as e:
 print('The server could not be found!')
else:
 print('It Worked!')

 bs = BeautifulSoup(html.read(), 'html.parser')
 print(bs.noneo)        


