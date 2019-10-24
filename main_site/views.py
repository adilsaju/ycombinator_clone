from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import Http404
from .models import NewsItem
from datetime import datetime
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import parsedatetime
# from .templates 
# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
    news=NewsItem.objects.exclude(users=request.user).order_by('posted_on')
    context={'news_items':news}
    # context={'news_items':NewsItem.objects.all().order_by('posted_on')}
    return render(request, "hello.html", context)

@csrf_exempt
@login_required(login_url='/accounts/login')
@require_http_methods(['POST'])
def hide(request, news_item_pk):
    print(news_item_pk)
    news = get_object_or_404(NewsItem, pk=news_item_pk)
    news.users.add(request.user)
    return HttpResponse("hide clicked")

@csrf_exempt
@login_required(login_url='/accounts/login')
@require_http_methods(['POST'])
def unhide(request, news_item_pk):
    # print(news_item_pk)
    news = get_object_or_404(NewsItem, pk=news_item_pk)
    # print("obj is:")
    # print(news)
    news.users.remove(request.user)
    return HttpResponse("unhide clicked")

@login_required(login_url='/accounts/login')
def about(request):
    return render(request,'about.html') 

@csrf_exempt
@login_required(login_url='/accounts/login')
def add(request):
    if request.method=="POST":
        url = request.POST['url']
        hackernews_url = request.POST['hackernews_url']
        title = request.POST['title']
        upvotes = request.POST['upvotes']
        comments = request.POST['comments']
        posted_on = request.POST['posted_on']

        cal = parsedatetime.Calendar()
        date_list = []
        date_db=[]
        # for date_str in posted_on:
        time_struct, parse_status = cal.parse(posted_on)
        res = datetime(*time_struct[:6])
        # date_list.append(res)
        date_db=res.strftime('%Y-%m-%d %H:%M:%S')

        # result = list(reversed([x for _,x in sorted(zip(date_list, posted_on))]))
        # print(posted_on)
        # print(date_db)
   
        obj=NewsItem(url=url,hacker_news_url=hackernews_url,title=title,upvote_count=upvotes,comment_count=comments,posted_on=date_db )
        # print(obj.posted_on)
        obj.save()

        return HttpResponse("added")
    else: 
        return render(request,'add-news-item.html')

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect('/')
    else:
        form=UserCreationForm()
    context={'form':form}
    return render(request,'registration/register.html',context)

@csrf_exempt
@login_required(login_url='/accounts/login')
# @require_http_methods(['GET'])
def hidden(request):
    news=NewsItem.objects.filter(users=request.user).order_by('posted_on')
    context={'news_items':news}
    # context={'news_items':NewsItem.objects.all().order_by('posted_on')}
    return render(request, "hidden-view.html", context)

    