# HashiCorp Terraform Associate - Preguntas y Respuestas Correctas

Total de preguntas: 367

---

Q1. The terraform.tfstate file always matches your currently built infrastructure.
Respuesta:B. False

---

Q2. One remote backend configuration always maps to a single remote workspace.
Respuesta:B. False

---

Q3. How is the Terraform remote backend different than other state backends such as S3, Consul, etc.?
Respuesta:A. It can execute Terraform runs on dedicated infrastructure on premises or in Terraform Cloud

---

Q4. What is the workflow for deploying new infrastructure with Terraform?
Respuesta:D. Write a Terraform configuration, run terraform init, run terraform plan to view planned infrastructure changes, and terraform apply to create new infrastructure.

---

Q5. A provider configuration block is required in every Terraform configuration.
Respuesta:A. Example:
- B. True

---

Q7. Which provisioner invokes a process on the resource created by Terraform?
Respuesta:A. remote-exec

---

Q8. Which of the following is not true of Terraform providers?
Respuesta:E. None of the above

---

Q9. What command does Terraform require the first time you run it within a configuration directory?
Respuesta:B. terraform init.

---

Q10. You have deployed a new webapp with a public IP address on a cloud provider. However, you did not create any outputs for your code. What is the best method to quickly find the IP address of the resource you deployed?
Respuesta:B. In a new folder, use the terraform_remote_state data source to load in the state file, then write an output for each resource that you find the state file.

---

Q11. Which of the following is not a key principle of infrastructure as code?
Respuesta:B. Golden images

---

Q12. Terraform variables and outputs that set the "description" argument will store that description in the state file.
Respuesta:B. False

---

Q13. What is the provider for this fictitious resource?
Respuesta:C. aws

---

Q14. If you manually destroy infrastructure, what is the best practice reflecting this change in Terraform?
Respuesta:A. Run terraform refresh

---

Q15. What is not processed when running a terraform refresh?
Respuesta:B. Configuration file

---

Q16. What information does the public Terraform Module Registry automatically expose about published modules?
Respuesta:D. All of the above

---

Q17. If a module uses a local values, you can expose that value with a terraform output.
Respuesta:A. True

---

Q18. You should store secret data in the same version control repository as your Terraform configuration.
Respuesta:B. False

---

Q19. Which of the following is not a valid string function in Terraform?
Respuesta:C. slice

---

Q20. You have provisioned some virtual machines (VMs) on Google Cloud Platform (GCP) using the gcloud command line tool. However, you are standardizing with Terraform and want to manage these VMs using Terraform instead. What are the two things you must do to achieve this? (Choose two.)
Respuesta:B. Use the terraform import command for the existing VMs.
- C. Write Terraform configuration for the existing VMs.

---

Q21. You have recently started a new job at a retailer as an engineer. As part of this new role, you have been tasked with evaluating multiple outages that occurred during peak shopping time during the holiday season. Your investigation found that the team is manually deploying new compute instances and configuring each compute instance manually. This has led to inconsistent configuration between each compute instance. How would you solve this using infrastructure as code?
Respuesta:C. Replace the compute instance type with a larger version to reduce the number of required deployments.

---

Q22. terraform init initializes a sample main.tf file in the current directory.
Respuesta:B. False

---

Q23. Which two steps are required to provision new infrastructure in the Terraform workflow? (Choose two.)
Respuesta:B. Apply
- D. Init

---

Q24. Why would you use the terraform taint command?
Respuesta:B. When you want to force Terraform to destroy and recreate a resource on the next apply

---

Q25. Terraform requires the Go runtime as a prerequisite for installation.
Respuesta:B. False

---

Q26. When should you use the force-unlock command?
Respuesta:C. Automatic unlocking failed.

---

Q27. Terraform can import modules from a number of sources; which of the following is not a valid source?
Respuesta:A. FTP server

---

Q28. Which of the following is available only in Terraform Enterprise or Cloud workspaces and not in Terraform CLI?
Respuesta:A. Secure variable storage

---

Q29. terraform validate validates the syntax of Terraform files.
Respuesta:A. True

---

Q30. You have used Terraform to create an ephemeral development environment in the cloud and are now ready to destroy all the infrastructure described by your Terraform configuration. To be safe, you would like to first see all the infrastructure that will be deleted by Terraform. Which command should you use to show all of the resources that will be deleted? (Choose two.)
Respuesta:C. Run terraform state rm *.

---

Q31. Which of the following is the correct way to pass the value in the variable num_servers into a module with the input servers?
Respuesta:D. servers = var.num_servers

---

Q32. A Terraform provisioner must be nested inside a resource configuration block.
Respuesta:A. True

---

Q33. Terraform can run on Windows or Linux, but it requires a Server version of the Windows operating system.
Respuesta:B. False

---

Q34. What does the default "local" Terraform backend store?
Respuesta:D. State file

---

Q36. What value does the Terraform Cloud/Terraform Enterprise private module registry provide over the public Terraform Module Registry?
Respuesta:C. The ability to restrict modules to members of Terraform Cloud or Enterprise organizations.

---

Q37. Which task does terraform init not perform?
Respuesta:D. Validates all required variables are present.

---

Q38. You have declared a variable called var.list which is a list of objects that all have an attribute id. Which options will produce a list of the IDs? (Choose two.)
Respuesta:A. { for o in var.list : o => o.id }
- C. [ var.list[*].id ]

---

Q39. Which argument(s) is (are) required when declaring a Terraform variable?
Respuesta:E. None of the above

---

Q40. When using a module block to reference a module stored on the public Terraform Module Registry such as: How do you specify version 1.0.0?
Respuesta:B. Append ?ref=v1.0.0 argument to the source path

---

Q41. What features does the hosted service Terraform Cloud provide? (Choose two.)
Respuesta:C. Remote state storage
- D. A web-based user interface (UI).

---

Q42. Where does the Terraform local backend store its state?
Respuesta:C. In the terraform.tfstate file

---

Q43. Which option cannot be used to keep secrets out of Terraform configuration files?
Respuesta:D. secure string.

---

Q44. What is one disadvantage of using dynamic blocks in Terraform?
Respuesta:C. They make configuration harder to read and understand.

---

Q45. Only the user that generated a plan may apply it.
Respuesta:B. False.

---

Q46. Examine the following Terraform configuration, which uses the data source for an AWS AMI. What value should you enter for the ami argument in the AWS instance resource?
Respuesta:B. data.aws_ami.ubuntu

---

Q47. FILL BLANK - You need to specify a dependency manually. What resource meta-parameter can you use to make sure Terraform respects the dependency? Type your answer in the field provided. The text field is not case-sensitive and all variations of the correct answer are accepted.
Respuesta:A. depends_on

---

Q48. You have never used Terraform before and would like to test it out using a shared team account for a cloud provider. The shared team account already contains 15 virtual machines (VM). You develop a Terraform configuration containing one VM, perform terraform apply, and see that your VM was created successfully. What should you do to delete the newly-created VM with Terraform?
Respuesta:A. The Terraform state file contains all 16 VMs in the team account. Execute terraform destroy and select the newly-created VM.

