#!/bin/bash                                                                        
if [ -e /home/ubuntu/DeploymentPythonLab/Keys/$1.pem  ]                                                          
then                                                                               
  echo "Key Exists"                                                                
else                                                                               
  ssh-keygen -m PEM -t rsa -b 8192 -N "" -f /home/ubuntu/DeploymentPythonLab/Keys/$1.pem                                        
fi 
