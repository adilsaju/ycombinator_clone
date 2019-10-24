from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import Http404
from .models import NewsItem
from datetime import datetime
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from .templates 
# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    context={'news_items':NewsItem.objects.all().order_by('posted_on')}
    # username = request.POST['username']
    # password = request.POST['password']
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
    return render(request, "hello.html", context)
    # return HttpResponse("sjklajfklsaklasd")

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
    
def hide(request):
    id=request[0]
    auth=request[1]
# def logout_view(request):
#     logout(request)
#     return HttpResponse("you're logged out")
#     # Redirect to a success page.

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})