from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator


def details(request, slug):
    article = Article.objects.get(slug=slug)

    return render(request, 'blog/details.html', context={'article': article})


def article_list(request):
    articles = Article.objects.all().order_by('-created')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 3)
    object_list = paginator.get_page(page_number)

    return render(request, 'blog/list.html', context={'articles': object_list})
