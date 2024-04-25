# Creating key-pair on AWS using SSH-public key
resource "aws_key_pair" "deployer" {
  key_name   = var.key-name
  public_key = file("/home/ubuntu/DeploymentPythonLab/Keys/${var.name}.key.pub")
}

# Creating security group to restrict/allow inbound connectivity
resource "aws_security_group" "network-security-group" {
  name        = var.network-security-group-name
  description = "Allow all traffic"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}


# Creating Ubuntu EC2 instance
resource "aws_instance" "ubuntu-vm-instance" {
  ami             = var.ubuntu-ami
  instance_type   = var.ubuntu-instance-type
  key_name        = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.network-security-group.id]
  tags = {
    Name = "ubuntu-vm"
  }
}
