# HashiCorp Vault Associate

Total: 86 preguntas

#### Q1. The vault lease renew command increments the lease time from:

- [x] A. The current time
- [ ] B. The end of the lease

> https://www.examtopics.com/discussions/hashicorp/view/131219-exam-vault-associate-002-topic-1-question-2-discussion/

#### Q2. You have a 2GB Base64 binary large object (blob) that needs to be encrypted. Which of the following best describes the transit secrets engine?

- [ ] A. A data key encrypts the blob locally, and the same key decrypts the blob locally.
- [ ] B. To process such a large blob. Vault will temporarily store it in the storage backend.
- [ ] C. Vault will store the blob permanently. Be sure to run Vault on a compute optimized machine.
- [x] D. The transit engine is not a good solution for binaries of this size.

> https://www.examtopics.com/discussions/hashicorp/view/131215-exam-vault-associate-002-topic-1-question-4-discussion/

#### Q3. How would you describe the value of using the Vault transit secrets engine?

- [ ] A. Vault has an API that can be programmatically consumed by applications
- [ ] B. The transit secrets engine ensures encryption in-transit and at-rest is enforced enterprise wide
- [ ] C. Encryption for application data is best handled by a storage system or database engine, while storing encryption keys in Vault
- [x] D. The transit secrets engine relieves the burden of proper encryption/decryption from application developers and pushes the burden onto the operators of Vault

> https://www.examtopics.com/discussions/hashicorp/view/131220-exam-vault-associate-002-topic-1-question-5-discussion/

#### Q4. What is the Vault CLI command to query information about the token the client is currently using?

- [ ] A. vault lookup token
- [x] B. vault token lookup
- [ ] C. vault lookup self
- [ ] D. vault self lookup

> https://www.examtopics.com/discussions/hashicorp/view/131221-exam-vault-associate-002-topic-1-question-6-discussion/

#### Q5. Which of the following is a machine-oriented Vault authentication backend?

- [ ] A. Okta
- [x] B. AppRole
- [ ] C. Transit
- [ ] D. GitHub

> https://www.examtopics.com/discussions/hashicorp/view/131222-exam-vault-associate-002-topic-1-question-7-discussion/

#### Q6. Security requirements demand that no secrets appear in the shell history. Which command does not meet this requirement?

- [ ] A. generate-password | vault kv put secret/password value=-
- [x] B. vault kv put secret/password value=itsasecret
- [ ] C. vault kv put secret/password value=@data.txt
- [ ] D. vault kv put secret/password value=$SECRET_VALUE

> 

#### Q7. You can build a high availability Vault cluster with any storage backend.

- [ ] A. True
- [x] B. False

> https://www.examtopics.com/discussions/hashicorp/view/131332-exam-vault-associate-002-topic-1-question-9-discussion/

#### Q8. What command creates a secret with the key "my-password" and the value "53cr3t" at path "my-secrets" within the KV secrets engine mounted at "secret"?

- [ ] A. vault kv put secret/my-secrets/my-password 53cr3t
- [ ] B. vault kv write secret/my-secrets/my-password 53cr3t
- [ ] C. vault kv write 53cr3t my-secrets/my-password
- [x] D. vault kv put secret/my-secrets my-password-53cr3t

> https://www.examtopics.com/discussions/hashicorp/view/131333-exam-vault-associate-002-topic-1-question-10-discussion/

#### Q9. What can be used to limit the scope of a credential breach?

- [ ] A. Storage of secrets in a distributed ledger
- [ ] B. Enable audit logging
- [x] C. Use of a short-lived dynamic secrets
- [ ] D. Sharing credentials between applications

> https://www.examtopics.com/discussions/hashicorp/view/131319-exam-vault-associate-002-topic-1-question-11-discussion/

#### Q10. What environment variable overrides the CLI’s default Vault server address?

- [x] A. VAULT_ADDR
- [ ] B. VAULT_HTTP_ADDRESS
- [ ] C. VAULT_ADDRESS
- [ ] D. VAULT_HTTPS_ADDRESS

> https://www.examtopics.com/discussions/hashicorp/view/131320-exam-vault-associate-002-topic-1-question-12-discussion/

#### Q11. Which of the following statements describe the CLI command below? $ vault login -method=ldap username=mitchellh

- [ ] A. Generates a token which is response wrapped
- [x] B. You will be prompted to enter the password
- [ ] C. By default, the generated token is valid for 24 hours
- [ ] D. Fails because the password is not provided

> https://www.examtopics.com/discussions/hashicorp/view/131336-exam-vault-associate-002-topic-1-question-13-discussion/

#### Q12. The following three policies exist in Vault What do these policies allow an organization to do? app.hcl

