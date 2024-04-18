terraform {
  backend "s3" {
    bucket = "py-app-state"
    key    = "terraform.tfstate"
    region = "us-east-1"
  }
}