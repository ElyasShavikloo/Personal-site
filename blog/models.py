from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=17, verbose_name="عنوان")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="عنوان")
    category = models.ManyToManyField(Category, related_name='articles', verbose_name="دسته بندی")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    image = models.ImageField(upload_to='articles/images', blank=True, null=True, verbose_name="تصویر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده")
    updated = models.DateTimeField(auto_now=True, verbose_name="به روز رسانی شده")
    body = models.TextField(verbose_name="بدنه")
    status = models.BooleanField(default=True, verbose_name="وضعیت")
    slug = models.SlugField(null=True, blank=True, unique=True, verbose_name="اسلاگ")

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="47px" height="37px">')
        else:
            return format_html('<h3 style="color: red">بدون تصویر</h3>')

    show_image.short_description = ' تصویر'

    def get_absolut_url(self):
        return reverse('blog:article_details', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title} {self.body[:30]}'

    def update_counter(self):
        pass


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name="مقاله")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="کاربر")
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField(verbose_name="بدنه")
    created = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد شده")

    def __str__(self):
        return self.body[:37]

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'


class Message(models.Model):
    title = models.CharField(max_length=107, verbose_name="عنوان")
    text = models.TextField(verbose_name="پیام")
    email = models.EmailField( verbose_name="ایمیل")
    age = models.IntegerField(default=0, verbose_name="سن")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="ایجاد شده")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes', verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده')

    def __str__(self):
        return f'{self.user.username} - {self.article.title}'

    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"
        ordering = ("-created_at",)
