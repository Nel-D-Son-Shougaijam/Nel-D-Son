from django.urls import path
from . import views
#this is a urls file

app_name = "home"

urlpatterns = [
    path('',views.home,name = 'home'),
    path('stories',views.stories,name = 'stories'),
    path('about',views.about,name = 'about'),
    path('sef/<str:slug>',views.story_detail,name = 'story_detail'),
    path('<str:slug>',views.like,name = 'like'),
    
]
