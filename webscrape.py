# This script makes a GET request to the specified URL using the requests 
# library, and then uses the BeautifulSoup library to parse the HTML of the
# website. The soup.find_all() method is used to find all of the <a> (anchor) 
# tags on the page, and the link.get('href') method is used to get the href 
# attribute of each link. This will print all the links found on the website.

import requests
from bs4 import BeautifulSoup


file = open("samplesite.html",'w')

url = 'https://www.ayadata.ai/'
response = requests.get(url)

#parses through the html
soup = BeautifulSoup(response.text, 'html.parser')

# Find all of the links on the page
#for link in soup.find_all('a'):
#   print(link.get('href'))

file.write(soup.prettify())
file.close()

