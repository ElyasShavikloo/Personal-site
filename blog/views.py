from django.shortcuts import render
from .models import Article


def details(request, slug):
    article = Article.objects.get(slug=slug)

    return render(request, 'blog/details.html', context={'article': article})
