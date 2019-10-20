# python bot that scrapes and organise release changes of mysql

def run():
    # print("Test")
    from bs4 import BeautifulSoup
    import requests
    from main_site.models import NewsItem

    import parsedatetime
    from datetime import datetime

    print("-"*100)
    print("Hackernews parser")
    print("-"*100)

    url="https://news.ycombinator.com/"
    # res=requests.get(url,stream=True)
    res=requests.get(url)
    html=res.content
    soup=BeautifulSoup(html)
    tr1s=soup.findAll('tr',{'class':'athing'})
    tr2s=[]
    for tr1 in tr1s:
        tr2s.append(tr1.findNextSibling())



    url=[]
    for i in range(3):
        url.append(tr1s[i].select_one('td:nth-of-type(3) > a').get('href'))
        
    title=[]
    for i in range(3):
        title.append(tr1s[i].select_one('td:nth-of-type(3) > a').get_text())

    hacker_news_url=[]
    for i in range(3):
        # hacker_news_url.append(tr1s[i].select_one('td:nth-of-type(3) > span > a').get('href'))
        hacker_news_url.append("https://news.ycombinator.com/"+tr2s[i].select_one('td:nth-of-type(2) > a:nth-of-type(3)').get('href'))

    upvote_count=[]
    for i in range(3):
        upvote_count.append(tr2s[i].select_one('td:nth-of-type(2) > span').get_text().split()[0])

    comment_count=[]
    for i in range(3):
        #exception handling
        if tr2s[i].select_one('td:nth-of-type(2) > a:nth-of-type(3)').get_text() == "discuss":
            comment_count.append('0')
        else:
            comment_count.append(tr2s[i].select_one('td:nth-of-type(2) > a:nth-of-type(3)').get_text().split()[0])

    posted_on=[]
    for i in range(3):
        posted_on.append(tr2s[i].select_one('td:nth-of-type(2) > span.age > a').get_text())

    # test=['7 hours ago', '58 minutes ago', '13 hours ago']
    cal = parsedatetime.Calendar()
    date_list = []
    date_db=[]
    for date_str in posted_on:
        time_struct, parse_status = cal.parse(date_str)
        res = datetime(*time_struct[:6])
        # date_list.append(res)
        date_db.append(res.strftime('%Y-%m-%d %H:%M:%S'))

    # result = list(reversed([x for _,x in sorted(zip(date_list, posted_on))]))
    print(posted_on)
    # print(date_list)
    print(date_db)
    # date_list[0].strftime('%Y-%m-%d %H:%M:%S')
    # print(result)

    for i in range(len(url)):
        item,created = NewsItem.objects.get_or_create(url=url[i])
        if created:
            print( 'New item was created')
            item.title=title[i]
            item.hacker_news_url=hacker_news_url[i]
            item.posted_on=date_db[i]
            item.comment_count=comment_count[i]
            item.upvote_count=upvote_count[i]
        else:
            print('updating current item')
            item.title=title[i]
            item.hacker_news_url=hacker_news_url[i]
            item.posted_on=date_db[i]
            item.comment_count=comment_count[i]
            item.upvote_count=upvote_count[i]

        item.save()
        # obj=NewsItem(url=url[i],title=title[i],hacker_news_url=hacker_news_url[i],posted_on=posted_on[i],comment_count=comment_count[i],upvote_count=upvote_count[0])
        # obj.save()


    print(url)
    print(title)
    print(hacker_news_url)
    print(upvote_count)
    print(comment_count)
    # print(posted_on)
    print(date_db)
    # print(links[2].get('href'))
