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

# @csrf_exempt
# @login_required(login_url='/accounts/login')
# @require_http_methods(['POST'])
# def hide(request, news_item_pk):
#     print(news_item_pk)
#     news = get_object_or_404(NewsItem, pk=news_item_pk)
#     news.users.add(request.user)
#     return HttpResponse("hide clicked")

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