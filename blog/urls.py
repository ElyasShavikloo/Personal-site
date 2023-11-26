from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('list', views.article_list, name='list'),
    path('search', views.searcher, name='search'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('message', views.MessageView.as_view(), name='message'),
    path('article_details/<slug:slug>', views.ArticleDetailView.as_view(), name='article_details'),
    path('message_list', views.MessageListView.as_view(), name='message_list'),
    path('message/edit/<int:pk>', views.UpdateMessageView.as_view(), name='message_edit'),
    path('message/delete/<int:pk>', views.DeleteMessageView.as_view(), name='message_delete'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like'),

]
