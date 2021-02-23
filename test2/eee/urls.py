"""test2 URL Configuration

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
from django.urls import path,include,re_path
from . import views

app_name = 'eee'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('registration/',views.registration,name='registration'),
    path('mainpage/',views.mainpage,name='mainpage'),
    path('contact/',views.contact,name='contact'),
    path('listing_filter/',views.listing_filter,name='listing_filter'),
    path('stu_search/',views.stu_search,name='stu_search'),
    path('profile/',views.profile,name='profile'),
    path('job/',views.job,name='job'),
    path('<int:id>/job_general',views.job_general,name='job_general'),
    path('jobupdate/',views.jobupdate,name='jobupdate'),
    path('education/',views.education,name='education'),
    path('<int:id>/education_general/',views.education_general,name='education_general'),
    path('msc/',views.msc,name='msc'),
    path('<int:id>/phd/',views.phd,name='phd'),
    path('paper/',views.paper,name='paper'),
    path('phd1/',views.phd1,name='phd1'),
    #path('infoupdate/',views.infoupdate,name='infoupdate'),
    #path('logout/', views.logout,name='logout'),
    #path('<int:id>/msc/',views.msc,name='msc'),
]
