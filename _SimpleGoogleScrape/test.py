 
import requests, re
from bs4 import BeautifulSoup

URL = 'https://www.google.com/search?pz=1&cf=all&ned=us&hl=en&tbm=nws&gl=us&as_q={query}' \
      '&as_occt=any&as_drrb=b&as_mindate={from_month}%2F%{from_day}%2F{year}' \
      '&as_maxdate={to_month}%2F{to_day}%2F{year}' \
      '&tbs=cdr%3A1%2Ccd_min%3A3%2F1%2F13%2Ccd_max%3A3%2F2%2F13' \
      '&authuser=0&start={start}'
    # &as_nsrc=Gulf%20Times only from Gulf and Times

#import newspaper
#from newspaper import Article
#from newspaper import ArticleException
#import nltk
#nltk.download('punkt')


def run(**params):
    #print("main link: ",URL.format(**params))
    response = requests.get(URL.format(**params))
    text = str(response.content)
    #print(text)
    #print(response.status_code)
    #possible_urls = re.findall(r'https?://\S+', text)
    #for url in possible_urls:
    #    print(url)
    soup=BeautifulSoup(response.content,'html5lib')
    for link in soup.find_all('a',class_=""):
        link = str(link)
        if "<a href=\"/url" in link:
            pure_link = link[16:]
            pure_link = pure_link.split("\"")
            pure_link = pure_link[0]
            print(pure_link)

for i in range(0,2000):
    run(query="Keyword", from_month=1, to_month=12, from_day=1, to_day=31, year=17, start=i*10)
