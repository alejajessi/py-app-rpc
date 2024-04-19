module "network" {
  source             = "./modules/network"
  name               = "${var.env}-py-app-network"
  availability_zones = slice(data.aws_availability_zones.available.names, 0, 3)
  private_subnets    = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets     = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
}

module "eks" {
  source = "./modules/eks"
  name   = "${var.env}-py-app-eks"
  cluster_version = "1.28"
  security_group = module.network.security_group
  vpc_id = module.network.vpc_id
  codebuild_role_name = "py-app-codebuild-role"
  subnets = module.network.private_subnets
  codebuild_role_policy = data.aws_iam_policy_document.codebuild_role_policy.json
  name_ecr = "py-app-ecr"
}
