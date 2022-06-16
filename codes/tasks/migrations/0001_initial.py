# Generated by Django 4.0.5 on 2022-06-16 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemSpecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('architecture', models.CharField(max_length=100)),
                ('cpu_op_modes', models.CharField(max_length=100)),
                ('byte_order', models.CharField(max_length=100)),
                ('cpu_s', models.CharField(max_length=100)),
                ('on_line_cpu_s_list', models.CharField(max_length=100)),
                ('threads_per_core', models.CharField(max_length=100)),
                ('cores_per_socket', models.CharField(max_length=100)),
                ('sockets', models.CharField(max_length=100)),
                ('numa_nodes', models.CharField(max_length=100)),
                ('vendor_id', models.CharField(max_length=100)),
                ('cpu_family', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('stepping', models.CharField(max_length=100)),
                ('cpu_mhz', models.CharField(max_length=100)),
                ('bogo_mips', models.CharField(max_length=100)),
                ('hypervisor_vendor', models.CharField(max_length=100)),
                ('virtualization_type', models.CharField(blank=True, max_length=100, null=True)),
                ('l1d_cache', models.CharField(max_length=100)),
                ('l1i_cache', models.CharField(max_length=100)),
                ('l2_cache', models.CharField(max_length=100)),
                ('l3_cache', models.CharField(max_length=100)),
                ('total_memory', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=64, null=True)),
                ('command', models.CharField(blank=True, max_length=4096, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('repo', models.CharField(blank=True, max_length=4096, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdout', models.TextField(blank=True, null=True)),
                ('file_log', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=64)),
                ('username', models.CharField(blank=True, max_length=4096, null=True)),
                ('password', models.CharField(blank=True, max_length=4096, null=True)),
                ('name', models.CharField(blank=True, max_length=4096, null=True)),
                ('error', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('alive', models.BooleanField(default=False)),
                ('in_use', models.BooleanField(default=False)),
                ('system_specs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.systemspecs')),
            ],
        ),
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo', models.CharField(max_length=4096)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='GithubHook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.BooleanField(default=False)),
                ('pipeline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.pipeline')),
            ],
        ),
        migrations.CreateModel(
            name='PipelineServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pipeline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.pipeline')),
                ('server', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.server')),
            ],
            options={
                'unique_together': {('pipeline', 'server')},
            },
        ),
    ]
