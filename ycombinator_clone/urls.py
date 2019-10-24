"""ycombinator_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main_site import views
# from . import views
from django.contrib.auth import views as auth_views
# from django.conf.urls import include
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home/', views.index),

    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/logout/', auth_views.LogoutView.as_view()),
    # path('accounts/logout/', auth_views.LoginView.as_view()),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html",redirect_field_name="next")),
    path('register/', views.register, name='register'),
    # path(r'^accounts/login$', 'django.contrib.auth.views.login')
    path('hide/<int:news_item_pk>/', views.hide),
    # path('read/<int:news_item_pk>/', views.read),
]
