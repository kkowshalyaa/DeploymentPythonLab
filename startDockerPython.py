import subprocess
import re
import paramiko 
import time

output = subprocess.getoutput('./getPublic.sh')
ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', output)[0]

myuser   = 'ubuntu'
mySSHK   = '/root/keys/kkowshalyaa.key'
sshcon   = paramiko.SSHClient() 
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshcon.connect(ip, username=myuser, key_filename=mySSHK)


stdin, stdout, stderr = ssh.exec_command("sudo apt-get update")
time.sleep(20)
stdin, stdout, stderr = ssh.exec_command("sudo apt-get install docker.io -y")
time.sleep(20)
stdin, stdout, stderr = ssh.exec_command("sudo systemctl start docker")
stdin, stdout, stderr = ssh.exec_command("sudo systemctl enable docker")

stdin, stdout, stderr = ssh.exec_command("git clone https://github.com/kkowshalyaa/PythonLab.git")
stdin, stdout, stderr = ssh.exec_command("sudo docker build -t python-lab PythonLab/")




