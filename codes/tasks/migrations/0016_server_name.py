# Generated by Django 4.0.5 on 2022-06-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_alter_pipelineserver_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='name',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
    ]
