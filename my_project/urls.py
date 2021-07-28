"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from game import views,templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.main_page,name='index'),
    path('register/', views.register,name='register'),
    path('', views.login,name='login'),
    path('home/', views.home,name='home'),
    path('movie/', views.movie_game,name='movie'),
    path('song/', views.song_game,name='song'),
    path('translator1/', views.translator,name='translator'),
    path('translator/', views.translator1 ,name='translator1'),
    path('check/', views.check_answer,name='check'),
    path('checkSong/', views.check_answer_song,name='checkSong'),

]
