#!/bin/bash                                                                        
if [ -e /home/ubuntu/DeploymentPythonLab/Keys/$1.key  ]                                                          
then                                                                               
  echo "Key Exists"                                                                
else                                                                               
  ssh-keygen -t rsa -N "" -f /home/ubuntu/DeploymentPythonLab/Keys/$1.key                                        
fi 
