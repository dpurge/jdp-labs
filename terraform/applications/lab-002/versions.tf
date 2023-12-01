terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.26"
    }
  }

  backend "s3" {
    # Variables may not be used here.
    bucket         = "dpurge-tfstate-lab001"
    key            = "terraform/lab002/terraform.tfstate"
    region         = "eu-central-1"
    dynamodb_table = "dpurge-tfstate-locking-lab001"
    encrypt        = true
  }
}

provider "aws" {
  region = var.aws_region
}