---

Q49. What is the name assigned by Terraform to reference this resource?
Respuesta:A. dev

---

Q50. Setting the TF_LOG environment variable to DEBUG causes debug messages to be logged into syslog.
Respuesta:B. False.

---

Q51. Where in your Terraform configuration do you specify a state backend?
Respuesta:A. The terraform block

---

Q52. In Terraform 0.13 and above, outside of the required_providers block, Terraform configurations always refer to providers by their local names.
Respuesta:A. True

---

Q53. What command should you run to display all workspaces for the current configuration?
Respuesta:C. terraform workspace list

---

Q54. Terraform providers are always installed from the Internet.
Respuesta:B. False

---

Q55. Which of these is the best practice to protect sensitive values in state files?
Respuesta:C. Enhanced remote backends

---

Q56. When does terraform apply reflect changes in the cloud environment?
Respuesta:B. However long it takes the resource provider to fulfill the request

---

Q57. How would you reference the "name" value of the second instance of this fictitious resource?
Respuesta:B. aws_instance.web[1].name

---

Q58. A Terraform provider is not responsible for:
Respuesta:B. Provisioning infrastructure in multiple clouds

---

Q59. Terraform provisioners can be added to any resource block.
Respuesta:A. True

---

Q60. What is terraform refresh intended to detect?
Respuesta:C. State file drift

---

Q62. FILL BLANK - What is the name of the default file where Terraform stores the state? Type your answer in the field provided. The text field is not case-sensitive and all variations of the correct answer are accepted.
Respuesta:A. terraform.tfstate

---

Q63. A Terraform local value can reference other Terraform local values.
Respuesta:A. True

---

Q64. Which of the following is not a valid Terraform collection type?
Respuesta:C. tree

---

Q65. When running the command terraform taint against a managed resource you want to force recreation upon, Terraform will immediately destroy and recreate the resource.
Respuesta:B. False

---

Q66. All standard backend types support state storage, locking, and remote operations like plan, apply and destroy.
Respuesta:A. True

---

Q67. How can terraform plan aid in the development process?
Respuesta:A. Validates your expectations against the execution plan without permanently modifying state

---

Q68. You would like to reuse the same Terraform configuration for your development and production environments with a different state file for each. Which command would you use?
Respuesta:A. terraform import

---

Q69. What is the name assigned by Terraform to reference this resource?
Respuesta:B. main

---

Q71. Your security team scanned some Terraform workspaces and found secrets stored in a plaintext in state files. How can you protect sensitive data stored in Terraform state files?
Respuesta:A. Delete the state file every time you run Terraform.

---

Q72. In contrast to Terraform Open Source, when working with Terraform Enterprise and Cloud Workspaces, conceptually you could think about them as completely separate working directories.
Respuesta:A. True

---

Q74. How is terraform import run?
Respuesta:D. By an explicit call

---

Q75. You have a simple Terraform configuration containing one virtual machine (VM) in a cloud provider. You run terraform apply and the VM is created successfully. What will happen if you delete the VM using the cloud provider console, and run terraform apply again without changing any Terraform code?
Respuesta:C. Terraform will not make any changes.

---

Q76. Which of these options is the most secure place to store secrets for connecting to a Terraform remote backend?
Respuesta:A. Defined in Environment variables.

---

Q77. Your DevOps team is currently using the local backend for your Terraform configuration. You would like to move to a remote backend to begin storing the state file in a central location. Which of the following backends would not work?
Respuesta:B. Artifactory

---

Q78. Which backend does the Terraform CLI use by default?
Respuesta:D. Local

---

Q79. When you initialize Terraform, where does it cache modules from the public Terraform Module Registry?
Respuesta:C. On disk in the .terraform sub-directory

---

Q80. You write a new Terraform configuration and immediately run terraform apply in the CLI using the local backend. Why will the apply fail?
Respuesta:A. Terraform needs you to format your code according to best practices first

---

Q81. What features stops multiple admins from changing the Terraform state at the same time?
Respuesta:D. State locking

---

Q82. A fellow developer on your team is asking for some help in refactoring their Terraform code. As part of their application's architecture, they are going to tear down an existing deployment managed by Terraform and deploy new. However, there is a server resource named aws_instance.ubuntu[1] they would like to keep performing some additional analysis. What command should be used to tell Terraform to no longer manage the resource?
Respuesta:A. terraform apply rm aws_instance.ubuntu[1]

---

Q83. Terraform can only manage resource dependencies if you set them explicitly with the depends_on argument.
Respuesta:B. False.

---

Q84. A terraform apply can not _________ infrastructure.
Respuesta:D. import

---

Q85. You need to constrain the GitHub provider to version 2.1 or greater. Which of the following should you put into the Terraform 0.12 configuration's provider block?
Respuesta:C. version = "<= 2.1"

---

Q87. Terraform provisioners that require authentication can use the ______ block.
Respuesta:A. connection

---

Q88. Terraform validate reports syntax check errors from which of the following scenarios?
Respuesta:B. There is missing value for a variable

---

Q89. Which of the following is allowed as a Terraform variable name?
Respuesta:B. name

---

Q90. What type of block is used to construct a collection of nested configuration blocks?
Respuesta:D. dynamic

---

Q91. Module variable assignments are inherited from the parent module and do not need to be explicitly set.
Respuesta:B. False.

---

Q92. If writing Terraform code that adheres to the Terraform style conventions, how would you properly indent each nesting level compared to the one above it?
Respuesta:D. With two spaces

---

Q93. Which of the following is not an action performed by terraform init?
Respuesta:A. Create a sample main.tf file

---

Q94. HashiCorp Configuration Language (HCL) supports user-defined functions.
Respuesta:B. False.

---

Q95. How can you trigger a run in a Terraform Cloud workspace that is connected to a Version Control System (VCS) repository?
Respuesta:B. Commit a change to the VCS working directory and branch that the Terraform Cloud workspace is connected to.

---

Q96. Terraform and Terraform providers must use the same major version number in a single configuration.
Respuesta:B. False

---

Q97. Which statement describes a goal of infrastructure as code?
Respuesta:D. The programmatic configuration of resources.

---

Q98. When using Terraform to deploy resources into Azure, which scenarios are true regarding state files? (Choose two.)
Respuesta:B. When a change is made to the resources via the Azure Cloud Console, Terraform will update the state file to reflect them during the next plan or apply.
- C. When a change is made to the resources via the Azure Cloud Console, the current state file will not be updated.

---

Q99. You need to deploy resources into two different cloud regions in the same Terraform configuration. To do that, you declare multiple provider configurations as follows: What meta-argument do you need to configure in a resource block to deploy the resource to the `us-west-2` AWS region?
Respuesta:B. provider = west

---

Q100. You have declared an input variable called environment in your parent module. What must you do to pass the value to a child module in the configuration?
Respuesta:C. Declare a node_count input variable for child module.

---

Q101. If a module declares a variable with a default, that variable must also be defined within the module.
Respuesta:B. False

---

Q102. Which option cannot be used to keep secrets out of Terraform configuration files?
Respuesta:B. Mark the variable as sensitive.

