# Generated by Django 4.2.6 on 2023-10-12 06:25
# Generated by Django 4.2.6 on 2023-10-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
