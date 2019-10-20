from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import NewsItem
from datetime import datetime

# from .templates 
# Create your views here.
def index(request):
    # return HttpResponse("You're looking at question")
    text="i'm just a sk8er boi, she's just a little girl"
    obj4=NewsItem.objects.get(pk=4)
    context={'avril':obj4}

    obj5=NewsItem(url="www.google.com",hacker_news_url="ssad")
    print(obj5)
    obj5.save()
    # obj4=NewsItem.objects.get(pk=4)
    # context={'avril':obj4}

    return render(request, "hello.html", context)

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})