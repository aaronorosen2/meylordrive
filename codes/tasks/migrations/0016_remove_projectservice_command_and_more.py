# Generated by Django 4.0.5 on 2023-09-25 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_projectmember_added_by_projectmember_admin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectservice',
            name='command',
        ),
        migrations.AddField(
            model_name='projectcommand',
            name='project_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.projectservice'),
        ),
    ]
