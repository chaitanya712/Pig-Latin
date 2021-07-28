# Generated by Django 3.2.4 on 2021-06-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='title')),
                ('year', models.IntegerField(default=2000, verbose_name='releaseYear')),
                ('genre', models.TextField(default='none', verbose_name='genre')),
                ('actors', models.TextField(default='none', verbose_name='actors')),
                ('hitFlop', models.IntegerField(default=0, verbose_name='hitFlop')),
            ],
        ),
    ]
