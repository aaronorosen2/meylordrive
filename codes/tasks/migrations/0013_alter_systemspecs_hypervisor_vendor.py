# Generated by Django 4.0.5 on 2023-08-19 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_projectservicelog_remove_tasklog_task_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemspecs',
            name='hypervisor_vendor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