- [x] A. callcenter.hcl
- [ ] B. rewrap.hcl
- [ ] C. Separates permissions allowed on actions associated with the transit secret engine
- [ ] D. Nothing, as the minimum permissions to perform useful tasks are not present
- [ ] E. Encrypt decrypt, and rewrap data using the transit engine all in one policy
- [ ] F. Create a transit encryption key for encrypting, decrypting, and rewrapping encrypted data

> https://www.examtopics.com/discussions/hashicorp/view/131341-exam-vault-associate-002-topic-1-question-14-discussion/

#### Q13. Your DevOps team would like to provision VMs in GCP via a CICD pipeline. They would like to integrate Vault to protect the credentials used by the tool. Which secrets engine would you recommend?

- [x] A. Google Cloud Secrets Engine
- [ ] B. Identity secrets engine
- [ ] C. Key/Value secrets engine version 2
- [ ] D. SSH secrets engine

> https://www.examtopics.com/discussions/hashicorp/view/131337-exam-vault-associate-002-topic-1-question-15-discussion/

#### Q14. Which of these is not a benefit of dynamic secrets?

- [ ] A. Supports systems which do not natively provide a method of expiring credentials
- [ ] B. Minimizes damage of credentials leaking
- [x] C. Ensures that administrators can see every password used
- [ ] D. Replaces cumbersome password rotation tools and practices

> https://www.examtopics.com/discussions/hashicorp/view/131339-exam-vault-associate-002-topic-1-question-16-discussion/

#### Q15. Which of the following cannot define the maximum time-to-live (TTL) for a token?

- [ ] A. By the authentication method
- [x] B. By the client system
- [ ] C. By the mount endpoint configuration
- [ ] D. A parent token TTL
- [ ] E. System max TTL

> https://www.examtopics.com/discussions/hashicorp/view/131374-exam-vault-associate-002-topic-1-question-17-discussion/

#### Q16. What are orphan tokens?

- [ ] A. Orphan tokens are tokens with a use limit so you can set the number of uses when you create them
- [x] B. Orphan tokens are not children of their parent; therefore, orphan tokens do not expire when their parent does
- [ ] C. Orphan tokens are tokens with no policies attached
- [ ] D. Orphan tokens do not expire when their own max TTL is reached

> https://www.examtopics.com/discussions/hashicorp/view/131342-exam-vault-associate-002-topic-1-question-18-discussion/

#### Q17. To give a role the ability to display or output all of the end points under the /secrets/apps/* end point it would need to have which capability set?

- [ ] A. update
- [ ] B. read
- [ ] C. sudo
- [x] D. list
- [ ] E. None of the above

> https://www.examtopics.com/discussions/hashicorp/view/131376-exam-vault-associate-002-topic-1-question-19-discussion/

#### Q18. When using Integrated Storage, which of the following should you do to recover from possible data loss?

- [ ] A. Failover to a standby node
- [x] B. Use snapshot
- [ ] C. Use audit logs
- [ ] D. Use server logs

> https://www.examtopics.com/discussions/hashicorp/view/131380-exam-vault-associate-002-topic-1-question-21-discussion/

#### Q19. How many Shamir’s key shares are required to unseal a Vault instance?

- [ ] A. All key shares
- [ ] B. A quorum of key shares
- [ ] C. One or more keys
- [x] D. The threshold number of key shares

> https://www.examtopics.com/discussions/hashicorp/view/127827-exam-vault-associate-002-topic-1-question-22-discussion/

#### Q20. Which of these are a benefit of using the Vault Agent?

- [ ] A. Vault Agent allows for centralized configuration of application secrets engines
- [ ] B. Vault Agent will auto-discover which authentication mechanism to use
- [ ] C. Vault Agent will enforce minimum levels of encryption an application can use
- [x] D. Vault Agent will manage the lifecycle of cached tokens and leases automatically

> https://www.examtopics.com/discussions/hashicorp/view/131389-exam-vault-associate-002-topic-1-question-23-discussion/

#### Q21. Which of the following describes usage of an identity group?

- [ ] A. Limit the policies that would otherwise apply to an entity in the group
- [ ] B. When they want to revoke the credentials for a whole set of entities simultaneously
- [ ] C. Audit token usage
- [x] D. Consistently apply the same set of policies to a collection of entities

> https://www.examtopics.com/discussions/hashicorp/view/131382-exam-vault-associate-002-topic-1-question-24-discussion/

#### Q22. Vault supports which type of configuration for source limited token?

- [ ] A. Cloud-bound tokens
- [ ] B. Domain-bound tokens
- [x] C. CIDR-bound tokens
- [ ] D. Certificate-bound tokens

