# Generated by Django 4.2.6 on 2023-10-08 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
