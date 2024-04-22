# PYTHON Grpc Application

## Tools/Languages

- Python
- Terraform
- AWS
- Kubernetes

## Architecture diagram

![Architecture diagram](diagrama.png)

## What is a Grpc?

Please check [this documentation](https://grpc.io/docs/languages/python/basics/)

## Pre requisites

- AWS Account
- Terraform

## Install

- Download/clone this repository  `https://github.com/alejajessi/py-app-rpc.git`
- Configure your AWS credentials as environment variables `AWS_ACCESS_KEY_ID` y `AWS_SECRET_ACCESS_KEY`
- Create one bucket for terraform.state (In our case is called `py-app-state`)
- Open a terminal to execute some terraform commands:

            (You should be located in the root of the project)
            ```
            cd ./terraform
            terraform init --reconfigure
            terraform plan ## Please check the plan
            terraform apply 
            ```

- Now, Open your AWS Console and in search, please write AWS CodeBuild
    - Select your new compile project called `py-app-rpc`
    - Clic on `Iniciar compilación` or `Start build`
    
## Future work

According with the architecture diagram, it's pending implement AWS Code Pipeline to finish our CI/CD

## Run python app in local

The only prerequisite is to have docker installed and the docker daemon running.
Please execute this command in your terminal `docker-compose up --build` to start our server
Finally open another terminal window and execute  `python3 main.py --type 0`

# Networking

We've two modules into terraform directory: 
- eks
- network
Those modules are linked because we're using the infrastructure created in network module for our eks cluster.

In the network module, we've one child module `terraform-aws-modules/vpc/aws` and this is the [repository](https://github.com/terraform-aws-modules/terraform-aws-vpc) for that child module.
But we configured some custom values.In the network module, I created:
- We're creating using a for lop our private and public subnets accoridng with the cidr input
- We're not using ipv6 address, just using ipv4 for this reason we don't have any intra subnets.
- We're enabling our nat gateway to allow sent traffic as output to internet.
- But when we enable the flag `single_nat_gateway` to create just one nat gateway. If we want, we can omit this configuration because the vpc module is able to configure per default the number of nat gwateys.
- Now, our configuration indicate that: "then all private subnets will route their Internet traffic through this single NAT gateway"

And finally to allow SSH access in our cluster, I added one security group in the module eks (just for SSH eks cluster communication). If we want, we can move this block of code to network but I prefer leave here because it's related property with eks connection.
