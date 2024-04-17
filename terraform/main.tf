module "network" {
  source = "./modules/network"
  name = "${var.env}-py-app-network"
}

module "eks" {
    source = "./modules/eks"
    name = "${var.env}-py-app-eks"
}