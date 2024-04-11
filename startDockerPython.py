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



import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


sender_email = "kowshalyaa.jk@gmail.com"
receiver_email = "kausalya2571998@gmail.com"
message = MIMEMultipart("alternative")
message["Subject"] = "Python Lab Access"
message["From"] = sender_email
message["To"] = receiver_email

# write the text/plain part
text = """\
Hi,
Check out the new post on the Mailtrap blog:
SMTP Server for Testing: Cloud-based or Local?
https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server/
Feel free to let us know what content would be useful for you!"""

# write the HTML part
html = """\
<div style="position: relative; width: 100%; height: 0; padding-top: 250.0000%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGCAGofyGA&#x2F;2NnkKSDRaeiCvS9vXr8-9A&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGCAGofyGA&#x2F;2NnkKSDRaeiCvS9vXr8-9A&#x2F;view?utm_content=DAGCAGofyGA&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">PythonLabSpace</a> by Kowshalyaa Kumaraguru
"""

# convert both parts to MIMEText objects and add them to the MIMEMultipart message
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

filename = "kkowshalyaa.pem"
attachment = open("/root/keys/kkowshalyaa.pem", "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
message.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(fromaddr, "mwlxdhtfndasmxjb") 
text = message.as_string() 
s.sendmail(fromaddr, toaddr, text) 
s.quit() 

print('Sent')


