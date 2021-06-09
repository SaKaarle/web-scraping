import requests
from bs4 import BeautifulSoup
import re
from pprint import pprint
# https://en-gb.wordpress.org/plugins/browse/popular/
# http://localhost:8000/wordpress.html
page = "https://en-gb.wordpress.org/plugins/browse/popular/"

# def lisari(soup):
#     lisariTiedot = soup.find_all('main', class_='site-main', role='main')
#     rows=[]
#     for tiedot in lisariTiedot:
#         str_name = tiedot.find('span', class_='plugin-author').text
#         str_ratings = tiedot.find('span',class_='rating-count').text
#         ratings = (str_ratings.replace(',', ''))
#         rivi = dict(name=str_name,ratings=ratings)

#         rows.append(rivi)
#     print(f"We have {len(rows)} rows of scraped WordPress data")
#     print(rows[0])
#     print(rows[-1])
#     print(len(str_name))
    
def lisari(soup):

    rows=[]
    lisariTiedot = soup.select("#main")
    articles = lisariTiedot[0].findAll('article')
    print(len(articles))
    print(articles[0].find( class_='plugin-author').text)
    print(articles[0].find( class_='rating-count').text)
    for tiedot in articles:
        str_author = tiedot.find(class_='plugin-author').text
        str_rating = tiedot.find(class_='rating-count').text
        author = (str_author.strip())
        ratings = (str_rating.strip().replace(',','').replace(' total ratings',''))

        rivi = dict(name=author,ratings=ratings)

        rows.append(rivi)
            
    print(f"We have {len(rows)} rows of scraped WordPress data")
    #pprint(rows)

    #pituus = len(rows)
    for infot in rows:
        print([infot])
        
    


if __name__ == "__main__":
    result = requests.get(page)
    assert result.status_code == 200, f"Got status code {result.status_code} \
    which isn't a success"
    source = result.text
    soup = BeautifulSoup(source,'html.parser')
    lisari(soup)
    

