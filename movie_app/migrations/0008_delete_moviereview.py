# Generated by Django 4.1.7 on 2023-02-28 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_moviereview'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MovieReview',
        ),
    ]