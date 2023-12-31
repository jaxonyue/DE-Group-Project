# Terraform configuration
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0.0"
    }
  }
  required_version = ">= 0.14.9"
}
# Configure the Azure provider
provider "azurerm" {
  features {}
}


# Create the resource group
resource "azurerm_resource_group" "rg" {
  name     = "DEGroup_project"
  location = "eastus"
}

# Create the Linux App Service Plan
resource "azurerm_service_plan" "appserviceplan" {
  name                = "yes"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "S1"
}


# Create the web app, pass in the App Service Plan ID
resource "azurerm_linux_web_app" "webapp" {
  name                  = "Wagess"
  location              = azurerm_resource_group.rg.location
  resource_group_name   = azurerm_resource_group.rg.name
  service_plan_id       = azurerm_service_plan.appserviceplan.id
  https_only            = true
  
  app_settings = {    
    "WEBSITES_ENABLE_APP_SERVICE_STORAGE" = "false"
    "WEBSITES_PORT"                       = "7000"
    "DOCKER_REGISTRY_SERVER_URL"          = "https://index.docker.io/v1"     
  }

  site_config {
    application_stack {
      docker_image     = "hiddenlayerr/wagesviz"
      docker_image_tag = "latest"
    }
    always_on = true
    ftps_state = "AllAllowed"
  }

}
