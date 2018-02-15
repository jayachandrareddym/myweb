# adding variables to all the resources to organize in a covineant amanner in a # single file
variable "region" {
  default = "ap-south-1"
}
variable "AmiLinux" {
  type = "map"
  default = {
    ap-south-1 = "ami-531a4c3c"
      }
  description = "I add only 1 regions (mumbai) to show the map feature but you can add all the regions"
}
variable "aws_access_key" {
  default = "AKIAIZJK4P2TDYDBPLVA"
  description = "the user aws access key"
}
variable "aws_secret_key" {
  default = "DiYOgqNYxZfRDJOdjfkYWXPLONL07CCssp8TewCV"
  description = "the user aws secret key"
}
variable "vpc-fullcidr" {
    default = "172.31.0.0/16"
  description = "the vpc cdir"
}
variable "Subnet-Public-AzA-CIDR" {
  default = "172.31.0.3/24"
  description = "the cidr of the public subnet"
}
variable "Subnet-Private-AzA-CIDR" {
  default = "172.31.0.4/24"
  description = "the cidr of the private subnet"
}
variable "key_name" {
  default = "keylinux"
  description = "the ssh key to use in the EC2 machines"
}
variable "DnsZoneName" {
  default = "linuxacademy.internal"
  description = "the internal dns name"
}