> https://www.examtopics.com/discussions/hashicorp/view/131390-exam-vault-associate-002-topic-1-question-25-discussion/

#### Q23. Where does the Vault Agent store its cache?

- [ ] A. In a file encrypted using the Vault transit secret engine
- [ ] B. In the Vault key/value store
- [ ] C. In an unencrypted file
- [x] D. In memory

> https://www.examtopics.com/discussions/hashicorp/view/131829-exam-vault-associate-002-topic-1-question-26-discussion/

#### Q24. Your organization has an initiative to reduce and ultimately remove the use of long lived X.509 certificates. Which secrets engine will best support this use case?

- [x] A. PKI
- [ ] B. Key/Value secrets engine version 2, with TTL defined
- [ ] C. Cloud KMS
- [ ] D. Transit

> https://www.examtopics.com/discussions/hashicorp/view/131387-exam-vault-associate-002-topic-1-question-27-discussion/

#### Q25. When unsealing Vault each Shamir unseal key should be entered:

- [ ] A. Sequentially from one system that all of the administrators are in front of
- [x] B. By different administrators each connecting from different computers
- [ ] C. While encrypted with each administrators PGP key
- [ ] D. At the command line in one single command

> https://www.examtopics.com/discussions/hashicorp/view/131384-exam-vault-associate-002-topic-1-question-28-discussion/

#### Q26. As a best practice, the root token should be stored in which of the following ways?

- [x] A. Should be revoked and never stored after initial setup
- [ ] B. Should be stored in configuration automation tooling
- [ ] C. Should be stored in another password safe
- [ ] D. Should be stored in Vault

> https://www.examtopics.com/discussions/hashicorp/view/131400-exam-vault-associate-002-topic-1-question-29-discussion/

#### Q27. When creating a policy, an error was thrown: Which statement describes the fix for this issue?

- [x] A. Replace write with create in the capabilities list
- [ ] B. You cannot have a wildcard (“*”) in the path
- [ ] C. sudo is not a capability

> https://www.examtopics.com/discussions/hashicorp/view/131402-exam-vault-associate-002-topic-1-question-30-discussion/

#### Q28. Where can you set the Vault seal configuration? (Choose two.)

- [ ] A. Cloud Provider KMS
- [ ] B. Vault CLI
- [x] C. Vault configuration file
- [x] D. Environment variables
- [ ] E. Vault API

> https://www.examtopics.com/discussions/hashicorp/view/131399-exam-vault-associate-002-topic-1-question-31-discussion/

#### Q29. Which of the following vault lease operations uses a lease_id as an argument? (Choose two.)

- [x] A. renew
- [ ] B. revoke -prefix
- [ ] C. create
- [ ] D. describe
- [x] E. revoke

> https://www.examtopics.com/discussions/hashicorp/view/131398-exam-vault-associate-002-topic-1-question-32-discussion/

#### Q30. An organization wants to authenticate an AWS EC2 virtual machine with Vault to access a dynamic database secret. The only authentication method which they can use in this case is AWS.

- [ ] A. True
- [x] B. False

> https://www.examtopics.com/discussions/hashicorp/view/131416-exam-vault-associate-002-topic-1-question-33-discussion/

#### Q31. You are using Vault’s Transit secrets engine to encrypt your data. You want to reduce the amount of content encrypted with a single key in case the key gets compromised. How would you do this?

- [ ] A. Use 4096-bit RSA key to encrypt the data
- [ ] B. Upgrade to Vault Enterprise and integrate with HSM
- [ ] C. Periodically re-key the Vault's unseal keys
- [x] D. Periodically rotate the encryption key

> https://www.examtopics.com/discussions/hashicorp/view/131418-exam-vault-associate-002-topic-1-question-34-discussion/

#### Q32. What does the following policy do?

- [x] A. Grants access for each user to a KV folder which shares their id
- [ ] B. Grants access to a special system entity folder
- [ ] C. Allows a user to read data about the secret endpoint identity
- [ ] D. Nothing, this is not a valid policy

> https://www.examtopics.com/discussions/hashicorp/view/131830-exam-vault-associate-002-topic-1-question-35-discussion/

#### Q33. To make an authenticated request via the Vault HTTP API, which header would you use?

- [x] A. The X-Vault-Token HTTP Header
- [ ] B. The X-Vault-Request HTTP Header
- [ ] C. The Content-Type HTTP Header
- [ ] D. The X-Vault-Namespace HTTP Header

> https://www.examtopics.com/discussions/hashicorp/view/131424-exam-vault-associate-002-topic-1-question-36-discussion/

#### Q34. Which of the following are replication methods available in Vault Enterprise? (Choose two.)

