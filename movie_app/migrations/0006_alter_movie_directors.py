# Generated by Django 4.1.7 on 2023-02-27 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_alter_reviews_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_director', to='movie_app.director'),
        ),
    ]
