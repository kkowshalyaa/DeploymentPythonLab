#!/bin/bash                                                                        
if [ -e keys/$1.key  ]                                                          
then                                                                               
  echo "Key Exists"                                                                
else                                                                               
  ssh-keygen -t rsa -N "" -f keys/$1.key                                        
fi 
