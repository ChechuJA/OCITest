# HashiCorp Terraform Associate

Total de preguntas: 379

#### Q1. The terraform.tfstate file always matches your currently built infrastructure.

- [ ] A. True
- [x] B. False

> Reference https://www.terraform.io/docs/language/state/index.html

#### Q2. One remote backend configuration always maps to a single remote workspace.

- [ ] A. True
- [x] B. False

> Reference https://www.terraform.io/docs/language/settings/backends/remote.html

#### Q3. How is the Terraform remote backend different than other state backends such as S3, Consul, etc.?

- [x] A. It can execute Terraform runs on dedicated infrastructure on premises or in Terraform Cloud
- [ ] B. It doesn't show the output of a terraform apply locally.
- [ ] C. It is only available to paying customers.
- [ ] D. All of the above

> If you and your team are using Terraform to manage meaningful infrastructure, we recommend using the remote backend with Terraform Cloud or Terraform Enterprise Reference https://www.terraform.io/docs/language/settings/backends/index.html

#### Q4. What is the workflow for deploying new infrastructure with Terraform?

- [ ] A. terraform plan to import the current infrastructure to the state file, make code changes, and terraform apply to update the infrastructure.
- [ ] B. Write a Terraform configuration, run terraform show to view proposed changes, and terraform apply to create new infrastructure.
- [ ] C. terraform import to import the current infrastructure to the state file, make code changes, and terraform apply to update the infrastructure.
- [x] D. Write a Terraform configuration, run terraform init, run terraform plan to view planned infrastructure changes, and terraform apply to create new infrastructure.

> 

#### Q5. A provider configuration block is required in every Terraform configuration.

- [x] A. Example:
- [x] B. True
- [ ] C. False

> Reference https://github.com/hashicorp/terraform/issues/17928

#### Q6. You run a local-exec provisioner in a null resource called null_resource.run_script and realize that you need to rerun the script. Which of the following commands would you use first?

- [ ] A. terraform taint null_resource.run_script.
- [ ] B. terraform apply -target=null_resource.run_script
- [ ] C. terraform validate null_resource.run_script.
- [ ] D. terraform plan -target=null_resource.run_script

> As discussed, the `taint` command used to be the right choice; however, it is deprecated. The right answer is: terraform apply -replace="null_resource.run_script"

#### Q7. Which provisioner invokes a process on the resource created by Terraform?

- [x] A. remote-exec
- [ ] B. null-exec
- [ ] C. local-exec
- [ ] D. file

> The remote-exec provisioner invokes a script on a remote resource after it is created. Reference https://www.terraform.io/docs/language/resources/provisioners/remote-exec.html

#### Q8. Which of the following is not true of Terraform providers?

- [ ] A. Providers can be written by individuals.
- [ ] B. Providers can be maintained by a community of users.
- [ ] C. Some providers are maintained by HashiCorp.
- [ ] D. Major cloud vendors and non-cloud vendors can write, maintain, or collaborate on Terraform providers.
- [x] E. None of the above

> All of the statements are true of Terraform providers. Providers can be written by individuals - Any person or organization can develop and distribute a Terraform provider, allowing them to expand Terraform's capabilities to manage resources that it previously could not. Providers can be maintained by a community of users - Many Terraform providers are open source projects, and the development and maintenance of these providers can be collaborative efforts between multiple individuals and organizations. Some providers are maintained by HashiCorp - HashiCorp, the creators of Terraform, maintain a number of official providers that cover popular infrastructure providers such as AWS, Google Cloud, and Microsoft Azure. Major cloud vendors and non-cloud vendors can write, maintain, or collaborate on Terraform providers - Providers can be developed and maintained by cloud vendors, non-cloud vendors, or a combination of both, to expand Terraform's capabilities and support for different types of infrastructure. Reference https://jayendrapatil.com/terraform-cheat-sheet/#Terraform_Read_and_write_configuration

#### Q9. What command does Terraform require the first time you run it within a configuration directory?

- [ ] A. terraform import.
- [x] B. terraform init.
- [ ] C. terraform plan.
- [ ] D. terraform workspace.

> Reference https://www.terraform.io/docs/cli/commands/init.html

#### Q10. You have deployed a new webapp with a public IP address on a cloud provider. However, you did not create any outputs for your code. What is the best method to quickly find the IP address of the resource you deployed?

- [ ] A. Run terraform output ip_address to view the result.
- [x] B. In a new folder, use the terraform_remote_state data source to load in the state file, then write an output for each resource that you find the state file.
- [ ] C. Run terraform state list to find the name of the resource, then terraform state show to find the attributes including public IP address.
- [ ] D. Run terraform destroy then terraform apply and look for the IP address in stdout.

> Reference https://www.terraform.io/docs/cli/commands/output.html

#### Q11. Which of the following is not a key principle of infrastructure as code?

- [ ] A. Versioned infrastructure
- [x] B. Golden images
- [ ] C. Idempotence
- [ ] D. Self-describing infrastructure

> Reference  https://docs.microsoft.com/en-us/azure/devops/learn/what-is-infrastructure-as-code#:~:text=Idempotence%20is%20a%20principle%20of,of%20the%20environment's%20starting%20state

#### Q12. Terraform variables and outputs that set the "description" argument will store that description in the state file.

- [ ] A. True
- [x] B. False

> 

#### Q13. What is the provider for this fictitious resource?

- [ ] A. vpc
- [ ] B. main
- [x] C. aws
- [ ] D. test

> Reference https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.htm

#### Q14. If you manually destroy infrastructure, what is the best practice reflecting this change in Terraform?

- [x] A. Run terraform refresh
- [ ] B. It will happen automatically
- [ ] C. Manually update the state file
- [ ] D. Run terraform import

> 

#### Q15. What is not processed when running a terraform refresh?

- [ ] A. State file
- [x] B. Configuration file
- [ ] C. Credentials
- [ ] D. Cloud provider

> Reference https://www.terraform.io/docs/cli/commands/refresh.html

#### Q16. What information does the public Terraform Module Registry automatically expose about published modules?

- [ ] A. Required input variables
- [ ] B. Optional inputs variables and default values
- [ ] C. Outputs
- [x] D. All of the above
- [ ] E. None of the above

> Reference https://www.terraform.io/docs/registry/modules/publish.html

#### Q17. If a module uses a local values, you can expose that value with a terraform output.

- [x] A. True
- [ ] B. False

> Output values are like function return values. Reference https://www.terraform.io/docs/language/values/locals.html https://www.terraform.io/docs/language/values/outputs.htm

#### Q18. You should store secret data in the same version control repository as your Terraform configuration.

- [ ] A. True
- [x] B. False

> Reference https://blog.gruntwork.io/a-comprehensive-guide-to-managing-secrets-in-your-terraform-code-1d586955ace1

#### Q19. Which of the following is not a valid string function in Terraform?

- [ ] A. split
- [ ] B. join
- [x] C. slice
- [ ] D. chomp

> Reference https://www.terraform.io/docs/language/functions/chomp.html

#### Q20. You have provisioned some virtual machines (VMs) on Google Cloud Platform (GCP) using the gcloud command line tool. However, you are standardizing with Terraform and want to manage these VMs using Terraform instead. What are the two things you must do to achieve this? (Choose two.)

- [ ] A. Provision new VMs using Terraform with the same VM names.
- [x] B. Use the terraform import command for the existing VMs.
- [x] C. Write Terraform configuration for the existing VMs.
- [ ] D. Run the terraform import-gcp command.

> The terraform import command is used to import existing infrastructure. Import existing Google Cloud resources into Terraform with Terraformer. Reference https://www.terraform.io/docs/cli/import/usage.html https://cloud.google.com/docs/terraform

#### Q21. You have recently started a new job at a retailer as an engineer. As part of this new role, you have been tasked with evaluating multiple outages that occurred during peak shopping time during the holiday season. Your investigation found that the team is manually deploying new compute instances and configuring each compute instance manually. This has led to inconsistent configuration between each compute instance. How would you solve this using infrastructure as code?

- [ ] A. Implement a ticketing workflow that makes engineers submit a ticket before manually provisioning and configuring a resource.
- [ ] B. Implement a checklist that engineers can follow when configuring compute instances.
- [x] C. Replace the compute instance type with a larger version to reduce the number of required deployments.
- [ ] D. Implement a provisioning pipeline that deploys infrastructure configurations committed to your version control system following code reviews.

> 

#### Q22. terraform init initializes a sample main.tf file in the current directory.

- [ ] A. True
- [x] B. False

> 

#### Q23. Which two steps are required to provision new infrastructure in the Terraform workflow? (Choose two.)

- [ ] A. Destroy
- [x] B. Apply
- [ ] C. Import
- [x] D. Init
- [ ] E. Validate

> Reference https://www.terraform.io/guides/core-workflow.html

#### Q24. Why would you use the terraform taint command?

- [ ] A. When you want to force Terraform to destroy a resource on the next apply
- [x] B. When you want to force Terraform to destroy and recreate a resource on the next apply
- [ ] C. When you want Terraform to ignore a resource on the next apply
- [ ] D. When you want Terraform to destroy all the infrastructure in your workspace

> The terraform taint command manually marks a Terraform-managed resource as tainted, forcing it to be destroyed and recreated on the next apply. IMPORTANT NOTE: taint command is deprecated. For Terraform v0.15.2 and later, Hashicorp recommends using the -replace option with terraform apply instead. Outdated question for v3.0.0 test. Although B is correct, but we now have terraform -replace="resource_name" for this now. Reference https://www.terraform.io/docs/cli/commands/taint.htm

#### Q25. Terraform requires the Go runtime as a prerequisite for installation.

- [ ] A. True
- [x] B. False

> Reference https://www.terraform.io/docs/extend/guides/v1-upgrade-guide.html

#### Q26. When should you use the force-unlock command?

- [ ] A. You see a status message that you cannot acquire the lock.
- [ ] B. You have a high priority change.
- [x] C. Automatic unlocking failed.
- [ ] D. You apply failed due to a state lock.

> Manually unlock the state for the defined configuration. Reference https://www.terraform.io/docs/cli/commands/force-unlock.html

#### Q27. Terraform can import modules from a number of sources; which of the following is not a valid source?

- [x] A. FTP server
- [ ] B. GitHub repository
- [ ] C. Local path
- [ ] D. Terraform Module Registry

> 

#### Q28. Which of the following is available only in Terraform Enterprise or Cloud workspaces and not in Terraform CLI?

- [x] A. Secure variable storage
- [ ] B. Support for multiple cloud providers
- [ ] C. Dry runs with terraform plan.
- [ ] D. Using the workspace as a data source

> 

#### Q29. terraform validate validates the syntax of Terraform files.

- [x] A. True
- [ ] B. False

> The terraform validate command validates the syntax and arguments of the Terraform configuration files. Reference https://www.terraform.io/docs/cli/code/index.html

#### Q30. You have used Terraform to create an ephemeral development environment in the cloud and are now ready to destroy all the infrastructure described by your Terraform configuration. To be safe, you would like to first see all the infrastructure that will be deleted by Terraform. Which command should you use to show all of the resources that will be deleted? (Choose two.)

- [ ] A. Run terraform plan -destroy.
- [ ] B. This is not possible. You can only show resources that will be created.
- [x] C. Run terraform state rm *.
- [ ] D. Run terraform destroy and it will first output all the resources that will be deleted before prompting for approval.

> Reference https://www.terraform.io/docs/cli/commands/state/rm.htm

#### Q31. Which of the following is the correct way to pass the value in the variable num_servers into a module with the input servers?

- [ ] A. servers = num_servers
- [ ] B. servers = variable.num_servers
- [ ] C. servers = var(num_servers)
- [x] D. servers = var.num_servers

> 

#### Q32. A Terraform provisioner must be nested inside a resource configuration block.

- [x] A. True
- [ ] B. False

> Provisioners are used to execute scripts on a local or remote machine as part of resource creation or destruction. Provisioners can be used to bootstrap a resource, cleanup before destroy, run configuration management, etc. How to use Provisioners Note: Provisioners should only be used as a last resort. For most common situations there are better alternatives. If you are certain that provisioners are the best way to solve your problem after considering the advice in the sections above, you can add a provisioner block inside the resource block of a compute instance. Reference https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax

#### Q33. Terraform can run on Windows or Linux, but it requires a Server version of the Windows operating system.

- [ ] A. True
- [x] B. False

> 

#### Q34. What does the default "local" Terraform backend store?

- [ ] A. tfplan files
- [ ] B. Terraform binary
- [ ] C. Provider plugins
- [x] D. State file

> Reference https://www.terraform.io/docs/language/settings/backends/local.html

#### Q35. You have multiple team members collaborating on infrastructure as code (IaC) using Terraform and want to apply formatting standards for readability. How can you format Terraform HCL (HashiCorp Configuration Language) code according to standard Terraform style convention?

- [ ] A. Run the terraform fmt command during the code linting phase of your CI/CD process
- [ ] B. Designate one person in each team to review and format everyone's code
- [ ] C. Manually apply two spaces indentation and align equal sign "=" characters in every Terraform file (*.tf)
- [ ] D. Write a shell script to transform Terraform files using tools such as AWK, Python, and sed

> Reference https://www.terraform.io/docs/language/syntax/style.html

#### Q36. What value does the Terraform Cloud/Terraform Enterprise private module registry provide over the public Terraform Module Registry?

- [ ] A. The ability to share modules with public Terraform users and members of Terraform Enterprise Organizations
- [ ] B. The ability to tag modules by version or release.
- [x] C. The ability to restrict modules to members of Terraform Cloud or Enterprise organizations.
- [ ] D. The ability to share modules publicly with any user of Terraform.

> Reference https://www.terraform.io/docs/language/modules/sources.html

#### Q37. Which task does terraform init not perform?

- [ ] A. Sources all providers present in the configuration and ensures they are downloaded and available locally.
- [ ] B. Connects to the backend.
- [ ] C. Sources any modules and copies the configuration locally.
- [x] D. Validates all required variables are present.

> Reference https://www.terraform.io/docs/cli/commands/init.html

#### Q38. You have declared a variable called var.list which is a list of objects that all have an attribute id. Which options will produce a list of the IDs? (Choose two.)

- [x] A. { for o in var.list : o => o.id }
- [ ] B. var.list[*].id
- [x] C. [ var.list[*].id ]
- [ ] D. [ for o in var.list : o.id ]

> You can retrieve the list of IDs in your Terraform configuration using either of these options: output "users_splat" { value = var.users[*].id } output "users_for" { value = [for user in var.users : user.id] } Both these outputs will produce the same list of IDs: ["id1", "id2", "id3"].

#### Q39. Which argument(s) is (are) required when declaring a Terraform variable?

- [ ] A. type
- [ ] B. default
- [ ] C. description
- [ ] D. All of the above
- [x] E. None of the above

> Terraform CLI defines the following OPTIONAL arguments for variable declarations: default - A default value which then makes the variable optional. type - This argument specifies what value types are accepted for the variable. description - This specifies the input variable's documentation. validation - A block to define validation rules, usually in addition to type constraints. sensitive - Limits Terraform UI output when the variable is used in configuration. nullable - Specify if the variable can be null within the module. Reference https://www.terraform.io/docs/language/values/variables.html

#### Q40. When using a module block to reference a module stored on the public Terraform Module Registry such as: How do you specify version 1.0.0?

- [ ] A. Modules stored on the public Terraform Module Registry do not support versioning
- [x] B. Append ?ref=v1.0.0 argument to the source path
- [ ] C. Add version = "1.0.0" attribute to module block
- [ ] D. Nothing modules stored on the public Terraform Module Registry always default to version 1.0.0.

