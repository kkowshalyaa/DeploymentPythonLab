#!/bin/bash                                                                        
if [ -e keys/$NAME.key  ]                                                          
then                                                                               
  echo "Key Exists"                                                                
else                                                                               
  ssh-keygen -t rsa -N "" -f keys/$NAME.key                                        
fi 
