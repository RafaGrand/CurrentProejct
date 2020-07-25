import requests
from bs4 import BeautifulSoup

base_url ='http://books.toscrape.com/index.html'
url= base_url 
loc= 'ibague'

yelp_r = requests.get(url)
yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')


businesess = (yelp_soup.findAll('ol', {'class': 'row'}))



for biz in businesess:
    #print(biz)
    title = biz.findAll('h3')
    print(title)
    print('\n')
    price = biz.findAll('img', {'class':'thumbnail'})
    print(price)
    print('\n')
    dispo = biz.findAll('div', {'class':'product_price'})
    print(dispo)


file_path = 'scrape-{loc}.txt'.format(loc=loc)

with open(file_path, "a") as textfile:
    businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
    for biz in businesess:
	    title = biz.findAll('h3')
	    print(title)
	    print('\n')
	    price = biz.findAll('img', {'class':'thumbnail'})
	    print(price)
	    print('\n')
	    dispo = biz.findAll('div', {'class':'product_price'})
	    print(dispo)
	    page_line = "{title}\n{price}\n{dispo}\n\n".format(
	            title=title,
	            price=price,
	            dispo = dispo
	        )
	    textfile.write(page_line)

