# Generated by Django 3.2.4 on 2021-06-25 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_rename_game_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='user_details',
        ),
    ]
