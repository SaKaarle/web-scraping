import requests
from bs4 import BeautifulSoup


# "https://en-gb.wordpress.org/plugins/browse/popular/"
PAGE = "https://hansard.parliament.uk/search/Members?house=commons&currentFormerFilter=1"
print(PAGE)
result = requests.get(PAGE)
type(result)

print(result.status_code)

# source = result.text
# with open('wordpress.html','w') as f:
#     f.write(result.text)

with open('hansard.html','w') as f:
    f.write(result.text)
# soup = BeautifulSoup(source,'html.parser')
# print(soup.prettify())