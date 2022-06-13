from tasks.models import Task, Server, SystemSpecs
import paramiko
import os
from django.core.management.base import BaseCommand
# from paramiko.client import SSHClient, AutoAddPolicy
import threading
server_prints = {}


def run_job(server, task):
    print("Run job server: %s %s" % (server.username, server.ip_address))
<<<<<<< HEAD
    finger_print = configure_node(server)
    return finger_print


def run_log_ssh_command(ssh, server, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    file1 = open("%s.txt" % server.ip, "a")
    file1.write(stderr.read().decode('utf-8') + "\n")
    print("COMMAND[%s]" % command)
    print("OUTPUT[%s]" % stdout.read())
    print("STDERROR[%s]" % stderr.read())


def fingerprint_node(ssh, server):
    # output = str(temp.communicate())
    stdin, stdout, stderr = ssh.exec_command("lscpu")
    memin, memout, memerr = ssh.exec_command("free -m")

    output = str(stdout.read())
    memoutput = str(memout.read())
    # print("OUTPUT", memoutput)
    memoutput = memoutput.split("\n")[0].split("\\n")
    totalMemory = memoutput[1].split(":")[1].strip()[0:5].strip()
    dic = {"total_memory": totalMemory}
    x = output.split("\n")[0].split("\\n")
    # print(x)
    for c, i in enumerate(x):
        if c < 22:
            if c == 0:
                dic[i[2:].split(":")[0]] = i[3:].split(":")[1].strip()
            if c != 0:
                dic[i.split(":")[0]] = i[1:].split(":")[1].strip()
    # print(dic)
    server_prints[server.id] = dic
    print(dic)


def configure_node(server):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

    # ssh.load_host_keys(os.path.expanduser(
    #    os.path.join("~", ".ssh", "known_hosts")))
    ssh.connect(server.ip_address, username=server.username)
    fingerprint_node(ssh, server)
    command = ("scp server-key %s@%s:~/"
               % (server.username, server.ip_address))
    os.system(command)

#    run_log_ssh_command(ssh, server, "ssh-agent")
#    run_log_ssh_command(ssh, server, "ssh-add server-key")
#    run_log_ssh_command(ssh, server, "rm -fr ~/django-zillow")
#    run_log_ssh_command(
#        ssh, server, "ssh-keyscan github.com >> ~/.ssh/known_hosts")


#    run_log_ssh_command(
#        ssh, server,
#        'git clone git@github.com:aaronorosen/django-zillow.git')
#    run_log_ssh_command(ssh, server, 'sudo touch /var/lib/dpkg/status')

#    run_log_ssh_command(
#        ssh, server, 'sudo apt-get update && apt-get upgrade -y')
#    run_log_ssh_command(
#        ssh, server,
#        'sudo rm -fr "rm -f /etc/apt/sources.list.d/buildkite-agent.list')
#    run_log_ssh_command(
#        ssh, server,
#        'cd ~/django-zillow; COMMAND="kingtax"; DOWN_SCRIPT="./scripts/batch-down2.sh"; SCRIPT="./scripts/batch2.sh"; STATE="WA" sudo bash scripts/batch2.sh')
    ssh.close()


def populate_system_specs(server, system_spec):
    if not server.system_specs:
        server.system_specs = SystemSpecs()
    server.system_specs.architecture = system_spec['Architecture']
    server.system_specs.cpu_op_modes = system_spec['CPU op-mode(s)']
    server.system_specs.byte_order = system_spec['Byte Order']
    # server.system_specs.address_sizes = system_spec['Address sizes']
    server.system_specs.cpu_s = system_spec['CPU(s)']
    server.system_specs.on_line_cpu_s_list = system_spec['On-line CPU(s) list']
    server.system_specs.threads_per_core = system_spec['Thread(s) per core']
    server.system_specs.cores_per_socket = system_spec['Core(s) per socket']
    server.system_specs.sockets = system_spec['Socket(s)']
    server.system_specs.numa_nodes = system_spec['NUMA node(s)']
    server.system_specs.vendor_id = system_spec['Vendor ID']
    server.system_specs.cpu_family = system_spec['CPU family']
    server.system_specs.model = system_spec['Model']
    server.system_specs.model_name = system_spec['Model name']
    server.system_specs.stepping = system_spec['Stepping']
    # server.system_specs.frequency_boost = system_spec['CPU max MHz']
    server.system_specs.cpu_mhz = system_spec['CPU MHz']
    # server.system_specs.cpu_max_mhz = system_spec['CPU max MHz']
    # server.system_specs.cpu_min_mhz = system_spec['CPU min MHz']
    server.system_specs.bogo_mips = system_spec['BogoMIPS']
    server.system_specs.hypervisor_vendor = system_spec['Hypervisor vendor']
    server.system_specs.virtualization_type = system_spec.get(
        'Virtualization Type')
    server.system_specs.l1d_cache = system_spec['L1d cache']
    server.system_specs.l1i_cache = system_spec['L1i cache']
    server.system_specs.l2_cache = system_spec['L2 cache']
    server.system_specs.l3_cache = system_spec['L3 cache']
    server.system_specs.total_memory = system_spec['total_memory']
    server.system_specs.save()
    server.save()

=======
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(server.ip_address, username=server.username,allow_agent=True) 
    #print(pprint.pprint(dir(client)))
    #client.channel.request_forward_agent()
    #stdin, stdout, stderr = client.exec_command('ls -alh /etc/apt/sources.list.d/')
    #stdin, stdout, stderr = client.exec_command('sudo rm -f /etc/apt/sources.list.d/buildkite-agent.list.save ; sudo cp /var/lib/dpkg/status-old /var/lib/dpkg/status ; sudo apt-get update -y')
    #stdin, stdout, stderr = client.exec_command('sudo cp /var/lib/dpkg/status-old /var/lib/dpkg/status')
    #stdin, stdout, stderr = client.exec_command('sudo mkdir /var/lib/dpkg ; sudo touch /var/lib/dpkg/status ; sudo apt-get update -y')
    stdin, stdout, stderr = client.exec_command('sudo apt-get update -y')

    task.stdout = stdout.read().decode().strip()
    task.stderr = stderr.read().decode().strip()
    task.save()

    if task.stderr != "":
        print("%s@%s" % (server.username, server.ip_address))
        print(task.stderr)
        #raise Exception('There was an error pulling the runtime: {}'.format(task.stderr))
    print(task.stdout)
    client.close()
>>>>>>> cfd6fd60fc3594919fcda060a5c383c6e9a52999

class Command(BaseCommand):
    help = 'run the tasks'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("Start...")
        tasks = Task.objects.filter(status='not-active')
        print("Number of tasks to run: %s" % len(tasks))

        threads = []
        hosts = []
        host_config = []
        servers = Server.objects.filter()
        # for task in tasks:
        #    server = Server.objects.filter().first()
        #    t = threading.Thread(target=run_job, args=(server, task))
        #    t.start()
        #    threads.append(t)

        for server in servers:
            task = Task()
            t = threading.Thread(target=run_job, args=(server, task))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        for server_print in server_prints.keys():
            populate_system_specs(server, server_prints[server_print])