- [ ] A. Cluster sharding
- [ ] B. Namespaces
- [x] C. Performance Replication
- [x] D. Disaster Recovery Replication

> https://www.examtopics.com/discussions/hashicorp/view/131428-exam-vault-associate-002-topic-1-question-37-discussion/

#### Q35. Use this screenshot to answer the question below: When are you shown these options in the GUI?

- [ ] A. Enabling policies
- [ ] B. Enabling authentication engines
- [x] C. Enabling secret engines
- [ ] D. Enabling authentication methods

> https://www.examtopics.com/discussions/hashicorp/view/131430-exam-vault-associate-002-topic-1-question-38-discussion/

#### Q36. Examine the command below. Output has been trimmed. Which of the following statements describe the command and its output?

- [x] A. Missing a default token policy
- [ ] B. Generated token’s TTL is 60 hours
- [ ] C. Generated token is an orphan token which can be renewed indefinitely
- [ ] D. Configures the AppRole auth method with user specified role ID and secret ID

> https://www.examtopics.com/discussions/hashicorp/view/131831-exam-vault-associate-002-topic-1-question-39-discussion/

#### Q37. The key/value v2 secrets engine is enabled at secret/. See the following policy: Which of the following operations are permitted by this policy? (Choose two.)

- [x] A. vault kv get secret/webapp1
- [x] B. vault kv put secret/webapp1 apikey-"ABCDEFGHIDK123W"
- [ ] C. vault kv metadata get secret/webapp1
- [ ] D. vault kv delete secret/super-secret
- [ ] E. vault kv list secret/super-secret

> https://www.examtopics.com/discussions/hashicorp/view/131435-exam-vault-associate-002-topic-1-question-40-discussion/

#### Q38. You are performing a high number of authentications in a short amount of time. You're experiencing slow throughput for token generation. How would you solve this problem?

- [ ] A. Increase the time-to-live on service tokens
- [x] B. Implement batch tokens
- [ ] C. Establish a rate limit quota
- [ ] D. Reduce the number of policies attached to the tokens

> https://www.examtopics.com/discussions/hashicorp/view/131436-exam-vault-associate-002-topic-1-question-41-discussion/

#### Q39. When looking at Vault token details, which key helps you find the paths the token is able to access?

- [ ] A. Meta
- [ ] B. Path
- [x] C. Policies
- [ ] D. Accessor

> https://www.examtopics.com/discussions/hashicorp/view/131824-exam-vault-associate-002-topic-1-question-42-discussion/

#### Q40. A developer mistakenly committed code that contained AWS S3 credentials into a public repository. You have been tasked with revoking the AWS S3 credential that was in the code. This credential was created using Vault’s AWS secrets engine and the developer received the following output when requesting a credential from Vault. Which Vault command will revoke the lease and remove the credential from AWS?

- [x] A. vault lease revoke aws/creds/s3-access/f3e92392-7d9c-09c8-c921-575d62fe80d8
- [ ] B. vault lease revoke AKIAIOMQXTLW36DV7IEA
- [ ] C. vault lease revoke f3e92392-7d9c-09c8-c921-575d62fe80d8
- [ ] D. vault lease revoke access_key=AKIAIOWQXTLW36DV7IEA

> https://www.examtopics.com/discussions/hashicorp/view/131437-exam-vault-associate-002-topic-1-question-43-discussion/

#### Q41. When an auth method is disabled, all users authenticated via that method lose access.

- [x] A. True
- [ ] B. False

> https://www.examtopics.com/discussions/hashicorp/view/131438-exam-vault-associate-002-topic-1-question-44-discussion/

#### Q42. An authentication method should be selected for a use case based on:

- [x] A. The auth method that best establishes the identity of the client
- [ ] B. The cloud provider for which the client is located on
- [ ] C. The strongest available cryptographic hash for the use case
- [ ] D. Compatibility with the secret engine which is to be used

> https://www.examtopics.com/discussions/hashicorp/view/131444-exam-vault-associate-002-topic-1-question-45-discussion/

#### Q43. A web application uses Vault’s transit secrets engine to encrypt data in-transit. If an attacker intercepts the data in transit, which of the following statements are true? (Choose two.)

- [x] A. You can rotate the encryption key so that the attacker won't be able to decrypt the data
- [x] B. The keys can be rotated and min_decryption_version moved forward to ensure this data cannot be decrypted B. The Vault administrator would need to seal the Vault server immediately
- [ ] C. Even if the attacker was able to access the raw data, they would only have encrypted bits (TLS in transit)

> https://www.examtopics.com/discussions/hashicorp/view/132399-exam-vault-associate-002-topic-1-question-46-discussion/

