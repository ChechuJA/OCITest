# Oracle Exam 1Z0-922: MySQL Implementation Associate Dump

#### Q1. Which statement would you use to add a role in MySQL?
- [ ] SET ROLE
- [ ] MAKE ROLE
- [x] CREATE ROLE ✅
- [ ] GRANT ROLE

#### Q2. Which uniquely defines each user account identity in MySQL?
- [x] Username and host ✅
- [ ] Username
- [ ] Usemame, host, and password
- [ ] Username and password

#### Q3. What are the minimum and maximum number of MySQL Servers you can have in an InnoDB Cluster?
- [ ] Minimum 1 and maximum 5
- [x] Minimum 3 and maximum 9 ✅
- [ ] Minimum 3 and maximum 7
- [ ] Minimum 5 and maximum 9

#### Q4. Which three public clouds offer the HeatWave service?
- [ ] DigitalOcean
- [x] Amazon Web Services (AWS) ✅
- [ ] Google Cloud Platform (GCP)
- [ ] IBM Cloud
- [x] Oracle Cloud Infrastructure (OCI) ✅
- [x] Azure ✅

#### Q5. Why are indexes used in MySQL?
- [ ] To speed up DELETE operations
- [x] To speed up SELECT operations ✅
- [ ] To speed up CREATE operations
- [ ] To speed up INSERT operations
- [ ] To speed up ALTER operations

#### Q6. Why should one choose MySQL Enterprise Edition over MySQL Community/Standard Edition?
- [x] It provides tools and advanced features. ✅
- [ ] It provides NDB storage engine.
- [ ] It provides access to MySQL Connectors.
- [ ] It provides ACID properties.

#### Q7. MySQL has many variables. Which two are mandatory MySQL variables?
- [ ] filedir
- [x] basedir ✅
- [x] datadir ✅
- [ ] dbdir
- [ ] tabledir

#### Q8. Which statement is used to assign privileges to a MySQL user?
- [ ] SET
- [ ] UPDATE
- [ ] USE
- [x] GRANT ✅
- [ ] ALTER

#### Q9. How would you start the MySQL server without using the privilege system or by disabling the access control?
- [x] Use the --skip-grant-tables option.  ✅
- [ ] Use the --disable-grants command option.
- [ ] Use the --no-grants command option.
- [ ] Use the --block-privilege option.

#### Q10. What are the two ways to install MySQL on a Linux platform?
- [ ] By using MySQL Installer
- [ ] By using .DMG disk image
- [x] By using Yum/APT Repositories ✅
- [x] By using RPM packages ✅

#### Q11. Which two statements about the download of MySQL Enterprise Backup are correct?
- [ ] MySQL Enterprise Backup comes with all MySQL editions including the Community Edition.
- [ ] MySQL Enterprise Backup comes with MySQL Connector and is freely available for download.
- [x] MySQL Enterprise Backup is a separate package from MySQL Enterprise Edition. It can be downloaded from https://edelivery.oracle.com. ✅
- [ ] MySQL Enterprise Backup comes with MySQL Utilities Package, which is available for download publicly on https://www.mysql.com.
- [x] MySQL Enterprise Backup can be downloaded from My Oracle Support (MOS). ✅

#### Q12. Under which category do FLOAT and DOUBLE data types fall?
- [x] Numeric Approximate Value ✅
- [ ] Bit-value Type
- [ ] Spatial Type
- [ ] Numeric Exact Value

#### Q13. Which two options are true about the MySQL Long-Term Support release model?
- [ ] Available only with MySQL Enterprise Edition
- [x] Allows backward compatibility ✅
- [x] Includes bug fix and security patches only ✅
- [ ] Ideal for fast-paced development environments
- [ ] Released every quarter

