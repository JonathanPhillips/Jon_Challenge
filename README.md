# Jon_Challenge
## Hello World web app running on AWS EC2 using Terraform to deploy the infrastructure

### IaC Demo 
Pre-requisites:
This demo uses AWS resources so you will need an AWS account as well as a user with the appropriate permissions and the Access key and Secret key, which you can store in the tfvars file.  You can also use awscli and create a profile which stores the access key and secret key (preferred method).

To run this demo, make sure you have Terraform installed and clone this repo into you local machine. From the command line, you can cd into the terraform folder and run  the following:

* terraform init
* terraform plan -out github.tfplan
* terraform apply "github.tfplan"

### 
This terraform plan will create a VPC with two subnets, 2 EC2 instances running NGINX, and an ALB in front of the 2 instances.
