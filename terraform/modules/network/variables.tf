variable "availability_zones" {
  type        = list(string)
  description = "A list of availability zones names or ids in the region"
  default     = []
}

variable "name" {
  type        = string
  description = "Name to be used on all the resources as identifier"
}

variable "private_subnets" {
  type        = list(string)
  description = "A list of private subnets inside the VPC"
  default     = []
}

variable "public_subnets" {
  type        = list(string)
  description = "A list of public subnets inside the VPC"
  default     = []
}

variable "env" {
  type        = string
  description = "Environment to be deployed"
  default     = "dev"
}

variable "cidr" {
  type        = string
  description = "The IPv4 CIDR block for the VPC"
}
