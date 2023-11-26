from django.shortcuts import render
from blog.models import Article, Category


def home(request):
    articles = Article.objects.all()

    return render(request, 'home/index.html', context={'articles': articles})