#### Q14. You install MySQL from binary archive and use the --initialize-insecure option to initialize the data directory. Why is this process insecure?
- [ ] It removes all the MySQL Enterprise Security features.
- [ ] It disables all the logging done by the MySQL server.
- [x] It does not generate a root password. ✅
- [ ] It prevents the MySQL server from starting up properly.

#### Q15. A table has this specification:
```sql
CREATE TABLE address {
id INT NOT NULL,
last_name CHAR(30) NOT NULL,
first_name CHAR(30) NOT NULL,
city CHAR(30) NOT NULL,
INDEX LASTFIRST (last_name, first_name)
};
```
#### Which statement will NOT use an index?
- [ ] SELECT * FROM address WHERE last_name='Doe';
- [x] SELECT * FROM address WHERE city='Chicago'; ✅
- [ ] SELECT * FROM address WHERE last_name='Doe' AND (first_name='John' OR first_name='Other');
- [ ] SELECT * FROM address WHERE last_name='Doe' AND first_name='John';

#### Q16. What statement allows you to assign a password to a MySQL user account?
- [ ] GRANT PASSWORD
- [ ] ASSIGN PASSWORD
- [ ] NEW PASSWORD
- [x] SET PASSWORD ✅
- [ ] CREATE PASSWORD

#### Q17. Which two statements are true about MySQL Enterprise Authentication?
- [x] MySQL Enterprise Authentication supports Windows Active Directory. ✅
- [ ] MySQL Enterprise Authentication determines what operations the user can perform.
- [x] MySQL Enterprise Authentication supports Linux Pluggable Authentication Modules (PAM). ✅
- [ ] MySQL Enterprise Authentication makes it more difficult to set up security because you have different sets of security policies.
- [ ] MySQL Enterprise Authentication automatically connects to Oracle Password Vault to verify user passwords.

#### Q18. Assume that the database world exists and does not contain a table called poi. You execute this statement:
```sql
CREATE TABLE world.poi (x INT, y INT, z INT);
```
#### What is the output?
- [ ] The world.poi table is created in the default database.
- [x] The poi table is created in the world database. ✅
- [ ] The poi table is created in the default database.
- [ ] The statement fails because world.poi is not a valid table name.

#### Q19. In MySQL, the word "schema" is a synonym for which word?
- [ ] Server
- [ ] Instance
- [ ] Table
- [ ] View
- [x] Database ✅

#### Q20. What type of backups do mysqldump and MySQL Shell take?
- [ ] Operating System
- [ ] Snapshot
- [x] Logical ✅
- [ ] Physical

#### Q21. Your customer has a 75 GB MySQL database. They are using mysqldump to take a backup of their database, which is taking the five hours to complete.
#### What can your customer do to decrease the amount of time it takes to back up their database?
- [ ] Back up the database by using mysqldump to send the backup to another server
- [ ] Back up the database to a local drive
- [ ] Use MySQL Enterprise Monitor
- [x] Use MySQL Enterprise Backup ✅

#### Q22. Which log file is used to perform a Point in time Recovery?
- [ ] Undo log
- [x] Binary log ✅
- [ ] Audit log
- [ ] Redo log

#### Q23. Which data type would you use for a column to store large chunks of binary data such as images and audio files?
- [x] BLOB ✅
- [ ] VARCHAR
- [ ] BIT
- [ ] JSON

#### Q24. When creating a table, which data type would you use for a column that contains only whole numbers (a number that is not a fraction)?
- [x] INT ✅
- [ ] DECIMAL(5, 2)
- [ ] FLOAT
- [ ] BIGNUM

#### Q25. By using MySQL replication, data can be replicated from source to replica.
#### What are two advantages of MySQL replication?
- [ ] In-memory cache
- [ ] Automatic backup
- [x] Scale out ✅
- [x] Analytics ✅
- [ ] Data compression

#### Q26. The replica connects to the source and asks for updated records.
#### What command was issued for this to happen?
- [ ] REPLICA RUN
- [x] START REPLICA ✅
- [ ] START RUN REPLICA
- [ ] RUN REPLICA
- [ ] REPLICA START

