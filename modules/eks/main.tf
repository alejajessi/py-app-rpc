module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = var.name
  cluster_version = var.cluster_version

  cluster_addons = {
    coredns = {
      most_recent = true
    }
    kube-proxy = {
      most_recent = true
    }
    vpc-cni = {
      most_recent = true
    }
  }

  vpc_id                   = var.vpc_id
  subnet_ids               = ["10.0.0.0/16"]
  control_plane_subnet_ids = ["10.0.0.0/16"]

  tags = {
    Environment = "${var.env}"
    Terraform   = "true"
    Name        = "${var.env}-py-app"
  }
}