> 

#### Q41. What features does the hosted service Terraform Cloud provide? (Choose two.)

- [ ] A. Automated infrastructure deployment visualization
- [ ] B. Automatic backups
- [x] C. Remote state storage
- [x] D. A web-based user interface (UI).

> Reference https://www.terraform.io/docs/enterprise/admin/automated-recovery.html https://www.terraform.io/docs/language/state/remote.html

#### Q42. Where does the Terraform local backend store its state?

- [ ] A. In the /tmp directory
- [ ] B. In the terraform file
- [x] C. In the terraform.tfstate file
- [ ] D. In the user's terraform.state file.

> The local backend stores state on the local filesystem, locks that state using system APIs, and performs operations locally. Reference https://www.terraform.io/docs/language/settings/backends/local.html

#### Q43. Which option cannot be used to keep secrets out of Terraform configuration files?

- [ ] A. A Terraform provider.
- [ ] B. Environment variables
- [ ] C. A -var flag
- [x] D. secure string.

> Terraform does not have a built-in concept of a "secure string". This means that you cannot use the secure_string keyword to define a secret in your Terraform configuration file. Link below recommends the three options. e.g. Vault e.g. export TF_VAR_db_username=admin TF_VAR_db_password=adifferentpassword -var-file="secret.tfvars" Reference https://secrethub.io/blog/secret-management-for-terraform/

#### Q44. What is one disadvantage of using dynamic blocks in Terraform?

- [ ] A. They cannot be used to loop through a list of values.
- [ ] B. Dynamic blocks can construct repeatable nested blocks.
- [x] C. They make configuration harder to read and understand.
- [ ] D. Terraform will run more slowly.

> Reference https://github.com/hashicorp/terraform/issues/19291

#### Q45. Only the user that generated a plan may apply it.

- [ ] A. True
- [x] B. False.

> 

#### Q46. Examine the following Terraform configuration, which uses the data source for an AWS AMI. What value should you enter for the ami argument in the AWS instance resource?

- [ ] A. aws_ami.ubuntu
- [x] B. data.aws_ami.ubuntu
- [ ] C. data.aws_ami.ubuntu.id
- [ ] D. aws_ami.ubuntu.id