#### Q44. The Vault encryption key is stored in Vault’s backend storage.

- [ ] A. True
- [x] B. False

> https://www.examtopics.com/discussions/hashicorp/view/129730-exam-vault-associate-002-topic-1-question-47-discussion/

#### Q45. Which of the following statements describe the secrets engine in Vault? (Choose three.)

- [ ] A. Some secrets engines simply store and read data
- [ ] B. Once enabled, you cannot disable the secrets engine
- [x] C. You can build your own custom secrets engine
- [x] D. Each secrets engine is isolated to its path
- [ ] E. A secrets engine cannot be enabled at multiple paths

> https://www.examtopics.com/discussions/hashicorp/view/131445-exam-vault-associate-002-topic-1-question-48-discussion/

#### Q46. What is a benefit of response wrapping?

- [ ] A. Log every use of a secret
- [ ] B. Load balance secret generation across a Vault cluster
- [ ] C. Provide error recovery to a secret so it is not corrupted in transit
- [x] D. Ensure that only a single party can ever unwrap the token and see what’s inside

> https://www.examtopics.com/discussions/hashicorp/view/131448-exam-vault-associate-002-topic-1-question-49-discussion/

#### Q47. Which of the following describes the Vault’s auth method component?

- [x] A. It verifies a client against an internal or external system, and generates a token with the appropriate policies attached
- [ ] B. It verifies a client against an internal or external system, and generates a token with root policy
- [ ] C. It is responsible for durable storage of client tokens
- [ ] D. It dynamically generates a unique set of secrets with appropriate permissions attached

> https://www.examtopics.com/discussions/hashicorp/view/131449-exam-vault-associate-002-topic-1-question-50-discussion/

#### Q49. Which of the following statements are true about Vault policies? (Choose two.)

- [ ] A. The default policy can not be modified
- [ ] B. You must use YAML to define policies
- [x] C. Policies provide a declarative way to grant or forbid access to certain paths and operations in Vault
- [ ] D. Vault must be restarted in order for a policy change to take an effect
- [x] E. Policies deny by default (empty policy grants no permission)

> https://www.examtopics.com/discussions/hashicorp/view/131451-exam-vault-associate-002-topic-1-question-52-discussion/

#### Q50. Use this screenshot to answer the question below: Where on this page would you click to view a secret located at secret/my-secret?

- [ ] A. Principio del formulario

> https://www.examtopics.com/discussions/hashicorp/view/131453-exam-vault-associate-002-topic-1-question-53-discussion/

#### Q51. An organization would like to use a scheduler to track & revoke access granted to a job (by Vault) at completion. What auth-associated Vault object should be tracked to enable this behavior?

- [ ] A. Token accessor
- [ ] B. Token ID
- [x] C. Lease ID
- [ ] D. Authentication method

> https://www.examtopics.com/discussions/hashicorp/view/131454-exam-vault-associate-002-topic-1-question-54-discussion/

#### Q52. Which statement describes the results of this command: $ vault secrets enable transit?

- [x] A. Enables the transit secrets engine at transit path
- [ ] B. Requires a root token to execute the command successfully
- [ ] C. Enables the transit secrets engine at secret path
- [ ] D. Fails due to missing -path parameter
- [ ] E. Fails because the transit secrets engine is enabled by default

> https://www.examtopics.com/discussions/hashicorp/view/131455-exam-vault-associate-002-topic-1-question-55-discussion/

#### Q53. Running the second command in the GUI CU will succeed.

- [ ] A. True
- [x] B. False
- [ ] C. Final del formulario

> https://www.examtopics.com/discussions/hashicorp/view/132733-exam-vault-associate-002-topic-1-question-56-discussion/

#### Q54. Which of these options does not allow the creation of a root token?

- [x] A. By using batch tokens
- [ ] B. By using another root token
- [ ] C. The initial root token generated at the vault operator init time
- [ ] D. By using vault operator generate-root with the permission of a quorum of unseal key holders

> https://www.examtopics.com/discussions/hashicorp/view/131456-exam-vault-associate-002-topic-1-question-57-discussion/

#### Q55. You manage two Vault dusters: “vaultduster1.acme.corp” and “vaultduster2.acme.corp”. You want to write a secret to the first Vaultcluster vaultcluster1.acme.corp and run vault kv put secret/foo value=‘bar’. The command times out and the error references the Vault cluster, “vaultcluster2.acme.corp”. You run the command again with the following address flag: vault kv put -address=‘https://vaultcluster1.acme.corp’ secret/foo value=‘bar’ The command completes successfully. You find that the terminal session defines the environment variable VAULT_ADDR=‘https://vaultcluster2.acxe.corp:8200’ Why was the second attempt successful?

