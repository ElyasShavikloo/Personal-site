from blog.models import Article, Category


def recent_articles(request):
    recent_article = Article.objects.order_by('-created')[:3]

    return {'recent_article': recent_article}


def category(request):
    categories = Category.objects.all()

    return {'categories': categories}
