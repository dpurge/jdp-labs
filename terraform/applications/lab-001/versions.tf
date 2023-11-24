terraform {
  required_providers {
  
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.23"
    }
  
    aws = {
	  source  = "hashicorp/aws"
	  version = "~> 5.26"
	}
	
	azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.82.0"
	}
	
	google = {
      source  = "hashicorp/google"
      version = "=5.7.0"
	}
	
  }
}

#provider "kubernetes" {
#  host = "https://104.196.242.174"

#  client_certificate     = "${file("~/.kube/client-cert.pem")}"
#  client_key             = "${file("~/.kube/client-key.pem")}"
#  cluster_ca_certificate = "${file("~/.kube/cluster-ca-cert.pem")}"
#}

provider "aws" {
  region = "us-east-1"
}

#provider "azurerm" {
#  skip_provider_registration = true
#  features {}
#}

#provider "google" {
#  credentials = "${file("~/google-account.json")}"
#  project     = "my-project-id"
#  region      = "europe-west1"
#}
