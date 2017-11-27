import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, json, request
from s6_scrape_score import score_imdb_url

app = Flask(__name__)

@app.route("/")
def main():
	return "Welcome!"

@app.route("/svm", methods=['POST'])
def svm():
	url = request.form.get('url', 'NONE')
	scrape_limit = request.form.get('scrape_limit', 'NONE')
	clf = 'svm'
	score = score_imdb_url(url, scrape_limit=scrape_limit, clf=clf)
	print("DONEEEEEEEEEEEEEEEEEEEEEEEEe")
	score = score * 10
	return str(score)

if __name__ == "__main__":
	app.run()