#### Q27. Which replication is the default in MySQL?
- [ ] Semi-synchronous
- [x] Asynchronous ✅
- [ ] Quasi-synchronous
- [ ] Synchronous

#### Q28. Which statement is true about MySQL Replication?
- [ ] Data is copied from replica to source.
- [x] Multiple replicas are possible. ✅
- [ ] There can only be one source.
- [ ] Replication can only be asynchronous

#### Q29. What is the benefit of using MySQL Enterprise Thread Pool?
- [ ] Observability
- [ ] Monitoring
- [ ] Availability
- [x] Scalability ✅

#### Q30. Which MySQL Enterprise Edition component or plug-in replaces real values with substitutes?
- [ ] MySQL Enterprise Audit
- [x] MySQL Enterprise Masking ✅
- [ ] MySQL Enterprise Authentication
- [ ] MySQL Transparent Data Encryption

#### Q31. Which MySQL Enterprise Security tool allows DBAs to track user activities such as Who, What, When, How, Status, From Where, DB version, OS version, and options?
- [ ] MySQL Enterprise Transparent Data Encryption (TDE)
- [x] MySQL Enterprise Audit ✅
- [ ] MySQL Enterprise Firewall
- [ ] MySQL Enterprise Monitor

#### Q32. Which three languages are supported by MySQL Shell?
- [x] JavaScript ✅
- [x] Python ✅
- [ ] Perl
- [ ] Java
- [ ] PHP
- [x] SQL ✅

#### Q33. Which two MySQL features are available in the Community Edition but are fully supported in the Enterprise Edition?
- [ ] MySQL Cluster Manager
- [x] MySQL Router ✅
- [x] MySQL Document Store ✅
- [ ] Storage Engine NDB
- [ ] MySQL Enterprise Backup

#### Q34. Which two Autopilot features you are during initial DB System and Analytics cluster deployment?
- [x] Auto Shape Prediction ✅
- [x] Auto Data Placement ✅
- [ ] Auto Parallel Loading
- [ ] Auto Provisioning
- [ ] Auto Encoding

#### Q35. What is true about MySQL Enterprise Transparent Data Encryption (TDE)?
- [ ] It encrypts data-in-flight so that it is only visible unencrypted at the server and client.
- [ ] Data is encrypted in real time after it is written to storage.
- [ ] Encryption key is stored in a centralized key memory location.
- [x] It enables data-at-rest encryption with a strong symmetric algorithm. ✅

#### Q36. Which three operating systems are supported by MySQL?
- [x] macOS ✅
- [x] Windows ✅
- [ ] Android
- [ ] iOS
- [x] Linux ✅

#### Q37. Where would you look to find easy-to-understand views that contain information about IO hot spots, locking, and costly SQL statements?
- [x] sys schema ✅
- [ ] Performance schema
- [ ] mysql schema
- [ ] Information schema

#### Q38. Which monitoring tool is included with MySQL Enterprise Edition?
- [ ] Oracle Automatic Database Diagnostic Monitor (ADDM)
- [x] Oracle Enterprise Manager ✅
- [ ] Oracle GoldenGate
- [ ] Oracle Exadata

#### Q39. Which schema provides runtime statistics to monitor MySQL server execution at a low level?
- [ ] sys schema
- [ ] mysql schema
- [ ] Information schema
- [x] Performance schema ✅

#### Q40. Consider this SQL statement which is using the InnoDB storage enginer and with global AUTOCOMMIT=1:
```sql
BEGIN;
CREATE TABLE t1 (cl INT);
CREATE TABLE t2 (cl INT);
ROLLBACK;
```
#### What is the result after issuing the ROLLBACK command?
- [ ] Both the tables t1 and t2 are not created because there is an explicit ROLLBACK
- [x] Both the tables t1 and t2 are created ✅
- [ ] Only the t1 table is created
- [ ] Only the t2 table is created