---

Q103. Which of the following arguments are required when declaring a Terraform output?
Respuesta:D. value

---

Q104. Your risk management organization requires that new AWS S3 buckets must be private and encrypted at rest. How can Terraform Enterprise automatically and proactively enforce this security control?
Respuesta:A. With a Sentinel policy, which runs before every apply.

---

Q105. Most Terraform providers interact with ____________.
Respuesta:A. API

---

Q106. terraform validate validates that your infrastructure matches the Terraform state file.
Respuesta:B. False

---

Q107. What does terraform import allow you to do?
Respuesta:C. Import provisioned infrastructure to your state file

---

Q108. FILL BLANK - In the below configuration, how would you reference the module output vpc_id? module "vpc" { source = "terraform-and-modules/vpc/aws" cidr = "10.0.0.0/16" name = "test-vpc" } Type your answer in the field provided. The text field is not case sensitive and all variations of the correct answer are accepted.
Respuesta:A. module.vpc.vpc_id

---

Q109. How would you reference the Volume IDs associated with the ebs_block_device blocks in this configuration?
Respuesta:D. aws_instance.example.ebs_block_device.*.volume_id.

---

Q110. What does state locking accomplish?
Respuesta:C. Blocks Terraform commands from modifying the state file

---

Q111. You just upgraded the version of a provider in an existing Terraform project. What do you need to do to install the new provider?
Respuesta:B. Run terraform init -upgrade

---

Q112. A module can always refer to all variables declared in its parent module.
Respuesta:A. True

---

Q113. When you use a remote backend that needs authentication, HashiCorp recommends that you:
Respuesta:A. Use partial configuration to load the authentication credentials outside of the Terraform code.

---

Q114. You have a simple Terraform configuration containing one virtual machine (VM) in a cloud provider. You run terraform apply and the VM is created successfully. What will happen if you terraform apply again immediately afterwards without changing any Terraform code?
Respuesta:C. Terraform will apply the VM to the state file.

---

Q115. A junior admin accidentally deleted some of your cloud instances. What does Terraform do when you run terraform apply?
Respuesta:C. Rebuild only the instances that were deleted.

---

Q116. You have created a main.tf Terraform configuration consisting of an application server, a database, and a load balancer. You ran terraform apply and all resources were created successfully. Now you realize that you do not actually need the load balancer so you run terraform destroy without any flags What will happen?
Respuesta:B. Terraform will prompt you to confirm that you want to destroy all the infrastructure.

---

Q117. Which type of block fetches or computes information for use elsewhere in a Terraform configuration?
Respuesta:D. data

---

Q118. You have just developed a new Terraform configuration for two virtual machines with a cloud provider. You would like to create the infrastructure for the first time. Which Terraform command should you run first?
Respuesta:C. terraform show.

---

Q119. All modules published on the official Terraform Module Registry have been verified by HashiCorp.
Respuesta:B. False.

---

Q120. You have to initialize a Terraform backend before it can be configured.
Respuesta:B. False.

---

Q121. Which of the following does terraform apply change after you approve the execution plan? (Choose two.)
Respuesta:A. Cloud infrastructure
- D. State file

---

Q122. A Terraform backend determines how Terraform loads state and stores updates when you execute ___________.
Respuesta:D. All of the above

---

Q123. What does Terraform use .terraform.lock.hcl file for?
Respuesta:A. Tracking provider dependencies

---

Q124. You've used Terraform to deploy a virtual machine and a database. You want to replace this virtual machine instance with an identical one without affecting the database. What is the best way to achieve this using Terraform?
Respuesta:B. Use the terraform taint command targeting the VMs then run terraform plan and terraform apply

---

Q125. How do you specify a module's version when publishing it to the public Terraform Module Registry?
Respuesta:C. The release tags in the associated repo

---

Q126. Terraform plan updates your state file.
Respuesta:B. False

---

Q127. To check if all code in a Terraform configuration with multiple modules is properly formatted without making changes, what command should be run?
Respuesta:D. terraform fmt -check -recursive.

---

Q128. As a member of the operations team, you need to run a script on a virtual machine created by Terraform. Which provision is best to use in your Terraform code?
Respuesta:C. remote-exec

---

Q129. You are using a networking module in your Terraform configuration with the name label my_network. In your main configuration you have the following code:
Respuesta:C. Define the attribute vnet_id as a variable in the networking module

---

Q131. How can a ticket-based system slow down infrastructure provisioning and limit the ability to scale? (Choose two.)
Respuesta:B. A request must be submitted for infrastructure changes
- C. As additional resources are required, more tickets are submitted

---

Q132. Which of the following statements about Terraform modules is not true?
Respuesta:A. Modules must be publicly accessible.

---

Q133. Which Terraform collection type should you use to store key/value pairs?
Respuesta:C. map

---

Q134. You have used Terraform to create an ephemeral development environment in the cloud and are now ready to destroy all the infrastructure described by your Terraform configuration. To be safe, you would like to first see all the infrastructure that will be deleted by Terraform. Which command should you use to show all of the resources that will be deleted? (Choose two.)
Respuesta:B. Run terraform show -destroy.

---

Q135. When do you need to explicitly execute terraform refresh?
Respuesta:D. None of the above.

---

Q136. All Terraform Cloud tiers support team management and governance.
Respuesta:B. False

---

Q137. What advantage does an operations team that uses infrastructure as code have?
Respuesta:C. The ability to reuse best practice configurations and settings.

---

Q140. Terraform variable names are saved in the state file.
Respuesta:B. False

---

Q141. Terraform Cloud is available only as a paid offering from HashiCorp.
Respuesta:B. False

---

Q142. Which of the following is not a way to trigger terraform destroy?
Respuesta:C. Passing --destroy at the end of a plan request.
- D. Delete the state file and run terraform apply.

---

Q143. Which of the following is not an advantage of using infrastructure as code operations?
Respuesta:B. Troubleshoot via a Linux diff command.

---

Q144. You're writing a Terraform configuration that needs to read input from a local file called id_rsa.pub. Which built-in Terraform function can you use to import the file's contents as a string?
Respuesta:C. templatefile("id_rsa.pub")

---

Q145. What does Terraform use providers for? (Choose three.)
Respuesta:A. Provision resources for on-premises infrastructure services
- B. Simplify API interactions.
- C. Provision resources for public cloud infrastructure services

---

Q146. You can reference a resource created with for_each using a Splat (*) expression.
Respuesta:B. False

---

Q147. How does Terraform determine dependencies between resources?
Respuesta:A. Terraform automatically builds a resource graph based on resources, provisioners, special meta-parameters, and the state file, if present.

---

Q148. Which parameters does terraform import require? (Choose two.)
Respuesta:C. Resource ID
- D. Resource address.

---

Q149. Once a new Terraform backend is configured with a Terraform code block, which command(s) is (are) used to migrate the state file?
Respuesta:D. terraform init.

---

Q150. What does this code do?
Respuesta:A. Requires any version of the AWS provider >= 3.0 and < 4.0

---

Q151. What does terraform refresh modify?
Respuesta:B. Your state file

---

