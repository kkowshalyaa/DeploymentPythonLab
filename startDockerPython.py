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


stdin, stdout, stderr = sshcon.exec_command("sudo apt-get update")
time.sleep(20)
stdin, stdout, stderr = sshcon.exec_command("sudo apt-get install docker.io -y")
time.sleep(20)
stdin, stdout, stderr = sshcon.exec_command("sudo systemctl start docker")
stdin, stdout, stderr = sshcon.exec_command("sudo systemctl enable docker")

stdin, stdout, stderr = sshcon.exec_command("git clone https://github.com/kkowshalyaa/PythonLab.git")
stdin, stdout, stderr = sshcon.exec_command("sudo docker build -t python-lab PythonLab/")



# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
fromaddr = "kowshalyaa.jk@gmail.com"
toaddr = "kausalya2571998@gmail.com"
msg = MIMEMultipart() 
msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] = "Subject of the Mail"
body = "Body_of_the_mail"
msg.attach(MIMEText(body, 'plain')) 
filename = "kkowshalyaa.pem"
attachment = open("/root/keys/kkowshalyaa.pem", "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(fromaddr, "Password_of_the_sender") 
text = msg.as_string() 
s.sendmail(fromaddr, toaddr, text) 
s.quit() 


