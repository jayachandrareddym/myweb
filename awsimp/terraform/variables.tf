variable "public_key_path" {
  default = "~/.ssh/terraform.pub/keylinuxpub"  
description = <<DESCRIPTION
Path to the SSH public key to be used for authentication.
Ensure this keypair is added to your local SSH agent so provisioners can
connect.
Example: ~/.ssh/terraform.pub
DESCRIPTION
}

variable "key_name" {
  default = "my-tf-linux"
  description = "Desired name of AWS key pair"
}

variable "aws_region" {
  description = "AWS region to launch servers."
  default     = "ap-south-1"
}

#Amzon linux AMI
variable "aws_amis" {
  default = {
    ap-south-1 = "ami-531a4c3c"
  }
}