Q152. Which of the following is not valid source path for specifying a module?
Respuesta:A. source = "./modulelversion=v1.0.0"

---

Q153. Which of the following is true about terraform apply? (Choose two.)
Respuesta:A. It only operates on infrastructure defined in the current working directory or workspace.
- C. Depending on provider specification, Terraform may need to destroy and recreate your infrastructure resources.

---

Q154. Which of the following statements about local modules is incorrect?
Respuesta:C. Local modules support versions.

---

Q155. Which of the following is true about Terraform's implementation of infrastructure as code? (Choose two.)
Respuesta:C. You can version your infrastructure configuration
- E. It allows you to automate infrastructure provisioning.

---

Q156. You need to write some Terraform code that adds 42 firewall rules to a security group as shown in the example. What can you use to avoid writing 42 different nested ingress config blocks by hand?
Respuesta:C. A for each block

---

Q157. Which of the following is the safest way to inject sensitive values into a Terraform Cloud workspace?
Respuesta:B. Set a value for the variable in the UI and check the "Sensitive" check box

---

Q158. terraform apply will fail if you have not a terraform plan first to update the plan output.
Respuesta:B. False.

---

Q159. How would you reference the attribute "name" of this fictitious resource in HCL?
Respuesta:C. kubernetes_namespace.example.name

---

Q160. A Terraform output that sets the "sensitive" argument to true will not store that value in the state file.
Respuesta:B. False.

---

Q161. Which are forbidden actions when the Terraform state file is locked? (Choose three.)
Respuesta:A. terraform destroy
- D. terraform apply
- E. terraform plan

---

Q162. Terraform installs its providers during which phase?
Respuesta:B. Init

---

Q163. When does Sentinel enforce policy logic during a Terraform Enterprise run?
Respuesta:C. Before the apply phase

---

Q164. What is the purpose of a Terraform workspace in either open source or enterprise?
Respuesta:A. Workspaces allow you to manage collections of infrastructure in state files

---

