from django.forms import utils
from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models
from django.contrib.auth.decorators import login_required
from .forms import CreateArticles
from django.utils.text import slugify

# Create your views here.

def first(request):
    return render(request, 'first.html')


def articles_home(request):
    articles = models.Article.objects.all()
    return render(request, 'articles_home.html' , {'articles' : articles})

def articles_details(request,slug):
    article_dtl = models.Article.objects.get(slug=slug)
    return render(request, 'articles_details.html',{'article_dtl': article_dtl})

@login_required(login_url='/accounts/login/')
def articles_create(request):

    if request.method == 'POST':
        form = CreateArticles(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user 
            instance.save() #ee

            return redirect('articles_home')



    else:
        form = CreateArticles()
        
    return render(request, 'articles_create.html', {'form' : form})