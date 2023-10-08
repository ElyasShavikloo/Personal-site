from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=17)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=17)
    category = models.ManyToManyField(Category, related_name='articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    status = models.BooleanField(default=True)
    # slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.title} {self.body[:30]}'
