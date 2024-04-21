locals {
  azs = data.aws_availability_zones.available.names
  cidr = "10.0.0.0/16"
}

module "network" {
  source             = "./modules/network"
  name               = "${var.env}-py-app-network"
  cidr               = "10.0.0.0/16"
  availability_zones = slice(local.azs, 0, 3)
  private_subnets = [for k, v in local.azs : cidrsubnet(local.cidr, 4, k)]
  public_subnets  = [for k, v in local.azs : cidrsubnet(local.cidr, 8, k + 48)]
}

module "eks" {
  source = "./modules/eks"
  name   = "${var.env}-py-app-eks"
  cluster_version = "1.29"
  security_group = module.network.security_group
  vpc_id = module.network.vpc_id
  codebuild_role_name = "py-app-codebuild-role"
  subnets = module.network.private_subnets
  codebuild_role_policy = data.aws_iam_policy_document.codebuild_role_policy.json
  name_ecr = "py-app-ecr"
}
