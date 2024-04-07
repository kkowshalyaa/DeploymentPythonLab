import subprocess
import re
output = subprocess.getoutput('./getPublic.sh')
ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', output)[0]

myuser   = 'ubuntu'
mySSHK   = '/keys/kkowshalyaa.key'
sshcon   = paramiko.SSHClient() 
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshcon.connect(ip, username=myuser, key_filename=mySSHK)

