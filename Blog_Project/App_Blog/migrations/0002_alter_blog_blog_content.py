# Generated by Django 5.0.2 on 2024-08-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.TextField(max_length=300, verbose_name='What is on your mind ?'),
        ),
    ]