Q165. Which is the best way to specify a tag of v1.0.0 when referencing a module stored in Git (for example git::https://example.com/vpc.git)?
Respuesta:A. Append ?ref=v1. 0. 0 argument to the source path

---

Q166. Changing the Terraform backend from the default "local" backend to a different one after doing your first terraform apply is:
Respuesta:B. Optional

---

Q167. You have modified your local Terraform configuration and ran terraform plan to review the changes. Simultaneously, your teammate manually modified the infrastructure component you are working on. Since you already ran terraform plan locally, the execution plan for terraform apply will be the same.
Respuesta:B. False

---

Q168. terraform apply is failing with the following error. What next step should you take to determine the root cause of the problem?
Respuesta:A. Error loading state: AccessDenied: Access Denied status code: 403, request id: 288766CE5CCA24A0, host id: FOOBAR

---

Q169. As a member of an operations team that uses infrastructure as code (IaC) practices, you are tasked with making a change to an infrastructure stack running in a public cloud. Which pattern would follow IaC best practices for making a change?
Respuesta:D. Make the change via the public cloud API endpoint.

---

Q170. What command can you run to generate DOT (Document Template) formatted data to visualize Terraform dependencies?
Respuesta:C. terraform graph

---

Q171. Which provider authentication method prevents credentials from being stored in the state file?
Respuesta:A. Using environment variables

---

Q172. Running terraform fmt without any flags in a directory with Terraform configuration files will check the formatting of those files without changing their contents.
Respuesta:B. False

---

Q173. terraform init retrieves the source code for all referenced modules.
Respuesta:A. True

---

Q174. You have a Terraform configuration that defines a single virtual machine with no references to it. You have run terraform apply to create the resource, and then removed the resource definition from your Terraform configuration file. What will happen when you run terraform apply in the working directory again?
Respuesta:A. Nothing

---

Q175. Which configuration consistency errors does terraform validate report?
Respuesta:D. Declaring a resource identifier more than once.

---

Q176. Pregunta no disponible - contenido en imagen no extraíble
Respuesta:A. Opción no disponible

---

Q177. Where can Terraform not load a provider from?
Respuesta:A. Source code

---

Q178. Which of the following locations can Terraform use as a private source for modules? (Choose two.)
Respuesta:A. Internally hosted SCM (Source Control Manager) platform
- C. Private repository on GitHub

---

Q179. Why should secrets not be hard coded into Terraform code? (Choose two.)
Respuesta:A. It makes the code less reusable.
- B. Terraform code is typically stored in version control, as well as copied to the systems from which it's run. Any of those may not have robust security mechanisms.

---

Q180. If a Terraform creation-time provisioner fails, what will occur by default?
Respuesta:C. The resource will be marked as "tainted."

---

Q181. When should Terraform configuration files be written when running terraform import on existing infrastructure?
Respuesta:D. Terraform configuration should be written before terraform import is executed.

---

Q182. Which command lets you experiment with Terraform's built-in functions?
Respuesta:B. terraform console

---

Q183. Why does this backend configuration not follow best practices?.
Respuesta:A. You should not store credentials in Terraform Configuration

---

Q184. Open source Terraform can only import publicly-accessible and open-source modules.
Respuesta:B. False.

---

Q185. What does terraform destroy do?
Respuesta:A. Destroy all infrastructure in the Terraform state file.

---

Q186. While attempting to deploy resources into your cloud provider using Terraform, you begin to see some odd behavior and experience sluggish responses. In order to troubleshoot you decide to turn on Terraform debugging. Which environment variables must be configured to make Terraform's logging more verbose?
Respuesta:C. TF_LOG

---

Q187. If a DevOps team adopts AWS CloudFormation as their standardized method for provisioning public cloud resources, which of the following scenarios poses a challenge for this team?
Respuesta:C. The organization decides to expand into Azure and wishes to deploy new infrastructure using their existing codebase.

---

Q188. You cannot install third party plugins using terraform init.
Respuesta:B. False.

---

Q189. Which of the following can you do with terraform plan? (Choose two.)
Respuesta:A. Save a generated execution plan to apply later.
- C. View the execution plan and check if the changes match your expectations.

---

Q190. Which are examples of infrastructure as code? (Choose two.)
Respuesta:C. Versioned configuration files
- D. Docker files.

---

Q191. FILL BLANK - You need to migrate a workspace to use a remote backend. After updating your configuration, what command do you run to perform the migration? Type your answer in the field provided. The text field is not case-sensitive and all variations of the correct answer are accepted.
Respuesta:A. terraform init

---

Q192. When using a module from the public Terraform Module Registry, the following parameters are required attributes in the module block. (Choose two.)
Respuesta:A. Each of the module’s required inputs
- B. The module’s source address

---

Q193. As a developer, you want to ensure your plugins are up to date with the latest versions. Which Terraform command should you use?
Respuesta:A. terraform init -upgrade.

---

Q194. You can access state stored with the local backend by using the terraform_remote_state data source.
Respuesta:B. False.

---

Q195. You have been working in a Cloud provider account that is shared with other team members. You previously used Terraform to create a load balancer that is listening on port 80. After some application changes, you updated the Terraform code to change the port to 443.
Respuesta:C. What will happen when you terraform apply upon returning to your desk?

---

Q196. In a Terraform Cloud workspace linked to a version control repository, speculative plan runs start automatically when you merge or commit changes to version control.
Respuesta:A. True

---

Q197. You have some Terraform code and a variable definitions file named dev.auto.tfvars that you tested successfully in the dev environment. You want to deploy the same code in the staging environment with a separate variable definition file and a separate state file. Which two actions should you perform? (Choose two.)
Respuesta:A. Copy the existing terraform.tfstate file and save it as staging.terraform.tfstate
- B. Write a new staging.auto.tfvars variable definition file and run Terraform with the var-file=”staging.auto.tfvars” flag

---

Q198. The ________ determines how Terraform creates, updates, or deletes resources.
Respuesta:C. Terraform provider.

---

Q199. Terraform destroy is the only way to remove infrastructure.
Respuesta:B. False.

---

Q200. Which of the following is the correct way to pass the value in the variable num_servers into a module with the input servers in HCL2?
Respuesta:A. servers = var.num_servers

---

Q201. Which of the fallowing commands would you use to access all of the attributes and details of a resource managed by Terraform?
Respuesta:B. terraform state show

---

Q202. How would you be able to reference an attribute from the vsphere_datacenter data source for use with the datacenter_id argument within the vsphere_folder resource in the following configuration?
Respuesta:D. data.vsphere_datacenter.dc.id.

---

Q203. You decide to move a Terraform state file to Amazon S3 from another location. You write the code below into a file called backend.tf. Which command will migrate your current state file to the new S3 remote backend?
Respuesta:A. terraform state.

---

Q205. Which of the following is not a benefit of adopting infrastructure as code?
Respuesta:A. Interpolation

---

Q206. Module version is required to reference a module on the Terraform Module Registry.
Respuesta:B. False

---

Q208. The public Module Registry is free to use.
Respuesta:A. True

---

Q209. Both Terraform Cloud and Terraform Enterprise support policy as code (Sentinel).
Respuesta:A. True

---

Q210. You want to define multiple data disks as nested blocks inside the resource block for a virtual machine. What Terraform feature would help you define the blocks using the values in a variable?
Respuesta:B. Collection functions

---

Q211. Which of the following module source paths does not specify a remote module?
Respuesta:A. source = “./modules/consul”

---

Q212. You have a list of numbers that represents the number of free CPU cores on each virtual cluster:
Respuesta:A. numcpus = [ 18, 3, 7, 11, 2 ]

---

Q213. Variables declared within a module are accessible outside of the module.
Respuesta:B. False.

---

Q214. Which of the following is not a valid Terraform variable type?
Respuesta:C. array

---

Q215. What is a key benefit of the Terraform state file?
Respuesta:D. A state file represents a source of truth for resources provisioned with Terraform.

---

Q216. Which of these statements about Terraform Enterprise workspaces is false?
Respuesta:B. You must use the CLI to switch between workspaces.

---

Q217. Define the purpose of state in Terraform.
Respuesta:A. State is used to map real world resources to your configuration and keep track of metadata

---

Q218. Which backend does the Terraform CLI use by default?
Respuesta:D. Local

---

Q219. Using the terraform state rm command against a resource will destroy it.
Respuesta:B. False

---

Q220. Which method for sharing Terraform configurations keeps them confidential within your organization, supports Terraform’s semantic version constraints, and provides a browsable directory?
Respuesta:B. Terraform Cloud/Terraform Enterprise private module registry

---

Q222. How would you refer to the indexing instance from the below configuration?
Respuesta:D. aws_instance.web[“indexing”]

---

Q223. Which feature is not included in Terraform Cloud’s free tier?
Respuesta:C. Audit logging

---

Q224. When should you run terraform init?
Respuesta:C. After you start coding a new Terraform project and before you run terraform plan for the first time

---

Q225. Terraform configuration (including any module references) can contain only one Terraform provider type.
Respuesta:A. True
- B. False

---

Q226. You are making changes to existing Terraform code to add some new infrastructure. When is the best time to run terraform validate?
Respuesta:B. Before you run terraform plan so you can validate your code syntax

---

Q227. How does Terraform manage most dependencies between resources?
Respuesta:D. Terraform will automatically manage most resource dependencies

---

Q228. What does running a terraform plan do?
Respuesta:B. Compares the state file to your Terraform code and determines if any changes need to be made

---

Q229. What are some benefits of using Sentinel with Terraform Cloud/Terraform Enterprise? (Choose three.)
Respuesta:A. Policy-as-code can enforce security best practices
- B. You can restrict specific configurations on resources like "CIDR=0.0.0.0/0" not allowed
- C. You can enforce a list of approved AWS AMIs

---

Q230. You want to share Terraform state with your team, store it securely, and provide state locking. How would you do this? (Choose three.)
Respuesta:A. Using the remote Terraform backend with Terraform Cloud / Terraform Enterprise.
- D. Using an s3 terraform backend with an appropriate IAM policy and dynamodb_field option configured.
- E. Using the consul Terraform backend.

---

Q231. From which of these sources can Terraform import modules?
Respuesta:D. All of the above

---

Q232. How would you output returned values from a child module?
Respuesta:B. Declare the output in the child module

---

Q233. You have decided to create a new Terraform workspace to deploy a development environment. What is different about this workspace?
Respuesta:A. It has its own state file

---

Q234. Any user can publish modules to the public Terraform Module Registry.
Respuesta:A. True

---

Q235. Which of these commands makes your code more human readable?
Respuesta:D. terraform fmt

---

Q236. Infrastructure as Code (IaC) can be stored in a version control system along with application code.
Respuesta:A. True

---

Q237. Select the command that doesn’t cause Terraform to refresh its state.
Respuesta:D. terraform state list

---

Q238. Sentinel policy-as-code is available in Terraform Enterprise.
Respuesta:A. True

---

Q239. Before you can use Terraform’s remote backend, you must first execute terraform init.
Respuesta:A. True

---

Q240. Which two steps are required to provision new infrastructure in the Terraform workflow? (Choose two.)
Respuesta:B. Apply
- D. Init

---

Q241. You are working on some new application features and you want to spin up a copy of your production deployment to perform some quick tests. In order to avoid having to configure a new state backend, what open source Terraform feature would allow you create multiple states but still be associated with your current code?
Respuesta:D. Terraform workspaces

---

Q242. Which provisioner invokes a process on the machine running Terraform?
Respuesta:C. local-exec

---

Q243. ____________ backends support state locking.
Respuesta:A. Some

---

Q244. Which of the following methods, used to provision resources into a public cloud, demonstrates the concept of infrastructure as code?
Respuesta:C. A script that contains a series of public cloud CLI commands

---

Q245. Which of the following should you put into the required_providers block?
Respuesta:B. version = “>= 3.1”

---

Q246. When should you write Terraform configuration files for existing infrastructure that you want to start managing with Terraform?
Respuesta:A. Before you run terraform import

---

Q247. Which command should you run to check if all code in a Terraform configuration that references multiple modules is properly formatted without making changes?
Respuesta:C. terraform fmt -check -recursive

---

Q248. What features stops multiple users from operating on the Terraform state at the same time?
Respuesta:C. State locking

---

Q249. You are creating a reusable Terraform configuration and want to include a billing_dept tag so your Finance team can track team-specific spending on resources. Which of the following billing_dept variable declarations will allow you to do this?
Respuesta:C. variable "billing_dept" { default = "" }

---

Q250. Which of these are secure options for storing secrets for connecting to a Terraform remote backend? (Choose two.)
Respuesta:B. Defined in Environment variables
- C. Defined in a connection configuration outside of Terraform

---

Q251. You want to define a single input variable to capture configuration values for a server. The values must represent memory as a number, and the server name as a string. Which variable type could you use for this input?
Respuesta:B. Object

---

Q252. What does Terraform not reference when running a terraform apply -refresh-only?
Respuesta:C. Terraform resource definitions in configuration files

---

Q253. Multiple team members are collaborating on infrastructure using Terraform and want to format their Terraform code following standard Terraform-style convention. How could they automatically ensure the code satisfies conventions?
Respuesta:A. Run the terraform fmt command during the code linting phase of your CI/CD process

---

Q254. When using a remote backend or Terraform Cloud integration, where does Terraform save resource state?
Respuesta:D. In the remote backend or Terraform Cloud

---

Q255. In Terraform HCL, an object type of object({ name=string, age=number }) would match this value:
Respuesta:B. { name = "John" age = 52 }

---

Q256. You add a new resource to an existing Terraform configuration, but do not update the version constraint in the configuration. The existing and new resources use the same provider. The working directory contains a .terraform-lock.hcl file. How will Terraform choose which version of the provider to use?
Respuesta:B. Terraform will use the version recorded in your lock file

---

Q257. You must use different Terraform commands depending on the cloud provider you use.
Respuesta:B. False

---

Q258. Define the purpose of state in Terraform.
Respuesta:D. State maps real world resources to your configuration and keeps track of metadata

---

Q259. Which of these actions will prevent two Terraform runs from changing the same state file at the same time?
Respuesta:C. Configure state locking for your state backend

---

Q260. While attempting to deploy resources into your cloud provider using Terraform, you begin to see some odd behavior and experience slow responses. In order to troubleshoot you decide to turn on Terraform debugging. Which environment variables must be configured to make Terraform’s logging more verbose?
Respuesta:C. TF_LOG

---

Q261. The Terraform binary version and provider versions must match each other in a single configuration.
Respuesta:B. False

---

Q262. The .terraform.lock.hcl file tracks module versions.
Respuesta:B. False

---

Q263. You can develop a custom provider to manage its resources using Terraform.
Respuesta:A. True

---

Q264. Which of these is not a benefit of remote state?
Respuesta:B. Easily share reusable code modules

---

Q265. When using multiple configurations of the same Terraform provider, what meta-argument must be included in any non-default provider configurations?
Respuesta:B. alias

---

Q266. A developer accidentally launched a VM (virtual machine) outside of the Terraform workflow and ended up with two servers with the same name. They don’t know which VM Terraform manages but do have a list of all active VM IDs. Which of the following methods could you use to discover which instance Terraform manages?
Respuesta:C. Run terraform state list to find the names of all VMs, then run terraform state show for each of them to find which VM ID Terraform manages

---

Q267. Which of the following is not considered a safe way to inject sensitive values into a Terraform Cloud workspace?
Respuesta:A. Edit the state file directly just before running terraform apply

---

Q268. If you update the version constraint in your Terraform configuration, Terraform will update your lock file the next time you run terraform init.
Respuesta:B. False

---

Q269. You must initialize your working directory before running terraform validate.
Respuesta:A. True

---

Q270. If you manually destroy infrastructure, what is the best practice reflecting this change in Terraform?
Respuesta:B. Remove the resource definition from your file and run terraform apply -refresh-only

---

Q271. You created infrastructure outside of the Terraform workflow that you now want to manage using Terraform. Which command brings the infrastructure into Terraform state?
Respuesta:D. terraform import

---

Q272. When using Terraform to deploy resources into Azure, which scenarios are true regarding state files?
Respuesta:D. Changing resources via the Azure Cloud Console does not update current state file

---

Q273. Which statement describes a goal of infrastructure as code?
Respuesta:D. The programmatic configuration of resources

---

Q274. Terraform validate confirms the syntax of Terraform files.
Respuesta:A. True

---

Q275. Which command adds existing resources into Terraform state?
Respuesta:D. terraform import

---

Q276. It is best practice to store secret data in the same version control repository as your Terraform configuration.
Respuesta:B. False

---

Q277. Which of the following commands would you use to access all of the attributes and details of a resource managed by Terraform?
Respuesta:B. terraform state show ‘provider_type.name’

---

Q278. terraform validate confirms that your infrastructure matches the Terraform state file.
Respuesta:B. False

---

Q279. A senior admin accidentally deleted some of your cloud instances. What does Terraform do when you run terraform apply?
Respuesta:C. Rebuild only the instances that were deleted

---

Q280. terraform init creates an example main.tf file in the current directory.
Respuesta:B. False

---

Q281. Which argument helps prevent unexpected updates when calling Terraform Registry modules?
Respuesta:C. version

---

Q282. Setting the TF_LOG environment variable to DEBUG causes debug messages to be logged into stdout.
Respuesta:B. False

---

Q283. How would you output returned values from a child module in the Terraform CLI output?
Respuesta:B. Declare the output in the child module
- C. Declare the output in both the root and child module

---

Q284. What is the Terraform resource name of the following resource block?
Respuesta:D. dev

---

Q285. When do you need to explicitly execute terraform refresh-only?
Respuesta:D. None of the above

---

Q286. How is the Terraform cloud integration differ from other state backends such as S3, Consul, etc.?
Respuesta:A. It can execute Terraform runs on dedicated infrastructure in Terraform Cloud

---

Q287. Which of the following are advantages of using infrastructure as code (IaC) instead of provisioning with a graphical user interface (GUI)? (Choose two.)
Respuesta:B. Let’s your version, reuse, and share infrastructure configuration
- D. Reduces risk of operator error

---

Q288. One cloud configuration always maps to a single remote workspace.
Respuesta:B. False

---

Q289. Multiple team members are collaborating on infrastructure using Terraform and want to format their Terraform code following standard Terraform-style convention. How could they automatically ensure the code satisfies conventions?
Respuesta:D. Use terraform fmt

---

Q290. Which backend does the Terraform CLI use by default?
Respuesta:D. Local

---

Q291. The Terraform CLI will print output values from a child module after running terraform apply.
Respuesta:B. False.

---

Q292. What does terraform refresh-only modify?
Respuesta:D. Your state file

---

Q293. What does terraform import do?
Respuesta:A. Imports existing resources into the state file

---

Q294. Which of the following is the correct way to pass the value in the variable num_servers into a module with the input server?
Respuesta:D. servers = var.num_servers

---

Q295. A developer on your team is going to tear down an existing deployment managed by Terraform and deploy a new one. However, there is a server resource named aws_instance.ubuntu[1] they would like to keep. What command should they use to tell Terraform to stop managing that specific resource?
Respuesta:C. terraform state rm aws_instance.ubuntu[1]

---

Q296. Before you can use a remote backend, you must first execute terraform init.
Respuesta:A. True

---

Q297. What does running a terraform plan do?
Respuesta:D. Compares the state file to your Terraform code and determines if any changes need to be made

---

Q298. Which of the following statements about Terraform modules is not true?
Respuesta:A. Modules must be publicly accessible

---

Q299. How can a ticket-based system slow down infrastructure provisioning and limit the ability to scale? (Choose two.)
Respuesta:A. End-users have to request infrastructure changes
- D. The more resources your organization needs, the more tickets your infrastructure team has to process

---

Q300. How do you specify a module's version when publishing it to the public Terraform Module Registry?
Respuesta:D. Tag a release in the associated repo

---

Q301. What Terraform command always causes a state file to be updated with changes that might have been made outside of Terraform?
Respuesta:A. terraform plan -refresh-only

---

Q302. Which command must you first run before performing further Terraform operations in a working directory?
Respuesta:C. terraform init

---

Q303. Which command lets you experiment with Terraform expressions?
Respuesta:A. terraform console

---

Q304. What kind of configuration block will create an infrastructure object with settings specified within the block?
Respuesta:D. resource

---

Q305. When do changes invoked by terraform apply take effect?
Respuesta:B. Once the resource provider has fulfilled the request

---

Q306. What is the workflow for deploying new infrastructure with Terraform?
Respuesta:A. Write Terraform configuration, run terraform init to initialize the working directory or workspace, and run terraform apply

---

Q307. Which of these are features of Terraform Cloud? (Choose two.)
Respuesta:A. Remote state storage
- B. A web-based user interface (UI)

---

Q308. Which option can not keep secrets out of Terraform configuration files?
Respuesta:B. Mark the variable as sensitive

---

Q309. Which of the following is not true of Terraform providers?
Respuesta:E. None of the above

---

Q310. Which Terraform command checks that your configuration syntax is correct?
Respuesta:B. terraform validate

---

Q311. terraform validate uses provider APIs to verify your infrastructure settings.
Respuesta:B. False

---

Q312. You add a new provider to your configuration and immediately run terraform apply in the CLI using the local backend. Why does the apply fail?
Respuesta:D. Terraform needs to install the necessary plugins first

---

Q313. Which of these statements about Terraform Cloud workspaces is false?
Respuesta:C. You must use the CLI to switch between workspaces

---

Q314. What value does the Terraform Cloud private registry provide over the public Terraform Module Registry?
Respuesta:A. The ability to restrict modules to members of Terraform Cloud or Enterprise organizations

---

Q315. Terraform providers are part of the Terraform core binary.
Respuesta:B. False

---

Q316. Which of the following is not a benefit of adopting infrastructure as code?
Respuesta:C. Graphical User Interface

---

Q317. Where does the Terraform local backend store its state?
Respuesta:A. In the terraform.tfstate file

---

Q318. Which of these is true about Terraform's plugin-based architecture?
Respuesta:B. You can create a provider for your API if none exists

---

Q319. Your risk management organization requires that new AWS S3 buckets must be private and encrypted at rest. How can Terraform Cloud automatically and proactively enforce this security control?
Respuesta:B. With a Sentinel policy, which runs before every apply

---

Q320. If you don't use the local backend, where does Terraform save resource state?
Respuesta:A. In the remote backend or Terraform Cloud

---

Q321. You are writing a child Terraform module that provisions an AWS instance. You want to reference the IP address returned by the child module in the root configuration. You name the instance resource "main". Which of these is the correct way to define the output value?
Respuesta:A. output "instance_ip_addr" { value = aws_instance.main.private_ip }

---

Q322. When does Sentinel enforce policy logic during a Terraform Cloud run?
Respuesta:C. Before the apply phase

---

Q323. What is terraform refresh-only intended to detect?
Respuesta:D. State file drift

---

Q324. You should run terraform fmt to rewrite all Terraform configurations within the current working directory to conform to Terraform-style conventions.
Respuesta:A. True

---

Q325. Why would you use the -replace flag for terraform apply?
Respuesta:C. You want to force Terraform to destroy and recreate a resource on the next apply

---

Q326. You can configure Terraform to log to a file using the TF_LOG environment variable.
Respuesta:B. False

---

Q327. When does Terraform create the .terraform.lock.hcl file?
Respuesta:C. After your first terraform init

---

Q328. What is the best and easiest way for Terraform to read and write secrets form Hashicorp Vault?
Respuesta:D. Vault provider

---

Q329. In Terraform Enterprise, a workspace can be mapped to how many VCS repos?
Respuesta:A. 1

---

Q330. Hashicorp offers multiple versions of Terraform, including Terraform open-source, Terraform Cloud and Terraform Enterprise. Which of the following Terraform feature is only available in the Enterprise Edition? (select one).
Respuesta:D. Locally managed installation

---

Q331. Which Terraform command will force a resource to be destroyed and recreated even if there no configuration changes that would require it?
Respuesta:A. terraform apply -replace=<address>

---

Q332. What is the purpose of using the local-exec provisioner? (select two)
Respuesta:B. to invoke a local executable
- C. to execute one or more commands on the machine running Terraform

---

Q333. Which of the following best describes a Terraform provider?
Respuesta:D. a plugin that Terraform uses to translate the API interactions with the service or provider

---

Q334. Kristen is using modules to provision an Azure environment for a new application. She is using the following code and specifying a version of her virtual machine module to ensure she's calling the correct module. Which of the following provides support for the versioning of a module? (select two)?
Respuesta:C. modules stored in GitLab

---

Q335. Select the answer below that completes the following statement:
Respuesta:C. authentication using MFA

---

Q336. What is the downside to using Terraform to interact with sensitive data, such as reading secrets from Vault?
Respuesta:D. secrets are persisted to the state file.

---

Q337. Terry is using a module to deploy some EC2 instances on AWS for a new project. He is viewing the code that is calling the module for deployment, which is shown below. Where is the value of the security group originating?
Respuesta:C. the output of another module

---

Q338. In the example below, where is the value of the DNS record's IP address originating from?
Respuesta:B. the output of a module named web_server

---

Q339. What does the command terraform fmt do?
Respuesta:D. rewrite Terraform configuration files to a canonical format and style

---

Q340. Which of the following allows Terraform users to apply policy as code to enforce standardized configurations for resources being deployed via infrastructure as code?
Respuesta:C. sentinel

---

Q341. What Terraform feature is shown in the example below?
Respuesta:A. Dynamic block

---

Q342. When configuring a remote backend in Terraform, it might be a good idea to purposely omit some of the required arguments to ensure secrets and other relevant data are not inadvertently shared with others. What are the ways the remaining configuration can be added to Terraform so it can initialize and communicate with the backend? (select three)
Respuesta:A. directly querying HashiCorp Vault for the secrets
- B. use the -backend-config=PATH to specify a separate config file
- C. interactively on the command line

---

Q343. In order to make a Terraform configuration file dynamic and/or reusable, static values should be converted to use what?
Respuesta:D. input variables

---

Q344. In regards to deploying resources in multi-cloud environments, what are some of the benefits of using Terraform rather than a provider's native tooling? (select three)
Respuesta:B. Terraform simplifies management and orchestration, helping operators build large-scale, multi-cloud infrastructure
- C. Terraform can manage cross-cloud dependencies
- D. Terraform can help businesses deploy applications on multiple clouds and on-premises infrastructure

---

Q345. After running into issues with Terraform, you need to enable verbose logging to assist with troubleshooting the error. Which of the following values provides the MOST verbose logging?
Respuesta:C. TRACE

---

Q346. By default, where does Terraform OSS/CLI store its state file?
Respuesta:A. current working directory

---

Q347. You have been given requirements to create a security group for a new application. Since your organization standardizes on Terraform, you want to add this new security group with the fewest number of lines of code. What feature could you use to iterate over a list of required tcp ports to add to the new security group?
Respuesta:C. terraform import

---

Q348. What happens when a terraform plan is executed?
Respuesta:D. creates an execution plan and determines what changes are required to achieve the desired state in the configuration files

---

Q349. When using modules to deploy infrastructure, how would you export a value from one module to import into another module?
Respuesta:C. preconfigure the IP address as a parameter in the DNS module

---

Q350. Given the Terraform configuration below, which order will the resources be created?
Respuesta:D. aws_instance will be created first & aws_eip will be created second

---

Q351. Rick is writing a new Terraform configuration file and wishes to use modules in order to easily consume Terraform code that has already been written. Which of the modules shown below Will be created first?
Respuesta:B. module "vpc"

---

Q352. What are some of the features of Terraform state? (select three)
Respuesta:A. determining the correct order to destroy resources
- C. increased performance
- D. mapping configuration to real-world resources

---

Q353. True or False? Starting in Terraform vO.12, the Terraform language now has built-in syntax for creating lists using the [ and ] delimiters, replacing and deprecating the list ( ) function.?
Respuesta:A. True

---

Q354. In the terraform block, which configuration would be used to identify the specific version of a provider required?
Respuesta:C. required_providers

---

Q355. In regards to Terraform state file, select all the statements below which are correct: (select four)
Respuesta:A. storing state remotely can provide better security
- B. Terraform Cloud always encrypts state at rest
- D. the Terraform state can contain sensitive data, therefore the state file should be protected from unauthorized access
- E. when using local state, the state file is stored in plain-text

---

Q356. From the answers below, select the advantages of using Infrastructure as Code. (select four)
Respuesta:A. Easily change and update existing infrastructure
- B. Safely test modifications using a "dry run" before applying any actual changes
- D. Provide reusable modules for easy sharing and collaboration
- E. Easily integrate with application workflows (GitLabActions, Azure DevOps, CI/CD tools)

---

Q357. Which of the following best describes the default local backend?
Respuesta:A. The local backend stores state on the local filesystem, locks the state using system APIS, and performs operations locally.

---

Q358. True or False? Provisioners should only be used as a last resort.
Respuesta:A. True

---

Q359. What are the benefits of using Infrastructure as Code? (select five)
Respuesta:B. Infrastructure as Code is relatively simple to learn and write, regardless of a user's prior experience with developing code
- C. Infrastructure as Code is easily repeatable, allowing the user to reuse code to deploy similar, yet different resources
- D. Infrastructure as Code allows a user to turn a manual task into a simple, automated deployment
- E. Infrastructure as Code gives the user the ability to recreate an application's infrastructure for disaster recovery scenarios
- F. Infrastructure as Code provides configuration consistency and standardization among deployments

---

Q360. Which of the following is considered a Terraform plugin?
Respuesta:D. Terraform provider

---

Q361. What are the core Terraform workflow steps to use infrastructure as code?
Respuesta:C. 1) Write 2) Plan 3) Apply

