module "network" {
  source = "./modules/network"
  name = "${var.env}-py-app-network"
  availability_zones = slice(data.aws_availability_zones.available.names, 0, 3)
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
}

module "eks" {
    source = "./modules/eks"
    name = "${var.env}-py-app-eks"
}