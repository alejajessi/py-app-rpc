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
  subnet_ids               = var.subnets
  cluster_security_group_id = var.security_group
  tags = {
    Environment = "${var.env}"
    Terraform   = "true"
    Name        = "${var.env}-py-app"
  }
}

resource "aws_iam_role" "codebuild_role" {
  name               = var.codebuild_role_name
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_role_policy" "codebuild_role_policy" {
  role   = aws_iam_role.codebuild_role.name
  policy = var.codebuild_role_policy
}

resource "aws_codebuild_project" "py-app" {
  name           = "py-app-rpc"
  description    = "py-app-rpc build"
  build_timeout  = 5
  queued_timeout = 5

  service_role = aws_iam_role.codebuild_role.arn

  artifacts {
    type = "NO_ARTIFACTS"
  }

##  cache {
##    type  = "LOCAL"
##    modes = ["LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE"]
##  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/amazonlinux2-x86_64-standard:4.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"

    environment_variable {
      name  = "DOCKER_USERNAME"
      value = "alejajessi"
    }
  }

  source {
    type            = "GITHUB"
    location        = "https://github.com/alejajessi/py-app-rpc.git"
    git_clone_depth = 1
  }
}

resource "aws_ecr_repository" "ecr_repo" {
  name                 = var.name_ecr
  image_tag_mutability = "MUTABLE"
}

resource "aws_secretsmanager_secret" "ecr_secret" {
  name        = "${var.name_ecr}-secret"
  description = "Secret with ECR information"
}

resource "aws_secretsmanager_secret_version" "ecr_secret" {
  secret_id = aws_secretsmanager_secret.ecr_secret.id
  secret_string = jsonencode(
    {
      ecr_url = aws_ecr_repository.ecr_repo.repository_url
    })
}

