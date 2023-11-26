# Generated by Django 4.2.6 on 2023-10-29 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'پیام', 'verbose_name_plural': 'پیام ها'},
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='بدنه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='blog.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='articles/images', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=True, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='به روز رسانی شده'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=17, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.article', verbose_name='مقاله'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='بدنه'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='message',
            name='age',
            field=models.IntegerField(default=0, verbose_name='سن'),
        ),
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='ایجاد شده'),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=107, verbose_name='عنوان'),
        ),
    ]