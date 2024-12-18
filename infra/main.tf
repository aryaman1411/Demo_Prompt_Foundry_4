Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently. Here is a basic example of how you can use Terraform to create an Azure cloud infrastructure for an e-commerce web application. 

Please note that this is a very basic example and does not include all the necessary components for a full-fledged e-commerce application. You would need to add more resources like databases, load balancers, etc. based on your specific requirements.

```hcl
provider "azurerm" {
  features {}
}

module "resource_group" {
  source  = "Azure/resource-group/azurerm"
  version = "2.0.2"

  name     = "example-resources"
  location = "West Europe"
}

module "network" {
  source              = "Azure/network/azurerm"
  version             = "3.1.1"
  resource_group_name = module.resource_group.name
  address_space       = "10.0.0.0/16"
  subnet_prefixes     = ["10.0.1.0/24"]
  subnet_names        = ["subnet1"]
  depends_on          = [module.resource_group]
}

module "linux_servers" {
  source              = "Azure/compute/azurerm"
  version             = "1.2.1"
  resource_group_name = module.resource_group.name
  vm_os_simple        = "UbuntuServer"
  public_ip_dns       = ["mypublicdns"]
  vnet_subnet_id      = module.network.vnet_subnets[0]
  depends_on          = [module.network]
}
```

This code creates a resource group, a virtual network with a single subnet, and a Linux virtual machine within that subnet. 

The code is modular, meaning each part of the infrastructure (resource group, network, servers) is defined in a separate module. This makes the code easier to manage and reuse.

The code is also cost-effective in the sense that it only creates the minimum necessary resources. However, the actual cost will depend on the specific Azure pricing for each resource.

Please replace the placeholders with your actual values and add more resources as per your requirements. Also, make sure to run `terraform init` to download the necessary provider plugins before running `terraform apply` to create the resources.