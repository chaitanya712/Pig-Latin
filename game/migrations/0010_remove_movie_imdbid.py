# Generated by Django 3.2.4 on 2021-06-26 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_movie_imdbid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='imdbID',
        ),
    ]
