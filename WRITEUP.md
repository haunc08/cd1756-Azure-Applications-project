# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

## Analysis result: VM vs App Service
### Cost
Azure App Service plans are generally more expensive than VMs. Furthermore, when an app is stopped, VMs simply charge disk costs, whereas App Service continues to charge. App Service, on the other hand, offers a Free Tier that is limited to 1GB of storage and is only suitable for very basic and demo projects.
### Scalability
In terms of scalability, Azure App Service is limited in comparison to Azure VMs. As a result, Azure VMs are preferred for apps that have the potential to grow in the future. Also, because Azure VMs give developers more control over the environment, you can't use App Service if you wish to choose the underlying OS of the VM or use a specific programming language.
### Workflow
In comparison to Azure Virtual Machines, Azure App Service requires far fewer configuration and management efforts. As a result, developing and deploying apps is more easier and faster when using Azure App Service.
## Solution
After considering the pros and cons of the two options, I choose Azure App Service for deploying the app:
- Because I use Azure App Service's Free Tier plan, cost is not an issue. This application is pretty simple, and the only user really use the app is me, therefore 1GB of storage and 60 CPU minutes each day should suffice.
- This app is developed with Flask, a popular Python framework, it has typical CRUD functionality, and doesn't need customized environment. Therefore App Service would be suffice in terms of scalability.
- App Service has clear advantage in the amount of work and effort needed to develop and deploy the application. As a result, I can deliver the application more quickly.