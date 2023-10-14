from django.shortcuts import render, redirect
from .models import Article, Comment
from django.core.paginator import Paginator


def details(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        if parent_id:
            patent_comment = Comment.objects.get(id=parent_id)
            body = request.POST.get('body')
            Comment.objects.create(body=body, article=article, user=request.user, parent_id=patent_comment)
        else:
            body = request.POST.get('body')
            Comment.objects.create(body=body, article=article, user=request.user)
            return redirect('home:main')

    return render(request, 'blog/details.html', context={'article': article})


def article_list(request):
    articles = Article.objects.all().order_by('-created')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 3)
    object_list = paginator.get_page(page_number)

    return render(request, 'blog/list.html', context={'articles': object_list})
