# Generated by Django 4.0.5 on 2022-09-23 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_usergroup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserGroup',
        ),
    ]
