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

    # url="https://news.ycombinator.com/"
    urls=["https://news.ycombinator.com/news?p=1","https://news.ycombinator.com/news?p=2","https://news.ycombinator.com/news?p=3"]
    # res=requests.get(url,stream=True)
    tr1s=[]
    tr2s=[]
    for u in urls:
        res=requests.get(u)
        html=res.content
        soup=BeautifulSoup(html)
        tr1s_tmp=[]
        tr1s_tmp=soup.findAll('tr',{'class':'athing'})
        tr1s+=tr1s_tmp
        for tr1 in tr1s_tmp:
            tr2s.append(tr1.findNextSibling())

    url=[]
    title=[]
    hacker_news_url=[]
    upvote_count=[]
    comment_count=[]
    posted_on=[]
    for i in range(len(tr1s)):
        url.append(tr1s[i].select_one('td:nth-of-type(3) > a').get('href'))
        
    
        title.append(tr1s[i].select_one('td:nth-of-type(3) > a').get_text())

    
        # hacker_news_url.append(tr1s[i].select_one('td:nth-of-type(3) > span > a').get('href'))
        # hacker_news_url.append("https://news.ycombinator.com/"+tr2s[i].select_one('td:nth-of-type(2) > a:nth-of-type(3)').get('href'))
        if tr2s[i].select_one('td:nth-of-type(2) > span.age > a') == None:
            hacker_news_url.append('')
        else:
            hacker_news_url.append("https://news.ycombinator.com/"+tr2s[i].select_one('td:nth-of-type(2) > span.age > a').get('href'))


        if tr2s[i].select_one('td:nth-of-type(2) > span.score') == None:
            upvote_count.append('0')
        else:
            upvote_count.append(tr2s[i].select_one('td:nth-of-type(2) > span.score').get_text().split()[0])

    
        #exception handling
        if tr2s[i].select_one('td:nth-of-type(2) > a:nth-of-type(3)') == None:
            comment_count.append('0')
        elif tr2s[i].select_one('td:nth-of-type(2) > a:nth-of-type(3)').get_text() == "discuss":
            comment_count.append('0')
        else:
            comment_count.append(tr2s[i].select_one('td:nth-of-type(2) > a:nth-of-type(3)').get_text().split()[0])

        if tr2s[i].select_one('td:nth-of-type(2) > span.age > a') == None:
            posted_on.append('')
        else:
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