#### Q41. Which MySQL storage engine is fully ACID compliant and also the default when creating a table?
- [ ] Memory
- [x] InnoDB ✅
- [ ] MyISAM
- [ ] Archive

#### Q42. What type of join returns all records from the left table and the matched records from the right table?
- [ ] Cross Join
- [x] Left Join ✅
- [ ] Right Join
- [ ] Inner Join

#### Q43. Which backup method allows you to back up only the data that has changed since the last FULL backup?
- [ ] Full
- [ ] Incremental
- [ ] Optimistic
- [x] Differential ✅
- [ ] Partial

#### Q44. Which replication topology does NOT implement any conflict detection or resolution?
- [ ] Replication conflicts are not possible in MySQL
- [ ] MySQL Chain
- [ ] Source-Replica
- [x] Source-Source ✅

#### Q45. Which keyword can be used in a SQL statement to view information about how tables will be joined and in which order?
- [ ] USE
- [x] EXPLAIN ✅
- [ ] DECLARE
- [ ] HELP

#### Q46. HeatWave is a fully-managed database service for MySQL in Oracle Cloud Infrastructure (OCI). 
#### Which three actions can be performed in the HeatWave cloud console without any SQL coding?
- [X] Deploy MySQL instances ✅
- [ ] Delete a schema
- [ ] Create database tables
- [x] Manage backups ✅
- [ ] Enable high availability
- [x] Reset user password ✅

#### Q47. Which query will find rows in a table that have no counterparts in another table?
- [ ] SELECT * FROM table1 INNER JOIN table2 ON table1.id=table2.id WHERE table1.id =! table2.id;
- [x] SELECT left_tbl.* FROM left_tb1 LEFT JOIN right_tbl ON left_tb1.id = right_tbl.id WHERE right_tbl.id IS NULL; ✅
- [ ] SELECT t1.name, t2.name2 FROM employee t1 INNER JOIN info t2 WHERE t1.name = t2.name;
- [ ] SELECT t1.name, t2.name2 FROM employee AS t1 INNER JOIN info AS t2 ON t1.name = t2.name2;

#### Q48. Which three components are part of the core MySQL database architecture?
- [x] Optimizer ✅
- [ ] Disk Parity/RAID
- [x] Parser ✅
- [ ] mysqldump
- [x] Storage Engine ✅
- [ ] MySQL Router

#### Q49. You just installed MySQL using a package manager on Linux.
#### Where is the default data directory (that is, datadir) located that holds InnoDB log files such as undo and redo logs?
- [ ] /usr/lib/mysql
- [ ] /us/local/mysql
- [x] /var/lib/mysql ✅
- [ ] /opt/mysql

#### Q50. How would you replicate between two InnoDB Clusters?
- [ ] Set up MySQL Replication.
- [ ] Set up MySQL InnoDB Read Replicas.
- [x] Set up MySQL InnoDB ClusterSet. ✅
- [ ] Set up MySQL ReplicaSet.

#### Q51. Which three components can MySQL InnoDB Cluster use to achieve database high availability?
- [ ] MySQL online hot backup, to keep data consistent and always ready to be used
- [x] MySQL Servers with Group Replication, to replicate data to all members of the cluster ✅
- [x] MySQL Shell, to create and administer InnoDB Cluster using the built-in AdminAPI ✅
- [x] MySQL Router, to ensure client requests are load balanced and routed to the correct server ✅
- [ ] MySQL X Plugin, to enable MySQL to use the X Protocol to speed up and monitor data replication

#### Q52. How does MySQL Enterprise Firewall block SQL Injection attacks?
- [x] By matching the SQL statements against the allowlist ✅
- [ ] By protecting the database files and encrypting them using AES-256
- [ ] By hiding or obfuscating sensitive data
- [ ] By Automatically and intelligently knowing beforehand when a SQL Injection is about to happen
