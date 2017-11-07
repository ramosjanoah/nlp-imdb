"""
@author: ramosjanoah
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

def scrapePage(url_string):     
    
    # all_review will contain all review from the url
    all_review_content = []
    
    # page varable is opened page from url string
    page = urlopen(url_string)
    
    # content is content from the page
    content = page.read()
    
    # soup is content that have been parsed
    soup = BeautifulSoup(content, 'html.parser')
    
    # tn15content is content of review. Find all paragraph (p) from div
    content = soup.find(id="tn15content")
    review_list = content.findAll('p')
    img_list = content.find_all('img')

    # Getting star

    star_list = []

    for element in img_list:
        rating = element.attrs.get('alt',None)
        if rating != None:
            if '/' in rating:
                star_list.append(rating)


    # trash_p_list is some <p> that has to be excluded because it doesnt a review
    trash_p_list = ["<p><b>*** This review may contain spoilers ***</b></p>", 
                    '<p><a href="reviews-enter">Add another review</a></p>']
    
    # check the review content if it is in trash_p_list, if no, include it to review
    idx_counter = 0
    for review in review_list:
        if str(review) not in trash_p_list:
            # remove html tag in review
            final_review = str(review).replace("<p>","")
            final_review = final_review.replace("</p>","")
            final_review = final_review.replace("<br/>","")
            final_review = final_review.replace("\n","")

            all_review_content.append((final_review, star_list[idx_counter]))
            idx_counter += 1
    
    return all_review_content


# example string, thor movie review
url_string = 'http://www.imdb.com/title/tt2250912/reviews?ref_=tt_ql_3'

reviews = scrapePage(url_string)

for review in reviews:
    print(review)
    print()