# python bot that scrapes and organise release changes of mysql

def run():
    # print("Test")
    from bs4 import BeautifulSoup
    import requests
    from main_site.models import NewsItem

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
        comment_count.append(tr2s[i].select_one('td:nth-of-type(2) > a:nth-of-type(3)').get_text().split()[0])

    posted_on=[]
    for i in range(3):
        posted_on.append(tr2s[i].select_one('td:nth-of-type(2) > span.age > a').get_text())

    for i in range(len(url)):
        item,created = NewsItem.objects.get_or_create(url=url[i])
        if created:
            print( 'New car was created')
            # car.slug = 'new-car-slug'
        else:
            print('changing current')
            item.title=title[i]
            item.hacker_news_url=hacker_news_url[i]
            item.posted_on=posted_on[i]
            item.comment_count=comment_count[i]
            item.upvote_count=upvote_count[i]
            # do whatever needs to be done here
            # with the existing car object, which will
            # be car
            # car.name = 'new name'

        item.save()

        # for obj in NewsItem.objects.all():
        #     if url[i] in obj.url:
        #         print('same')
        #         # obj.title=title[i]
        #         # obj.hacker_news_url=hacker_news_url[i]
        #         # obj.posted_on=posted_on[i]
        #         # obj.comment_count=comment_count[i]
        #         # obj.upvote_count=upvote_count[i]
        #         # obj.save()
        #         pass
        #         # NewsItem.objects.get(url=url[i])
        #     else:
        #         obj=NewsItem(url=url[i],title=title[i],hacker_news_url=hacker_news_url[i],posted_on=posted_on[i],comment_count=comment_count[i],upvote_count=upvote_count[i])
        #         obj.save()
        # obj=NewsItem(url=url[i],title=title[i],hacker_news_url=hacker_news_url[i],posted_on=posted_on[i],comment_count=comment_count[i],upvote_count=upvote_count[0])
        # obj.save()


    print(url)
    print(title)
    print(hacker_news_url)
    print(upvote_count)
    print(comment_count)
    print(posted_on)
    # print(links[2].get('href'))
