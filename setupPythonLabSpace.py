import subprocess
import re
import paramiko 
import time
import sys 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

#Get EC2 instance IP from Terraform output 
output = subprocess.getoutput('./getPublic.sh ' + sys.argv[0])
ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', output)[0]

#Establish SSH Connection to EC2 Instance
myuser   = 'ubuntu'
mySSHK   = '/root/keys/' + sys.argv[0] + '.key'
sshcon   = paramiko.SSHClient() 
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshcon.connect(ip, username=myuser, key_filename=mySSHK)

#Build Docker image on EC2 Instance
stdin, stdout, stderr = sshcon.exec_command("sudo apt-get update")
time.sleep(20)
stdin, stdout, stderr = sshcon.exec_command("sudo apt-get install docker.io -y")
time.sleep(20)
stdin, stdout, stderr = sshcon.exec_command("sudo systemctl start docker")
stdin, stdout, stderr = sshcon.exec_command("sudo systemctl enable docker")

stdin, stdout, stderr = sshcon.exec_command("git clone https://github.com/kkowshalyaa/PythonLab.git")
time.sleep(20)
stdin, stdout, stderr = sshcon.exec_command("sudo docker build -t python-lab PythonLab/")
time.sleep(300)


#Send Key and IP to the students
fromaddr = "kowshalyaa.jk@gmail.com"
toaddr = "kausalya2571998@gmail.com"
msg = MIMEMultipart() 
msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] = "Python Lab Space Credentials."
body = "Dear Student, \n Your EC2 instance IP is " + ip + ". The Key to access EC2 instance is attached in this mail, please follow the instructions attached in this mail to use the instance, you can also check out the instructions at https://www.canva.com/design/DAGCAGofyGA/2NnkKSDRaeiCvS9vXr8-9A/view"
msg.attach(MIMEText(body, 'plain')) 
cmd = "openssl rsa -in /root/keys/" + sys.argv[0] + ".key -text > /root/keys/" + sys.argv[0] + ".pem"
output = subprocess.getoutput(cmd)
filename =  sys.argv[0] ".pem"
attachment = open("/root/keys/" + sys.argv[0] + ".pem", "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
filename = "Instructions.pdf"
attachment = open("/root/PythonLab.pdf", "rb")
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(fromaddr, "mwlxdhtfndasmxjb") 
text = msg.as_string() 
s.sendmail(fromaddr, toaddr, text) 
s.quit() 

