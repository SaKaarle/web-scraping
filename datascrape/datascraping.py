import requests
from bs4 import BeautifulSoup

PAGE = "http://localhost:8000/auto-mpg.html"
print(PAGE)
result = requests.get(PAGE)
type(result)

print(result.status_code)

# print(result.content[:10])
# print(type(result.content))
source = result.text
# print(type(source))

soup = BeautifulSoup(source,'html.parser')

print(soup.prettify())