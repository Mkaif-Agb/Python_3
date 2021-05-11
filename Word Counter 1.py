import requests
import operator
from bs4 import BeautifulSoup

def start(url):
    word_list = []
    Source_Code = requests.get(url).text
    soup = BeautifulSoup(Source_Code,'html.parser')
    for post_text in soup.findAll('a', {'class': 'result-title hdrlnk'}):
        content= post_text.string
        word = content.lower().split()
        for each_word in word:
            print(each_word)
            word_list.append(each_word)


start("https://mumbai.craigslist.co.in/d/architect-engineer-cad/search/egr")