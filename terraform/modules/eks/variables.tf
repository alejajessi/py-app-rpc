variable "env" {
    type = string
    description = "Environment to be deployed"
    default = ""
}

variable "cluster_version" {
    type = string
    description = "Cluster version"
}


variable "name" {
    type = string
    description = "Name of the cluster"
}

variable "subnets_control_plane" {
    type = list(string)
    description = "A list of subnets IDs where the EKS cluster control plane will be provisioned"
    default = []
}

variable "subnets" {
    type = list(string)
    description = "A list of subnets IDs where the node/nodes groups will be provisioned"
    default = []
}

variable "vpc_id" {
    type = string
    description = "ID of the VPC where the cluster security group will be provisioned"
    default = null
}