---

Q362. Which of the following represents a feature of Terraform Cloud that is NOT free to customers?
Respuesta:B. team management and governance

---

Q363. Terraform-specific settings and behaviors are declared in which configuration block type?
Respuesta:B. terraform block

---

Q364. What are some of the problems of how infrastructure was traditionally managed before Infrastructure as Code? (select three)
Respuesta:A. Traditional deployment methods are not able to meet the demands of the modem business where resources tend to live days to weeks, rather than months to years
- B. Traditionally managed infrastructure can’t keep up with cyclic or elastic applications
- D. Requests for infrastructure or hardware often required a ticket, increasing the time required to deploy applications

---

Q365. Why is it a good idea to declare the required version of a provider in a Terraform configuration file?
Respuesta:B. providers are released on a separate schedule from Terraform itself; therefore, a newer version could introduce breaking changes

---

Q366. Stephen is writing brand new code and needs to ensure it is syntactically valid and internally consistent. Stephen doesn't want to wait for Terraform to access any remote services while making sure his code is valid. What command can he use to accomplish this?
Respuesta:A. terraform validate

---

Q367. Select two answers to complete the following sentence:
Respuesta:B. approved by HashiCorp
- C. initialized

---

Q368. After executing a terraform plan , you notice that a resource has a tilde (~) next to it. What does this mean?
Respuesta:C. the resource will be updated in place

