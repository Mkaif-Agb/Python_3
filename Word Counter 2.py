import requests
import operator
from bs4 import BeautifulSoup
import array

def start(url):
    word_list = []
    Source_Code = requests.get(url).text
    soup = BeautifulSoup(Source_Code,'html.parser')
    for post_text in soup.findAll('a', {'class': 'result-title hdrlnk'}):
        content= post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_word_list(word_list)



def clean_word_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbol = "!@#$%^&*()_+=-|\"[]';/.,'"
        for i in range(0,len(symbol)):
            word = word.replace(symbol[i],"")
        if len(word)>1:
            print(word)
            clean_word_list.append(word)











start("https://mumbai.craigslist.co.in/d/architect-engineer-cad/search/egr")