- [ ] A. Environment variables take precedence over flags
- [ ] B. VAULT_CLUSTER_ADDR needs to be provided
- [x] C. Flags take precedence over environment variables
- [ ] D. Vault listener is misconfigured

> https://www.examtopics.com/discussions/hashicorp/view/131556-exam-vault-associate-002-topic-1-question-58-discussion/

#### Q56. The ‘alpha’ secrets are stored in the team-based paths using this convention: secret/<team_name>/alpha.

- [ ] A. For example, secret/team01/alpha and /secrets/team02/alpha. Which Vault policy would not allow reading paths with the word “beta” in them, such as secrets/team01/beta?

> https://www.examtopics.com/discussions/hashicorp/view/131825-exam-vault-associate-002-topic-1-question-59-discussion/

#### Q57. Which statement describes the results of this command: vault kv list secret/test?

- [ ] A. Check the status of a specific key/value secrets engine
- [x] B. List the existing key names at the “secret/test” path
- [ ] C. Output all key/value secrets engines
- [ ] D. Output all key names from all key/value secrets engine

> https://www.examtopics.com/discussions/hashicorp/view/131447-exam-vault-associate-002-topic-1-question-60-discussion/

#### Q58. To encrypt your secret with the transit secrets engine, you must send the Base32-encoded plaintext to Vault.

- [ ] A. True
- [x] B. False

> https://www.examtopics.com/discussions/hashicorp/view/131823-exam-vault-associate-002-topic-1-question-62-discussion/

#### Q59. Vault Agent supports which of the following? (Choose two.)

- [x] A. Secrets Cachin
- [ ] B. Local key/value store
- [ ] C. Local replica of transit encryption key
- [ ] D. Auto-unseal Vault
- [x] E. Auto authentication

> https://www.examtopics.com/discussions/hashicorp/view/131559-exam-vault-associate-002-topic-1-question-63-discussion/

#### Q60. Which is not true of Vault tokens?

- [ ] A. Vault tokens are the core method for authentication in Vault
- [ ] B. Vault tokens are generated by every authentication method login
- [ ] C. Vault tokens map to information including polices the token holder has, TTL and max usage, metadata, creation and last renewal time, and more
- [x] D. Vault tokens are required for every Vault call

> https://www.examtopics.com/discussions/hashicorp/view/131562-exam-vault-associate-002-topic-1-question-64-discussion/

#### Q61. When using Integrated Storage, which of the following should you do to recover from possible data loss?

- [ ] A. Use local storage
- [ ] B. Enable audit device
- [x] C. Use snapshot
- [ ] D. Use external storage

> https://www.examtopics.com/discussions/hashicorp/view/130406-exam-vault-associate-002-topic-1-question-65-discussion/

#### Q62. Which of the following is a reason to rekey a Vault cluster? (Choose two.)

- [x] A. A keyholder joins or leaves the organization
- [ ] B. Adding additional Vault nodes to a cluster
- [ ] C. The rook token is lost
- [x] D. A compliance mandate to rotate the master key at a regular interval
- [ ] E. Upgrading Vault Community Edition to Vault Enterprise

> https://www.examtopics.com/discussions/hashicorp/view/131561-exam-vault-associate-002-topic-1-question-66-discussion/

#### Q63. What information is required to revoke a Vault lease?

- [ ] A. Secret ID
- [ ] B. User ID
- [x] C. Lease ID
- [ ] D. Token ID

> https://www.examtopics.com/discussions/hashicorp/view/131563-exam-vault-associate-002-topic-1-question-67-discussion/

#### Q64. Use this screenshot to answer the question below: Which statement describes this AppRole auth method configuration?

- [x] A. Generates batch tokens with TTL set to 5 minutes
- [ ] B. Generates multiple tokens with TTL set to 5 minutes
- [ ] C. It is enabled at “App1” path
- [ ] D. It is enabled at “auth_approle_f23dd79f” path

> https://www.examtopics.com/discussions/hashicorp/view/131564-exam-vault-associate-002-topic-1-question-68-discussion/

#### Q65. What is a secret in the context of Vault?

- [ ] A. HTTP session token that provides authorization to Vault
- [ ] B. Threshold of keys required to unseal the Vault
- [x] C. Anything stored or returned that contains confidential material
- [ ] D. Engine responsible for logging all requests and responses

> https://www.examtopics.com/discussions/hashicorp/view/131565-exam-vault-associate-002-topic-1-question-69-discussion/

#### Q66. What methods of authentication does Vault support? (Choose four.)

