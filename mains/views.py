from django.shortcuts import render,redirect
from .models import Story

# Create your views here.

def home(request):
    story = Story.objects.all()
    return render(request,'home.html',{'story':story})

def stories(request):
    story = Story.objects.all()
    return render(request,'stories.html',{'story':story})

def about(request):
    return render(request,'about.html')

def story_detail(request,slug):
    story= Story.objects.get(slug=slug)
    try:
        comment = Comment.objects.get(article=story)
    except:
        comment = None
    return render(request,'story_detail.html',{'story':story,'comment':comment})

def like(request,slug):
    story = Story.objects.get(slug=slug)
    if request.user in story.likes.all():
        story.likes.remove(request.user)
    else:
        story.likes.add(request.user)
    return render(request,'story_detail.html',{'story':story})