---

Q369. Your organization has moved to AWS and has manually deployed infrastructure using the console. Recently, a decision has been made to standardize on Terraform for all deployments moving forward. What can you do to ensure that the existing resources are managed by Terraform moving forward without causing interruption to existing resources?
Respuesta:D. using terraform import , import the existing infrastructure into your Terraform state

---

Q370. Which of the following Terraform files should be ignored by Git when committing code to a repo? (select two)
Respuesta:A. terraform.tfvars
- C. terraform.tfstate

---

Q371. What Terraform command can be used to inspect the current state file?
Respuesta:B. terraform show

---

Q372. Select the feature below that best completes the sentence:
Respuesta:D. named values

---

Q373. Which of the following connection types are supported by the remote-exec provisioner? (select two)
Respuesta:B. winrm
- C. ssh

---

Q374. True or False? State is a requirement for Terraform to function.
Respuesta:B. True

---

Q375. True or False? Workspaces provide similar functionality in the open-source, Terraform Cloud, and Enterprise versions of Terraform.
Respuesta:B. True

---

Q376. Published modules via the Terraform Registry provide which of the following benefits? (select four)
Respuesta:B. show examples and READMEs
- C. allow browsing version histories
- D. support versioning
- E. automatically generated documentation

---

Q377. What happens when a terraform apply command is executed?
Respuesta:D. applies the changes required in the target infrastructure in order to reach the desired configuration

---

Q378. Frank has a file named main.tf which is shown below. Which of the following statements are true about this code? (select two)
Respuesta:B. main.tf is the calling module
- D. app-cluster is the child module

---

Q379. Using multi-cloud and provider-agnostic tools provides which of the following benefits? (select two)
Respuesta:B. operations teams only need to learn and manage a single tool to manage infrastructure, regardless of where the infrastructure is deployed
- D. can be used across major cloud providers and VM hypervisors

---

