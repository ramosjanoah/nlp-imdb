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
    review_list = soup.find(id="tn15content").findAll('p')

    # trash_p_list is some <p> that has to be excluded because it doesnt a review
    trash_p_list = ["<b>*** This review may contain spoilers ***</b>", 
                    '<a href="reviews-enter">Add another review</a>']
    
    # check the review content if it is in trash_p_list, if no, include it to review
    for review in review_list:
        if str(review.contents[0]) not in trash_p_list:
            all_review_content.append(review.contents[0])
    
    return all_review_content


# example string, thor movie review
url_string = 'http://www.imdb.com/title/tt3501632/reviews?ref_=tt_ql_3'

reviews = scrapePage(url_string)

for review in reviews:
    print(review)
    print()