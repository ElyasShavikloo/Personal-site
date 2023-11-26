from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MessageForm
from .models import Article, Comment, Category, Message, Like
from django.core.paginator import Paginator
from django.views.generic.base import View, TemplateView, RedirectView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .mixins import CustomLoginRequiredView


def article_list(request):
    articles = Article.objects.all().order_by('-created')
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 3)
    object_list = paginator.get_page(page_number)

    return render(request, 'blog/list.html', context={'articles': object_list})


def searcher(request):
    search = request.GET.get('search')
    articles = Article.objects.filter(title__icontains=search)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 3)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/list.html', context={'articles': object_list})


def contact_us(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.age += 1
            return redirect('home:main')

    else:
        form = MessageForm()
    return render(request, 'blog/message_form.html', {'form': form})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/details.html'

    def __init__(self, **kwargs):
        super().__init__()
        self.object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.comments.filter(article__slug=self.object.slug, user_id=self.request.user.id).exists():
            context['commented'] = True

        elif self.request.user.likes.filter(article__slug=self.object.slug, user_id=self.request.user.id).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False

        return context


def like(request, slug, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(article__slug=slug, user_id=request.user.id)
            like.delete()
            return JsonResponse({'response': 'unliked'})

        except:
            like = Like.objects.create(article_id=pk, user_id=request.user.id)
            return JsonResponse({'response': 'liked'})


def comment(request, slug, pk):
    if request.user.is_authenticated:
        comment = Comment.objects.create(article_id=pk, user_id=request.user.id)
        comment.save()
        return JsonResponse({'response': 'commented'})


# class ArticleListView(ListView):
#     model = Article
#     template_name = 'blog/list.html'
#     paginate_by = 3


class MessageView(CreateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('home:main')

    # this project template's is awful, and I can't do or run some things like this function
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['titles'] = Message.objects.all()
    #
    #     return context


class MessageListView(CustomLoginRequiredView, ListView):
    model = Message
    template_name = 'blog/messages_list.html'


class UpdateMessageView(UpdateView):
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('blog:message_list')


class DeleteMessageView(DeleteView):
    model = Message
    success_url = reverse_lazy('blog:message_list')
