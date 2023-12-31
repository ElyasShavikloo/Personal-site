# Generated by Django 4.2.6 on 2023-10-29 05:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'حساب کاربری', 'verbose_name_plural': 'حساب های کاربری'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='father_name',
            field=models.CharField(max_length=30, verbose_name='نام پدر'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='national_code',
            field=models.CharField(max_length=10, verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/img', verbose_name='تصویر کاربر'),
        ),
    ]
