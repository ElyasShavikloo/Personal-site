from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('details/<slug:slug>', views.details, name='details'),
    path('list', views.article_list, name='list')
]
