# Servu päälle python -m http.server
# https://app.pluralsight.com/library/courses/web-scraping-python-data-playbook/table-of-contents
import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
# https://en-gb.wordpress.org/plugins/browse/popular/
PAGE = "http://localhost:8000/wordpress.html"
print(PAGE)
result = requests.get(PAGE)
print(type(result))
source = result.text
print(result.status_code)
soup = BeautifulSoup(source,'html.parser')

#print(soup.prettify())

print(soup.select('article.plugin-card:nth-child(2) > footer:nth-child(4) > span:nth-child(1)'))