> resource "aws_instance" "web" { ami = data.aws_ami.ubuntu.id Reference https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance

#### Q47. FILL BLANK - You need to specify a dependency manually. What resource meta-parameter can you use to make sure Terraform respects the dependency? Type your answer in the field provided. The text field is not case-sensitive and all variations of the correct answer are accepted.

- [x] A. depends_on

> Correct Answer: depends_on

#### Q48. You have never used Terraform before and would like to test it out using a shared team account for a cloud provider. The shared team account already contains 15 virtual machines (VM). You develop a Terraform configuration containing one VM, perform terraform apply, and see that your VM was created successfully. What should you do to delete the newly-created VM with Terraform?

- [x] A. The Terraform state file contains all 16 VMs in the team account. Execute terraform destroy and select the newly-created VM.
- [ ] B. The Terraform state file only contains the one new VM. Execute terraform destroy.
- [ ] C. Delete the Terraform state file and execute Terraform apply.
- [ ] D. Delete the VM using the cloud provider console and terraform apply to apply the changes to the Terraform state file.

> 

#### Q49. What is the name assigned by Terraform to reference this resource?

- [x] A. dev
- [ ] B. azurerm_resource_group
- [ ] C. azurerm
- [ ] D. test

> 

#### Q50. Setting the TF_LOG environment variable to DEBUG causes debug messages to be logged into syslog.

- [ ] A. True
- [x] B. False.

> Reference https://www.terraform.io/docs/internals/debugging.html

#### Q51. Where in your Terraform configuration do you specify a state backend?

- [x] A. The terraform block
- [ ] B. The resource block
- [ ] C. The provider block
- [ ] D. The datasource block.

> Backends are configured with a nested backend block within the top-level terraform block Reference https://www.terraform.io/docs/language/settings/backends/configuration.html

#### Q52. In Terraform 0.13 and above, outside of the required_providers block, Terraform configurations always refer to providers by their local names.

- [x] A. True
- [ ] B. False.

> Outside of the required_providers block, Terraform configurations always refer to providers by their local names. Reference https://www.terraform.io/docs/language/providers/requirements.html

#### Q53. What command should you run to display all workspaces for the current configuration?

- [ ] A. terraform workspace
- [ ] B. terraform workspace show
- [x] C. terraform workspace list
- [ ] D. terraform show workspace.

> terraform workspace list The command will list all existing workspaces. Reference https://www.terraform.io/docs/cli/commands/workspace/list.html

#### Q54. Terraform providers are always installed from the Internet.

- [ ] A. True
- [x] B. False

> Terraform configurations must declare which providers they require, so that Terraform can install and use them. Reference https://www.terraform.io/docs/language/providers/configuration.html

#### Q55. Which of these is the best practice to protect sensitive values in state files?

- [ ] A. Blockchain
- [ ] B. Secure Sockets Layer (SSL)
- [x] C. Enhanced remote backends
- [ ] D. Signed Terraform providers

> Use of remote backends and especially the availability of Terraform Cloud, there are now a variety of backends that will encrypt state at rest and will not store the state in cleartext on machines running. Reference https://www.terraform.io/docs/extend/best-practices/sensitive-state.html

#### Q56. When does terraform apply reflect changes in the cloud environment?

- [ ] A. Immediately
- [x] B. However long it takes the resource provider to fulfill the request
- [ ] C. After updating the state file
- [ ] D. Based on the value provided to the -refresh command line argument
- [ ] E. None of the above.

> 

#### Q57. How would you reference the "name" value of the second instance of this fictitious resource?

- [ ] A. element(aws_instance.web, 2)
- [x] B. aws_instance.web[1].name
- [ ] C. aws_instance.web[1]
- [ ] D. aws_instance.web[2].name
- [ ] E. aws_instance.web.*.name.

> Reference https://www.terraform.io/docs/configuration-0-11/interpolation.html

#### Q58. A Terraform provider is not responsible for:

- [ ] A. Understanding API interactions with some service
- [x] B. Provisioning infrastructure in multiple clouds
- [ ] C. Exposing resources and data sources based on an API
- [ ] D. Managing actions to take based on resource differences.

> Reference https://www.terraform.io/docs/configuration-0-11/providers.html

#### Q59. Terraform provisioners can be added to any resource block.

- [x] A. True
- [ ] B. False.

> Reference https://www.terraform.io/docs/language/resources/provisioners/syntax.html

#### Q60. What is terraform refresh intended to detect?

- [ ] A. Terraform configuration code changes
- [ ] B. Empty state files
- [x] C. State file drift
- [ ] D. Corrupt state files.

> Reference https://www.hashicorp.com/blog/detecting-and-managing-drift-with-terraform

#### Q61. FILL BLANK - Which flag would you add to terraform plan to save the execution plan to a file?

- [ ] A. Type your answer in the field provided. The text field is not case-sensitive and all variations of the correct answer are accepted.

> Reference https://www.terraform.io/docs/cli/commands/plan.html

#### Q62. FILL BLANK - What is the name of the default file where Terraform stores the state? Type your answer in the field provided. The text field is not case-sensitive and all variations of the correct answer are accepted.

- [x] A. terraform.tfstate

> Terraform must store state about your managed infrastructure and configuration. This state is used by Terraform to map real world resources to your configuration, keep track of metadata, and to improve performance for large infrastructures. This state is stored by default in a local file named 'terraform.tfstate', but it can also be stored remotely, which works better in a team environment. Reference https://www.terraform.io/docs/language/state/index.html

#### Q63. A Terraform local value can reference other Terraform local values.

- [x] A. True
- [ ] B. False.

> Reference https://www.terraform.io/docs/configuration-0-11/locals.html

#### Q64. Which of the following is not a valid Terraform collection type?

- [ ] A. list
- [ ] B. map
- [x] C. tree
- [ ] D. set

> Reference https://www.terraform.io/docs/language/expressions/type-constraints.html

#### Q65. When running the command terraform taint against a managed resource you want to force recreation upon, Terraform will immediately destroy and recreate the resource.

- [ ] A. True
- [x] B. False

> Mark as taint until next apply, then destroys and recreates. Reference https://www.devopsschool.com/blog/terraform-taint-and-untaint-explained-with-example-programs-and-tutorials/

#### Q66. All standard backend types support state storage, locking, and remote operations like plan, apply and destroy.

- [x] A. True
- [ ] B. False

> 

#### Q67. How can terraform plan aid in the development process?

- [x] A. Validates your expectations against the execution plan without permanently modifying state
- [ ] B. Initializes your working directory containing your Terraform configuration files
- [ ] C. Formats your Terraform configuration files
- [ ] D. Reconciles Terraform state against deployed resources and permanently modifies state using the current status of deployed resources.

> Reference https://github.com/hashicorp/terraform/issues/19235

#### Q68. You would like to reuse the same Terraform configuration for your development and production environments with a different state file for each. Which command would you use?

- [x] A. terraform import
- [ ] B. terraform workspace
- [ ] C. terraform state
- [ ] D. terraform init

> 

#### Q69. What is the name assigned by Terraform to reference this resource?

- [ ] A. compute_instance
- [x] B. main
- [ ] C. google
- [ ] D. teat

> 

#### Q70. You're building a CI/CD (continuous integration/ continuous delivery) pipeline and need to inject sensitive variables into your Terraform run. How can you do this safely?

- [ ] A. Pass variables to Terraform with a -var flag.
- [ ] B. Copy the sensitive variables into your Terraform code.
- [ ] C. Store the sensitive variables in a secure_vars.tf file.
- [ ] D. Store the sensitive variables as plain text in a source code repository.

> 

#### Q71. Your security team scanned some Terraform workspaces and found secrets stored in a plaintext in state files. How can you protect sensitive data stored in Terraform state files?

- [x] A. Delete the state file every time you run Terraform.
- [ ] B. Store the state in an encrypted backend.
- [ ] C. Edit your state file to scrub out the sensitive data.
- [ ] D. Always store your secrets in a secrets.tfvars file.

> Reference https://www.terraform.io/docs/language/state/sensitive-data.html

#### Q72. In contrast to Terraform Open Source, when working with Terraform Enterprise and Cloud Workspaces, conceptually you could think about them as completely separate working directories.

- [x] A. True
- [ ] B. False.

> 

#### Q73. You want to know from which paths Terraform is loading providers referenced in your Terraform configuration (*.tf files). You need to enable debug messages to find this out. Which of the following would achieve this?

- [ ] A. Set the environment variable TF_LOG=TRACE
- [ ] B. Set verbose logging for each provider in your Terraform configuration.
- [ ] C. Set the environment variable TF_VAR_log=TRACE
- [ ] D. Set the environment variable TF_LOG_PATH.

> Reference https://www.terraform.io/docs/cli/config/environment-variables.html

#### Q74. How is terraform import run?

- [ ] A. As a part of terraform init
- [ ] B. As a part of terraform plan
- [ ] C. As a part of terraform refresh
- [x] D. By an explicit call
- [ ] E. All of the above.

> Latest version of Terraform can import as part of apply in case you have import {} clauses. Since this is not part of the answers, explicit call remains, answer D.

#### Q75. You have a simple Terraform configuration containing one virtual machine (VM) in a cloud provider. You run terraform apply and the VM is created successfully. What will happen if you delete the VM using the cloud provider console, and run terraform apply again without changing any Terraform code?

- [ ] A. Terraform will remove the VM from state file.
- [ ] B. Terraform will report an error.
- [x] C. Terraform will not make any changes.
- [ ] D. Terraform will recreate the VM.

> 

#### Q76. Which of these options is the most secure place to store secrets for connecting to a Terraform remote backend?

- [x] A. Defined in Environment variables.
- [ ] B. Inside the backend block within the Terraform configuration
- [ ] C. Defined in a connection configuration outside of Terraform.
- [ ] D. None of above.

> Reference https://www.terraform.io/language/settings/backends/configuration#credentials-and-sensitive-data

#### Q77. Your DevOps team is currently using the local backend for your Terraform configuration. You would like to move to a remote backend to begin storing the state file in a central location. Which of the following backends would not work?

- [ ] A. Amazon S3
- [x] B. Artifactory
- [ ] C. Git
- [ ] D. Terraform Cloud.

> Reference https://secrethub.io/blog/secret-management-for-terraform/

#### Q78. Which backend does the Terraform CLI use by default?

- [ ] A. Terraform Cloud
- [ ] B. Consul
- [ ] C. Remote
- [x] D. Local

> Reference https://www.terraform.io/docs/language/settings/backends/configuration.html

#### Q79. When you initialize Terraform, where does it cache modules from the public Terraform Module Registry?

- [ ] A. On disk in the /tmp directory
- [ ] B. In memory
- [x] C. On disk in the .terraform sub-directory
- [ ] D. They are not cached.

> Reference https://www.terraform.io/docs/language/modules/sources.html

#### Q80. You write a new Terraform configuration and immediately run terraform apply in the CLI using the local backend. Why will the apply fail?

- [x] A. Terraform needs you to format your code according to best practices first
- [ ] B. Terraform needs to install the necessary plugins first
- [ ] C. The Terraform CLI needs you to log into Terraform cloud first
- [ ] D. Terraform requires you to manually run terraform plan first.

> 

#### Q81. What features stops multiple admins from changing the Terraform state at the same time?

- [ ] A. Version control
- [ ] B. Backend types
- [ ] C. Provider constraints
- [x] D. State locking

> Reference https://blog.gruntwork.io/how-to-manage-terraform-state-28f5697e68fa

#### Q82. A fellow developer on your team is asking for some help in refactoring their Terraform code. As part of their application's architecture, they are going to tear down an existing deployment managed by Terraform and deploy new. However, there is a server resource named aws_instance.ubuntu[1] they would like to keep performing some additional analysis. What command should be used to tell Terraform to no longer manage the resource?

- [x] A. terraform apply rm aws_instance.ubuntu[1]
- [ ] B. terraform state rm aws_instance.ubuntu[1]
- [ ] C. terraform plan rm aws_instance.ubuntu[1]
- [ ] D. terraform delete aws_instance.ubuntu[1].

> Reference https://www.terraform.io/docs/cli/commands/state/rm.html

#### Q83. Terraform can only manage resource dependencies if you set them explicitly with the depends_on argument.

- [ ] A. True
- [x] B. False.

> Reference https://learn.hashicorp.com/tutorials/terraform/dependencies?in=terraform/0-13

#### Q84. A terraform apply can not _________ infrastructure.

- [ ] A. change
- [ ] B. destroy
- [ ] C. provision
- [x] D. import

> *with the new “import” block, in fact, it can.

#### Q85. You need to constrain the GitHub provider to version 2.1 or greater. Which of the following should you put into the Terraform 0.12 configuration's provider block?

- [ ] A. version >= 2.1
- [ ] B. version ~> 2.1
- [x] C. version = "<= 2.1"
- [ ] D. version = ">= 2.1"

> Reference https://github.com/hashicorp/terraform-provider-null/issues/31

#### Q86. You just scaled your VM infrastructure and realized you set the count variable to the wrong value. You correct the value and save your change. What do you do next to make your infrastructure match your configuration?

- [ ] A. Run an apply and confirm the planned changes.
- [ ] B. Inspect your Terraform state because you want to change it.
- [ ] C. Reinitialize because your configuration has changed.
- [ ] D. Inspect all Terraform outputs to make sure they are correct.

> 

#### Q87. Terraform provisioners that require authentication can use the ______ block.

- [x] A. connection
- [ ] B. credentials
- [ ] C. secrets
- [ ] D. ssh.

> 

#### Q88. Terraform validate reports syntax check errors from which of the following scenarios?

- [ ] A. Code contains tabs indentation instead of spaces
- [x] B. There is missing value for a variable
- [ ] C. The state files does not match the current infrastructure
- [ ] D. None of the above.

> Reference http://man.hubwiz.com/docset/Terraform.docset/Contents/Resources/Documents/docs/commands/validate.html

#### Q89. Which of the following is allowed as a Terraform variable name?

- [ ] A. count
- [x] B. name
- [ ] C. source
- [ ] D. version

> Reference https://www.terraform.io/docs/language/values/variables.html

#### Q90. What type of block is used to construct a collection of nested configuration blocks?

- [ ] A. for_each
- [ ] B. repeated
- [ ] C. nesting
- [x] D. dynamic

> Reference https://www.hashicorp.com/blog/hashicorp-terraform-0-12-preview-for-and-for-each

#### Q91. Module variable assignments are inherited from the parent module and do not need to be explicitly set.

- [ ] A. True
- [x] B. False.

> Modules do not inherit variables from the parent module. All modules are self-contained units. So, you have to explicitly define variables in the child module, and then explicit set these variables in the parent module, when you instantiate the child module. Reference https://github.com/hashicorp/terraform/issues/15818

#### Q92. If writing Terraform code that adheres to the Terraform style conventions, how would you properly indent each nesting level compared to the one above it?

- [ ] A. With four spaces
- [ ] B. With a tab
- [ ] C. With three spaces
- [x] D. With two spaces

> Reference https://www.terraform.io/docs/language/syntax/style.html

#### Q93. Which of the following is not an action performed by terraform init?

- [x] A. Create a sample main.tf file
- [ ] B. Initialize a configured backend
- [ ] C. Retrieve the source code for all referenced modules
- [ ] D. Load required provider plugins.

> Reference https://www.terraform.io/docs/cli/init/index.html

#### Q94. HashiCorp Configuration Language (HCL) supports user-defined functions.

- [ ] A. True
- [x] B. False.

> Reference https://www.packer.io/docs/templates/hcl_templates/functions

#### Q95. How can you trigger a run in a Terraform Cloud workspace that is connected to a Version Control System (VCS) repository?

- [ ] A. Only Terraform Cloud organization owners can set workspace variables on VCS connected workspaces.
- [x] B. Commit a change to the VCS working directory and branch that the Terraform Cloud workspace is connected to.
- [ ] C. Only members of a VCS organization can open a pull request against repositories that are connected to Terraform Cloud workspaces.
- [ ] D. Only Terraform Cloud organization owners can approve plans in VCS connected workspaces.

> Reference https://www.terraform.io/docs/cloud/vcs/index.html

#### Q96. Terraform and Terraform providers must use the same major version number in a single configuration.

- [ ] A. True
- [x] B. False

> Reference https://www.terraform.io/docs/language/expressions/version-constraints.html

#### Q97. Which statement describes a goal of infrastructure as code?

- [ ] A. An abstraction from vendor specific APIs
- [ ] B. Write once, run anywhere.
- [ ] C. A pipeline process to test and deliver software.
- [x] D. The programmatic configuration of resources.

> 

#### Q98. When using Terraform to deploy resources into Azure, which scenarios are true regarding state files? (Choose two.)

- [ ] A. When a change is made to the resources via the Azure Cloud Console, the changes are recorded in a new state file.
- [x] B. When a change is made to the resources via the Azure Cloud Console, Terraform will update the state file to reflect them during the next plan or apply.
- [x] C. When a change is made to the resources via the Azure Cloud Console, the current state file will not be updated.
- [ ] D. When a change is made to the resources via the Azure Cloud Console, the changes are recorded in the current state file.

> 

#### Q99. You need to deploy resources into two different cloud regions in the same Terraform configuration. To do that, you declare multiple provider configurations as follows: What meta-argument do you need to configure in a resource block to deploy the resource to the `us-west-2` AWS region?

- [ ] A. alias = west
- [x] B. provider = west
- [ ] C. provider = aws.west
- [ ] D. alias = aws.west.

> Reference https://github.com/hashicorp/terraform/issues/451

#### Q100. You have declared an input variable called environment in your parent module. What must you do to pass the value to a child module in the configuration?

- [ ] A. Add node_count = var.node_count
- [ ] B. Declare the variable in a terraform.tfvars file.
- [x] C. Declare a node_count input variable for child module.
- [ ] D. Nothing, child modules inherit variables of parent module.

> When passing variables from a parent module to a child module in Terraform, you need to explicitly declare the variables in both the parent and the child modules. In this case, you would need to declare an input variable for the child module that corresponds to the input variable declared in the parent module. So, the correct option is C. Option A is incorrect because it is using an example variable that is not related to the input variable mentioned in the question. Option B is incorrect because it refers to how to set the value of the variable, but not how to pass the value from the parent to the child module. Option D is also incorrect because child modules do not automatically inherit the variables of their parent modules.

#### Q101. If a module declares a variable with a default, that variable must also be defined within the module.

- [ ] A. True
- [x] B. False

> If a module declares a variable with a default value, it is not necessary to define the variable within the module calling the module. The module will automatically use the default value if a value is not explicitly assigned to the variable in the calling module

#### Q102. Which option cannot be used to keep secrets out of Terraform configuration files?

- [ ] A. Environment Variables
- [x] B. Mark the variable as sensitive.
- [ ] C. A Terraform provider.
- [ ] D. A -var flag.

> Environment Variables: This method keeps secrets out of configuration files by setting them externally. Mark the variable as sensitive: While this marks the variable as sensitive in Terraform's state and prevents it from being displayed in CLI outputs, the secret can still be present in the configuration files and state file. A Terraform provider: This doesn't inherently store or hide secrets in configuration files. A -var flag: This method can be used to pass variables at runtime, thus keeping them out of configuration files. Reference https://developer.hashicorp.com/terraform/tutorials/configuration-language/sensitive-variable

#### Q103. Which of the following arguments are required when declaring a Terraform output?

- [ ] A. sensitive
- [ ] B. description
- [ ] C. default
- [x] D. value

> 

#### Q104. Your risk management organization requires that new AWS S3 buckets must be private and encrypted at rest. How can Terraform Enterprise automatically and proactively enforce this security control?

- [x] A. With a Sentinel policy, which runs before every apply.
- [ ] B. By adding variables to each TFE workspace to ensure these settings are always enabled
- [ ] C. With an S3 module with proper settings for buckets
- [ ] D. Auditing cloud storage buckets with a vulnerability scanning tool.

> 

#### Q105. Most Terraform providers interact with ____________.

- [x] A. API
- [ ] B. VCS Systems
- [ ] C. Shell scripts
- [ ] D. None of the above.

> 

#### Q106. terraform validate validates that your infrastructure matches the Terraform state file.

- [ ] A. True
- [x] B. False

> 

#### Q107. What does terraform import allow you to do?

- [ ] A. Import a new Terraform module
- [ ] B. Use a state file to import infrastructure to the cloud
- [x] C. Import provisioned infrastructure to your state file
- [ ] D. Import an existing state file to a new Terraform workspace.

> 

#### Q108. FILL BLANK - In the below configuration, how would you reference the module output vpc_id? module "vpc" { source = "terraform-and-modules/vpc/aws" cidr = "10.0.0.0/16" name = "test-vpc" } Type your answer in the field provided. The text field is not case sensitive and all variations of the correct answer are accepted.

- [x] A. module.vpc.vpc_id

> Correct Answer: module.vpc.vpc_id

#### Q109. How would you reference the Volume IDs associated with the ebs_block_device blocks in this configuration?

- [ ] A. aws_instance.example.ebs_block_device.[*].volume_id
- [ ] B. aws_instance.example.ebs_block_device.volume_id
- [ ] C. aws_instance.example.ebs_block_device[sda2,sda3].volume_id
- [x] D. aws_instance.example.ebs_block_device.*.volume_id.

> The brackets do not work, asterisk only.

#### Q110. What does state locking accomplish?

- [ ] A. Copies the state file from memory to disk
- [ ] B. Encrypts any credentials stored within the state file
- [x] C. Blocks Terraform commands from modifying the state file
- [ ] D. Prevents accidental deletion of the state file.

> Reference https://www.terraform.io/language/state/locking

#### Q111. You just upgraded the version of a provider in an existing Terraform project. What do you need to do to install the new provider?

- [ ] A. Run terraform apply -upgrade
- [x] B. Run terraform init -upgrade
- [ ] C. Run terraform refresh
- [ ] D. Upgrade your version of Terraform.

> 

#### Q112. A module can always refer to all variables declared in its parent module.

- [x] A. True
- [ ] B. False.

> A module can always refer to all variables declared in its parent module.

#### Q113. When you use a remote backend that needs authentication, HashiCorp recommends that you:

- [x] A. Use partial configuration to load the authentication credentials outside of the Terraform code.
- [ ] B. Push your Terraform configuration to an encrypted git repository.
- [ ] C. Write the authentication credentials in the Terraform configuration files.
- [ ] D. Keep the Terraform configuration files in a secret store.

> 

#### Q114. You have a simple Terraform configuration containing one virtual machine (VM) in a cloud provider. You run terraform apply and the VM is created successfully. What will happen if you terraform apply again immediately afterwards without changing any Terraform code?

- [ ] A. Terraform will terminate and recreate the VM.
- [ ] B. Terraform will create another duplicate VM.
- [x] C. Terraform will apply the VM to the state file.
- [ ] D. Nothing.

> 

#### Q115. A junior admin accidentally deleted some of your cloud instances. What does Terraform do when you run terraform apply?

- [ ] A. Build a completely brand new set of infrastructure.
- [ ] B. Tear down the entire workspace infrastructure and rebuild it.
- [x] C. Rebuild only the instances that were deleted.
- [ ] D. Stop and generate an error message about the missing instances.

> 

#### Q116. You have created a main.tf Terraform configuration consisting of an application server, a database, and a load balancer. You ran terraform apply and all resources were created successfully. Now you realize that you do not actually need the load balancer so you run terraform destroy without any flags What will happen?

- [ ] A. Terraform will destroy the application server because it is listed first in the code.
- [x] B. Terraform will prompt you to confirm that you want to destroy all the infrastructure.
- [ ] C. Terraform will destroy the main.tf file.
- [ ] D. Terraform will prompt you to pick which resource you want to destroy.
- [ ] E. Terraform will immediately destroy all the infrastructure.

> 

#### Q117. Which type of block fetches or computes information for use elsewhere in a Terraform configuration?

- [ ] A. provider
- [ ] B. resource
- [ ] C. local
- [x] D. data

> 

#### Q118. You have just developed a new Terraform configuration for two virtual machines with a cloud provider. You would like to create the infrastructure for the first time. Which Terraform command should you run first?

- [ ] A. terraform apply.
- [ ] B. terraform plan.
- [x] C. terraform show.
- [ ] D. terraform init.

> 

#### Q119. All modules published on the official Terraform Module Registry have been verified by HashiCorp.

- [ ] A. True
- [x] B. False.

> Verified modules are expected to be actively maintained by HashiCorp partners. The verified badge isn’t indicative of flexibility or feature support; very simple modules can be verified just because they're great examples of modules. Likewise, an unverified module could be extremely high quality and actively maintained. An unverified module shouldn't be assumed to be poor quality, it only means it hasn't been created by a HashiCorp partner. Reference:  https://developer.hashicorp.com/terraform/registry/modules/verified

#### Q120. You have to initialize a Terraform backend before it can be configured.

- [ ] A. True
- [x] B. False.

> Terraform init requires backend already created and configured

#### Q121. Which of the following does terraform apply change after you approve the execution plan? (Choose two.)

- [x] A. Cloud infrastructure
- [ ] B. The .terraform directory.
- [ ] C. The execution plan.
- [x] D. State file
- [ ] E. Terraform code.

> 

#### Q122. A Terraform backend determines how Terraform loads state and stores updates when you execute ___________.

- [ ] A. apply
- [ ] B. taint
- [ ] C. destroy
- [x] D. All of the above
- [ ] E. None of the above.

> 

#### Q123. What does Terraform use .terraform.lock.hcl file for?

- [x] A. Tracking provider dependencies
- [ ] B. There is no such file.
- [ ] C. Preventing Terraform runs from occurring.
- [ ] D. Storing references to workspaces which are locked.

> The .terraform.lock.hcl file is used to track provider dependencies and their exact versions. This file is automatically generated by Terraform when you run terraform init. It locks the versions of the providers used in your configuration, ensuring that subsequent Terraform runs use the same provider versions for consistency and reproducibility across environments. This file should be committed to your version control system to maintain consistency across team members and environments. Reference https://www.terraform.io/language/files/dependency-lock

#### Q124. You've used Terraform to deploy a virtual machine and a database. You want to replace this virtual machine instance with an identical one without affecting the database. What is the best way to achieve this using Terraform?

- [ ] A. Use the terraform state rm command to remove the VM from state file
- [x] B. Use the terraform taint command targeting the VMs then run terraform plan and terraform apply
- [ ] C. Use the terraform apply command targeting the VM resources only
- [ ] D. Delete the Terraform VM resources from your Terraform code then run terraform plan and terraform apply.

> 

#### Q125. How do you specify a module's version when publishing it to the public Terraform Module Registry?

- [ ] A. The module's configuration page on the Terraform Module Registry
- [ ] B. Terraform Module Registry does not support versioning modules
- [x] C. The release tags in the associated repo
- [ ] D. The module's Terraform code.

> 

#### Q126. Terraform plan updates your state file.

- [ ] A. True
- [x] B. False

> 

#### Q127. To check if all code in a Terraform configuration with multiple modules is properly formatted without making changes, what command should be run?

- [ ] A. terraform fmt -check
- [ ] B. terraform fmt -write-false
- [ ] C. terraform fmt -list -recursive
- [x] D. terraform fmt -check -recursive.

> terraform fmt takes following options Options: -list=false: Don't list files whose formatting differs (always disabled if using STDIN) -write=false: Don't write to source files (always disabled if using STDIN or -check) -diff: Display diffs of formatting changes -check: Checks if the input is formatted. Exit status will be 0 if all input is properly formatted and non-zero otherwise. -no-color: If specified, output won't contain any color. -recursive: Also process files in subdirectories. By default, only the given directory (or current directory) is processed.

#### Q128. As a member of the operations team, you need to run a script on a virtual machine created by Terraform. Which provision is best to use in your Terraform code?

- [ ] A. null-exec
- [ ] B. local-exec
- [x] C. remote-exec
- [ ] D. file

> Reference https://www.terraform.io/language/resources/provisioners/remote-exec

#### Q129. You are using a networking module in your Terraform configuration with the name label my_network. In your main configuration you have the following code:

- [ ] A. When you run terraform validate, you get the following error:
- [ ] B. What must you do to successfully retrieve this value from your networking module?
- [x] C. Define the attribute vnet_id as a variable in the networking module
- [ ] D. Change the referenced value to module.my_network.outputs.vnet_id
- [ ] E. Define the attribute vnet_id as an output in the networking module
- [ ] F. Change the referenced value to my_network.outputs.vnet_id.

> 

#### Q130. You are writing a child Terraform module which provisions an AWS instance. You want to make use of the IP address returned in the root configuration. You name the instance resource "main". Which of these is the correct way to define the output value using HCL2?


> no such definition as "return"

#### Q131. How can a ticket-based system slow down infrastructure provisioning and limit the ability to scale? (Choose two.)

- [ ] A. A full audit trail of the request and fulfillment process is generated
- [x] B. A request must be submitted for infrastructure changes
- [x] C. As additional resources are required, more tickets are submitted
- [ ] D. A catalog of approved resources can be accessed from drop down lists in a request form.

> 

#### Q132. Which of the following statements about Terraform modules is not true?

- [x] A. Modules must be publicly accessible.
- [ ] B. Modules can be called multiple times.
- [ ] C. Module is a container for one or more resources.
- [ ] D. Modules can call other modules.

> Can be also privately accessible.

#### Q133. Which Terraform collection type should you use to store key/value pairs?

- [ ] A. tuple
- [ ] B. set
- [x] C. map
- [ ] D. list

> 

#### Q134. You have used Terraform to create an ephemeral development environment in the cloud and are now ready to destroy all the infrastructure described by your Terraform configuration. To be safe, you would like to first see all the infrastructure that will be deleted by Terraform. Which command should you use to show all of the resources that will be deleted? (Choose two.)

- [ ] A. Run terraform plan -destroy.
- [x] B. Run terraform show -destroy.
- [ ] C. Run terraform destroy and it will first output all the resources that will be deleted before prompting for approval.
- [ ] D. Run terraform show -destroy.

> 

#### Q135. When do you need to explicitly execute terraform refresh?

- [ ] A. Before every terraform plan
- [ ] B. Before every terraform apply
- [ ] C. Before every terraform import
- [x] D. None of the above.

> 

#### Q136. All Terraform Cloud tiers support team management and governance.

- [ ] A. True
- [x] B. False

> "Cloud Free" does not provide "Team management". In below link, click "Unified workflow management" under "Features" and search the whole page (Ctrl-F) with "Team management". Reference: https://www.hashicorp.com/products/terraform/pricing

#### Q137. What advantage does an operations team that uses infrastructure as code have?

- [ ] A. The ability to delete infrastructure.
- [ ] B. The ability to update existing infrastructure.
- [x] C. The ability to reuse best practice configurations and settings.
- [ ] D. The ability to autoscale a group of servers.

> 

#### Q138. You have modified your Terraform configuration to fix a typo in the Terraform ID of a resource from aws_security_group.htp to aws_security_group.http Which of the following commands would you run to update the ID in state without destroying the resource?

- [ ] A. Terraform state mv aws_security_group.htp aws_security_group.http
- [ ] B. terraform apply
- [ ] C. terraform refresh.

> 

#### Q139. You are creating a Terraform configuration which needs to make use of multiple providers, one for AWS and one for Datadog. Which of the following provider blocks would allow you to do this?


> Reference https://www.terraform.io/language/providers/configuration

#### Q140. Terraform variable names are saved in the state file.

- [ ] A. True
- [x] B. False

> 

#### Q141. Terraform Cloud is available only as a paid offering from HashiCorp.

- [ ] A. True
- [x] B. False

> 

#### Q142. Which of the following is not a way to trigger terraform destroy?

- [ ] A. Using the destroy command with auto-approve.
- [ ] B. Running terraform destroy from the correct directory and then typing "yes" when prompted in the CLI.
- [x] C. Passing --destroy at the end of a plan request.
- [x] D. Delete the state file and run terraform apply.

> 

#### Q143. Which of the following is not an advantage of using infrastructure as code operations?

- [ ] A. Self-service infrastructure deployment
- [x] B. Troubleshoot via a Linux diff command.
- [ ] C. Public cloud console configuration workflows
- [ ] D. Modify a count parameter to scale resources.
- [ ] E. API driven workflows.

> 

#### Q144. You're writing a Terraform configuration that needs to read input from a local file called id_rsa.pub. Which built-in Terraform function can you use to import the file's contents as a string?

- [ ] A. fileset("id_rsa.pub")
- [ ] B. filebase64("id_rsa.pub")
- [x] C. templatefile("id_rsa.pub")
- [ ] D. file("id_rsa.pub").

> 

#### Q145. What does Terraform use providers for? (Choose three.)

- [x] A. Provision resources for on-premises infrastructure services
- [x] B. Simplify API interactions.
- [x] C. Provision resources for public cloud infrastructure services
- [ ] D. Enforce security and compliance policies.
- [ ] E. Group a collection of Terraform configuration files that map to a single state file.

> 

#### Q146. You can reference a resource created with for_each using a Splat (*) expression.

- [ ] A. True
- [x] B. False

> “A resource”. Only one can’t be referenced by Splat.

#### Q147. How does Terraform determine dependencies between resources?

- [x] A. Terraform automatically builds a resource graph based on resources, provisioners, special meta-parameters, and the state file, if present.
- [ ] B. Terraform requires all dependencies between resources to be specified using the depends_on parameter.
- [ ] C. Terraform requires resources in a configuration to be listed in the order they will be created to determine dependencies.
- [ ] D. Terraform requires resource dependencies to be defined as modules and sourced in order.

> 

#### Q148. Which parameters does terraform import require? (Choose two.)

- [ ] A. Path
- [ ] B. Provider
- [x] C. Resource ID
- [x] D. Resource address.

> 

#### Q149. Once a new Terraform backend is configured with a Terraform code block, which command(s) is (are) used to migrate the state file?

- [ ] A. terraform apply.
- [ ] B. terraform push.
- [ ] C. terraform destroy, then terraform apply.
- [x] D. terraform init.

> 

#### Q150. What does this code do?

- [x] A. Requires any version of the AWS provider >= 3.0 and < 4.0
- [ ] B. Requires any version of the AWS provider >= 3.0
- [ ] C. Requires any version of the AWS provider after the 3.0 major release, like 4.1.
- [ ] D. Requires any version of the AWS provider > 3.0.

> 

#### Q151. What does terraform refresh modify?

- [ ] A. Your cloud infrastructure
- [x] B. Your state file
- [ ] C. Your Terraform plan.
- [ ] D. Your Terraform configuration.

> 

#### Q152. Which of the following is not valid source path for specifying a module?

- [x] A. source = "./modulelversion=v1.0.0"
- [ ] B. source = "github.com/hashicorp/example?ref=v1.0.0"
- [ ] C. source = "./module"
- [ ] D. source = "hashicorp/consul/aws".

> 

#### Q153. Which of the following is true about terraform apply? (Choose two.)

- [x] A. It only operates on infrastructure defined in the current working directory or workspace.
- [ ] B. You must pass the output of a terraform plan command to it.
- [x] C. Depending on provider specification, Terraform may need to destroy and recreate your infrastructure resources.
- [ ] D. By default, it does not refresh your state file to reflect current infrastructure configuration.
- [ ] E. You cannot target specific resources for the operation.

> 

#### Q154. Which of the following statements about local modules is incorrect?

- [ ] A. Local modules are not cached by terraform init command.
- [ ] B. Local modules are sourced from a directory on disk.
- [x] C. Local modules support versions.
- [ ] D. All of the above (all statements above are incorrect)
- [ ] E. None of the above (all statements above are correct).

> 

#### Q155. Which of the following is true about Terraform's implementation of infrastructure as code? (Choose two.)

- [ ] A. It is only compatible with AWS infrastructure management
- [ ] B. You cannot reuse infrastructure configuration
- [x] C. You can version your infrastructure configuration
- [ ] D. It requires manual configuration of infrastructure resources
- [x] E. It allows you to automate infrastructure provisioning.

> 

#### Q156. You need to write some Terraform code that adds 42 firewall rules to a security group as shown in the example. What can you use to avoid writing 42 different nested ingress config blocks by hand?

- [ ] A. A count loop
- [ ] B. A for block
- [x] C. A for each block
- [ ] D. A dynamic block.

> Reference https://awstip.com/terraform-for-vs-for-each-7ff8506a1f94

#### Q157. Which of the following is the safest way to inject sensitive values into a Terraform Cloud workspace?

- [ ] A. Write the value to a file and specify the file with the -var-file flag
- [x] B. Set a value for the variable in the UI and check the "Sensitive" check box
- [ ] C. Edit the state file directly just before running terraform apply
- [ ] D. Set the variable value on the command line with the -var flag.

> 

#### Q158. terraform apply will fail if you have not a terraform plan first to update the plan output.

- [ ] A. True
- [x] B. False.

> 

#### Q159. How would you reference the attribute "name" of this fictitious resource in HCL?

- [ ] A. resource.kubernetes_namespace.example.name
- [ ] B. kubernetes_namespace.test.name
- [x] C. kubernetes_namespace.example.name
- [ ] D. data.kubernetes_namespace.name
- [ ] E. None of the above.

> 

#### Q160. A Terraform output that sets the "sensitive" argument to true will not store that value in the state file.

- [ ] A. True
- [x] B. False.

> 

#### Q161. Which are forbidden actions when the Terraform state file is locked? (Choose three.)

- [x] A. terraform destroy
- [ ] B. terraform fmt
- [ ] C. terraform state list
- [x] D. terraform apply
- [x] E. terraform plan
- [ ] F. terraform validate

> 

#### Q162. Terraform installs its providers during which phase?

- [ ] A. Plan
- [x] B. Init
- [ ] C. Refresh
- [ ] D. All of the above.

> 

#### Q163. When does Sentinel enforce policy logic during a Terraform Enterprise run?

- [ ] A. Before the plan phase
- [ ] B. During the plan phase
- [x] C. Before the apply phase
- [ ] D. After the apply phase.

> Enforcing policy checks on runs - Policies are checked when a run is performed, after the terraform plan but before it can be confirmed or the terraform apply is executed.

#### Q164. What is the purpose of a Terraform workspace in either open source or enterprise?

- [x] A. Workspaces allow you to manage collections of infrastructure in state files
- [ ] B. A logical separation of business units
- [ ] C. A method of grouping multiple infrastructure security policies
- [ ] D. Provides limited access to a cloud environment.

> 

#### Q165. Which is the best way to specify a tag of v1.0.0 when referencing a module stored in Git (for example git::https://example.com/vpc.git)?

- [x] A. Append ?ref=v1. 0. 0 argument to the source path
- [ ] B. Add version = "1.0.0" parameter to module block
- [ ] C. Nothing: modules stored on GitHub always default to version 1.0.0
- [ ] D. Modules stored on GitHub do not support versioning.

> source = "git::https://example.com/vpc.git?ref=v1.2.0"

#### Q166. Changing the Terraform backend from the default "local" backend to a different one after doing your first terraform apply is:

- [ ] A. Mandatory
- [x] B. Optional
- [ ] C. Impossible
- [ ] D. Discouraged

> 

#### Q167. You have modified your local Terraform configuration and ran terraform plan to review the changes. Simultaneously, your teammate manually modified the infrastructure component you are working on. Since you already ran terraform plan locally, the execution plan for terraform apply will be the same.

- [ ] A. True
- [x] B. False

> 

#### Q168. terraform apply is failing with the following error. What next step should you take to determine the root cause of the problem?

- [x] A. Error loading state: AccessDenied: Access Denied status code: 403, request id: 288766CE5CCA24A0, host id: FOOBAR
- [ ] B. Set TF_LOG=DEBUG
- [ ] C. Review syslog for Terraform error messages
- [ ] D. Run terraform login to reauthenticate with the provider
- [ ] E. Review /var/log/terraform.log for error messages.

> You can set TF_LOG to one of the log levels (in order of decreasing verbosity) TRACE, DEBUG, INFO, WARN or ERROR to change the verbosity of the log

#### Q169. As a member of an operations team that uses infrastructure as code (IaC) practices, you are tasked with making a change to an infrastructure stack running in a public cloud. Which pattern would follow IaC best practices for making a change?

- [ ] A. Clone the repository containing your infrastructure code and then run the code.
- [ ] B. Use the public cloud console to make the change after a database record has been approved.
- [ ] C. Make the change programmatically via the public cloud CLI.
- [x] D. Make the change via the public cloud API endpoint.
- [ ] E. Submit a pull request and wait for an approved merge of the proposed changes.

> 

#### Q170. What command can you run to generate DOT (Document Template) formatted data to visualize Terraform dependencies?

- [ ] A. terraform refresh
- [ ] B. terraform show
- [x] C. terraform graph
- [ ] D. terraform output

> 

#### Q171. Which provider authentication method prevents credentials from being stored in the state file?

- [x] A. Using environment variables
- [ ] B. Specifying the login credentials in the provider block
- [ ] C. Setting credentials as Terraform variables
- [ ] D. None of the above.

> 

#### Q172. Running terraform fmt without any flags in a directory with Terraform configuration files will check the formatting of those files without changing their contents.

- [ ] A. True
- [x] B. False

> 

#### Q173. terraform init retrieves the source code for all referenced modules.

- [x] A. True
- [ ] B. False.

> Reference https://www.terraform.io/cli/commands/init

#### Q174. You have a Terraform configuration that defines a single virtual machine with no references to it. You have run terraform apply to create the resource, and then removed the resource definition from your Terraform configuration file. What will happen when you run terraform apply in the working directory again?

- [x] A. Nothing
- [ ] B. Terraform will destroy the virtual machine.
- [ ] C. Terraform will error.
- [ ] D. Terraform will remove the virtual machine from the state file, but the resource will still exist.

> 

#### Q175. Which configuration consistency errors does terraform validate report?

- [ ] A. A mix of spaces and tabs in configuration files
- [ ] B. Differences between local and remote state
- [ ] C. Terraform module isn't the latest version.
- [x] D. Declaring a resource identifier more than once.

> 

#### Q176. Pregunta no disponible - contenido en imagen no extraíble

- [x] A. Opción no disponible

> Esta pregunta no pudo ser extraída del documento original

#### Q177. Where can Terraform not load a provider from?

- [x] A. Source code
- [ ] B. Plugins directory
- [ ] C. Official HashiCorp distribution on releases.hashicorp.com
- [ ] D. Provider plugin cache.

> no info about TF loading a provider directly from source code, so this must be the correct answer. In the plugin directory are stored the providers, so TF could load providers from it. releases.hashicorp.com is a valid source where providers can be downloaded from. If the plugin provider cache is enabled eventually a provider could be loaded from it.

#### Q178. Which of the following locations can Terraform use as a private source for modules? (Choose two.)

- [x] A. Internally hosted SCM (Source Control Manager) platform
- [ ] B. Public Terraform Module Registry
- [x] C. Private repository on GitHub
- [ ] D. Public repository on GitHub.

> 

#### Q179. Why should secrets not be hard coded into Terraform code? (Choose two.)

- [x] A. It makes the code less reusable.
- [x] B. Terraform code is typically stored in version control, as well as copied to the systems from which it's run. Any of those may not have robust security mechanisms.
- [ ] C. The Terraform code is copied to the target resources to be applied locally and could expose secrets if a target resource is compromised.
- [ ] D. All passwords should be rotated on a quarterly basis.

> AB, terraform code will not be copied to target resource, only to runners; if you deploy a VM the code will not copied to the VM

#### Q180. If a Terraform creation-time provisioner fails, what will occur by default?

- [ ] A. The resource will not be affected, but the provisioner will need to be applied again.
- [ ] B. The resource will be destroyed.
- [x] C. The resource will be marked as "tainted."
- [ ] D. Nothing, provisioners will not show errors in the command line.

> Reference https://www.terraform.io/language/resources/provisioners/syntax#creation-time-provisioner

#### Q181. When should Terraform configuration files be written when running terraform import on existing infrastructure?

- [ ] A. Infrastructure can be imported without corresponding Terraform code.
- [ ] B. Terraform will generate the corresponding configuration files for you.
- [ ] C. You should write Terraform configuration files after the next terraform import is executed.
- [x] D. Terraform configuration should be written before terraform import is executed.

> The current implementation of Terraform import can only import resources into the state. It does not generate configuration. A future version of Terraform will also generate configuration. Because of this, prior to running terraform import it is necessary to write manually a resource configuration block for the resource, to which the imported object will be mapped. Reference https://www.terraform.io/cli/import

#### Q182. Which command lets you experiment with Terraform's built-in functions?

- [ ] A. terraform env
- [x] B. terraform console
- [ ] C. terraform test
- [ ] D. terraform validate

> Reference https://www.terraform.io/language/functions

#### Q183. Why does this backend configuration not follow best practices?.

- [x] A. You should not store credentials in Terraform Configuration
- [ ] B. You should use the local enhanced storage backend whenever possible
- [ ] C. An alias meta-argument should be included in backend blocks whenever possible
- [ ] D. The backend configuration should contain multiple credentials so that more than one user can execute terraform plan and terraform apply

> 

#### Q184. Open source Terraform can only import publicly-accessible and open-source modules.

- [ ] A. True
- [x] B. False.

> Reference https://www.terraform.io/language/modules

#### Q185. What does terraform destroy do?

- [x] A. Destroy all infrastructure in the Terraform state file.
- [ ] B. Destroy all Terraform code files in the current directory while leaving the state file intact.
- [ ] C. Destroy all infrastructure in the configured Terraform provider.
- [ ] D. Destroy the Terraform state file while leaving infrastructure intact.

> Reference https://learn.hashicorp.com/tutorials/terraform/aws-destroy

#### Q186. While attempting to deploy resources into your cloud provider using Terraform, you begin to see some odd behavior and experience sluggish responses. In order to troubleshoot you decide to turn on Terraform debugging. Which environment variables must be configured to make Terraform's logging more verbose?

- [ ] A. TF_LOG_LEVEL
- [ ] B. TF_LOG_FILE
- [x] C. TF_LOG
- [ ] D. TP_LOG_PATH.

> Reference https://www.terraform.io/internals/debugging

#### Q187. If a DevOps team adopts AWS CloudFormation as their standardized method for provisioning public cloud resources, which of the following scenarios poses a challenge for this team?

- [ ] A. The team is asked to build a reusable code base that can deploy resources into any AWS region.
- [ ] B. The team is asked to manage a new application stack built on AWS-native services.
- [x] C. The organization decides to expand into Azure and wishes to deploy new infrastructure using their existing codebase.
- [ ] D. The DevOps team is tasked with automating a manual provisioning process.

> Reference https://developer.hashicorp.com/terraform/intro/vs/cloudformation

#### Q188. You cannot install third party plugins using terraform init.

- [ ] A. True
- [x] B. False.

> 

#### Q189. Which of the following can you do with terraform plan? (Choose two.)

- [x] A. Save a generated execution plan to apply later.
- [ ] B. Execute a plan in a different workspace.
- [x] C. View the execution plan and check if the changes match your expectations.
- [ ] D. Schedule Terraform to run at a planned time in the future.

> Reference https://learn.hashicorp.com/tutorials/terraform/plan

#### Q190. Which are examples of infrastructure as code? (Choose two.)

- [ ] A. Cloned virtual machine images.
- [ ] B. Change management database records.
- [x] C. Versioned configuration files
- [x] D. Docker files.

> 

#### Q191. FILL BLANK - You need to migrate a workspace to use a remote backend. After updating your configuration, what command do you run to perform the migration? Type your answer in the field provided. The text field is not case-sensitive and all variations of the correct answer are accepted.

- [x] A. terraform init

> Correct Answer: terraform init. Reference https://developer.hashicorp.com/terraform/cli/commands/init

#### Q192. When using a module from the public Terraform Module Registry, the following parameters are required attributes in the module block. (Choose two.)

- [x] A. Each of the module’s required inputs
- [x] B. The module’s source address
- [ ] C. Terraform Module Registry account token.
- [ ] D. Each of the module’s dependencies (example: submodules)
- [ ] E. The version of the module.

> Reference https://developer.hashicorp.com/terraform/language/modules/syntax

#### Q193. As a developer, you want to ensure your plugins are up to date with the latest versions. Which Terraform command should you use?

- [x] A. terraform init -upgrade.
- [ ] B. terraform apply -upgrade.
- [ ] C. terraform refresh -upgrade.
- [ ] D. terraform providers -upgrade.

> 

#### Q194. You can access state stored with the local backend by using the terraform_remote_state data source.

- [ ] A. True
- [x] B. False.

> The terraform_remote_state data source is used to fetch outputs from the state of a different Terraform configuration, which is stored remotely, and use them as input for the current configuration. It is used with remote backends, not local ones.

#### Q195. You have been working in a Cloud provider account that is shared with other team members. You previously used Terraform to create a load balancer that is listening on port 80. After some application changes, you updated the Terraform code to change the port to 443.

- [ ] A. You run terraform plan and see that the execution plan shows the port changing from 80 to 443 like you intended, and step away to grab some coffee.
- [ ] B. In the meantime, another team member manually changes the load balancer port to 443 through the Cloud provider console before you get back to your desk.
- [x] C. What will happen when you terraform apply upon returning to your desk?
- [ ] D. Terraform will fail with an error because the state file is no longer accurate.
- [ ] E. Terraform will change the load balancer port to 80, and then change it back to 443.
- [ ] F. Terraform will not make any changes to the Load Balancer and will update the state file to reflect any changes made.
- [ ] G. Terraform will change the port back to 80 in your code.

> 

#### Q196. In a Terraform Cloud workspace linked to a version control repository, speculative plan runs start automatically when you merge or commit changes to version control.

- [x] A. True
- [ ] B. False.

> Reference https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings/vcs

#### Q197. You have some Terraform code and a variable definitions file named dev.auto.tfvars that you tested successfully in the dev environment. You want to deploy the same code in the staging environment with a separate variable definition file and a separate state file. Which two actions should you perform? (Choose two.)

- [x] A. Copy the existing terraform.tfstate file and save it as staging.terraform.tfstate
- [x] B. Write a new staging.auto.tfvars variable definition file and run Terraform with the var-file=”staging.auto.tfvars” flag
- [ ] C. Create a new Terraform workspace for staging.
- [ ] D. Create a new Terraform provider for staging.
- [ ] E. Add new Terraform code (*.tf files) for staging in the same directory.

> 

#### Q198. The ________ determines how Terraform creates, updates, or deletes resources.

- [ ] A. Terraform configuration.
- [ ] B. Terraform core.
- [x] C. Terraform provider.
- [ ] D. Terraform provisioner.

> provider = how, .tf = what

#### Q199. Terraform destroy is the only way to remove infrastructure.

- [ ] A. True
- [x] B. False.

> 

#### Q200. Which of the following is the correct way to pass the value in the variable num_servers into a module with the input servers in HCL2?

- [x] A. servers = var.num_servers
- [ ] B. servers = num_servers
- [ ] C. servers = var(num_servers)
- [ ] D. $(var.num_servers).

> 

#### Q201. Which of the fallowing commands would you use to access all of the attributes and details of a resource managed by Terraform?

- [ ] A. terraform state list
- [x] B. terraform state show
- [ ] C. terraform get
- [ ] D. terraform state list.

> Reference https://developer.hashicorp.com/terraform/cli/commands/state/show

#### Q202. How would you be able to reference an attribute from the vsphere_datacenter data source for use with the datacenter_id argument within the vsphere_folder resource in the following configuration?

- [ ] A. data.dc.id
- [ ] B. data.vsphere_datacenter.dc
- [ ] C. vsphere_datacenter.dc.id
- [x] D. data.vsphere_datacenter.dc.id.

> 

#### Q203. You decide to move a Terraform state file to Amazon S3 from another location. You write the code below into a file called backend.tf. Which command will migrate your current state file to the new S3 remote backend?

- [x] A. terraform state.
- [ ] B. terraform init.
- [ ] C. terraform refresh.
- [ ] D. terraform push.

> 

#### Q204. You want to tag multiple resources with a string that is a combination of a generated random_id and a variable. How should you use the same value in all these resources without repeating the random_id and variable in each resource?

- [ ] A. Local values
- [ ] B. Data source
- [ ] C. Modules
- [ ] D. Outputs.

> 

#### Q205. Which of the following is not a benefit of adopting infrastructure as code?

- [x] A. Interpolation
- [ ] B. Reusability of code
- [ ] C. Versioning
- [ ] D. Automation.

> 

#### Q206. Module version is required to reference a module on the Terraform Module Registry.

- [ ] A. True
- [x] B. False

> Specifying a versions is not mandatory. When a version is not specified, Terraform just downloads the latest version

#### Q207. While deploying a virtual machine, the first launch user_data script fails due to race condition with another resource deployed during the same Terraform run. What is the least disruptive method to correct the issue?

- [ ] A. Run terraform taint against the virtual machine’s resource name, then terraform apply.
- [ ] B. Restart the virtual machine from the cloud portal.
- [ ] C. Run terraform apply again.
- [ ] D. Run terraform destroy then terraform apply.

> Reference https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax

#### Q208. The public Module Registry is free to use.

- [x] A. True
- [ ] B. False.

> 

#### Q209. Both Terraform Cloud and Terraform Enterprise support policy as code (Sentinel).

- [x] A. True
- [ ] B. False

> 

#### Q210. You want to define multiple data disks as nested blocks inside the resource block for a virtual machine. What Terraform feature would help you define the blocks using the values in a variable?

- [ ] A. Local values
- [x] B. Collection functions
- [ ] C. Dynamic blocks
- [ ] D. Count arguments.

> 

#### Q211. Which of the following module source paths does not specify a remote module?

- [x] A. source = “./modules/consul”
- [ ] B. source = “git@github.com:hashicorp/example.git”
- [ ] C. source = “github.com/hashicorp/example”
- [ ] D. source = “hashicorp/consul/aws.

> since its local path and question says "remote".

#### Q212. You have a list of numbers that represents the number of free CPU cores on each virtual cluster:

- [x] A. numcpus = [ 18, 3, 7, 11, 2 ]
- [ ] B. What Terraform function could you use to select the largest number from the list?
- [ ] C. max(numcpus)
- [ ] D. ceil(numcpus)
- [ ] E. top(numcpus)
- [ ] F. high[numcpus]

> Reference https://developer.hashicorp.com/terraform/language/functions/

#### Q213. Variables declared within a module are accessible outside of the module.

- [ ] A. True
- [x] B. False.

> 

#### Q214. Which of the following is not a valid Terraform variable type?

- [ ] A. list
- [ ] B. map
- [x] C. array
- [ ] D. string

> 

#### Q215. What is a key benefit of the Terraform state file?

- [ ] A. A state file can be used to schedule recurring infrastructure tasks.
- [ ] B. A state file represents a source of truth for resources provisioned with a public cloud console.
- [ ] C. A state file represents the desired state expressed by the Terraform code files.
- [x] D. A state file represents a source of truth for resources provisioned with Terraform.

> A key benefit of the Terraform state file is that it represents a source of truth for resources provisioned with Terraform. The state file is used to keep track of the current state of the infrastructure resources that are being managed by Terraform. It contains information about the resources, their properties, and the dependencies between them. The state file is used by Terraform to determine what changes need to be made to the infrastructure to reach the desired state defined in the configuration files.

#### Q216. Which of these statements about Terraform Enterprise workspaces is false?

- [ ] A. They can securely store cloud credentials.
- [x] B. You must use the CLI to switch between workspaces.
- [ ] C. Plans and applies can be triggered via version control system integrations.
- [ ] D. They have role-based access controls.

> Terraform Enterprise provides a web-based UI that allows you to switch between workspaces, view the state of your infrastructure, and run Terraform commands without having to use the command line interface.

#### Q217. Define the purpose of state in Terraform.

- [x] A. State is used to map real world resources to your configuration and keep track of metadata
- [ ] B. State is a method of codifying the dependencies of related resources
- [ ] C. State is used to enforce resource configurations that relate to compliance policies
- [ ] D. State is used to store variables and quickly reuse existing code.

> 

#### Q218. Which backend does the Terraform CLI use by default?

- [ ] A. API
- [ ] B. Remote
- [ ] C. Terraform Cloud
- [x] D. Local
- [ ] E. HTTP

> 

#### Q219. Using the terraform state rm command against a resource will destroy it.

- [ ] A. True
- [x] B. False

> 

#### Q220. Which method for sharing Terraform configurations keeps them confidential within your organization, supports Terraform’s semantic version constraints, and provides a browsable directory?

- [ ] A. Generic git repository
- [x] B. Terraform Cloud/Terraform Enterprise private module registry
- [ ] C. Public Terraform Module Registry
- [ ] D. Subfolder within a workspace.

> The Terraform Cloud/Terraform Enterprise private module registry allows organizations to store and share Terraform configurations in a private and secure way. This method keeps the configurations confidential within your organization, supports Terraform's semantic version constraints, and provides a browsable directory.

#### Q221. You are writing a child Terraform module which provisions an AWS instance. You want to make use of the IP address returned in the root configuration. You name the instance resource “main”. Which of these is the correct way to define the output value using HCL2?

- [ ] A. C.
- [ ] B. D.

> C is not valid because the quotes.

#### Q222. How would you refer to the indexing instance from the below configuration?

- [ ] A. aws_instance[“web”][“indexing”]
- [ ] B. aws_instance.web.indexing
- [ ] C. aws_instance-web[“indexing”]
- [x] D. aws_instance.web[“indexing”]

> 

#### Q223. Which feature is not included in Terraform Cloud’s free tier?

- [ ] A. Workspace
- [ ] B. Remote state management
- [x] C. Audit logging
- [ ] D. Private module registry

> Reference https://www.hashicorp.com/products/terraform/pricing

#### Q224. When should you run terraform init?

- [ ] A. After you run terraform apply for the first time in a new Terraform project and before you run terraform plan
- [ ] B. After you run terraform plan for the first time in a new Terraform project and before you run terraform apply
- [x] C. After you start coding a new Terraform project and before you run terraform plan for the first time
- [ ] D. Before you start coding a new Terraform project

> 

#### Q225. Terraform configuration (including any module references) can contain only one Terraform provider type.

- [x] A. True
- [x] B. False

> “Can” indicates that could be one or many so the answer is “A.” If the question is “must”, then the answer is “B.”

#### Q226. You are making changes to existing Terraform code to add some new infrastructure. When is the best time to run terraform validate?

- [ ] A. After you run terraform plan so you can validate that your state file is consistent with your infrastructure
- [x] B. Before you run terraform plan so you can validate your code syntax
- [ ] C. Before you run terraform apply so you can validate your infrastructure changes
- [ ] D. After you run terraform apply so you can validate that your infrastructure is reflected in your code

> 

#### Q227. How does Terraform manage most dependencies between resources?

- [ ] A. By defining dependencies as modules and including them in a particular order
- [ ] B. The order that resources appear in Terraform configuration indicates dependencies
- [ ] C. Using the depends_on parameter
- [x] D. Terraform will automatically manage most resource dependencies

> 

#### Q228. What does running a terraform plan do?

- [ ] A. Imports all of your existing cloud provider resources to the state file
- [x] B. Compares the state file to your Terraform code and determines if any changes need to be made
- [ ] C. Imports all of your existing cloud provider resources to your Terraform configuration file
- [ ] D. Compares your Terraform code and local state file to the remote state file in a cloud provider and determines if any changes need to be made

> 

#### Q229. What are some benefits of using Sentinel with Terraform Cloud/Terraform Enterprise? (Choose three.)

- [x] A. Policy-as-code can enforce security best practices
- [x] B. You can restrict specific configurations on resources like "CIDR=0.0.0.0/0" not allowed
- [x] C. You can enforce a list of approved AWS AMIs
- [ ] D. Sentinel Policies can be written in HashiCorp Configuration Language (HCL)
- [ ] E. You can check out and check in cloud access keys

> Sentinel is a policy-as-code framework that integrates with Terraform Cloud and Terraform Enterprise, allowing you to enforce policies on your infrastructure as part of the provisioning process. By using Sentinel, you can enforce security best practices, restrict specific configurations such as disallowing overly permissive CIDR blocks, and maintain a list of approved AWS AMIs, among other things. This helps to ensure that your infrastructure is secure, compliant, and adheres to organizational standards.

#### Q230. You want to share Terraform state with your team, store it securely, and provide state locking. How would you do this? (Choose three.)

- [x] A. Using the remote Terraform backend with Terraform Cloud / Terraform Enterprise.
- [ ] B. Using the local backend.
- [ ] C. Using the s3 terraform backend. The dynamodb_field option is not needed.
- [x] D. Using an s3 terraform backend with an appropriate IAM policy and dynamodb_field option configured.
- [x] E. Using the consul Terraform backend.

> Dynamodb_field acts as “lease” on Azure Storage. Reference: https://developer.hashicorp.com/terraform/language/settings/backends/s3 flag needs to be enabled

#### Q231. From which of these sources can Terraform import modules?

- [ ] A. Local path
- [ ] B. GitHub Repository
- [ ] C. Terraform Module Registry
- [x] D. All of the above

> 

#### Q232. How would you output returned values from a child module?

- [ ] A. Declare the output in the root configuration
- [x] B. Declare the output in the child module
- [ ] C. Declare the output in both the root and child module
- [ ] D. None of the above

> In Terraform, it is not necessary to declare an output in both the root and child module. The output declared in the child module will be available to the root module, so you only need to declare an output in the root module if you want to expose that value to the outside world or use it in another module. If you declare an output in both the root and child module with the same name, Terraform will use the output from the root module as the final output. This can be useful if you want to override the output value of the child module with a different value in the root module. However, it is generally a good practice to avoid duplicate output names between modules to prevent confusion and ensure that the output values are clearly defined and organized. In summary, it is not necessary to declare an output in both the root and child module, but if you do, the output from the root module will override the output from the child module. It is recommended to use unique output names to avoid confusion and ensure clear organization of output values

#### Q233. You have decided to create a new Terraform workspace to deploy a development environment. What is different about this workspace?

- [x] A. It has its own state file
- [ ] B. It pulls in a different terraform.tfvars file
- [ ] C. It uses a different branch of code
- [ ] D. It uses a different backend

> 

#### Q234. Any user can publish modules to the public Terraform Module Registry.

- [x] A. True
- [ ] B. False

> 

#### Q235. Which of these commands makes your code more human readable?

- [ ] A. terraform validate
- [ ] B. terraform output
- [ ] C. terraform plan
- [x] D. terraform fmt

> 

#### Q236. Infrastructure as Code (IaC) can be stored in a version control system along with application code.

- [x] A. True
- [ ] B. False

> 

#### Q237. Select the command that doesn’t cause Terraform to refresh its state.

- [ ] A. terraform apply
- [ ] B. terraform destroy
- [ ] C. terraform plan
- [x] D. terraform state list

> 

#### Q238. Sentinel policy-as-code is available in Terraform Enterprise.

- [x] A. True
- [ ] B. False

> Reference https://docs.hashicorp.com/sentinel/terraform

#### Q239. Before you can use Terraform’s remote backend, you must first execute terraform init.

- [x] A. True
- [ ] B. False

> You can configure remote backend without init, but you can’t use it.

#### Q240. Which two steps are required to provision new infrastructure in the Terraform workflow? (Choose two.)

- [ ] A. Plan
- [x] B. Apply
- [ ] C. Import
- [x] D. Init
- [ ] E. Validate

> 

#### Q241. You are working on some new application features and you want to spin up a copy of your production deployment to perform some quick tests. In order to avoid having to configure a new state backend, what open source Terraform feature would allow you create multiple states but still be associated with your current code?

- [ ] A. Terraform data sources
- [ ] B. Terraform local values
- [ ] C. Terraform modules
- [x] D. Terraform workspaces
- [ ] E. None of the above

> 

#### Q242. Which provisioner invokes a process on the machine running Terraform?

- [ ] A. remote-exec
- [ ] B. file
- [x] C. local-exec
- [ ] D. null-exec

> Reference https://developer.hashicorp.com/terraform/language/resources/provisioners/local-exec

#### Q243. ____________ backends support state locking.

- [x] A. Some
- [ ] B. No
- [ ] C. Only local
- [ ] D. All

> 

#### Q244. Which of the following methods, used to provision resources into a public cloud, demonstrates the concept of infrastructure as code?

- [ ] A. curl commands manually run from a terminal
- [ ] B. A sequence of REST requests you pass to a public cloud API endpoint
- [x] C. A script that contains a series of public cloud CLI commands
- [ ] D. A series of commands you enter into a public cloud console

> 

#### Q245. Which of the following should you put into the required_providers block?

- [ ] A. version >= 3.1
- [x] B. version = “>= 3.1”
- [ ] C. version ~> 3.1

> 

#### Q246. When should you write Terraform configuration files for existing infrastructure that you want to start managing with Terraform?

- [x] A. Before you run terraform import
- [ ] B. You can import infrastructure without corresponding Terraform code
- [ ] C. Terraform will generate the corresponding configuration files for you
- [ ] D. After you run terraform import

> 

#### Q247. Which command should you run to check if all code in a Terraform configuration that references multiple modules is properly formatted without making changes?

- [ ] A. terraform fmt -write=false
- [ ] B. terraform fmt -list -recursive
- [x] C. terraform fmt -check -recursive
- [ ] D. terraform fmt -check

> 

#### Q248. What features stops multiple users from operating on the Terraform state at the same time?

- [ ] A. Provider constraints
- [ ] B. Remote backends
- [x] C. State locking
- [ ] D. Version control

> 

#### Q249. You are creating a reusable Terraform configuration and want to include a billing_dept tag so your Finance team can track team-specific spending on resources. Which of the following billing_dept variable declarations will allow you to do this?

- [ ] A. variable "billing_dept" { optional = true }
- [ ] B. variable "billing_dept" { type = optional(string) }
- [x] C. variable "billing_dept" { default = "" }
- [ ] D. variable "billing_dept" { type = default }

> Correct Answer: C

#### Q250. Which of these are secure options for storing secrets for connecting to a Terraform remote backend? (Choose two.)

- [ ] A. Inside the backend block within the Terraform configuration
- [x] B. Defined in Environment variables
- [x] C. Defined in a connection configuration outside of Terraform
- [ ] D. A variable file

> 

#### Q251. You want to define a single input variable to capture configuration values for a server. The values must represent memory as a number, and the server name as a string. Which variable type could you use for this input?

- [ ] A. List
- [x] B. Object
- [ ] C. Map
- [ ] D. Terraform does not support complex input variables of different types

> 

#### Q252. What does Terraform not reference when running a terraform apply -refresh-only?

- [ ] A. Credentials
- [ ] B. State file
- [x] C. Terraform resource definitions in configuration files
- [ ] D. Cloud provider

> 

#### Q253. Multiple team members are collaborating on infrastructure using Terraform and want to format their Terraform code following standard Terraform-style convention. How could they automatically ensure the code satisfies conventions?

- [x] A. Run the terraform fmt command during the code linting phase of your CI/CD process
- [ ] B. Manually apply two spaces indentation and align equal sign "=" characters in every Terraform file (*.tf)
- [ ] C. Run the terraform validate command prior to executing terraform plan or terraform apply

> 

#### Q254. When using a remote backend or Terraform Cloud integration, where does Terraform save resource state?

- [ ] A. On the disk
- [ ] B. In memory
- [ ] C. In an environment variable
- [x] D. In the remote backend or Terraform Cloud

> 

#### Q255. In Terraform HCL, an object type of object({ name=string, age=number }) would match this value:

- [ ] A. { name = "John" age = fifty two }
- [x] B. { name = "John" age = 52 }
- [ ] C. { name = John age = two }
- [ ] D. { name = John age = 52 }

> Correct Answer: B

#### Q256. You add a new resource to an existing Terraform configuration, but do not update the version constraint in the configuration. The existing and new resources use the same provider. The working directory contains a .terraform-lock.hcl file. How will Terraform choose which version of the provider to use?

- [ ] A. Terraform will use the latest version of the provider for the new resource and the version recorded in the lock file to manage existing resources
- [x] B. Terraform will use the version recorded in your lock file
- [ ] C. Terraform will check your state file to determine the provider version to use
- [ ] D. Terraform will use the latest version of the provider available at the time you provision your new resource

> 

#### Q257. You must use different Terraform commands depending on the cloud provider you use.

- [ ] A. True
- [x] B. False

> 

#### Q258. Define the purpose of state in Terraform.

- [ ] A. State stores variables and lets you quickly reuse existing code
- [ ] B. State lets you enforce resource configurations that relate to compliance policies
- [ ] C. State codifies the dependencies of related resources
- [x] D. State maps real world resources to your configuration and keeps track of metadata

> 

#### Q259. Which of these actions will prevent two Terraform runs from changing the same state file at the same time?

- [ ] A. Refresh the state after running Terraform
- [ ] B. Delete the state before running Terraform
- [x] C. Configure state locking for your state backend
- [ ] D. Run Terraform with parallelism set to 1

> 

#### Q260. While attempting to deploy resources into your cloud provider using Terraform, you begin to see some odd behavior and experience slow responses. In order to troubleshoot you decide to turn on Terraform debugging. Which environment variables must be configured to make Terraform’s logging more verbose?

- [ ] A. TF_LOG_PATH
- [ ] B. TF_VAR_log_level
- [x] C. TF_LOG
- [ ] D. TF_VAR_log_path

> 

#### Q261. The Terraform binary version and provider versions must match each other in a single configuration.

- [ ] A. True
- [x] B. False

> 

#### Q262. The .terraform.lock.hcl file tracks module versions.

- [ ] A. True
- [x] B. False

> The .terraform.lock.hcl file is not used to track module versions; it is used to lock the versions of the provider dependencies used by your Terraform configuration. At present, the dependency lock file tracks only provider dependencies. Terraform does not remember version selections for remote modules, and so Terraform will always select the newest available module version that meets the specified version constraints. You can use an exact version constraint to ensure that Terraform will always select the same module version.

#### Q263. You can develop a custom provider to manage its resources using Terraform.

- [x] A. True
- [ ] B. False

> 

#### Q264. Which of these is not a benefit of remote state?

- [ ] A. Keeping unencrypted sensitive information off disk
- [x] B. Easily share reusable code modules
- [ ] C. Working in a team
- [ ] D. Delegate output to other teams

> 

#### Q265. When using multiple configurations of the same Terraform provider, what meta-argument must be included in any non-default provider configurations?

- [ ] A. depends_on
- [x] B. alias
- [ ] C. id
- [ ] D. name

> 

#### Q266. A developer accidentally launched a VM (virtual machine) outside of the Terraform workflow and ended up with two servers with the same name. They don’t know which VM Terraform manages but do have a list of all active VM IDs. Which of the following methods could you use to discover which instance Terraform manages?

- [ ] A. Run terraform taint/code on all the VMs to recreate them
- [ ] B. Update the code to include outputs for the ID of all VMs, then run terraform plan to view the outputs
- [x] C. Run terraform state list to find the names of all VMs, then run terraform state show for each of them to find which VM ID Terraform manages
- [ ] D. Use terraform refresh/code to find out which IDs are already part of state

> 

#### Q267. Which of the following is not considered a safe way to inject sensitive values into a Terraform Cloud workspace?

- [x] A. Edit the state file directly just before running terraform apply
- [ ] B. Set the variable value on the command line with the -var flag
- [ ] C. Write the value to a file and specify the file with the -var-file flag

> 

#### Q268. If you update the version constraint in your Terraform configuration, Terraform will update your lock file the next time you run terraform init.

- [ ] A. True
- [x] B. False

> You will get an error. You have to run terraform init -upgrade to change the version in .terraform.lock.hcl file.

#### Q269. You must initialize your working directory before running terraform validate.

- [x] A. True
- [ ] B. False

> 

#### Q270. If you manually destroy infrastructure, what is the best practice reflecting this change in Terraform?

- [ ] A. Manually update the state file
- [x] B. Remove the resource definition from your file and run terraform apply -refresh-only
- [ ] C. Run terraform import
- [ ] D. It will happen automatically

> 

#### Q271. You created infrastructure outside of the Terraform workflow that you now want to manage using Terraform. Which command brings the infrastructure into Terraform state?

- [ ] A. terraform init
- [ ] B. terraform get
- [ ] C. terraform refresh
- [x] D. terraform import

> 

#### Q272. When using Terraform to deploy resources into Azure, which scenarios are true regarding state files?

- [ ] A. When you change a Terraform-managed resource via the Azure Cloud Console, Terraform updates the state file to reflect the change during the next plan or apply
- [ ] B. Changing resources via the Azure Cloud Console records the change in the current state file
- [ ] C. When you change a resource via the Azure Cloud Console, Terraform records the changes in a new state file
- [x] D. Changing resources via the Azure Cloud Console does not update current state file

> 

#### Q273. Which statement describes a goal of infrastructure as code?

- [ ] A. A pipeline process to test and deliver software
- [ ] B. Defining a vendor-agnostic API
- [ ] C. Write once, run anywhere
- [x] D. The programmatic configuration of resources

> 

#### Q274. Terraform validate confirms the syntax of Terraform files.

- [x] A. True
- [ ] B. False

> 

#### Q275. Which command adds existing resources into Terraform state?

- [ ] A. terraform init
- [ ] B. terraform plan
- [ ] C. terraform refresh
- [x] D. terraform import
- [ ] E. All of these

> 

#### Q276. It is best practice to store secret data in the same version control repository as your Terraform configuration.

- [ ] A. True
- [x] B. False

> 

#### Q277. Which of the following commands would you use to access all of the attributes and details of a resource managed by Terraform?

- [ ] A. terraform state list ‘provider_type.name’
- [x] B. terraform state show ‘provider_type.name’
- [ ] C. terraform get ‘provider_type.name’
- [ ] D. terraform state list

> 

#### Q278. terraform validate confirms that your infrastructure matches the Terraform state file.

- [ ] A. True
- [x] B. False

> 

#### Q279. A senior admin accidentally deleted some of your cloud instances. What does Terraform do when you run terraform apply?

- [ ] A. Build a completely brand new set of infrastructure
- [ ] B. Tear down the entire workspace infrastructure and rebuild it
- [x] C. Rebuild only the instances that were deleted
- [ ] D. Stop and generate an error message about the missing instances.

> 

#### Q280. terraform init creates an example main.tf file in the current directory.

- [ ] A. True
- [x] B. False

> 

#### Q281. Which argument helps prevent unexpected updates when calling Terraform Registry modules?

- [ ] A. count
- [ ] B. source
- [x] C. version
- [ ] D. lifecycle

> The version argument helps prevent unexpected updates when calling Terraform Registry modules. It allows you to specify the exact version of the module you want to use. This ensures that your configuration consistently uses the same version of the module until you explicitly decide to update it to a newer version. Using the version argument is a good practice to ensure that your infrastructure remains stable and predictable, as it prevents unintentional changes caused by automatic module updates.

#### Q282. Setting the TF_LOG environment variable to DEBUG causes debug messages to be logged into stdout.

- [ ] A. True
- [x] B. False

> Terraform has detailed logs that you can enable by setting the TF_LOG environment variable to any value. Enabling this setting causes detailed logs to appear on stderr.

#### Q283. How would you output returned values from a child module in the Terraform CLI output?

- [ ] A. Declare the output in the root configuration
- [x] B. Declare the output in the child module
- [x] C. Declare the output in both the root and child module
- [ ] D. None of the above

> Child parent  Output CLI

#### Q284. What is the Terraform resource name of the following resource block?

- [ ] A. azurerm_resource_group
- [ ] B. azurerm
- [ ] C. test
- [x] D. dev

> 

#### Q285. When do you need to explicitly execute terraform refresh-only?

- [ ] A. Before every terraform plan
- [ ] B. Before every terraform apply
- [ ] C. Before every terraform import
- [x] D. None of the above

> 

#### Q286. How is the Terraform cloud integration differ from other state backends such as S3, Consul, etc.?

- [x] A. It can execute Terraform runs on dedicated infrastructure in Terraform Cloud
- [ ] B. It doesn't show the output of a terraform apply locally
- [ ] C. It is only available to paying customers
- [ ] D. All of the above

> 

#### Q287. Which of the following are advantages of using infrastructure as code (IaC) instead of provisioning with a graphical user interface (GUI)? (Choose two.)

- [ ] A. Secures your credentials
- [x] B. Let’s your version, reuse, and share infrastructure configuration
- [ ] C. Provisions the same resources at a lower cost
- [x] D. Reduces risk of operator error
- [ ] E. Prevents manual modifications to your resources

> 

#### Q288. One cloud configuration always maps to a single remote workspace.

- [ ] A. True
- [x] B. False

> 

#### Q289. Multiple team members are collaborating on infrastructure using Terraform and want to format their Terraform code following standard Terraform-style convention. How could they automatically ensure the code satisfies conventions?

- [ ] A. Replace all tabs with spaces
- [ ] B. Terraform automatically formats configuration on terraform apply
- [ ] C. Run terraform validate prior to executing terraform plan or terraform apply
- [x] D. Use terraform fmt

> 

#### Q290. Which backend does the Terraform CLI use by default?

- [ ] A. Depends on the cloud provider configured
- [ ] B. Remote
- [ ] C. Terraform Cloud
- [x] D. Local
- [ ] E. HTTP

> 

#### Q291. The Terraform CLI will print output values from a child module after running terraform apply.

- [ ] A. True
- [x] B. False.

> A child module can use outputs to expose a subset of its resource attributes to a parent module. A root module can use outputs to print certain values in the CLI output after running terraform apply.

#### Q292. What does terraform refresh-only modify?

- [ ] A. Your cloud infrastructure
- [ ] B. Your Terraform plan
- [ ] C. Your Terraform configuration
- [x] D. Your state file

> 

#### Q293. What does terraform import do?

- [x] A. Imports existing resources into the state file
- [ ] B. Imports all infrastructure from a given cloud provider
- [ ] C. Imports a new Terraform module
- [ ] D. Imports clean copies of tainted resources
- [ ] E. None of the above

> 

#### Q294. Which of the following is the correct way to pass the value in the variable num_servers into a module with the input server?

- [ ] A. servers = var(num_servers)
- [ ] B. $(var.num_servers)
- [ ] C. servers = num_servers
- [x] D. servers = var.num_servers

> 

#### Q295. A developer on your team is going to tear down an existing deployment managed by Terraform and deploy a new one. However, there is a server resource named aws_instance.ubuntu[1] they would like to keep. What command should they use to tell Terraform to stop managing that specific resource?

- [ ] A. terraform destroy aws_instance.ubuntu[1]
- [ ] B. terraform apply rm aws_instance.ubuntu[1]
- [x] C. terraform state rm aws_instance.ubuntu[1]
- [ ] D. terraform plan rm aws_instance.ubuntu[1]

> 

#### Q296. Before you can use a remote backend, you must first execute terraform init.

- [x] A. True
- [ ] B. False

> 

#### Q297. What does running a terraform plan do?

- [ ] A. Compares your Terraform code and local state file to the remote state file in a cloud provider and determines if any changes need to be made
- [ ] B. Imports all of your existing cloud provider resources to the state file
- [ ] C. Installs all providers and modules referenced by configuration
- [x] D. Compares the state file to your Terraform code and determines if any changes need to be made

> 

#### Q298. Which of the following statements about Terraform modules is not true?

- [x] A. Modules must be publicly accessible
- [ ] B. You can call the same module multiple times
- [ ] C. A module is a container for one or more resources
- [ ] D. Modules can call other modules

> Not necessarily must be public. Can be private.

#### Q299. How can a ticket-based system slow down infrastructure provisioning and limit the ability to scale? (Choose two.)

- [x] A. End-users have to request infrastructure changes
- [ ] B. Ticket based systems generate a full audit trail of the request and fulfillment process
- [ ] C. Users can access a catalog of approved resources from drop down lists in a request form
- [x] D. The more resources your organization needs, the more tickets your infrastructure team has to process

> 

#### Q300. How do you specify a module's version when publishing it to the public Terraform Module Registry?

- [ ] A. Configure it in the module's Terraform code
- [ ] B. Mention it on the module s configuration page on the Terraform Module Registry
- [ ] C. The Terraform Module Registry does not support versioning modules
- [x] D. Tag a release in the associated repo

> 

#### Q301. What Terraform command always causes a state file to be updated with changes that might have been made outside of Terraform?

- [x] A. terraform plan -refresh-only
- [ ] B. terraform show -json
- [ ] C. terraform apply -lock-false
- [ ] D. terraform plan -target-state.

> None is valid, needs to be on “apply” phase.

#### Q302. Which command must you first run before performing further Terraform operations in a working directory?

- [ ] A. terraform plan
- [ ] B. terraform workspace
- [x] C. terraform init
- [ ] D. terraform import

> 

#### Q303. Which command lets you experiment with Terraform expressions?

- [x] A. terraform console
- [ ] B. terraform validate
- [ ] C. terraform env
- [ ] D. terraform test

> 

#### Q304. What kind of configuration block will create an infrastructure object with settings specified within the block?

- [ ] A. provider
- [ ] B. state
- [ ] C. data
- [x] D. resource

> 

#### Q305. When do changes invoked by terraform apply take effect?

- [ ] A. After Terraform has updated the state file
- [x] B. Once the resource provider has fulfilled the request
- [ ] C. Immediately
- [ ] D. None of the above are correct

> 

#### Q306. What is the workflow for deploying new infrastructure with Terraform?

- [x] A. Write Terraform configuration, run terraform init to initialize the working directory or workspace, and run terraform apply
- [ ] B. Write Terraform configuration, run terraform show to view proposed changes, and terraform apply to create new infrastructure
- [ ] C. Write Terraform configuration, run terraform apply to create infrastructure, use terraform validate to confirm Terraform deployed resources correctly
- [ ] D. Write Terraform configuration, run terraform plan to initialize the working directory or workspace, and terraform apply to create the infrastructure

> 

#### Q307. Which of these are features of Terraform Cloud? (Choose two.)

- [x] A. Remote state storage
- [x] B. A web-based user interface (UI)
- [ ] C. Automatic backups
- [ ] D. Automated infrastructure deployment visualization

> 

#### Q308. Which option can not keep secrets out of Terraform configuration files?

- [ ] A. A shared credential file
- [x] B. Mark the variable as sensitive
- [ ] C. Environment Variables
- [ ] D. A -var flag

> 

#### Q309. Which of the following is not true of Terraform providers?

- [ ] A. An individual person can write a Terraform Provider
- [ ] B. A community of users can maintain a provider
- [ ] C. HashiCorp maintains some providers
- [ ] D. Cloud providers and infrastructure vendors can write, maintain, or collaborate on Terraform providers
- [x] E. None of the above

> All are true.

#### Q310. Which Terraform command checks that your configuration syntax is correct?

- [ ] A. terraform fmt
- [x] B. terraform validate
- [ ] C. terraform init
- [ ] D. terraform show

> 

#### Q311. terraform validate uses provider APIs to verify your infrastructure settings.

- [ ] A. True
- [x] B. False

> 

#### Q312. You add a new provider to your configuration and immediately run terraform apply in the CLI using the local backend. Why does the apply fail?

- [ ] A. Terraform needs you to format your code according to best practices first
- [ ] B. Terraform requires you to manually run terraform plan first
- [ ] C. The Terraform CLI needs you to log into Terraform Cloud first
- [x] D. Terraform needs to install the necessary plugins first

> 

#### Q313. Which of these statements about Terraform Cloud workspaces is false?

- [ ] A. They can securely store cloud credentials
- [ ] B. They have role-based access controls
- [x] C. You must use the CLI to switch between workspaces
- [ ] D. Plans and applies can be triggered via version control system integrations

> Is not mandatory the use of CLI, you can also use UI.

#### Q314. What value does the Terraform Cloud private registry provide over the public Terraform Module Registry?

- [x] A. The ability to restrict modules to members of Terraform Cloud or Enterprise organizations
- [ ] B. The ability to share modules publicly with any user of Terraform
- [ ] C. The ability to tag modules by version or release
- [ ] D. The ability to share modules with public Terraform users and members of Terraform Cloud Organizations

> The primary value of the Terraform Cloud private registry over the public Terraform Module Registry is the ability to restrict modules to members of specific organizations, making option A the most accurate answer. It also allows for the curation of approved modules and providers for your organization, which is not explicitly listed in the options.

#### Q315. Terraform providers are part of the Terraform core binary.

- [ ] A. True
- [x] B. False

> Terraform is logically split into two main parts: Terraform Core and Terraform Plugins. Terraform Core uses remote procedure calls (RPC) to communicate with Terraform Plugins and offers multiple ways to discover and load plugins to use. Terraform Plugins expose an implementation for a specific service, such as AWS, or provisioner, such as bash.

#### Q316. Which of the following is not a benefit of adopting infrastructure as code?

- [ ] A. Reusability of code
- [ ] B. Automation
- [x] C. Graphical User Interface
- [ ] D. Versioning

> 

#### Q317. Where does the Terraform local backend store its state?

- [x] A. In the terraform.tfstate file
- [ ] B. In the .terraform directory
- [ ] C. In the terraform.tfstate directory
- [ ] D. In the .terraform.lock.hcl file

> 

#### Q318. Which of these is true about Terraform's plugin-based architecture?

- [ ] A. Terraform can only source providers from the internet
- [x] B. You can create a provider for your API if none exists
- [ ] C. Every provider in a configuration has its own state file for its resources
- [ ] D. All providers are part of the Terraform core binary

> 

#### Q319. Your risk management organization requires that new AWS S3 buckets must be private and encrypted at rest. How can Terraform Cloud automatically and proactively enforce this security control?

- [ ] A. Auditing cloud storage buckets with a vulnerability scanning tool
- [x] B. With a Sentinel policy, which runs before every apply
- [ ] C. With an S3 module with proper settings for buckets
- [ ] D. By adding variables to each Terraform Cloud workspace to ensure these settings are always enabled

> 

#### Q320. If you don't use the local backend, where does Terraform save resource state?

- [x] A. In the remote backend or Terraform Cloud
- [ ] B. On the disk
- [ ] C. In memory
- [ ] D. In an environment variable

> 

#### Q321. You are writing a child Terraform module that provisions an AWS instance. You want to reference the IP address returned by the child module in the root configuration. You name the instance resource "main". Which of these is the correct way to define the output value?

- [x] A. output "instance_ip_addr" { value = aws_instance.main.private_ip }
- [ ] B. output "aws_instance.instance_ip_addr" { value = ${main.private_ip} }
- [ ] C. output "instance_ip_addr" { return aws_instance.main.private_ip }
- [ ] D. output "aws_instance.instance_ip_addr" { return aws_instance.main.private_ip }

> Correct Answer: A. B is incorrect because the name of the output can't be the address of the resource

#### Q322. When does Sentinel enforce policy logic during a Terraform Cloud run?

- [ ] A. Before the plan phase
- [ ] B. During the plan phase
- [x] C. Before the apply phase
- [ ] D. After the apply phase

> Reference https://developer.hashicorp.com/sentinel/docs/terraform#:~:text=the%20sentinel%20integration%20with%20terraform%20runs%20within%20terraform%20enterprise%20after%20a%20terraform%20plan%20and%20before%20a%20terraform%20apply

#### Q323. What is terraform refresh-only intended to detect?

- [ ] A. Empty state files
- [ ] B. Corrupt state files
- [ ] C. Terraform configuration code changes
- [x] D. State file drift

> The terraform refresh-only command is intended to detect and reconcile any drift between the actual state of the infrastructure and the state described in the Terraform state file.

#### Q324. You should run terraform fmt to rewrite all Terraform configurations within the current working directory to conform to Terraform-style conventions.

- [x] A. True
- [ ] B. False

> 

#### Q325. Why would you use the -replace flag for terraform apply?

- [ ] A. You want to force Terraform to destroy a resource on the next apply
- [ ] B. You want Terraform to ignore a resource on the next apply
- [x] C. You want to force Terraform to destroy and recreate a resource on the next apply
- [ ] D. You want Terraform to destroy all the infrastructure in your workspace

> 

#### Q326. You can configure Terraform to log to a file using the TF_LOG environment variable.

- [ ] A. True
- [x] B. False

> 

#### Q327. When does Terraform create the .terraform.lock.hcl file?

- [ ] A. After your first terraform plan
- [ ] B. After your first terraform apply
- [x] C. After your first terraform init
- [ ] D. Whenever you enable state locking

> Terraform automatically creates or updates the dependency lock file each time you run the terraform init command.

#### Q328. What is the best and easiest way for Terraform to read and write secrets form Hashicorp Vault?

- [ ] A. Api Access using the AppRole auth method
- [ ] B. Integration with a tool like Jenkins
- [ ] C. CLI access from the same machine running Terraform
- [x] D. Vault provider

> 

#### Q329. In Terraform Enterprise, a workspace can be mapped to how many VCS repos?

- [x] A. 1
- [ ] B. 3
- [ ] C. 5
- [ ] D. 2

> 

#### Q330. Hashicorp offers multiple versions of Terraform, including Terraform open-source, Terraform Cloud and Terraform Enterprise. Which of the following Terraform feature is only available in the Enterprise Edition? (select one).

- [ ] A. Audit Logs
- [ ] B. Private Network Connectivity
- [ ] C. Private Module Registry
- [x] D. Locally managed installation
- [ ] E. SAML/SSO

> 

#### Q331. Which Terraform command will force a resource to be destroyed and recreated even if there no configuration changes that would require it?

- [x] A. terraform apply -replace=<address>
- [ ] B. terraform fmt
- [ ] C. terraform apply -refresh-only
- [ ] D. terraform destroy

> 

#### Q332. What is the purpose of using the local-exec provisioner? (select two)

- [ ] A. executes a command on the resource to invoke an update to the Terraform state
- [x] B. to invoke a local executable
- [x] C. to execute one or more commands on the machine running Terraform
- [ ] D. ensures that the resource is only executed in the local infrastructure where Terraform is deployed

> 

#### Q333. Which of the following best describes a Terraform provider?

- [ ] A. serves as a parameter for a Terraform module that allows a module to be customized
- [ ] B. describes an infrastructure object, such a virtual network, compute instance, or other components
- [ ] C. a container for multiple resources that are used together
- [x] D. a plugin that Terraform uses to translate the API interactions with the service or provider

> 

#### Q334. Kristen is using modules to provision an Azure environment for a new application. She is using the following code and specifying a version of her virtual machine module to ensure she's calling the correct module. Which of the following provides support for the versioning of a module? (select two)?

- [ ] A. public module registry
- [ ] B. local file paths
- [x] C. modules stored in GitLab
- [ ] D. private module registry

> Version constraints are supported only for modules installed from a module registry, such as the public Terraform Registry or Terraform Cloud's private module registry. Other module sources can provide their own versioning mechanisms within the source string itself or might not support versions at all. In particular, modules sourced from local file paths do not support version; since they're loaded from the same source repository, they always share the same version as their caller. Reference: https://www.terraform.io/language/modules/syntax#version

#### Q335. Select the answer below that completes the following statement:

- [ ] A. Terraform Cloud can be managed from the CLI but requires ____________?
- [ ] B. a username and password
- [x] C. authentication using MFA
- [ ] D. an API token
- [ ] E. a TOTPtoken

> Terraform Cloud requires it.

#### Q336. What is the downside to using Terraform to interact with sensitive data, such as reading secrets from Vault?

- [ ] A. Terraform requires a unique auth method to work with Vault
- [ ] B. Terraform and Vault must be running on the same physical host
- [ ] C. Terraform and Vault must be running on the same version
- [x] D. secrets are persisted to the state file.

> 

#### Q337. Terry is using a module to deploy some EC2 instances on AWS for a new project. He is viewing the code that is calling the module for deployment, which is shown below. Where is the value of the security group originating?

- [ ] A. from a variable likely declared in a .tfvars file being passed to another module
- [ ] B. the Terraform public module registry
- [x] C. the output of another module
- [ ] D. an environment variable being using during a terraform apply.

> 

#### Q338. In the example below, where is the value of the DNS record's IP address originating from?

- [ ] A. the regular expression named module.web_server
- [x] B. the output of a module named web_server
- [ ] C. value of the web_server parameter from the variables.tf file
- [ ] D. by querying the AWS EC2 API to retrieve the IP address

> 

#### Q339. What does the command terraform fmt do?

- [ ] A. updates the font of the configuration file to the official font supported by HashiCorp
- [ ] B. formats the state file in order to ensure the latest state of resources can be obtained
- [ ] C. deletes the existing configuration file
- [x] D. rewrite Terraform configuration files to a canonical format and style

> 

#### Q340. Which of the following allows Terraform users to apply policy as code to enforce standardized configurations for resources being deployed via infrastructure as code?

- [ ] A. module registry
- [ ] B. workspaces
- [x] C. sentinel
- [ ] D. functions

> 

#### Q341. What Terraform feature is shown in the example below?

- [x] A. Dynamic block
- [ ] B. Data source
- [ ] C. Conditional expression
- [ ] D. Local values

> 

#### Q342. When configuring a remote backend in Terraform, it might be a good idea to purposely omit some of the required arguments to ensure secrets and other relevant data are not inadvertently shared with others. What are the ways the remaining configuration can be added to Terraform so it can initialize and communicate with the backend? (select three)

- [x] A. directly querying HashiCorp Vault for the secrets
- [x] B. use the -backend-config=PATH to specify a separate config file
- [x] C. interactively on the command line
- [ ] D. command-line key/value pairs

> 

#### Q343. In order to make a Terraform configuration file dynamic and/or reusable, static values should be converted to use what?

- [ ] A. module
- [ ] B. regular expressions
- [ ] C. output value
- [x] D. input variables

> 

#### Q344. In regards to deploying resources in multi-cloud environments, what are some of the benefits of using Terraform rather than a provider's native tooling? (select three)

- [ ] A. Terraform is not cloud-agnostic and can be used to deploy resources across a single public cloud
- [x] B. Terraform simplifies management and orchestration, helping operators build large-scale, multi-cloud infrastructure
- [x] C. Terraform can manage cross-cloud dependencies
- [x] D. Terraform can help businesses deploy applications on multiple clouds and on-premises infrastructure

> 

#### Q345. After running into issues with Terraform, you need to enable verbose logging to assist with troubleshooting the error. Which of the following values provides the MOST verbose logging?

- [ ] A. ERROR
- [ ] B. DEBUG
- [x] C. TRACE
- [ ] D. WARN
- [ ] E. INFO

> 

#### Q346. By default, where does Terraform OSS/CLI store its state file?

- [x] A. current working directory
- [ ] B. Amazon S3 bucket
- [ ] C. remotely using Terraform Cloud
- [ ] D. shared directory

> 

#### Q347. You have been given requirements to create a security group for a new application. Since your organization standardizes on Terraform, you want to add this new security group with the fewest number of lines of code. What feature could you use to iterate over a list of required tcp ports to add to the new security group?

- [ ] A. dynamic backend
- [ ] B. splat expression
- [x] C. terraform import
- [ ] D. dynamic block

> 

#### Q348. What happens when a terraform plan is executed?

- [ ] A. applies the changes required in the target infrastructure in order to reach the desired configuration
- [ ] B. the backend is initialized and the working directory is prepped
- [ ] C. reconciles the state Terraform knows about with the real-world infrastructure
- [x] D. creates an execution plan and determines what changes are required to achieve the desired state in the configuration files

> 

#### Q349. When using modules to deploy infrastructure, how would you export a value from one module to import into another module?

- [ ] A. For example, a module dynamically deploys an application instance or virtual machine, and you need the IP address in another module to configure a related DNS record in order to reach the new/y deployed application.
- [ ] B. configure the pertinent provider's configuration with a list of possible IPaddresses to use
- [x] C. preconfigure the IP address as a parameter in the DNS module
- [ ] D. configure an output value in the application module in order to use that value for the DNS module
- [ ] E. export the value using terraform export and input the value using terraform input

> 

#### Q350. Given the Terraform configuration below, which order will the resources be created?

- [ ] A. resources will be created in parallel
- [ ] B. aws_eip will be created first & aws_instance will be created second
- [ ] C. no resources will be created
- [x] D. aws_instance will be created first & aws_eip will be created second

> 

#### Q351. Rick is writing a new Terraform configuration file and wishes to use modules in order to easily consume Terraform code that has already been written. Which of the modules shown below Will be created first?

- [ ] A. module "ec2_instances"
- [x] B. module "vpc"

> 

#### Q352. What are some of the features of Terraform state? (select three)

- [x] A. determining the correct order to destroy resources
- [ ] B. inspection of cloud resources
- [x] C. increased performance
- [x] D. mapping configuration to real-world resources

> 

#### Q353. True or False? Starting in Terraform vO.12, the Terraform language now has built-in syntax for creating lists using the [ and ] delimiters, replacing and deprecating the list ( ) function.?

- [x] A. True
- [ ] B. False

> 

#### Q354. In the terraform block, which configuration would be used to identify the specific version of a provider required?

- [ ] A. required_versions
- [ ] B. required-provider
- [x] C. required_providers
- [ ] D. required-version

> 

#### Q355. In regards to Terraform state file, select all the statements below which are correct: (select four)

- [x] A. storing state remotely can provide better security
- [x] B. Terraform Cloud always encrypts state at rest
- [ ] C. the state file is always encrypted at rest
- [x] D. the Terraform state can contain sensitive data, therefore the state file should be protected from unauthorized access
- [x] E. when using local state, the state file is stored in plain-text
- [ ] F. using the mask feature, you can instruct Terraform to mask sensitive data in the state file

> 

#### Q356. From the answers below, select the advantages of using Infrastructure as Code. (select four)

- [x] A. Easily change and update existing infrastructure
- [x] B. Safely test modifications using a "dry run" before applying any actual changes
- [ ] C. Provide a codified workflow to develop customer-facing applications
- [x] D. Provide reusable modules for easy sharing and collaboration
- [x] E. Easily integrate with application workflows (GitLabActions, Azure DevOps, CI/CD tools)

> Not C, we`re not deploying applications. Only infrastructure

#### Q357. Which of the following best describes the default local backend?

- [x] A. The local backend stores state on the local filesystem, locks the state using system APIS, and performs operations locally.
- [ ] B. The local backend is the directory where resources deployed by Terraform have direct access to in order to update their current state
- [ ] C. The local backend is how Terraform connects to public cloud services, such as AWS, Azure, or GCP.
- [ ] D. The local backend is where Terraform Enterprise stores logs to be processed by a log collector

> 

#### Q358. True or False? Provisioners should only be used as a last resort.

- [x] A. True
- [ ] B. False

> 

#### Q359. What are the benefits of using Infrastructure as Code? (select five)

- [ ] A. Infrastructure as Code easily replaces development languages such as Go and .Net for application development
- [x] B. Infrastructure as Code is relatively simple to learn and write, regardless of a user's prior experience with developing code
- [x] C. Infrastructure as Code is easily repeatable, allowing the user to reuse code to deploy similar, yet different resources
- [x] D. Infrastructure as Code allows a user to turn a manual task into a simple, automated deployment
- [x] E. Infrastructure as Code gives the user the ability to recreate an application's infrastructure for disaster recovery scenarios
- [x] F. Infrastructure as Code provides configuration consistency and standardization among deployments

> No A, we’re deploying infra, not applications

#### Q360. Which of the following is considered a Terraform plugin?

- [ ] A. Terraform logic
- [ ] B. Terraform tooling
- [ ] C. Terraform language
- [x] D. Terraform provider

> 

#### Q361. What are the core Terraform workflow steps to use infrastructure as code?

- [ ] A. 1) Plan 2) Apply 3) Pray
- [ ] B. 1) Code 2) Validate 3) Apply
- [x] C. 1) Write 2) Plan 3) Apply
- [ ] D. 1) Plan 2) Apply 3) Destroy

> Correct Answer: C

#### Q362. Which of the following represents a feature of Terraform Cloud that is NOT free to customers?

- [ ] A. workspace management
- [x] B. team management and governance
- [ ] C. private module registry
- [ ] D. VCS integration

> 

#### Q363. Terraform-specific settings and behaviors are declared in which configuration block type?

- [ ] A. data block
- [x] B. terraform block
- [ ] C. provider block
- [ ] D. resource block

> 

#### Q364. What are some of the problems of how infrastructure was traditionally managed before Infrastructure as Code? (select three)

- [x] A. Traditional deployment methods are not able to meet the demands of the modem business where resources tend to live days to weeks, rather than months to years
- [x] B. Traditionally managed infrastructure can’t keep up with cyclic or elastic applications
- [ ] C. Pointing and clicking in a management console is a scalable approach and reduces human error as businesses are moving to a multi-cloud deployment model
- [x] D. Requests for infrastructure or hardware often required a ticket, increasing the time required to deploy applications

> 

#### Q365. Why is it a good idea to declare the required version of a provider in a Terraform configuration file?

- [ ] A. to remove older versions of the provider
- [x] B. providers are released on a separate schedule from Terraform itself; therefore, a newer version could introduce breaking changes
- [ ] C. to match the version number of your application being deployed via Terraform
- [ ] D. to ensure that the provider version matches the version of Terraform you are using

> 

#### Q366. Stephen is writing brand new code and needs to ensure it is syntactically valid and internally consistent. Stephen doesn't want to wait for Terraform to access any remote services while making sure his code is valid. What command can he use to accomplish this?

- [x] A. terraform validate
- [ ] B. terraform apply -refresh-only
- [ ] C. terraform fmt
- [ ] D. terraform show

> 

#### Q367. Select two answers to complete the following sentence:

- [ ] A. Before a new provider can be used, it must be ______ and ______. (select two)
- [x] B. approved by HashiCorp
- [x] C. initialized
- [ ] D. declared or used in a configuration file
- [ ] E. uploaded to source control

> 

#### Q368. After executing a terraform plan , you notice that a resource has a tilde (~) next to it. What does this mean?

- [ ] A. the resource will be destroyed and recreated
- [ ] B. the resource will be created
- [x] C. the resource will be updated in place
- [ ] D. Terraform can't determine how to proceed due to a problem with the state file

> 

#### Q369. Your organization has moved to AWS and has manually deployed infrastructure using the console. Recently, a decision has been made to standardize on Terraform for all deployments moving forward. What can you do to ensure that the existing resources are managed by Terraform moving forward without causing interruption to existing resources?

- [ ] A. delete the existing resources and recreate them using new a Terraform configuration so Terraform can manage them moving forward
- [ ] B. resources that are manually deployed in the AWS console cannot be imported by Terraform
- [ ] C. submit a ticket to AWS and ask them to export the state of all existing resources and use terraform import to import them into the state file
- [x] D. using terraform import , import the existing infrastructure into your Terraform state

> 

#### Q370. Which of the following Terraform files should be ignored by Git when committing code to a repo? (select two)

- [x] A. terraform.tfvars
- [ ] B. output.tf
- [x] C. terraform.tfstate
- [ ] D. variables.tf

> 

#### Q371. What Terraform command can be used to inspect the current state file?

- [ ] A. terraform read
- [x] B. terraform show
- [ ] C. terraform state
- [ ] D. terraform inspect

> 

#### Q372. Select the feature below that best completes the sentence:

- [ ] A. The following list represents the different types of _____ available in Terraform.
- [ ] B. data sources
- [ ] C. backends
- [x] D. named values
- [ ] E. functions

> 

#### Q373. Which of the following connection types are supported by the remote-exec provisioner? (select two)

- [ ] A. smb
- [x] B. winrm
- [x] C. ssh
- [ ] D. rdp

> 

#### Q374. True or False? State is a requirement for Terraform to function.

- [ ] A. False
- [x] B. True

> 

#### Q375. True or False? Workspaces provide similar functionality in the open-source, Terraform Cloud, and Enterprise versions of Terraform.

- [ ] A. False
- [x] B. True

> 

#### Q376. Published modules via the Terraform Registry provide which of the following benefits? (select four)

- [ ] A. support from any code repo
- [x] B. show examples and READMEs
- [x] C. allow browsing version histories
- [x] D. support versioning
- [x] E. automatically generated documentation

> 

#### Q377. What happens when a terraform apply command is executed?

- [ ] A. the backend is initialized and the working directory is prepped
- [ ] B. reconciles the state Terraform knows about with the real-world infrastructure
- [ ] C. creates the execution plan for the deployment of resources
- [x] D. applies the changes required in the target infrastructure in order to reach the desired configuration

> 

#### Q378. Frank has a file named main.tf which is shown below. Which of the following statements are true about this code? (select two)

- [ ] A. app-cluster is the calling module
- [x] B. main.tf is the calling module
- [ ] C. main.tf is the child module
- [x] D. app-cluster is the child module

> 

#### Q379. Using multi-cloud and provider-agnostic tools provides which of the following benefits? (select two)

- [ ] A. slower provisioning speed allows the operations team to catch mistakes before they are applied
- [x] B. operations teams only need to learn and manage a single tool to manage infrastructure, regardless of where the infrastructure is deployed
- [ ] C. increased risk due to all infrastructure relying on a single tool for management
- [x] D. can be used across major cloud providers and VM hypervisors

> 

