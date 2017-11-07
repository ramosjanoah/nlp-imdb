"""
@author: ramosjanoah
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

url_string = 'http://www.imdb.com/title/tt2250912/reviews?ref_=tt_ql_3'


# all_review will contain all review from the url
all_review_content = []

# page varable is opened page from url string
page = urlopen(url_string)

# content is content from the page
content = page.read()

# soup is content that have been parsed
soup = BeautifulSoup(content, 'html.parser')

# tn15content is content of review. Find all paragraph (p) from div
review_list = soup.find(id="tn15content")
img = review_list.find_all('img')
star_list = []

for element in img:
	rating = element.attrs.get('alt',None)
	if rating != None:
		if '/' in rating:
			star_list.append(rating)
print(star_list)