- [x] A. JWT/OIDC
- [x] B. AppRole
- [x] C. GitHub
- [ ] D. MMSQL
- [ ] E. PostgreSQL
- [ ] F. Nomad
- [x] G. LDAP

> https://www.examtopics.com/discussions/hashicorp/view/131566-exam-vault-associate-002-topic-1-question-70-discussion/

#### Q67. Vault Agent allows client-side caching of tokens and leases. If the agent is shut down, those tokens and leases cached will be revoked.

- [ ] A. True
- [x] B. False

> https://www.examtopics.com/discussions/hashicorp/view/132817-exam-vault-associate-002-topic-1-question-71-discussion/

#### Q68. Which kind of token can be renewed indefinitely?

- [x] A. Periodic token
- [ ] B. Orphan token
- [ ] C. Use-limit token
- [ ] D. Root token
- [ ] E. All of the above

> https://www.examtopics.com/discussions/hashicorp/view/131567-exam-vault-associate-002-topic-1-question-72-discussion/

#### Q69. You can use a response-wrapping token more than once for as long as it has not expired.

- [ ] A. True
- [x] B. False

> https://www.examtopics.com/discussions/hashicorp/view/131568-exam-vault-associate-002-topic-1-question-73-discussion/

#### Q70. Which statement describes the results of this command: $ vault secrets enable -version=2 kv (Choose two.)

- [ ] A. Enables the secrets engine at path kv2/
- [ ] B. The -version is an invalid flag
- [x] C. Enables the secrets engine at path kv/
- [ ] D. Enables K/V v1 secrets engine
- [x] E. Enables K/V v2 secrets engine

> https://www.examtopics.com/discussions/hashicorp/view/131570-exam-vault-associate-002-topic-1-question-74-discussion/

#### Q71. Which of these are names of the replication methods available in Vault Enterprise? (Choose two.)

- [x] A. Disaster Recovery
- [ ] B. Cluster sharping
- [ ] C. Namespaces
- [ ] D. Seal-Wrap
- [x] E. Performance

> https://www.examtopics.com/discussions/hashicorp/view/131571-exam-vault-associate-002-topic-1-question-75-discussion/

#### Q72. What attributes are unique to batch tokens? (Choose three.)

- [x] A. Cannot be renewed
- [x] B. Are not persisted
- [ ] C. Can be periodic
- [x] D. Have a set time-to-live (TTL)
- [ ] E. Are persisted

> https://www.examtopics.com/discussions/hashicorp/view/131573-exam-vault-associate-002-topic-1-question-76-discussion/

#### Q73. You have manually created some usernames and passwords for a Microsoft SQL database on Azure, and need to store these credentials in Vault. What secrets engine should you use for this?

- [ ] A. MSSQL database secrets engine
- [x] B. Key/Value secrets engine version 2
- [ ] C. Azure secrets engine
- [ ] D. Transit engine

> https://www.examtopics.com/discussions/hashicorp/view/131579-exam-vault-associate-002-topic-1-question-77-discussion/

#### Q74. To create a non-root token with time-to-live (TTL) set to 30 minutes but with no max TTL which flag would you use?

- [ ] A. -ttl=30n
- [x] B. -explicit-max-ttl=0
- [ ] C. -orphan
- [ ] D. None of the above

> https://www.examtopics.com/discussions/hashicorp/view/131576-exam-vault-associate-002-topic-1-question-78-discussion/

#### Q75. A user successfully logs into Vault with the following cURL command: curl --request POST --data @payload.json http://127.0.0.1:8200/v1/auth/ldap/login/mitchellh The response will include what information?

- [x] A. client_token and policies
- [ ] B. access_key and policies
- [ ] C. access_key and secrets available
- [ ] D. client_token and secrets available

> https://www.examtopics.com/discussions/hashicorp/view/132822-exam-vault-associate-002-topic-1-question-79-discussion/

#### Q76. Which of the following statements are true about the default policy? (Choose two.)

- [x] A. It is one of the built-in policies
- [x] B. Provides a common set of permissions and is included on all tokens by default
- [ ] C. Can not be modified or deleted
- [ ] D. Gives a super admin permissions, similar to a root user on a Linux machine
- [ ] E. Vault upgrade will overwrite any update you made to the default policy

> https://www.examtopics.com/discussions/hashicorp/view/131574-exam-vault-associate-002-topic-1-question-80-discussion/

#### Q77. Why might an application be mapped to an identity entity?

- [ ] A. To prohibit Vault administrators from revoking tokens associated with that application
- [ ] B. To get around cloud license limitations
- [x] C. To allow an application deployed with multiple authentication methods have a consistent set of policies
- [ ] D. To allow the same application in one cloud to access already provisioned Vault tokens for that application in another cloud

