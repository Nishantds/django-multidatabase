# Generated by Django 3.1.2 on 2021-07-10 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='User',
        ),
    ]
