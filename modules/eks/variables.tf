variable "env" {
  type        = string
  description = "Environment to be deployed"
  default     = ""
}

variable "cluster_version" {
  type        = string
  description = "Cluster version"
}

variable "name_ecr" {
  type        = string
  description = "Name of the ECR repository"
}

variable "name" {
  type        = string
  description = "Name of the cluster"
}

variable "subnets_control_plane" {
  type        = list(string)
  description = "A list of subnets IDs where the EKS cluster control plane will be provisioned"
  default     = []
}

variable "subnets" {
  type        = list(string)
  description = "A list of subnets IDs where the node/nodes groups will be provisioned"
  default     = []
}

variable "security_group" {
  type        = string
  description = "Security group ID of the cluster"
}

variable "vpc_id" {
  type        = string
  description = "ID of the VPC where the cluster security group will be provisioned"
  default     = null
}

variable "codebuild_role_policy" {
  type        = string
  description = "Code Build JSON data policy"
}

variable "codebuild_role_name" {
  type        = string
  description = "Code Build IAM role name"
}

