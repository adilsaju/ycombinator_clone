from django.db import models
from datetime import datetime
# Create your models here.


class NewsItem(models.Model):
    url = models.CharField(max_length=500, default="",unique=True)
    title = models.CharField(max_length=500, default="")
    hacker_news_url = models.CharField(max_length=500, default="")
    posted_on = models.DateTimeField(default=datetime.now)
    # posted_on = models.CharField(max_length=100,default="")
    upvote_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    contents=models.TextField(default="")

    def __str__(self):              # __unicode__ on Python 2
        return self.url
