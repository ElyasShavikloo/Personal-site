from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=17)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, related_name='articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    status = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolut_url(self):
        return reverse('blog:details', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title} {self.body[:30]}'


class Comment(models.Model):
    article = models. ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models. ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:37]

