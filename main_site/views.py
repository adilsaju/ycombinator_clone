from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import NewsItem
from datetime import datetime
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# from .templates 
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    # return HttpResponse("You're looking at question")

    # text="i'm just a sk8er boi, she's just a little girl"
    # obj4=NewsItem.objects.get(pk=4)
    context={'news_items':NewsItem.objects.all()}
    
    # obj5=NewsItem(url="www.google.com",hacker_news_url="ssad")
    # print(obj5)
    # obj5.save()

    # obj4=NewsItem.objects.get(pk=4)
    # context={'avril':obj4}

    # for i,v in enumerate(NewsItem.objects.all()):
    #     context[i]=v.url
    username = request.POST['username']
    password = request.POST['password']
    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # user = authenticate(request,username=username, password=password)
    # if user is not None:
    #     print('authed')
    #     login(request, user)
    #     return render(request, "hello.html", context)
    # else:
    #     print('no')
    #     return HttpResponse("You ain't logged in")
    return HttpResponse("sjklajfklsakl")

def logout_view(request):
    logout(request)
    # Redirect to a success page.

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})