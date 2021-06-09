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

print(soup.title.text)
#print(soup.html.head)

# testi onko true
# print(soup.html.head == soup.head)

#print(soup.body.text[:100])
#print(soup.body.p.next_sibling.next_sibling)

#soup.find(id='car-0')
print(soup.body.a.attrs['href'])
print (len(soup.find_all('a')))
print (len(soup.find_all('span', class_='rating-count')))


artik = soup.find_all('article', class_='plugin-card post-158 plugin type-plugin status-publish'+
' hentry plugin_category-communication plugin_category-contact-forms'+
' plugin_category-utilities-and-tools plugin_contributors-takayukister plugin_committers-takayukister'+
' plugin_tags-contact plugin_tags-contact-form plugin_tags-email plugin_tags-feedback plugin_tags-form')[0]
# print(artik.text)

print(list(artik.stripped_strings))
print(artik.find_all('span'))

print(artik.find('span', class_='rating-count').text)
print(list(pluginauthor.text for pluginauthor in soup.find_all('span',class_='plugin-author')))
# print(re.findall('.* (\d+.\d+) total ratings', artik.text))
# print(artik.prettify())
# print (soup.find_all('span', class_='plugin-author'))
# etsi plugin author "class=plugin-author" = print (soup.find_all('span', class_='plugin-author'))

# imasee [0]:n listasta Takayuki Miyoshin ja get_text/text printtaa sen käyttäjän
# pluginauthors = soup.find_all('span', class_='plugin-author')[0]
# print(pluginauthors.text)
listauspaska = list(author.text for author in soup.findAll('span', class_='plugin-author'))
pprint(listauspaska)