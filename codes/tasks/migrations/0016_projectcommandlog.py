# Generated by Django 4.0.5 on 2023-09-23 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_projectmember_added_by_projectmember_admin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCommandLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdout', models.TextField(blank=True, null=True)),
                ('file_log', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project_command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.projectcommand')),
            ],
        ),
    ]