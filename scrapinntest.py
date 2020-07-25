import requests
from bs4 import BeautifulSoup

base_url ='https://webscraper.io/test-sites/e-commerce/allinone/computers'
url= base_url 
loc= 'ibague'

yelp_r = requests.get(url)
yelp_soup = BeautifulSoup(yelp_r.content, 'html.parser')


businesess = (yelp_soup.findAll('div', {'class': 'col-md-9'}))
print(businesess)

for biz in businesess:
    #print(biz)
    title = biz.findAll('a', {'class':'title'})
    print(title)
    print('\n')
    price = biz.findAll('h4', {'class':'pull-right price'})
    print(price)
    print('\n')
    dispo = biz.findAll('p', {'class':'description'})
    print(dispo)


file_path = 'scrape-{loc}.txt'.format(loc=loc)

with open(file_path, "a") as textfile:
    businesess = yelp_soup.findAll('div', {'class': 'biz-listing-large'})
    for biz in businesess:
	    title = biz.findAll('a', {'class':'title'})
	    print(title)
	    print('\n')
	    price = biz.findAll('h4', {'class':'pull-right price'})
	    print(price)
	    print('\n')
	    dispo = biz.findAll('p', {'class':'description'})
	    print(dispo)
	    page_line = "{title}\n{price}\n{dispo}\n\n".format(
	            title=title,
	            price=price,
	            dispo = dispo
	        )
	    textfile.write(page_line)