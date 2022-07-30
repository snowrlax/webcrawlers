from urllib.request import urlopen  
# from urllib library navigate to module called request and then only import
# urlopen function from there

html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())