variable "key_name" {
  description = "Name of the SSH keypair to use in AWS."
}

variable "aws_region" {
  description = "AWS region to launch servers."
  default = "ap-southeast-2"
}

# ubuntu-trusty-14.04 (x64)
variable "aws_amis" {
  default = {
    "us-east-1" = "ami-5f709f34"
    "us-west-2" = "ami-7f675e4f"
    "ap-southeast-2" = "ami-6c14310f"
  }
}

variable "aws_secret_key" {
  description = "IAM API key secret"
}

variable "aws_access_key" {
  description = "IAM access key ID"
}
