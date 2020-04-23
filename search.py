import urllib
import re
import requests
from bs4 import BeautifulSoup

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

query = "dolar hoy"
query = query.replace(' ', '+')
URL = "https://google.com/search?q="+ query

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)
print(query)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser") 
    print(soup.find_all("div", class_=re.compile("vk_c card-section")))
    #results = []
    #for g in soup.find_all('div', class_='sfgbx'):
    #    print(g)
    #    print(results)
        #anchors = g.find_all('span')
        #print(anchors)
        #if anchors:
        #    link = anchors[0]['href']
        #    title = g.find('h3').text
        #    item = {
        #        "title": title,
        #        "link": link
        #    }
        #    results.append(item)
    #print(results)