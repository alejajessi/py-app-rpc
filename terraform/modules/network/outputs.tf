output "vpc_id" {
  description = "The ID of the VPC"
  value       = try(module.vpc.vpc_id, null)
}

output "security_group" {
  description = "The security group of the VPC"
  value       = try(module.vpc.default_vpc_default_security_group_id, null)
}
 

output "public_subnet" {
  description = "List of ARNs of public subnets"
  value       = module.vpc.public_subnets
}

output "private_subnets" {
  description = "List of IDs of private subnets"
  value       = module.vpc.private_subnets
}
