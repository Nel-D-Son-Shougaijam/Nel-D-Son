# Generated by Django 5.1.1 on 2024-09-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='thumb',
            field=models.ImageField(blank=True, default='static/blog_cover.jpg', upload_to='static/'),
        ),
    ]
