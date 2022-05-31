from django.core.management.base import BaseCommand
from paramiko.client import SSHClient, AutoAddPolicy
import threading
from pssh.clients import ParallelSSHClient

from pssh.config import HostConfig


from tasks.models import Task, Server

def run_job(server, task):
    print("Run job server: %s %s" % (server.username, server.ip_address))
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(server.ip_address, username=server.username)
    # stdin, stdout, stderr = client.exec_command('git clone git@github.com:aaronorosen/django-zillow.git')
    stdin, stdout, stderr = client.exec_command('sudo apt-get update')

    task.stdout = stdout.read().decode().strip()
    task.stderr = stderr.read().decode().strip()
    task.save()

    if task.stderr != "":
        raise Exception('There was an error pulling the runtime: {}'.format(task.stderr))
    print("HERE is program output: %s" % task.stdout)
    client.close()

class Command(BaseCommand):
    help = 'run the tasks'

    def add_arguments(self, parser):
        # parser.add_argument('is_local', type=str)
        pass

    def handle(self, *args, **options):
        print("Start...")
        tasks = Task.objects.filter(status='not-active')
        print("Number of tasks to run: %s" % len(tasks))

        threads = []
        hosts = []
        host_config = []
        servers = Server.objects.filter()
        for server in servers:
            hosts.append(server.ip_address)
            host_config.append(
                HostConfig(port=22, user='aaronoro',
                            private_key='server-key'),
                )

        client = ParallelSSHClient(hosts, host_config=host_config)

        output = client.run_command('cd ~; git clone git@github.com:aaronorosen/django-zillow.git')
        output = client.run_command('uname')
        client.join()

        for host_output in output:
            for line in host_output.stdout:
                print(line)
            exit_code = host_output.exit_code
            print("Error exit code: %s" % exit_code)

        return

        for task in tasks:
            print(task)
            server = Server.objects.filter().first()
            t = threading.Thread(target=run_job, args=(server, task))
            t.start()
            threads.append(t)
        for server in servers:
            task = Task()
            t = threading.Thread(target=run_job, args=(server, task))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
