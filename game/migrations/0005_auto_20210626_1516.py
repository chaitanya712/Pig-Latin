# Generated by Django 3.2.4 on 2021-06-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_rename_user_user_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='sex',
        ),
        migrations.AlterField(
            model_name='user_details',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]