> https://www.examtopics.com/discussions/hashicorp/view/131581-exam-vault-associate-002-topic-1-question-81-discussion/

#### Q78. Unsealing a single Vault server in a cluster unseals all Vault servers in that cluster.

- [ ] A. True
- [x] B. False

> https://www.examtopics.com/discussions/hashicorp/view/131582-exam-vault-associate-002-topic-1-question-82-discussion/

#### Q79. Which endpoint can be used to list all tokens?

- [ ] A. /kv/secrets
- [ ] B. /auth/token/list
- [ ] C. /secrets/kv
- [x] D. /auth/token/accessors

> https://www.examtopics.com/discussions/hashicorp/view/131822-exam-vault-associate-002-topic-1-question-83-discussion/

#### Q80. The mechanism to associate an authentication method with access to specific secrets is by specifying a/an:

- [ ] A. Accessor
- [ ] B. Token
- [x] C. Policy
- [ ] D. Secret

> https://www.examtopics.com/discussions/hashicorp/view/131583-exam-vault-associate-002-topic-1-question-84-discussion/

#### Q81. You are managing a Vault implementation that has been integrated with Azure SQL database to provide dynamic credentials. You have created a role that will provide database credentials for database administrators (DBAs) to use for managing their database in Azure SQL. A DBA has requested a new credential by issuing the following Vault CLI command:

- [ ] A. vault read azuresql/creds/dba_access.
- [ ] B. The following output is returned: The DBA has completed their work and would like to proactively remove the credential now that their work is complete. Which of the following commands should the DBA execute?
- [ ] C. vault delete azuresql/creds/dba_access
- [x] D. vault lease revoke v-token-dba_acccss-tr2t4x9pxvqlz8878s9s-1513446795
- [ ] E. vault delete azuresql/creds/dba_access/2e5b1e0b-a081-c7el-5622-39f58e79a7l9
- [ ] F. vault lease revoke azuresql/creds/dba_access/2e5b1e0b-a081-c7el-5622-39f58e79a719

> https://www.examtopics.com/discussions/hashicorp/view/131821-exam-vault-associate-002-topic-1-question-85-discussion/

#### Q82. One of the benefits of using the Vault transit secrets engine is its ability to easily rotate encryption keys. Which of these is true regarding key rotation?

- [ ] A. Vault automatically rotates the encryption key based on a set period
- [ ] B. Vault can rotate encryption keys, but cannot enforce restrictions about the minimum encryption key version
- [ ] C. Vault does not maintain the versioned keyring
- [x] D. Encryption keys can be rotated manually by a user, or by an automated process which invokes the key rotation API

> https://www.examtopics.com/discussions/hashicorp/view/131820-exam-vault-associate-002-topic-1-question-86-discussion/

#### Q83. What is not a function provided by Vault’s transit secret engine?

- [ ] A. Generating random bytes
- [ ] B. Encrypting data
- [x] C. Storing ciphertext data
- [ ] D. Verifying signed data
- [ ] E. None of the above

> https://www.examtopics.com/discussions/hashicorp/view/131819-exam-vault-associate-002-topic-1-question-87-discussion/

#### Q85. Which command will generate a new transit key?

- [ ] A. vault put transit/keys/my-key
- [ ] B. vault create -f transit/keys/my-key
- [x] C. vault write -f transit/keys/my-key
- [ ] D. vault create transit/keys/my-key

> https://www.examtopics.com/discussions/hashicorp/view/131638-exam-vault-associate-002-topic-1-question-90-discussion/

#### Q86. Which of the following is the correct option to authenticate to Vault using a token using the CLI?

- [ ] A. A token can be used to authenticate to Vault through the API, not the CLI or the UI
- [x] B. vault login
- [ ] C. vault <token>
- [ ] D. A token cannot be used to authenticate to Vault

> https://www.examtopics.com/discussions/hashicorp/view/131585-exam-vault-associate-002-topic-1-question-91-discussion/

#### Q87. A child token must be assigned the same or a subset the parent token’s policies.

- [x] A. True
- [ ] B. False

> https://www.examtopics.com/discussions/hashicorp/view/131817-exam-vault-associate-002-topic-1-question-92-discussion/

#### Q88. When enabling auto-unseal, how do you specify the seal type? (Choose two.)

- [x] A. Set the VAULT_SEAL_TYPE environment variable
- [ ] B. Use the /sys/seal endpoint on the Vault API
- [x] C. Create a seal block in the server configuration file
- [ ] D. Configure in the storage block of the server configuration file
- [ ] E. Use the vault operator command

> https://www.examtopics.com/discussions/hashicorp/view/131639-exam-vault-associate-002-topic-1-question-93-discussion/

