# Generated by Django 5.0.1 on 2024-09-05 10:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0005_delete_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='likes',
            field=models.ManyToManyField(related_name='liked_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
