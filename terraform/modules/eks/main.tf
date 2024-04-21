module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = var.name
  cluster_version = var.cluster_version
  cluster_endpoint_public_access = true
  cluster_addons = {
    coredns = {
      most_recent = true
      resolve_conflicts_on_create = "OVERWRITE"
      resolve_conflicts_on_update = "OVERWRITE"
    }
    kube-proxy = {
      most_recent = true
    }
    vpc-cni = {
      most_recent = true
      before_compute = true
      configuration_values = jsonencode({
        env = {
          # Reference docs https://docs.aws.amazon.com/eks/latest/userguide/cni-increase-ip-addresses.html
          ENABLE_PREFIX_DELEGATION = "true"
          WARM_PREFIX_TARGET       = "1"
        }
      })
    }
  }
  eks_managed_node_groups = {
    nodegroup = {
      min_size     = 1
      max_size     = 10
      desired_size = 3
      use_custome_launch_template = true
      capacity_type  = "SPOT"
    }
  }
  eks_managed_node_group_defaults = {
    ami_type       = "AL2_x86_64"
    instance_types = [ "m5.large"]
  }
  create_iam_role          = true
  vpc_id                   = var.vpc_id
  subnet_ids               = var.subnets
  cluster_security_group_id = aws_security_group.remote_access.id
  iam_role_additional_policies = {
        AmazonEC2ContainerRegistryReadOnly = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
        additional                         = aws_iam_policy.node_additional.arn
  }
  tags = {
    Environment = "${var.env}"
    Terraform   = "true"
    Name        = "${var.env}-py-app"
  }
}

resource "aws_security_group" "remote_access" {
  name_prefix = "${var.name}-remote-access"
  description = "Allow remote SSH access"
  vpc_id      = var.vpc_id

  ingress {
    description = "SSH access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
}

resource "aws_iam_policy" "node_additional" {
  name        = "${var.name}-additional"
  description = "node additional policy"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:Describe*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

module "key_pair" {
  source  = "terraform-aws-modules/key-pair/aws"
  version = "~> 2.0"

  key_name_prefix    = var.name
  create_private_key = true

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
  build_timeout  = 60
  queued_timeout = 480

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
    image                       = "aws/codebuild/amazonlinux2-aarch64-standard:3.0"
    type                        = "ARM_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"

    environment_variable {
      name  = "CODEBUILD_CONFIG_AUTO_DISCOVER"
      value = "true"
    }
    environment_variable {
      name  = "AWS_ACCOUNT"
      value = data.aws_caller_identity.current.account_id
    }
    environment_variable {
      name  = "ECR_URL"
      value = "py-app-ecr-secret:ecr_url"
      type = "SECRETS_MANAGER"
    }
  }

  source {
    type            = "GITHUB"
    location        = "https://github.com/alejajessi/py-app-rpc.git"
    git_clone_depth = 1
    buildspec = "buildspec.yaml"
    git_submodules_config {
      fetch_submodules = false
    }
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
