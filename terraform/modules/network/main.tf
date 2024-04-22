module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = var.name
  cidr = var.cidr
  azs             = var.availability_zones
  private_subnets = var.private_subnets
  public_subnets  = var.public_subnets
  enable_nat_gateway     = true
  single_nat_gateway     = true

  tags = {
    Terraform   = "true"
    Environment = "${var.env}"
  }
}