# python bot that scrapes and organise release changes of mysql
from bs4 import BeautifulSoup
import requests
from .models import NewsItem

print("-"*100)
print("Hackernews parser")
print("-"*100)

url="https://news.ycombinator.com/"
# res=requests.get(url,stream=True)
res=requests.get(url)
html=res.content
soup=BeautifulSoup(html)

# links=soup.find_all('a',{'class':'storylink'})
# print(links)

# table=soup.find_all('table')[2]
# print(table)

# table_body = table.select('tbody')

tr1s=soup.findAll('tr',{'class':'athing'})
tr2s=[]
for tr1 in tr1s:
    tr2s.append(tr1.findNextSibling())

url=[]
for i in range(3):
    url.append(tr1s[i].select_one('td:nth-of-type(3) > a').get('href'))

hacker_news_url=[]
for i in range(3):
    hacker_news_url.append(tr1s[i].select_one('td:nth-of-type(3) > span > a').get('href'))

upvote_count=[]
for i in range(3):
    upvote_count.append(tr2s[i].select_one('td:nth-of-type(2) > span').get_text())

comment_count=[]
for i in range(3):
    comment_count.append(tr2s[i].select_one('td:nth-of-type(2) > a:nth-of-type(3)').get_text())

posted_on=[]
for i in range(3):
    posted_on.append(tr2s[i].select_one('td:nth-of-type(2) > span.age > a').get_text())

# links=soup.select("#hnmain > tr:nth-child(3) > td > table")

# table=soup.select('#hnmain > tbody')

# tt1=soup.findChild(table)
# for table in tables:
#     print(table)
print(url)
print(hacker_news_url)
print(upvote_count)
print(comment_count)
print(posted_on)
# print(links[2].get('href'))