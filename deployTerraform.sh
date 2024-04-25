cp -r TerrformDeploy ${1}_Terraform 
cd ${1}_Terraform                                                                  
terraform init                                                                     
sleep 10                                                                           
terraform plan -var "name=${1}"                                                    
sleep 20                                                                           
terraform apply -auto-approve -var "name=${1}"                                     
sleep 90
