# Transcripción: PL-200 Q&A.pdf

- PDF original: [PL-200 Q&A.pdf](PL-200%20Q%26A.pdf)
- Cada encabezado de página enlaza a la página correspondiente del PDF.


- Archivo fuente: `PL-200 Q&A.pdf`
- Páginas del archivo: 297
- Páginas incluidas: `1-297`
- Extracción: 2026-10-02T11:18+02:00
- Aviso: resultado automático; cotejar cifras e identificadores con el original.

## [Página 1](PL-200%20Q%26A.pdf#page=1) · texto nativo

Instructions
 Before taking the test, hide Questions and
 Answers by clicking on a heading→
 Expand Collapse and Select “Collapse All
 Headings.”

 Navigate through the Questions to read
 them and Expand the Answer to check if
 you are successful.


 MACRO ICONS:
                                                                           : Insert a new blank question to fulfill.

                                                                            : insert a “REVIEW” statement.





001 Question.
The owner of a company needs to know who signs into the system.
You need to ensure that the owner can view the user audit logs.
Where does each action need to be performed? To answer, select the appropriate options in the
answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 2](PL-200%20Q%26A.pdf#page=2) · texto nativo

Hot Area:





                                                                                                                                      .
Answer
   Correct Answer:

---

## [Página 3](PL-200%20Q%26A.pdf#page=3) · texto nativo

Explanation:

Activate user auditing → System Settings

       •   Auditing is enabled at the organization level from Settings → Administration → System
          Settings → Auditing.
       •   This is where you turn on auditing for users and entities.

View the user audit logs → User Summary report

       •  To review who signed in and other user-related audit events, administrators use the
         User Summary Report, which displays audit information for users.

Discussion: https://www.examtopics.com/discussions/microsoft/view/42604-exam-pl-200-topic-
1-question-1-discussion/

002 Question.
Your organization does not permit the use of custom code for solutions.
You need to create a view that can be viewed by all users in an organization.
Where should you create the view?

    A.  List view of the entity
    B.  Microsoft Visual Studio
   C. Templates area

---

## [Página 4](PL-200%20Q%26A.pdf#page=4) · texto nativo

D. Maker portal

Answer
   Correct Answer: D

   Explanation:

The requirement is:

       •  No custom code allowed → eliminates Microsoft Visual Studio.
       •  Create a view available to all users → requires a public/system view.
       •   In modern Dataverse and Power Apps environments, system views are created and
         managed through the Power Apps Maker portal.

Discussion: https://www.examtopics.com/discussions/microsoft/view/61448-exam-pl-200-topic-
1-question-2-discussion/

003 Question.
You create a Power Apps portal to provide training and documentation for students. Students
create a profile on the portal and then select and pay for courses.
You plan to add free courses to the training portfolio. Free courses must be automatically available
to all students after they sign in.
You need to assign default permissions to students.
What should you do?

    A.  Create a Students web role and set the Authenticated Users Role option to true. Assign the
     web role to each registered user.
    B.  Create an entity for managing free courses. Create entity permission records to provide
      access to entity records for free courses and assign the entity permissions to users when
       they register on the portal for the first time.
   C. Create an entity for managing free courses. Create a Students web role and set the
       Authenticated Users role option to true. Create appropriate entity permissions to access
       the free course entity records and assign the entity permissions to the web role.
Answer
   Correct Answer: B

   Explanation:

   You The requirement is that:

       •   All students who sign in should automatically have access to free courses.
       •  Permissions must be assigned automatically.
       •  The portal uses Power Apps Portals (Power Pages).

---

## [Página 5](PL-200%20Q%26A.pdf#page=5) · texto nativo

Setting the Authenticated Users Role option to True on the Students web role automatically
    assigns that role to every authenticated portal user. Then, by associating Entity Permissions
    for the Free Courses entity with that web role, all authenticated students can access the free
   course records without manual assignment

Discussion: https://www.examtopics.com/discussions/microsoft/view/41457-exam-pl-200-topic-
1-question-3-discussion/

004 Question.
You create workflows to automate business processes.
You need to configure a workflow to meet the following requirements:

    •  Be triggered when a condition is met.
    •  Run immediately.
    •  Perform an action when a condition is met.

You need to create a workflow that automatically sends emails based on a mail merge template. To
answer, select the appropriate configuration in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 6](PL-200%20Q%26A.pdf#page=6) · texto nativo

Explanation:

    Here's the breakdown of the correct configurations:

   Workflow Requirement: Be triggered when a condition is met.

       •   Configuration Option: Subject contains data. : This implies a trigger based on the
          content of a subject line, indicating a condition being met.
       •  Workflow Requirement: Run immediately.
       •   Configuration Option: Configure the workflow to run now. This is the direct and obvious
         way to make a workflow execute instantly.
       •  Workflow Requirement: Perform an action when a condition is met.
       •   Configuration Option: Send an email. This is the specific action mentioned in the
          scenario

Discussion: https://www.examtopics.com/discussions/microsoft/view/41260-exam-pl-200-topic-
1-question-4-discussion/

005 Question.
You are a Dynamics 365 Customer Service administrator.
You need to configure the following automation for the sales team:

    •  Send an email when the status changes on an Opportunity.
    •   Text the sales manager when an Opportunity is created.

Create a Wunderlist task when an Opportunity is open for 30 days.

---

## [Página 7](PL-200%20Q%26A.pdf#page=7) · texto nativo

Which tool should you use for each requirement? To answer, select the appropriate options in the
answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 8](PL-200%20Q%26A.pdf#page=8) · texto nativo

Explanation:

    Here's the correct tool selection for each automation requirement:

   Email when the status changes on an Opportunity: Tool: Dynamics 365 workflow:
   Dynamics 365 workflows are ideal for automating actions within the Dynamics 365
   environment based on specific triggers like status changes.

   Text the sales manager when an Opportunity is created: Tool: Microsoft Flow (now Power
   Automate):

   Power Automate is best suited for connecting to external services like SMS gateways or other
   communication platforms to send text messages.

   Create a Wunderlist task when an Opportunity is open for 30 days: Tool: Microsoft Flow
   (now Power Automate):

   Power Automate excels at integrating with various applications, including task management
    tools like Wunderlist (now Microsoft To Do, but the principle remains the same). It can also
   handle time-based triggers.

Discussion: https://www.examtopics.com/discussions/microsoft/view/41762-exam-pl-200-topic-
1-question-5-discussion/

---

## [Página 9](PL-200%20Q%26A.pdf#page=9) · texto nativo

006 Question.
A company uses Microsoft Dataverse to manage prospects. The company has a business process
flow named BPFA that is associated with the Prospect entity to streamline the prospect
management process.
You add a field named Category to the Prospect entity. You create additional business process
flows. You apply the business process flows to Prospect records based on the selected category.
Users can switch to any other newly configured business process flows but must not use BPFA.
You need to configure the solution.
What are two possible ways to achieve this goal? Each correct answer presents a complete
solution.
NOTE: Each correct selection is worth one point.

    A. Remove all of the privileges for BPFA.
    B. Use a business rule to prevent users from switching to BPFA.
   C. Deactivate BPFA.
   D. Change the display order of the business process flows to move BPFA to the bottom of the
          list.
Answer
   Correct Answer:

   Explanation:

The requirement is that users:

       •  Can use the new Business Process Flows.
       •  Must not be able to use BPFA.


           A. Remove all of the privileges for BPFA

Business process flows are secured through security roles. Removing users' privileges for BPFA
prevents them from using or switching to that process.

          C. Deactivate BPFA

A deactivated business process flow is unavailable for use and cannot be selected by users.

Not B: Business rules cannot control which Business Process Flow a user selects. They operate on
form fields and data logic, not BPF selection.

Not D: This only affects the order in which processes are displayed. Users could still select BPFA.

Discussion: https://www.examtopics.com/discussions/microsoft/view/41763-exam-pl-200-topic-
1-question-6-discussion/

---

## [Página 10](PL-200%20Q%26A.pdf#page=10) · texto nativo

007 Question.
You are creating a business rule to implement new business logic.
You must apply the business logic to a canvas app that has a single screen named Screen1.
You need to configure the scope for the business rule.
Which scope should you use?

    A. Screen1
    B.  Entity
   C.  All Forms
   D. Global
Answer
   Correct Answer: B

   Explanation:

   Business Rules in Dataverse can have different scopes:

       •   Entity (Correct) – Applies the business rule at the table/entity level and works across
          model-driven apps and other clients that support business rules.
       •   All Forms – Applies only to all forms of a model-driven app.
       •   Specific Form (e.g., Main Form) – Applies only to a particular form.
       •  Global – Not a valid business rule scope in Dataverse.
       •  Screen1 – Canvas apps do not use business rule scopes tied to screens.

   Because the requirement is to apply business logic to a canvas app, the business rule must be
    configured at the Entity scope so that it is enforced at the Dataverse table level and can be
   used by the app.

Discussion: https://www.examtopics.com/discussions/microsoft/view/42523-exam-pl-200-topic-
1-question-7-discussion/

008 Question.
You are a Dynamics 365 Customer Services administrator. You have a Production instance and
Sandbox instance.
Users record Production instance data in the Sandbox instance.
You need to ensure that the users only record data in the Production instance.
Which security function needs to be edited to prevent access to the Sandbox? To answer, select
the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 11](PL-200%20Q%26A.pdf#page=11) · texto nativo

Hot Area:





Answer
   Correct Answer:

---

## [Página 12](PL-200%20Q%26A.pdf#page=12) · texto nativo

Explanation:

    •  Microsoft 365 admin center → Licenses

        o  To prevent users from accessing Dynamics 365 environments, you can control
             access through the assignment of Dynamics 365 licenses in the Microsoft 365
            admin center. Users require an appropriate license to access the application.
    •  Dynamics 365 Sandbox instance → Groups
        o  A common practice is to associate a Sandbox environment with an Azure
              AD/Microsoft Entra security group. Only members of the security group can access
              the sandbox. Removing users from the group prevents them from accessing the
            Sandbox while allowing continued access to Production

Discussion: https://www.examtopics.com/discussions/microsoft/view/41589-exam-pl-200-topic-
1-question-8-discussion/

009 Question.
You must create a new entity to support a new feature for an app. Records for the entity must be
associated with a business unit and specify security roles for the business unit.
You need to configure entity ownership.
Which entity ownership type should you use?

---

## [Página 13](PL-200%20Q%26A.pdf#page=13) · texto nativo

A.  user or team owned
    B.  organization-owned
   C. none
   D. business-owned
Answer
   Correct Answer: A

   Explanation:
   The requirement states that:

       •  Records must be associated with a business unit.
       •  Access must be controlled through security roles.
       •   Security should be applied at the user, team, business unit, parent-child business unit,
           or organization level.

   Only User or Team Owned tables support the full Dataverse security model based on
   ownership and security roles.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60726-exam-pl-200-topic-
1-question-9-discussion/

010 Question.
You need to ensure that there are no leads for a customer before you create a new opportunity for
the customer.
How can you use duplicate detection rules to achieve this goal? To answer, select the appropriate
options in the answer area.

NOTE:
Each correct selection is worth one point.

---

## [Página 14](PL-200%20Q%26A.pdf#page=14) · texto nativo

Hot Area:





Answer
   Correct Answer:

---

## [Página 15](PL-200%20Q%26A.pdf#page=15) · texto nativo

Explanation:

   Duplicate detection on Lead will not trigger on Opportunity creation/update

   The rule must be created as follow: - Base Record Type: Opportunity

       •  Matching Record Type: Lead
       •  Base Record field: Account
       •  Matching Record field: Parent Account for Lead (or another if you use a different one)
       •   Criteria: Exact Match

   So answer is Opportunity - Account

   Discussion: https://www.examtopics.com/discussions/microsoft/view/384386-exam-ab-100-
    topic-1-question-12-discussion/

011 Question.
You have two Microsoft Power Platform environments.
Users in one environment must not be able to see the other environment.
You need to grant salespeople access to the sales company environment.
What should you do?

    A. Add salespeople to an Office 365 security group.
    B. Add salespeople to a security role.

---

## [Página 16](PL-200%20Q%26A.pdf#page=16) · texto nativo

C. Set privileges.
   D. Set app security.
Answer
   Correct Answer: A

   Explanation:

   To prevent users in one Power Platform environment from seeing or accessing another
   environment, you should associate the environment with a Microsoft Entra ID (Azure AD) /
   Microsoft 365 security group.

   By doing this:

       •  Only members of the security group can access the environment.
       •  Users who are not members cannot see or access the environment.
       •  Access is managed centrally through group membership

Discussion: https://www.examtopics.com/discussions/microsoft/view/60489-exam-pl-200-topic-
1-question-11-discussion/

012 Question.
A veterinary office plans to use Power Platform to streamline customer experiences. The customer
creates a canvas apps to manage appointments.

On the client appointment form, there is a dropdown field for clients to select their type of pet. If a
client selects the option Other, the veterinarian wants a text field to appear so that additional
details can be added.

You need to create a dynamically visible field.

What should you configure?

    A.  workflow
    B.  business process flow
   C. business rule

Answer
   Correct Answer: C

   Explanation:

   The requirement is to:

       •  Show or hide a field dynamically.
       •  Respond to a user's selection in a dropdown (Choice) field.
       •  No background process or multi-stage process is required.

---

## [Página 17](PL-200%20Q%26A.pdf#page=17) · texto nativo

A Business Rule can:

       •  Show or hide fields.
       •  Set field values.
       •  Set business-required fields.
       •  Apply logic based on conditions (e.g., If Pet Type = Other, show Additional Details field)

Discussion: https://www.examtopics.com/discussions/microsoft/view/60490-exam-pl-200-topic-
1-question-12-discussion/

013 Question.
You create an app for the sales team at a company.
Members of the sales team cannot access the app.
You need to ensure that sales team members can access the app.
Where should you configure app permissions?

    A. Dynamics administration center
    B. Manage Roles
   C. Security Roles
Answer
   Correct Answer: B

   Explanation:

   For a model-driven app in Dynamics 365 / Power Apps, app access is controlled by App Roles.

   To allow the sales team to access the app:

    1. Open the app in the Power Apps maker portal.
    2.  Select Manage Roles.
    3.  Assign the appropriate security roles to the app.
    4.  Ensure the users have one of those security roles

Discussion: https://www.examtopics.com/discussions/microsoft/view/60491-exam-pl-200-topic-
1-question-13-discussion/

014 Question.
You create a parent entity and a child entity. The parent entity has a 1:N relationship with the child
entity.
You need to ensure that when the owner changes on the parent record that all child records are
assigned to the new owner.
You need to configure the relationship behavior type.
What should you use?

---

## [Página 18](PL-200%20Q%26A.pdf#page=18) · texto nativo

A.  Referential
    B.  Referential, Restrict Delete
   C. Parental
   D.  Restrict
Answer
   Correct Answer: C

   Explanation:

   The requirement is:

       •  When the owner of the parent record changes, all related child records must
           automatically be assigned to the new owner.

    In Dataverse/Dynamics 365, the Parental relationship behavior supports cascading actions
   such as:

       •  Assign
       •  Share
       •  Unshare
       •  Delete
       •  Reparent
       •  Merge

   With a Parental relationship, an Assign operation on the parent record cascades to the child
    records, causing them to be reassigned automatically.

Discussion: https://www.examtopics.com/discussions/microsoft/view/54352-exam-pl-200-topic-
1-question-14-discussion/

015 Question.
You need to recommend a role for users to perform several required tasks. The solution must use
the principle of least privilege.
Which roles should you recommend? To answer, drag the appropriate roles to the correct
functions. Each role may be used once, more than once, or not at all.
You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:

---

## [Página 19](PL-200%20Q%26A.pdf#page=19) · texto nativo

Answer
   Correct Answer:





   Explanation:

    •   Office 365 Global Administrator

         o  Can create and manage users in Microsoft 365/Azure AD.

         o  Required for creating new user accounts.

    •  Dynamics 365 System Administrator

         o  Can manage security roles and assign roles within the Dynamics 365 environment.

         o  Has the necessary permissions for user role assignment.

    •  Dynamics 365 Service Administrator

         o  Manages Dynamics 365 instances, including backup and restore operations.

         o  Provides the least privilege necessary for instance administration

---

## [Página 20](PL-200%20Q%26A.pdf#page=20) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/54100-exam-pl-200-topic-
1-question-15-discussion/

016 Question.
You are designing an app for a bank.
You must create entities for the app and configure relationships between entities:





Which relationship types should you use? To answer, drag the appropriate relationship types to the
correct requirements. Each relationship type may be used once, more than once, or not at all. You
may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





.


Answer
   Correct Answer:

---

## [Página 21](PL-200%20Q%26A.pdf#page=21) · texto nativo

Explanation:

            1. N : 1 - A many-to-one (N:1) relationship from LoanApplicant to Contact (or similar
                 entity) allows multiple applicants to reference the same email/contact.
            2.  1 : N - A one-to-many (1:N) relationship from LoanApplicant to Loan means one
              applicant can have multiple loan applications.
            3. N : 1 - A many-to-one (N:1) relationship from Loan to Property ensures that multiple
              loans can reference a single property.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60234-exam-pl-200-topic-
1-question-16-discussion/

017 Question.
You need to create a system chart for the Account entity.
The chart must display a count of accounts grouped by owner and then display the accounts by
Address 1: State/Province for each owner. You begin to configure chart options as shown in the
image below.

---

## [Página 22](PL-200%20Q%26A.pdf#page=22) · texto nativo

How should you complete the configuration? To answer, select the appropriate options in the
answer area.
NOTE: Each correct selection is worth one point.

The chart must display a count of accounts grouped by owner, and then display the accounts by
Address 1 to State/Province for each owner.
Hot Area:

---

## [Página 23](PL-200%20Q%26A.pdf#page=23) · texto nativo

Answer
   Correct Answer:

---

## [Página 24](PL-200%20Q%26A.pdf#page=24) · texto nativo

Explanation:

    •  The requirement is:
        o  Display a count of accounts grouped by Owner, and then display the accounts
             by Address 1: State/Province for each owner.
    •   Therefore:
        o  The measure being counted is the number of Account records → Account +
             Count: All.
        o  The primary grouping is Owner.
        o  The secondary grouping within each owner is Address 1: State/Province.
    •   Final Answer
        o  Legend Entries (Series): Select Field → Account
        o  Legend Entries (Series): Aggregate → Count: All

---

## [Página 25](PL-200%20Q%26A.pdf#page=25) · texto nativo

o   First grouping field → Owner
           o  Second grouping field → Address 1: State/Province

   Discussion: https://www.examtopics.com/discussions/microsoft/view/60584-exam-pl-200-
    topic-1-question-20-discussion/

018 Question.
A user has access to an existing Common Data Service database.
You need to ensure that the user can create canvas apps that consume data from Dataverse. You
must not grant permissions that are not required.
Which out-of-the-box security role should you assign to the user?

    A.  Environment Admin
    B.  System Customizer
    C. Common Data Service User
    D.  Environment Maker
Answer
   Correct Answer: D

   Explanation:

   The requirement is:

       •  The user must be able to create canvas apps.
       •  The apps must consume data from Dataverse.
       •  Apply the principle of least privilege.

   The Environment Maker role allows users to:

       •  Create canvas apps.
       •  Create flows.
       •  Create and use connections.
       •  Use Dataverse data (assuming they also have the necessary table permissions

Discussion: https://www.examtopics.com/discussions/microsoft/view/81536-exam-pl-200-topic-
1-question-21-discussion/

019 Question.
A company deploys several model-driven apps. The company uses shared devices in their
warehouse. The devices are always powered on. Users log on to the devices and then launch the
apps to perform actions.
Unauthorized users recently uploaded several files after another user failed to log out of a device.
The company needs to prevent these incidents from occurring in the future.
You need to configure the solution to prevent the reported security incidents.

---

## [Página 26](PL-200%20Q%26A.pdf#page=26) · texto nativo

What should you do? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





.
Answer
   Correct Answer:





   Explanation:

    •  Prevent unauthorized access to devices → Set a timeout in the Power Platform admin
       center
        o  The issue occurs because users leave sessions open on shared devices.
              Configuring a session timeout in the Power Platform admin center automatically
               signs out inactive users, reducing the risk of unauthorized access.

    •  Prevent users from uploading a specific type of file → Enter the restricted file types in
       the Power Platform admin center

        o  Power Platform allows administrators to configure blocked file extensions for file
             attachments. This is configured in the Power Platform admin center.

---

## [Página 27](PL-200%20Q%26A.pdf#page=27) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/61196-exam-pl-200-
    topic-1-question-22-discussion/

020 Question.
A company's sales staff wants a simplified way to manage their opportunities in Dynamics 365
Sales without adding custom code.
You need to provide a solution for each requirement.
Which solutions should you provide? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 28](PL-200%20Q%26A.pdf#page=28) · texto nativo

Explanation:

        1. Drag and drop opportunities to change the stage → Add a Kanban control
            •  The Kanban control provides drag-and-drop functionality, allowing salespeople to
           move opportunities between stages visually.
        2. Show opportunities in Calendar and Kanban view → Add both controls to the My
          Opportunities view
            •  To provide both visualizations for a salesperson's own opportunities, configure the
          My Opportunities view with both controls.
        3. Show the number of open opportunities by stage → Use the chart pane on the
          view.
            •  A standard Dynamics 365 view can display aggregated information through the
             Chart Pane, showing counts grouped by stage.

Discussion: https://www.examtopics.com/discussions/microsoft/view/63137-exam-pl-200-topic-
1-question-23-discussion/

021 Question.
You plan to implement Microsoft Dataverse.
You must track changes for two columns in the Account table. You must maintain a historical log of
changes for the two columns and track only what is necessary.
You configure the appropriate organization settings.
You need to configure the system to track changes for the two columns.

---

## [Página 29](PL-200%20Q%26A.pdf#page=29) · texto nativo

Which two actions should you perform? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

    A.  Enable auditing for the Account table.
    B.  Enable auditing for the two specific columns.
    C. Enable change tracking for the Account table.
    D.  Enable change tracking for the two specific columns.
Answer
   Correct Answer: A,B

   Explanation:

   The requirement is to:

    •   Maintain a historical log of changes.

    •   Track changes for only two specific columns.

    •   Organization-level auditing has already been enabled.

    In Dataverse, to track historical changes to specific fields, you must use Auditing, not Change
    Tracking.

    •   A. Enable auditing for the Account table

    Auditing must first be enabled at the table level before any column auditing can occur.

    •   B. Enable auditing for the two specific columns

   To minimize tracking and record only the required changes, enable auditing only on the two
   columns that need to be monitored.

    •  Not C. Enable change tracking for the Account table

   Change Tracking is used for data synchronization and integration scenarios, not for maintaining
   an audit history of field changes.

    •  Not D. Enable change tracking for the two specific columns

   Change Tracking is enabled at the table level, not for individual columns, and does not provide
   an audit log.

Discussion: https://www.examtopics.com/discussions/microsoft/view/63338-exam-pl-200-topic-
1-question-25-discussion/

022 Question.
You are implementing a model-driven app to support a new line of business.
There are several places where automated business logic must be applied.

---

## [Página 30](PL-200%20Q%26A.pdf#page=30) · texto nativo

You need to determine how to apply the business logic.
Which method should you use?

To answer, drag the appropriate methods to the appropriate business logic statements. Each
method may be used once, more than once, or not at all. You may need to drag the split bar
between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





Answer
   Correct Answer:





   Explanation:

    •  Make a field read only until a predetermined value is exceeded → Business rule

   A Business Rule can:

         o  Lock/unlock fields

         o  Show/hide fields

         o  Set field requirements

---

## [Página 31](PL-200%20Q%26A.pdf#page=31) · texto nativo

o  Apply client-side logic without code

    •  Automatically send an email when a record's status is changed to deactivated → Real-
      time workflow

   A Real-time Workflow can:

         o   Trigger immediately on record changes

         o  Send emails automatically

         o  Execute synchronously

    •  Use the previous value of a field when the value is automatically updated as part of the
       process → Real-time workflow
         o  Accessing and acting on the value during the update process requires server-side
              execution before/during save, which is handled by a Real-time Workflow.

Discussion: https://www.examtopics.com/discussions/microsoft/view/79698-exam-pl-200-topic-
1-question-29-discussion/

023 Question.
Your organization does not permit the use of custom code for solutions.
You need to create a view that can be viewed by all users in an organization.
Where should you create the view?

    A.  Advanced Find
    B.  Entities component of a solution
    C.  Microsoft Excel template
    D. Templates area
Answer
   Correct Answer: B

   Explanation:

   The The requirement is to create a view that can be viewed by all users in the organization
   and without custom code.

   A view available to all users is a system (public) view. System views are created and managed
   as part of a table/entity within a solution.

                •   Entities component of a solution (Correct)
                o  Allows creation and modification of system views.
                o  Views are available to all users with access to the table.
                •  Advanced Find (Incorrect)

---

## [Página 32](PL-200%20Q%26A.pdf#page=32) · texto nativo

o  Creates personal views, which are only visible to the user unless
                              explicitly shared.
                •   Microsoft Excel template (Incorrect)
                o  Used for exporting and reporting, not for creating Dataverse/Dynamics
                         views.
                •  Templates area (Incorrect)
                o  Used for document, email, and similar templates, not views.

Discussion: https://www.examtopics.com/discussions/microsoft/view/79699-exam-pl-200-topic-
1-question-30-discussion/

024 Question.
You develop a Power Apps app.
Users report that the main form does not display data from other entities or allow them to edit data
from other entities.
You need to embed information from other entities in the form and allow users to edit the data.
Which actions should you perform? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 33](PL-200%20Q%26A.pdf#page=33) · texto nativo

Explanation:

    •   Edit data → Add a sub-grid
o  A sub-grid displays related records from another table on a form. Users can open and edit
   those related records directly from the sub-grid, provided they have the necessary
   permissions.
    •  View data → Add a quick view
o  A Quick View form displays information from a related table on the current form. The data
    is read-only and cannot be edited directly.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60498-exam-pl-200-topic-
1-question-31-discussion/

025 Question.
A company uses a canvas app to manage production resources in a specific region. Employees
must be at company locations to use the app.
Due to a sudden requirement for employees to work remotely, employees no longer commute to a
specific location to conduct their work and cannot access the canvas app.
You must reconfigure the app to ensure that employees only access the app from a limited number
of locations.
You need to restrict access to the app.
Which components should you configure? To answer, select the appropriate options in the answer
area.
NOTE: Each correct selection is worth one point.
Hot Area:

---

## [Página 34](PL-200%20Q%26A.pdf#page=34) · texto nativo

Answer
   Correct Answer:





   Explanation:

   Azure Active Directory (Microsoft Entra ID) provides Conditional Access capabilities that
   can restrict access based on:

    •  Named locations
    •   IP address ranges
    •   Countries/regions

---

## [Página 35](PL-200%20Q%26A.pdf#page=35) · texto nativo

•  Device state
    •   Risk conditions

   To allow access only from approved locations while employees work remotely:

    1.  Configure the policy in Azure Active Directory (Microsoft Entra ID).
    2.  Create a Conditional Access policy.
    3.  Define the allowed locations (named locations, IP ranges, countries/regions).
    4.  Apply the policy to Power Apps / Power Platform users.

Discussion: https://www.examtopics.com/discussions/microsoft/view/81623-exam-pl-200-topic-
1-question-32-discussion/

026 Question.
You attempt to deactivate several currencies in a Microsoft Dataverse environment.
You are not able to deactivate one of the currencies.
You need to determine why you cannot deactivate the currency.
What is the reason?

    A. You are not the currency record owner.
    B. The currency is used by an active business process.
   C. The currency is the base currency.
   D. The currency is used by another record.
Answer
   Correct Answer: C

   Explanation:

    In Microsoft Dataverse, every environment has a base currency that is defined when the
   environment is created.

   Key points:

      o  The base currency cannot be deactivated or deleted.
      o  Additional currencies can be deactivated if they are no longer needed.
      o  Record ownership (A) does not determine whether a currency can be deactivated.
      o  Active business processes (B) do not prevent currency deactivation.
      o  A currency can still be deactivated even if it has been used by records; those records
            retain their currency information (D).

    Therefore, if one specific currency cannot be deactivated while others can, the most likely
   reason is that it is the base currency of the Dataverse environment.

Discussion: https://www.examtopics.com/discussions/microsoft/view/81624-exam-pl-200-topic-
1-question-33-discussion/

---

## [Página 36](PL-200%20Q%26A.pdf#page=36) · texto nativo

027 Question.
A user has access to an existing Microsoft Dataverse database.
You need to ensure that the user can create canvas apps that consume data from Dataverse. You
must not grant permissions that are not required.
Which out-of-the-box security role should you assign to the user?

    A.  Environment Admin
    B.  Basic User
   C. Environment Maker
   D. System Customizer

Answer
   Correct Answer: C

   Explanation:

   The requirement is:

      o  The user must be able to create canvas apps.
      o  The apps must consume data from Dataverse.
      o  You must follow the principle of least privilege.

   The Environment Maker role is specifically designed for users who need to create and
   manage Power Apps, Power Automate flows, and other environment resources, without
    granting broad administrative privileges.

Discussion: https://www.examtopics.com/discussions/microsoft/view/79701-exam-pl-200-topic-
1-question-34-discussion/

028 Question.
You are configuring Microsoft Dataverse security. You plan to assign users to teams.
Record ownership and permissions will differ based on business requirements.
You need to determine which team types meet the requirements.
Which team type should you use? To answer, drag the appropriate team types to the correct
requirements. Each team type may be used once, more than once, or not at all. You may need to
drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

---

## [Página 37](PL-200%20Q%26A.pdf#page=37) · texto nativo

Select and Place:





      .
  Answer
       Correct Answer:





       Explanation:

   o   Ability to own records in Dataverse → Azure Active Directory group team
o  An Azure Active Directory (Microsoft Entra ID) group team can be assigned security roles and
   can own records in Dataverse.
   o  Provides permissions without a security role assigned → Access team
o  An Access Team does not require security roles. It grants access to specific records through
    sharing and access team templates

   Discussion: https://www.examtopics.com/discussions/microsoft/view/80881-exam-pl-200-topic-
    1-question-35-discussion/

---

## [Página 38](PL-200%20Q%26A.pdf#page=38) · texto nativo

029 Question.
A company has an AI agent that automates the review of customer feedback stored in a cloud
database.

A company has locations in the United States, Brazil, India, and Japan. The company conducts
financial transactions in all of these regions.
Financial transactions in Brazil are going to stop, but the office will remain open.
Users must no longer be able to create records associated with the Brazilian currency. Historical
records must remain intact.
You need to configure Microsoft Dataverse to meet the requirement
What should you do?

    A.  Disable the Brazilian language pack.
    B. Rename the Brazilian currency.
   C. Delete the Brazilian currency record.
   D. Deactivate the Brazilian currency record.
Answer
   Correct Answer: D

   Explanation:

   For The requirements are:

        •  Users must no longer create new records using the Brazilian currency.
        •   Historical records must remain intact.

   When a currency is deactivated in Dataverse:

        •    It is no longer available for new transactions or records.
        •   Existing records that already use the currency continue to function and retain their
            historical currency values.

Discussion: https://www.examtopics.com/discussions/microsoft/view/81627-exam-pl-200-topic-
1-question-36-discussion/

030 Question.
You are setting up Power Apps security for a company. The company has a CEO, two vice
presidents, and 10 managers. Five support representatives report to each manager.
You set up Manager Hierarchy so managers are able to view data only for the representatives who
report to them. The CEO must be able to view all data for everyone. All support representatives
must be able to view customer information in each other's data across all managers.
You need to resolve issues that arise during testing.
What should you do? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 39](PL-200%20Q%26A.pdf#page=39) · texto nativo

Hot Area:





Answer
   Correct Answer:





   Explanation:

Discussion: https://www.examtopics.com/discussions/microsoft/view/81443-exam-pl-200-topic-
1-question-37-discussion/

031 Question.
You are embedding a Power Apps visual in a Power BI dashboard.
External customers must authenticate to have access to the dashboard.
You need to configure the solution.

---

## [Página 40](PL-200%20Q%26A.pdf#page=40) · texto nativo

Which two actions should you perform? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

    A.  Set the Power BI service to authenticate users.
    B. Use a table in the Power BI dashboard.
   C. Publish to Power BI Report Server.
   D. Set the Power BI service to allow anonymous access.
    E.  Share the Power Apps visual components with external users.
Answer
   Correct Answer: A,E

   Explanation:

   To allow external customers to use a Power BI dashboard containing a Power Apps visual,
    while ensuring they authenticate:

A. Set the Power BI service to authenticate users

    External users must authenticate through Azure AD/Microsoft Entra ID (typically B2B guest
   access) to access Power BI content.

E. Share the Power Apps visual components with external users

   Users need permission not only to the Power BI report but also to the embedded Power Apps
   app. The Power Apps visual must be shared with those external users.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83259-exam-pl-200-topic-
1-question-38-discussion/

032 Question.
Your organization does not permit the use of custom code for solutions.
You need to create a view that can be viewed by all users in an organization.
Where should you create the view?

    A. Advanced Find
    B.  Entities component of a solution
   C. Microsoft Excel template
   D. System Settings
Answer
   Correct Answer: B

   Explanation:

   The requirement is to create a view that can be viewed by all users in the organization.

    In Dynamics 365/Dataverse:

---

## [Página 41](PL-200%20Q%26A.pdf#page=41) · texto nativo

•  Advanced Find creates personal views, which are only available to the user who created
      them (unless shared). (Incorrect)

    •   Entities component of a solution is where system (public) views are created and
      managed. These views are available to all users with access to the table. (Correct)

    •   Microsoft Excel template is used for exporting/importing data, not creating views.
        (Incorrect)

    •  System Settings does not provide functionality for creating views (Incorrect)

Discussion: https://www.examtopics.com/discussions/microsoft/view/79704-exam-pl-200-topic-
1-question-39-discussion/

033 Question.
You are designing the organization structure for a company that has 5,000 users.
You need to configure security roles for the company while minimizing administrative effort.
What should you do? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:





   Explanation:

---

## [Página 42](PL-200%20Q%26A.pdf#page=42) · texto nativo

Apply a security role to everyone in a business unit → Assign the security role to the default
business unit team

   For 5,000 users, the lowest administrative effort is to assign the role to the default business
    unit team. All users in the business unit inherit the team's security role.

Ensure an individual can see records in their current business unit and a child business unit →
Grant the user the Parent: Child Business Units security permission

   Dataverse security roles support the access level:

   Parent: Child Business Units

    This allows a user to access records in their own business unit and subordinate business units.

Discussion: https://www.examtopics.com/discussions/microsoft/view/81641-exam-pl-200-topic-
1-question-40-discussion/

034 Question.
You are using the Data import wizard to import records into the account table from a CSV file.
The CSV-to-table mapping is as follows:

        •  The Name column represents the account name and maps to the Account Name
          column.
        •  The Parent Name column represents the holding company of the account with
           subsidiaries underneath.

Records that are imported into the table are only related to other records in the file.
You need to configure the import to create the relationship between records.
What should you do?

    A. Map Parent Name in the CSV file to the Parent Account column. Select Account Name as
       the lookup criteria.
    B. Map Parent Name in the file to the Parent Account column. Select Parent Account as the
       lookup criteria.
   C. Create an alternate key on the account table by using the Account Name column. Do not
     map Parent Name in the file.
   D. Look up the record IDs of the records in the Parent Account column. Add the record IDs as
      a new column in the file. Map the new column to the Parent Account column.
Answer
   Correct Answer: A

   Explanation:

   The Parent Account field is a lookup column that references another Account record.

---

## [Página 43](PL-200%20Q%26A.pdf#page=43) · texto nativo

When importing data with the Data Import Wizard, if the parent and child accounts are all
   contained within the same import file, Dataverse can create the relationships during the import
    by:

         1.  Mapping Parent Name → Parent Account (lookup field).
         2.  Specifying the field used to identify the parent record, which is Account Name.

Discussion: https://www.examtopics.com/discussions/microsoft/view/81645-exam-pl-200-topic-
1-question-43-discussion/

035 Question.
A company has a sales application that is supported by an Azure SQL database. You are developing
a Power Apps app for use by customer service agents.
The app must reference customer data from the sales application. Data in the sales application is
constantly changing and must not be replicated in Microsoft
Dataverse.
Some customer data is considered sensitive. You must protect data for specific fields when users
view data in the app.
You need to configure table creation for the app.
How should you configure the app? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 44](PL-200%20Q%26A.pdf#page=44) · texto nativo

Explanation:

         1.  Dataverse table type → Create a virtual table

The data resides in an Azure SQL Database, changes frequently, and must not be replicated into
Dataverse.

Therefore, use a Virtual Table:

    •   Displays data from an external source (Azure SQL) in Dataverse.
    •  Does not store a copy of the data in Dataverse.
    •  Always reflects current data from the source system.

         2.  Protect sensitive customer data → Create a secured column

To restrict access to specific fields, Dataverse provides Column Security.

A secured column:

    •  Allows field-level security.
    •   Controls which users can view, create, or update the data in that column.
    •   Protects sensitive information regardless of forms or apps using the table.

Discussion: https://www.examtopics.com/discussions/microsoft/view/81517-exam-pl-200-topic-
1-question-44-discussion/

036 Question.
A customer uses Power Apps to view and maintain their contacts that are stored in Microsoft
Dataverse.
Several columns must be configured to ensure the security settings for sales associates are view
only.
You need to configure the access restrictions.
Which component for field-level security should you use? To answer, select the appropriate

---

## [Página 45](PL-200%20Q%26A.pdf#page=45) · texto nativo

options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





.

Answer
   Correct Answer:





   Explanation:

         1.  Enable the fields for field-level security → Power Platform admin center

---

## [Página 46](PL-200%20Q%26A.pdf#page=46) · texto nativo

To make a Dataverse column eligible for field-level security, you enable Column Security on
    the field. This configuration is managed within the Microsoft Power Platform admin center
   and Dataverse customization tools.

         2.  Set sales associates to view-only access → Field Security Profiles

    Field Security Profiles control whether users can:

        •  Read a secured field
        •  Create values in the field
        •  Update values in the field

   To make sales associates view-only, assign them a Field Security Profile with:

        •  Read = Allowed
        •  Create = Not Allowed
        •  Update = Not Allowed

Discussion: https://www.examtopics.com/discussions/microsoft/view/81518-exam-pl-200-topic-
1-question-45-discussion/

037 Question.
You modify a model-driven app for a bicycle repair help desk. The model-driven app is for help desk
users when customers have an issue with their bicycle.
After you add a custom table named bicycle, you configure the table for Microsoft Dataverse
search. The table will contain information from callers about their bicycles. The account table is
related to the custom table. Contact information is brought over to the custom table.
You add the following columns to the table:

        •   Bicycle type
        •   Tire brand
        •   Special equipment

Users must be able to perform the following types of searches:

        •  Search for all customers who have a bicycle type of Contoso and live in Florida.
        •  Search all tables for any record that contains the word broken.

You need to decide which type of search will give you the results desired.
Which search should you configure? To answer, drag the appropriate search types to the correct
requirements. Each search type may be used once, more than once, or not at all. You may need to
drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

---

## [Página 47](PL-200%20Q%26A.pdf#page=47) · texto nativo

Select and Place:





Answer
   Correct Answer:





   Explanation:

Customer with bicycle type of Contoso and lives in Florida → Advanced Find is designed for
complex queries with multiple criteria and relationships.

This requires filtering on multiple fields and potentially across related tables (Bicycle Type =
Contoso and Address State = Florida).

Includes the word broken across tables → Dataverse Search (formerly Relevance Search)
performs a global search across configured Dataverse tables and returns records containing the
specified term.

This requires searching for a keyword across multiple tables and columns in Dataverse.

Discussion: https://www.examtopics.com/discussions/microsoft/view/81519-exam-pl-200-topic-
1-question-46-discussion/

038 Question.
You make the following customizations to a Microsoft Dataverse environment:

    •  Create a new table.
    •  Add data to the new table.
    •  Delete an unused area from the site map.


The components must be transported to a different environment.

---

## [Página 48](PL-200%20Q%26A.pdf#page=48) · texto nativo

You need to determine the method required to transport each component.

Which method should you use? To answer, drag the appropriate methods to the correct
components. Each method may be used once, more than once, or not at all. You may need to drag
the split bar between panes or scroll to view content.





Answer
   Correct Answer:





   Explanation:

Solution is used to transport Dataverse customizations and metadata, including:

       •  Tables (entities)
       •  Columns
       •  Forms
       •  Views
       •   Site map changes

Configuration Migration tool is used to move data/configuration records between environments.

---

## [Página 49](PL-200%20Q%26A.pdf#page=49) · texto nativo

SolutionPackager tool is primarily used by developers to unpack and repack solution files for
source control and ALM; it is not the tool used to transport these components directly.

Discussion: https://www.examtopics.com/discussions/microsoft/view/95988-exam-pl-200-topic-
1-question-47-discussion/

039 Question.
Your organization does not permit the use of custom code for solutions.

You need to create a view that can be viewed by all users in an organization.

Where should you create the view?

    A. System Settings
    B.  Microsoft Excel template
   C. Microsoft Visual Studio
   D. Table component of a solution
Answer
   Correct Answer: D

   Explanation:

   A view that can be seen by all users is a System View. System views are created and managed
   as part of the table (entity) customization and are transported through solutions.

    •  Table component of a solution (Correct)
        o  Create a system view within the table and include it in a solution.
        o  Available to all users with access to the table.
    •  System Settings (Incorrect)
        o  Used for environment-wide settings, not for creating views.
    •  Microsoft Excel template (Incorrect)
        o  Used for exporting/importing data and templates, not Dataverse views.
    •  Microsoft Visual Studio (Incorrect)
        o  Custom code is not permitted, and Visual Studio is not required to create Dataverse
             views

Discussion: https://www.examtopics.com/discussions/microsoft/view/157696-exam-pl-200-
topic-1-question-48-discussion/

040 Question.
A company plans to add another language to a Microsoft Dataverse environment.

Several components were added or modified in the environment.

---

## [Página 50](PL-200%20Q%26A.pdf#page=50) · texto nativo

You need to ensure that these components get translated.

Which method should you use? To answer, drag the appropriate methods to the correct
component types. Each method may be used once, more than once, or not at all. You may need to
drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





.
Answer
   Correct Answer:





   Explanation:

       •  Views are part of Dataverse metadata and can be translated by exporting translations,
            translating the text, and then re-importing the translation file.
       •  Email templates are not automatically translated. Typically, you create a separate
          email template for each language.
       •  Reports (SSRS reports) support localization through embedded labels, which allow
           the report to display text in different languages.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96867-exam-pl-200-topic-
1-question-49-discussion/

041 Question.
A company uses Power Apps.

Users must be able to view only the address1 columns in the Account table.

---

## [Página 51](PL-200%20Q%26A.pdf#page=51) · texto nativo

You need to ensure other address columns are not visible to users when creating views and filters.

What should you do?

    A.  Delete the other address columns from the table.
    B.  Disable the Search option for the columns.
   C. Use column-level security to remove read access to all users.
   D. Create business rules to hide the other address columns.
Answer
   Correct Answer: C

   Explanation:

   The requirement is not just to hide the columns on forms, but to ensure that users cannot see
   or use the other address columns in views and filters.

   Column-level security (Field Security):

        •   Restricts access to specific columns.
        •   Prevents users from viewing secured columns.
        •   Prevents the columns from being available in views, searches, and filters for users
          without access.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96051-exam-pl-200-topic-
1-question-50-discussion/

042 Question.
A company uses Power Apps.

You create a custom table and configure a child table relationship with the contact table.
You need to configure the cascading rules for each action.

Which behavior should you use? To answer, drag the appropriate behaviors to the correct actions.
Each behavior may be used once, more than once, or not at all. You may need to drag the split bar
between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

---

## [Página 52](PL-200%20Q%26A.pdf#page=52) · texto nativo

Answer
   Correct Answer:





   Explanation:

        •  Delete → Restrict

        o  Prevents the parent Contact record from being deleted if related child records exist.

        o  Commonly used to preserve referential integrity.

        •  Share → Cascade All

        o  When a Contact record is shared, the sharing permissions automatically cascade
               to all related child records.

Discussion: https://www.examtopics.com/discussions/microsoft/view/95989-exam-pl-200-topic-
1-question-51-discussion/

043 Question.
You plan to add a Power Apps app to Microsoft Teams.

A Microsoft Dataverse for Teams environment has not been provisioned.

---

## [Página 53](PL-200%20Q%26A.pdf#page=53) · texto nativo

You need to create a Dataverse for Teams environment.

Which two actions can you perform? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

    A.  Create a new app in Teams.
    B.  Install an existing app in Teams.
    C.  Create a new environment in the Microsoft Power Platform Admin Center.
    D.  Create an app permission policy in the Teams admin center.
Answer
   Correct Answer: A,B

   Explanation:

A Dataverse for Teams environment is automatically created (provisioned) when:

        •  A user creates a new Power Apps app within Teams.
        •  A user installs an app in Teams that requires Dataverse for Teams.

Creating a Dataverse for Teams environment is not done from the Power Platform Admin Center,
and app permission policies in the Teams admin center do not provision Dataverse environments.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96880-exam-pl-200-topic-
1-question-52-discussion/

044 Question.
A company uses Power Apps with Microsoft Dataverse.

The company enables auditing on the Dataverse database. The company tenant reaches the
maximum storage capacity.

You need to delete some auditing data.

Which three deletion options should you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

    A. by record
    B. between two specified dates
   C. by table
   D. older than a specified date
    E.  by column

---

## [Página 54](PL-200%20Q%26A.pdf#page=54) · texto nativo

Answer
   Correct Answer: A,B,D

   Explanation:

   Dataverse auditing logs can be deleted using the Audit Log Management features. Supported
    deletion options include:

        •  By record – delete audit history for specific records.
        •  Between two specified dates – remove audit logs within a date range.
        •  Older than a specified date – bulk delete historical audit data older than a chosen
           date.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96056-exam-pl-200-topic-
1-question-53-discussion/

045 Question.
A company uses a Power Apps app with Microsoft Dataverse.

The company requires the import of records into Dataverse. Duplicate records in the data must be
deleted without user intervention.

You create a duplicate detection rule.

You need to configure the rule for the data import.

Which option should you configure?

    A.  Enable the During data import option.
    B. Enable the Templates for Data Import option.
   C. Disable the Allow Duplicates option.
   D. Enable the When a record is created or updated option.
Answer
   Correct Answer: A

   Explanation:

   A duplicate detection rule in Dataverse can be configured to run in different scenarios:

        •  When a record is created or updated
        •  During data import

   Since the requirement is to detect and remove/prevent duplicate records during an import
   without user intervention, the duplicate detection rule must be enabled for data imports.

---

## [Página 55](PL-200%20Q%26A.pdf#page=55) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/96717-exam-pl-200-topic-
1-question-54-discussion/

046 Question.
A company has a model-driven app that uses Microsoft Dataverse.

Users need to add an alternate phone number when entering their account information. The users
also require a list that displays the customers that do not have an alternate phone number.

You need to enable the required features.

Which features should you use? To answer, drag the appropriate features to the correct
requirements. Each feature may be used once, more than once, or not at all. You may need to drag
the split bar between panes or scroll to view content.





Answer
   Correct Answer:

---

## [Página 56](PL-200%20Q%26A.pdf#page=56) · texto nativo

Explanation

        •  Column: To store an alternate phone number, you add a new column (field) to the
         Account table.
        •  View: To display all customers that do not have an alternate phone number, create a
          view with a filter such as Alternate Phone Number does not contain data.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96881-exam-pl-200-topic-
1-question-55-discussion/

047 Question.
You create a model-driven app for an automobile parts help desk.

A help desk agent uses a form to gather information about customers’ automobiles in two custom
tables. The names of the tables are Client and Automobile.

The form must prepopulate the following information about the customer from the client table:

    •   First name
    •   Last name

The agent must be able to type the following information about the automobile:

    •  Automobile make
    •  Automobile model

You need to implement the form.

What should you configure? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 57](PL-200%20Q%26A.pdf#page=57) · texto nativo

Answer
   Correct Answer:

---

## [Página 58](PL-200%20Q%26A.pdf#page=58) · texto nativo

Explanation:

   Prepopulate client information → Relationship

   To automatically display the client's First Name and Last Name from the Client table when
   working with an automobile record, you need to create a relationship between the Client and
   Automobile tables. The relationship allows the form to access and display data from the
    related client record.

   Enter automobile information → Table

   The Automobile Make and Automobile Model are attributes of the automobile itself, so they
   should be stored as columns in the Automobile table. Therefore, the relevant configuration is
    the Table.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96058-exam-pl-200-topic-
1-question-56-discussion/

048 Question.
A company uses Power Apps. You enable auditing in Microsoft Dataverse.

Users report the following issues when viewing the audit logs:

    •  Unable to view the read access audit logs.

---

## [Página 59](PL-200%20Q%26A.pdf#page=59) · texto nativo

•  Unable to view the Account table audit logs.


You need to troubleshoot the issues.

What are the causes of the issues? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

  Unable to view the read access audit logs → Auditing for read access is not enabled

---

## [Página 60](PL-200%20Q%26A.pdf#page=60) · texto nativo

•  Dataverse does not audit record reads by default. To see read access audit entries,
         read access auditing must be explicitly enabled. If it is not enabled, no read audit logs
           are generated.

   Unable to view the Account table audit logs → Auditing is disabled at the table level

       •   Auditing must be enabled at multiple levels:

        o  Environment/organization level

        o  Table level

        o  Column level (if applicable)

       •    If users cannot view audit logs for the Account table specifically, the most likely cause
             is that auditing is not enabled on the Account table.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96882-exam-pl-200-topic-
1-question-57-discussion/

049 Question.
A company is implementing a data model by using Dataverse.

The company requires the following columns in a new custom table:





You need to choose the column type that uses the least amount of database storage for each
column.

Which column types should you choose? To answer, select the appropriate options in the answer
area.

NOTE: Each correct selection is worth one point.

---

## [Página 61](PL-200%20Q%26A.pdf#page=61) · texto nativo

Answer
   Correct Answer:

---

## [Página 62](PL-200%20Q%26A.pdf#page=62) · texto nativo

Explanation:

•   Special Notes → Text Area

      o  Stores up to 100 characters.

      o  Must be displayed as a multiline control.

      o  Text Area is designed for shorter multiline text and uses less storage than Multiline
            Text.

•   Specification → Multiline Text

      o  Must store up to 8,000 characters.

      o  Requires a multiline control.

---

## [Página 63](PL-200%20Q%26A.pdf#page=63) · texto nativo

•  Student → Customer (special lookup type that can reference both Account and
       Contact)

         o  Must reference either an Account or a Contact.

    •  Course Type → Choice (single-select option set)

         o  Users select one value from a predefined list.

Discussion: https://www.examtopics.com/discussions/microsoft/view/112129-exam-pl-200-
topic-1-question-58-discussion/

050 Question.
A company plans to implement a model-driven app. The company will enter data through the app.

The company has the following requirements:

    •  Users must be able to search for the data inside the app.
    •  Users must be able to search for the data outside the app.


You need to configure a solution for each requirement.

What should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 64](PL-200%20Q%26A.pdf#page=64) · texto nativo

Answer
   Correct Answer:





   Explanation:

       •  Search data inside the app → Dataverse Search

           o  Dataverse Search (formerly Relevance Search) provides a fast, global search
                 experience within model-driven apps.

           o  Users can search across multiple tables and columns from within the app.

       •  Search data outside the app → Microsoft Search

           o  Microsoft Search enables users to find Dataverse information from Microsoft
               365 experiences such as Bing, Office.com, and SharePoint.

           o  This satisfies the requirement to search for data outside the model-driven app.


Discussion: https://www.examtopics.com/discussions/microsoft/view/112046-exam-pl-200-
topic-1-question-59-discussion/

051 Question.
A company is implementing Microsoft Power Platform solutions.

The company requests information on the features that are supported by Power Fx.

---

## [Página 65](PL-200%20Q%26A.pdf#page=65) · texto nativo

You need to identify the features of Power Fx.

What should you identify?

    A.   It uses an undefined value for uninitialized variables.
    B.   It uses formulas that are similar to Microsoft Excel formulas.
   C.  It uses synchronous data operations.
   D.  It uses the model-driven app formula language.
Answer
   Correct Answer: B

   Explanation:

   Power Fx is the low-code formula language used in Microsoft Power Platform, especially in
   canvas apps. It is designed to be familiar to users who know Microsoft Excel, using functions
   and expressions similar to Excel formulas.

Discussion: https://www.examtopics.com/discussions/microsoft/view/132058-exam-pl-200-
topic-1-question-60-discussion/

052 Question.
A company is evaluating the capabilities in Dataverse and the scenarios for using virtual tables.

You need to identify the capabilities of virtual tables.

What is a capability of virtual tables?

    A.  Virtual tables store data in the Dataverse environment.
    B.  Virtual tables retrieve data from an external data source.
   C.  Virtual tables can be configured for user and team ownership.
   D.  Virtual tables support Dataverse auditing.
Answer
   Correct Answer: B

   Explanation

    Virtual tables (formerly known as virtual entities) allow Dataverse to display data that resides
    in an external system without copying or storing the data in Dataverse.

   Key characteristics:

       •   Retrieve data from external data sources such as SQL Server, Azure services, or other
         OData providers.

---

## [Página 66](PL-200%20Q%26A.pdf#page=66) · texto nativo

•  Data remains in the source system.
       •  Appears in Dataverse and model-driven apps like a standard table.
       •  Data is not stored in Dataverse.
       •   Virtual tables do not support all Dataverse capabilities, including auditing.
       •   Virtual tables are organization-owned and do not support user/team ownership.

Discussion: https://www.examtopics.com/discussions/microsoft/view/132059-exam-pl-200-
topic-1-question-61-discussion/

053 Question.
You must create a new table to support a new feature for an app. Records for the table must be
associated with a business unit and specify security roles for the business unit.

You need to configure table ownership.

Which table ownership type should you use?

    A.  user or team owned
    B. business-owned
   C. none
   D. organization-owned
Answer
   Correct Answer: B

   Explanation:

   A business-owned table is used when:

        •  Records belong to a specific business unit.
        •  Access is controlled through security roles assigned to business units.
        •  Records are not owned by individual users or teams.

    This exactly matches the requirement:

   "Records for the table must be associated with a business unit and specify security roles for
    the business unit."

Discussion: https://www.examtopics.com/discussions/microsoft/view/140624-exam-pl-200-
topic-1-question-66-discussion/

054 Question.
A company uses Power Apps.

You create a custom phone table that is a child of the contact table.

---

## [Página 67](PL-200%20Q%26A.pdf#page=67) · texto nativo

You need to configure the cascading rules for each action.

Which behavior should you use? To answer, drag the appropriate behaviors to the correct actions.
Each behavior may be used once, more than once, or not at all. You may need to drag the split bar
between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

        •   Restrict prevents deletion of the parent (Contact) record when related child (Phone)
          records exist.
        •  Cascade All causes ownership changes on the parent Contact record to automatically
         cascade to all related Phone records.

Discussion: https://www.examtopics.com/discussions/microsoft/view/147251-exam-pl-200-
topic-1-question-67-discussion/

055 Question.
Your organization does not permit the use of custom code for solutions.

You need to create a view that can be viewed by all users in an organization.

---

## [Página 68](PL-200%20Q%26A.pdf#page=68) · texto nativo

Where should you create the view?

    A. System Settings
    B. Advanced Find
   C. Table component of a solution
   D. Microsoft Excel template
Answer
   Correct Answer: C

   Explanation:

    There are two types of views in Dataverse:

        •  System Views – visible to all users who have access to the table.
        •  Personal Views – created by individual users, typically through Advanced Find, and
            visible only to the creator unless shared.

   Since the requirement is:

   "Create a view that can be viewed by all users in an organization"

   you must create a System View, which is configured within the table component of a
    solution.

Discussion: https://www.examtopics.com/discussions/microsoft/view/144216-exam-pl-200-
topic-1-question-68-discussion/

056 Question.
Your organization does not permit the use of custom code for solutions.

You need to create a view that can be viewed by all users in an organization.

Where should you create the view?

    A.  Templates area
    B. System Settings
   C.  List view of the table
   D. Table component of a solution
Answer
   Correct Answer: D

   Explanation:

---

## [Página 69](PL-200%20Q%26A.pdf#page=69) · texto nativo

To create a view that is available to all users in the organization, you must create a System
   View.

   System views are created and managed as part of a Dataverse table within a Solution. Once
    published, they are available to all users who have access to the table.

   Discussion: https://www.examtopics.com/discussions/microsoft/view/144217-exam-pl-200-
    topic-1-question-69-discussion/

057 Question.
A company is evaluating the capabilities in Dataverse and the scenarios for using virtual tables.

You need to identify the capabilities of virtual tables.

What is a capability of virtual tables?

    A.  Virtual tables can be configured for user and team ownership.
    B.  Virtual tables support Dataverse auditing.
   C.  Virtual tables contain columns for Status, Created On, and Modified On by default.
   D.  Virtual tables require configuration of a data provider.
Answer
   Correct Answer: D

   Explanation:

   A virtual table allows Dataverse to display data stored in an external data source without
    physically storing that data in Dataverse. To connect to the external source, a data provider
   must be configured

Discussion: https://www.examtopics.com/discussions/microsoft/view/144219-exam-pl-200-
topic-1-question-70-discussion/

058 Question.
A company is evaluating the capabilities in Dataverse and the scenarios for using virtual tables.

You need to identify the capabilities of virtual tables.

What is a capability of virtual tables?

    A.  Virtual tables support change tracking.
    B.  Virtual tables retrieve data from an external data source.
   C.  Virtual tables can be configured for user and team ownership.

---

## [Página 70](PL-200%20Q%26A.pdf#page=70) · texto nativo

D.  Virtual tables support Dataverse auditing.

Answer
   Correct Answer: B

   Explanation:

    Virtual tables in Dataverse allow you to work with data that remains in an external system
   without storing that data in Dataverse.

   Key characteristics:

        •   Retrieve data from external data sources (for example, SQL Server, Azure SQL, OData
            services).
        •  Data remains in the source system.
        •  Appears in Dataverse like a standard table.
        •  Do not support Dataverse auditing.
        •  Cannot be configured for user or team ownership (they are organization-owned).
        •  Do not support change tracking.

Discussion: https://www.examtopics.com/discussions/microsoft/view/157213-exam-pl-200-
topic-1-question-76-discussion/

059 Question.
A Your organization does not permit the use of custom code for solutions.

You need to create a view that can be viewed by all users in an organization.

Where should you create the view?

    A. Advanced Find
    B.  Studio System Settings
   C. Templates area
   D. Maker portal
Answer
   Correct Answer:

   Explanation: D

     A view that is available to all users is a system view. System views are created and managed
        in the Power Apps Maker portal as part of a table definition (typically within a solution).

---

## [Página 71](PL-200%20Q%26A.pdf#page=71) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/306446-exam-pl-200-
topic-1-question-77-discussion/

060 Question.
A company is using Dataverse with a model-driven app. The app includes a table named
Quotations.

Users in the system enter relevant details, such as customer, address, line items, and total
amounts. The users then create a standardized report to manually populate the details.

The company requires the formatted report to be generated from the record and populated with the
record details. The company does not want to purchase additional licenses.

You need to recommend a solution.

Which solution should you recommend?

    A. a Word template
    B. an Excel template
   C. an article template
Answer
   Correct Answer: A

   Explanation:

      The requirement is to:

        •  Generate a formatted report from a Dataverse record.
        •   Automatically populate the report with data from the Quotation record (customer,
          address, line items, totals, etc.).
        •   Avoid purchasing additional licenses.

     Word templates in Dataverse are specifically designed for this scenario. They allow users
       to create standardized documents that merge data directly from Dataverse records and
      can be generated from within a model-driven app

Discussion: https://www.examtopics.com/discussions/microsoft/view/319525-exam-pl-200-
topic-1-question-78-discussion/

061 Question.
Your organization does not permit the use of custom code for solutions.

You need to create a view that can be viewed by all users in an organization.

---

## [Página 72](PL-200%20Q%26A.pdf#page=72) · texto nativo

Where should you create the view?

    A.  Templates area
    B.  Microsoft Excel template
   C. Advanced Find
   D. Table component of a solution
Answer
   Correct Answer: D

   Explanation:

   To create a view that is available to all users in the organization, you must create a System
   View.

   System views are created and managed within the table definition in Dataverse, typically
   through a Solution in the Power Apps Maker portal. Once published, the view is available to all
   users who have access to the table.

Discussion: https://www.examtopics.com/discussions/microsoft/view/157215-exam-pl-200-
topic-1-question-79-discussion/

062 Question.
You are configuring Dataverse for a company.

The company has the following requirements for document management, which must be met by
using native functionality:

        •  A single file must be stored and accessed directly from an Account row. No additional
         metadata should be captured.
        •   Multiple files must be stored and accessed from a Contact with support for version
            control.
        •  Documents must be stored within an on-premises environment.
        •   Additional rich-text notes must be stored alongside one or multiple file uploads.

You need to recommend a solution for each requirement.

Which solution should you recommend? To answer, move the appropriate solutions to the correct
requirements. You may use each solution once, more than once, or not at all. You may need to
move the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

---

## [Página 73](PL-200%20Q%26A.pdf#page=73) · texto nativo

.

Answer
   Correct Answer:





   Explanation:

        •  Document column → Best for storing a single file directly on a Dataverse record with
         no additional metadata requirements.
        •   Microsoft SharePoint → Provides document management, multiple files, and version
           control.
        •   Microsoft Azure Blob Storage → Can be configured for on-premises document
          storage scenarios using native Dataverse integration options.
        •  Attachments (Notes/Annotations) → Support one or more file uploads along with
           rich-text notes in the note body.
Discussion: https://www.examtopics.com/discussions/microsoft/view/321803-exam-pl-200-
topic-1-question-82-discussion/

063 Question.
A company is evaluating the capabilities in Dataverse and the scenarios for using virtual tables.

You need to identify the capabilities of virtual tables.

---

## [Página 74](PL-200%20Q%26A.pdf#page=74) · texto nativo

What is a capability of virtual tables?

    A.  Virtual tables store data in the Dataverse environment.
    B.  Virtual tables contain time dimension attributes by default.
   C.  Virtual tables support change tracking.
   D.  Virtual tables retrieve data from an external data source.

Answer
   Correct Answer: D

   Explanation:

     Virtual tables (formerly called virtual entities) allow Dataverse to present data that resides in an
   external data source without storing a copy of the data in Dataverse.

   Key characteristics of virtual tables:

        •   Retrieve data from external systems (SQL Server, Azure SQL, OData, custom providers,
             etc.)
        •  Data remains in the source system
        •  Can be used in model-driven apps like regular Dataverse tables
        •  Do not store data in Dataverse
        •  Do not support change tracking
        •  Do not include time-dimension attributes by default.

Discussion: https://www.examtopics.com/discussions/microsoft/view/394308-exam-pl-200-
topic-1-question-83-discussion/

064 Question.
A You create an app to manage customer service cases.
Cases entered in forms require different types of data to be stored in different types of columns.
You need to create forms for each of the following case types:





Which form types should you create? To answer, drag the appropriate form types to the meet the
data entry requirements. Each source may be used once, more than once, or not at all. You may

---

## [Página 75](PL-200%20Q%26A.pdf#page=75) · texto nativo

need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





Answer
   Correct Answer:

---

## [Página 76](PL-200%20Q%26A.pdf#page=76) · texto nativo

Explanation:

    This question tests the different Dataverse form types:

        •  Main form → Supports timelines, business process flows, and full data entry.
        •  Card form → Used in interactive dashboards.
        •  Quick Create form → Mobile-friendly, minimal fields for rapid record creation.
        •  Quick View form → Displays fields from a related (parent) record and is read-only.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60298-exam-pl-200-topic-
2-question-1-discussion/

065 Question.
You are a Dynamics 365 Customer Service developer.
A salesperson creates a chart.
You need to ensure that the chart is available to all users on the team.
Which actions should the salesperson perform? To answer, drag the appropriate actions to the
correct users. Each action may be used once, more than once, or not at all. You may need to drag
the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

---

## [Página 77](PL-200%20Q%26A.pdf#page=77) · texto nativo

Select and Place:





Answer
   Correct Answer:





   Explanation:

   A chart created by a salesperson is initially a personal (user) chart.

   To make it broadly available:

    1.  Export the user chart for import as a system chart
         o  System charts are available to all users who have access to the table.
    2.  Share the chart with the team
         o  This allows the team members to access the chart immediately as a shared chart.

  Why not the others?

    •  Assign the chart to each person on the team
      Not how charts are distributed.
    •  Export to Power BI
      Unnecessary for making a Dynamics 365 chart available to users.

---

## [Página 78](PL-200%20Q%26A.pdf#page=78) · texto nativo

•  Export the user chart for import as a user chart
      Would still be a personal chart rather than an organization-wide chart.


Discussion: https://www.examtopics.com/discussions/microsoft/view/42126-exam-pl-200-topic-
2-question-2-discussion/

066 Question.
You implement an editable grid for the Account entity.
The business team provides the following list of features that they would like you to implement:

    •  Group by or sort columns in the current view.
    •  Configure a business rule to show an error message.
    •   Edit values in calculated fields.
    •   Edit the Address composite field.
    •  Use the editable grid on mobile phones.


Which actions can you perform? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 79](PL-200%20Q%26A.pdf#page=79) · texto nativo

Hot Area:





Answer
   Correct Answer:

---

## [Página 80](PL-200%20Q%26A.pdf#page=80) · texto nativo

Explanation:

    •  Group by or sort columns → Yes. Editable grids support sorting and grouping.
    •  Business rule to show an error message → Yes. Business rules are supported in
       editable grids.
    •   Edit calculated fields → No. Calculated fields are read-only.
    •   Edit Address composite field → No. Composite fields cannot be edited directly in an
       editable grid.
    •  Use on mobile phones → Yes. Editable grids are supported on mobile clients.

Discussion: https://www.examtopics.com/discussions/microsoft/view/41345-exam-pl-200-topic-
2-question-3-discussion/

067 Question.
You must create a form for team members to use. The form must provide the ability to:

    •  Lock a field on a form.
    •   Trigger business logic based on a field value.

---

## [Página 81](PL-200%20Q%26A.pdf#page=81) · texto nativo

•  Use existing business information to enhance data entry.

You need to implement business rule components to create the form.
Which components should you use? To answer, drag the appropriate components to the correct
requirements. Each component may be used once, more than once, or not at all. You may need to
drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





Answer
   Correct Answer:





   Explanation:

       •  Actions perform operations such as Lock or Unlock field, Set Business Required, Set
            Field Value, Show Error Message, etc.
       •  Conditions evaluate field values and determine when business logic should execute.

---

## [Página 82](PL-200%20Q%26A.pdf#page=82) · texto nativo

•  Recommendation provides suggested values or actions based on existing business
           information to improve data entry.

   .Discussion: https://www.examtopics.com/discussions/microsoft/view/41777-exam-pl-200-
    topic-2-question-4-discussion/

068 Question.
You have a form that displays a custom field from an entity.
A customer wants to restrict users from filtering on the custom field.
You need to prevent users from filtering the field in Advanced Find.
What should you modify?

    A.  Fields in the Edit Filter Criteria option of the Quick Find view
    B. a searchable field on the Field Properties form
   C.  Fields in the Add Find Columns option of the Quick Find view
Answer
   Correct Answer: B

   Explanation:

    In Dataverse, whether a column can be used in Advanced Find is controlled by the column's
   Searchable property.

      If you want to prevent users from filtering on a custom field in Advanced Find:

         1.  Open the column properties.
         2.  Set the column to not searchable.
         3.  Publish the changes.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60506-exam-pl-200-topic-
2-question-5-discussion/

069 Question.
You are designing a canvas app that connects to Common Data Service.
You need to configure the app to meet the requirements and ensure that the canvas app is
available offline.
What should you implement? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 83](PL-200%20Q%26A.pdf#page=83) · texto nativo

Hot Area:





Answer
   Correct Answer:





   Explanation:

        •  Pass values from the current screen when moving to another screen → Navigate
                o  Use the Navigate function. It allows you to move to another screen and
                      pass context variables/parameters to that screen.
        •  Display data to a user when the app is offline → LoadData
                o  Use LoadData. In offline scenarios, data is typically stored locally with
                     SaveData and retrieved with LoadData when the device is
                        disconnected.

---

## [Página 84](PL-200%20Q%26A.pdf#page=84) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/63420-exam-pl-200-topic-
2-question-6-discussion/

070 Question.
You have a canvas app that allows users to view, select, and purchase products. The app uses a
Gallery control to display products and checkboxes that allow users to select products.
When users select items from the product catalog, they move to a different screen to complete a
purchase.
Users must be able to clear all product selections when they click the button.
You need to configure the button.
What should you do?

    A. Use the Reset(Control) formula and pass the gallery control as a parameter to the Reset
       formula.
    B. Use the Reload(Control) formula and pass the gallery control as a parameter to the Reload
       formula.
   C. Use the ForAll() function to iterate through each item of the Gallery and clear user
        selections.
   D. Set the OnCheck value to populate a collection and the OnUncheck value to remove the
       item from the collection. Clear collection when the user selects the button.
Answer
   Correct Answer: D

   Explanation:

In a Gallery with multiple checkboxes, a common pattern is:

        •  OnCheck → Add the selected item to a collection (Collect()).
        •  OnUncheck → Remove the item from the collection (Remove()).
        •  Clear selections button → Use Clear() or ClearCollect() to empty the collection.

This effectively removes all selected products at once and ensures selections remain available
when navigating between screen

Discussion: https://www.examtopics.com/discussions/microsoft/view/42355-exam-pl-200-topic-
2-question-7-discussion/

071 Question.
You have a canvas app that contains the following text input fields: Id, FirstName, LastName. The
app also has a button named Button1.
The OnSelect property for Button1 contains the following expression:
Collect(People, {Id:Id.Text, FirstName:FirstName.Text, LastName:LastName.Text})
For each of the following statements, select Yes if the statement is true. Otherwise, select No.

---

## [Página 85](PL-200%20Q%26A.pdf#page=85) · texto nativo

NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:





   Explanation:

    1.  People collection automatically created → Yes

       •   Collect() creates the collection if it does not already exist.

    2.  Existing record is updated → No

       •   Collect() always adds a new record.

       •    It does not search for existing records or update them. Functions such as Patch() or
           UpdateIf() would be used for updates.

    3.  Adding a new Age field causes an error → No

       •   Collections are flexible.

---

## [Página 86](PL-200%20Q%26A.pdf#page=86) · texto nativo

•  Adding a new column (such as Age) automatically adds that column to the collection
         and populates blanks for existing records.

Discussion: https://www.examtopics.com/discussions/microsoft/view/79710-exam-pl-200-topic-
2-question-8-discussion/

072 Question.
You are a Dynamics 365 Customer Service administrator.
A user must be able to view system posts and activities in a dashboard.
You need to create the dashboard for the user.
Which components should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 87](PL-200%20Q%26A.pdf#page=87) · texto nativo

Explanation:

       •  Timeline is used to display posts, notes, activities, and system-generated posts in
         Dynamics 365 records and dashboards.
       •   Lists can display activity views (tasks, phone calls, appointments, emails, etc.) on a
          dashboard.

Discussion: https://www.examtopics.com/discussions/microsoft/view/54310-exam-pl-200-topic-
2-question-9-discussion/

073 Question.
You are building a model-driven app. The environment has Advanced settings enabled.

A form in the app requires a custom interface.

You need to embed the custom interface onto the form without using custom code.

What should you do?

    A.  Create a canvas app and bind its properties to the form.
    B.  Modify the model-driven app to use tablet form factor.
   C. Use an IFRAME.
   D. Create a quick view form.

---

## [Página 88](PL-200%20Q%26A.pdf#page=88) · texto nativo

Answer
   Correct Answer: C

   Explanation:

     When Advanced Settings are enabled in a model-driven app, you can embed external or
      custom user interfaces directly into a form by using an IFRAME. This allows you to
       incorporate custom web content without writing custom code in the form itself.

       •  Why the other options are incorrect:
       •   A. Create a canvas app and bind its properties to the form
           o  Modern model-driven apps support embedding canvas apps, but the question
                    specifically refers to a custom interface and the traditional approach available
                 through Advanced Settings. Canvas apps are not simply "bound" to form
                  properties in the way described.
       •   B. Modify the model-driven app to use tablet form factor
           o  Form factor affects layout and device experience, not embedding custom
                   interfaces.
       •  D. Create a quick view form
           o  Quick view forms display related Dataverse record information and cannot host
                    arbitrary custom interfaces.

     Exam Tip

                In Dynamics 365/Dataverse, when a question mentions embedding custom web
             content into a form without custom code and references Advanced Settings, the
             expected answer is usually IFRAME.

Discussion: https://www.examtopics.com/discussions/microsoft/view/169996-exam-pl-200-
topic-2-question-10-discussion/

074 Question.
A company is implementing Power Apps and Power Automate.
Several components are created within Power Apps, Microsoft Dataverse, and Power Automate.
These components must be promoted from the development environment to the user acceptance
test environment in a single solution package.
You need to create the solution package for promotion.
Where should you create the package?

    A.  Azure DevOps
    B. Power Apps designer
   C. Microsoft Power Platform admin center
   D. Azure portal
    E.  Office 365 admin center

---

## [Página 89](PL-200%20Q%26A.pdf#page=89) · texto nativo

Answer
   Correct Answer: B

   Explanation:

   To promote components from Power Apps, Dataverse, and Power Automate together, you
   must first add them to a Solution. Solutions are created and managed within the Power Apps
   maker portal (Power Apps designer).

   The typical process is:

         1.  Create a Solution in Power Apps.
         2.  Add app components, Dataverse tables, cloud flows, and other artifacts to the solution.
         3.  Export the solution as Managed or Unmanaged.
         4.  Import the solution into the UAT environment.

Discussion: https://www.examtopics.com/discussions/microsoft/view/80261-exam-pl-200-topic-
2-question-11-discussion/

075 Question.
A company is creating a Power Apps solution for a production facility.
The current solution is in English. The customized components must be translated into several
languages.
You need to extract the text for translation.
In which location can you achieve this goal?

    A. The tables in the web application.
    B. The selected environment in the Microsoft Power Platform admin center.
   C. The solution in the web application.
   D. The individual solution components in the web application.
Answer
   Correct Answer: C

   Explanation:

   To translate customized components in Power Apps/Dataverse, you use the solution
    translation feature:

         1.  Open the Solution that contains the customizations.
         2.  Select Translate → Export Translations.
         3.  A ZIP file containing translation labels is generated.
         4.  Translate the text.
         5.  Import the translated file back into the solution using Import Translations.

---

## [Página 90](PL-200%20Q%26A.pdf#page=90) · texto nativo

Because translation export/import is performed at the solution level, the correct location is the
    solution in the web application.

Discussion: https://www.examtopics.com/discussions/microsoft/view/81768-exam-pl-200-topic-
2-question-12-discussion/

076 Question.
You have a canvas app that allows users to view, select, and purchase products. The app uses a
Gallery control to display products and checkboxes that allow users to select products.
When users select items from the product catalog, they move to a different screen to complete a
purchase.
Users must be able to clear all product selections when they click the button.
You need to configure the button.
What should you do?

    A. Use the Reload(Control) formula and pass the gallery control as parameter to the Reload
       formula.
    B. Use the Reset(control) formula and pass the checkbox to the formula to clear user
        selections.
   C. Set the OnCheck value to populate a collection and the OnUncheck value to remove the
       item from the collection. Clear the collection when the user selects the button.
   D. Use the Revert(Products) formula and pass the checkbox to the formula to clear user
        selections.
    E. Use the Reset(Control) formula and pass the gallery control as a parameter to the Reset
       formula.
Answer
   Correct Answer: C

   Explanation:

   Set the OnCheck value to populate a collection and the OnUncheck value to remove the item
   from the collection. Clear the collection when the user selects the button.

    In canvas apps, when users select products in a gallery and then navigate to another screen,
    the selected items are commonly stored in a collection.

   A typical implementation is:

        •  OnCheck → Collect(...) the selected product into a collection.
        •  OnUncheck → Remove(...) the product from the collection.
        •  Clear selections button → Clear(CollectionName).

    This approach reliably clears all selected products, regardless of screen navigation.

Discussion: https://www.examtopics.com/discussions/microsoft/view/54114-exam-pl-200-topic-
2-question-13-discussion/

---

## [Página 91](PL-200%20Q%26A.pdf#page=91) · texto nativo

077 Question.
A customer tracks events by using a custom entity.
The custom entity includes a custom field for the venue of the events. The customer must be able
to display the events by venue in a calendar.
You need to ensure that all events display by venue in the calendar.
To which component should you add a control?

    A. Form
    B.  Subgrid
   C. Chart
   D. View
Answer
   Correct Answer: D

   Explanation:

   To display records in a calendar, you add a Calendar control to a view of the entity.

   The calendar control can use fields such as:

        •   Start Date
        •  End Date
        •  Venue (location)

   Once configured on the view, users can switch to the calendar visualization and see events
   grouped or displayed according to the configured fields

Discussion: https://www.examtopics.com/discussions/microsoft/view/54515-exam-pl-200-topic-
2-question-14-discussion/

078 Question.
You are creating a canvas app.
A user will click a button on each screen of a Power Apps app to proceed to the next screen.
You need to implement the action which selects the next screen that the user sees.
Which event should you handle?

    A.  ScreenTransition
    B. OnSelect
   C. OnLoad
   D. OnCheck

.

---

## [Página 92](PL-200%20Q%26A.pdf#page=92) · texto nativo

Answer
   Correct Answer: B

   Explanation:

    In a canvas app, when a user clicks a button, the action is handled by the button's OnSelect
    property. To navigate to another screen, you typically use the Navigate() function within the
   OnSelect event.

   Example:

   Navigate(Screen2, ScreenTransition.Fade)

  Why the other options are incorrect

    A. ScreenTransition – Specifies the visual effect used during navigation; it is not an event.

   C. OnLoad – Runs when a screen or app loads, not when a button is clicked.

   D. OnCheck – Used for controls such as checkboxes and toggle controls, not buttons

Discussion: https://www.examtopics.com/discussions/microsoft/view/54381-exam-pl-200-topic-
2-question-15-discussion/

079 Question.
A company has a canvas app that includes the following screens: Screen1 and Screen2.
The OnVisible property for Screen1 contains the following expression.
Set(AgeGroups, ["1-25", "26-54", "55+"])
For each of the following statements, select Yes if the statement is true. Otherwise, select No.
NOTE: Each correct selection is worth one point.
Hot Area:





.

---

## [Página 93](PL-200%20Q%26A.pdf#page=93) · texto nativo

Answer
   Correct Answer:





   Explanation:

    •  AgeGroups can be accessed from Screen1 and Screen2 → Yes

         o   Set() creates a global variable that is available throughout the app, including all
              screens.

    •  AgeGroups is a collection → No

         o  Collections are created using functions such as Collect() or ClearCollect().

         o   Set() creates a global variable, not a collection.

    •  You can use the Update function to change values in AgeGroups → No

         o  Update() is used to modify records in a data source or collection.

         o  Since AgeGroups is a global variable, you would modify it by calling Set() again.

Discussion: https://www.examtopics.com/discussions/microsoft/view/41519-exam-pl-200-topic-
2-question-16-discussion/

080 Question.
You are a Dynamics 365 Customer Service developer.
A salesperson creates a chart.
You need to ensure that the chart is available to all users on the team.
What should you do?

    A.  Share the chart with the team.
    B.  Assign the chart to each person on the team.
   C. Export the user chart to Power BI. Import the chart as a Power BI visualization.

---

## [Página 94](PL-200%20Q%26A.pdf#page=94) · texto nativo

D. Export the user chart for import as a user chart.
Answer
   Correct Answer: A

   Explanation:

    In Dynamics 365 Customer Service, when a user creates a personal (user) chart, it is only
    visible to that user by default. To make the chart available to other users or a team, the chart
   must be shared.

    •  Share the chart with the team → Makes the personal chart available to all members of the
      team.
    •  No need to assign it individually to each user.

Discussion: https://www.examtopics.com/discussions/microsoft/view/61453-exam-pl-200-topic-
2-question-17-discussion/

081 Question.
You create an app.
You need to create the site map for the app.
Which three actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.
Select and Place:





.

---

## [Página 95](PL-200%20Q%26A.pdf#page=95) · texto nativo

Answer
   Correct Answer:





   Explanation:

When creating a sitemap, you first create an Area, then within the area create a Group, and finally
add Subareas that link to tables, dashboards, pages, or URLs.

"Add a view" is not part of the sitemap hierarchy.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60445-exam-pl-200-topic-
2-question-18-discussion/

082 Question.
A company is implementing Microsoft Power Platform solutions.

The company requests information on the features that are supported by Power Fx.

You need to identify the features of Power Fx.

What should you identify?

    A.   It is available for purchase through a Microsoft reseller.
    B.   It uses a plug-in.
   C.  It uses imperative and declarative logic.
   D.  It uses synchronous data operations.

---

## [Página 96](PL-200%20Q%26A.pdf#page=96) · texto nativo

Answer
   Correct Answer: C

   Explanation:

Power Fx is the low-code formula language used in Microsoft Power Apps. It supports both:

    •   Declarative logic: Describes what a value should be (similar to Excel formulas).

      Sum(Products, Price)

    •   Imperative logic: Describes actions to perform in sequence, typically in behavior properties
      such as OnSelect.

       Set(varTotal, 100);

Discussion: https://www.examtopics.com/discussions/microsoft/view/157047-exam-pl-200-
topic-2-question-19-discussion/

083 Question.
You are configuring a new Power Apps portal. You have two web roles, one for authenticated users
and one for anonymous users. You grant the Anonymous
Users role to users.
A test user reports that they can access the home page but cannot view a page linked from the
home page.
You need to determine why the test user cannot view the portal page.
What is the cause of the issue?

    A. The setting to make the page available to everyone is disabled.
    B.  Inherited permissions are not enabled for the linked page.
   C. The Authenticated Users Web role does not have permission to view the page.
   D. Maintenance mode is enabled on the portal.
Answer
   Correct Answer: B

   Explanation:

In Power Apps Portals (Power Pages), a page can inherit permissions from its parent page.

In this scenario:

        •  The test user can access the home page.
        •  The user cannot access a page linked from the home page.
        •  The user has the Anonymous Users web role.

---

## [Página 97](PL-200%20Q%26A.pdf#page=97) · texto nativo

A common cause is that the linked page is not configured to inherit permissions from the parent
page (Home page). As a result, the linked page does not grant access to anonymous users even
though the parent page does.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83641-exam-pl-200-topic-
2-question-20-discussion/

084 Question.
A company is configuring a Power Apps portal using Microsoft Dataverse.
The company requires the following:

        •  Only authenticated users must be able to sign into the portal.
        •   Authenticated users must have varying degrees of access to the different parts of the
            portal.
        •  Users must enter one of several external identities when creating an account during the
         open registration process.

You need to configure user authentication and permissions.
Which component should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 98](PL-200%20Q%26A.pdf#page=98) · texto nativo

Explanation:

   Required for each authenticated user before security can be assigned → Contact table
   record

In Power Apps Portals (Power Pages), every authenticated user must be associated with a Contact
record in Dataverse. Security permissions and web roles are assigned to the Contact record.

   Required for authenticated users to access restricted pages of the portal → Web roles

Access to secured pages is controlled through Web Roles. Users are assigned one or more web
roles, and page permissions are granted to those roles.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83766-exam-pl-200-topic-
2-question-21-discussion/

085 Question.
You create a new solution for a business process.
The business process includes uploading specific file types to a web service.
You need to ensure that the business process works the same way anywhere the solution is
deployed.
Which option should you use? To answer, drag the appropriate options to the correct
configurations. Each option may be used once, more than once, or not at all.
You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:

---

## [Página 99](PL-200%20Q%26A.pdf#page=99) · texto nativo

.
Answer
   Correct Answer:





   Explanation:

   Blocked file types → Solution system settings

Blocked file extensions are configured as solution system settings so that the solution carries the
configuration and behaves consistently when deployed to other environments.

   URL to a web service → Environment variable

---

## [Página 100](PL-200%20Q%26A.pdf#page=100) · texto nativo

An environment variable is used for values that may differ between environments (Dev, Test,
Prod), such as:

        •  Web service URLs
        •   API endpoints
        •  Connection strings
        •   External service identifiers

This allows the same solution to be deployed while changing only the environment-specific value.

  Why not Connection reference?

A connection reference is used to reference connectors (e.g., SharePoint, Outlook, Dataverse) in
Power Automate flows and apps, not for storing a web service URL.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83286-exam-pl-200-topic-
2-question-22-discussion/

086 Question.
A company collaborates by using Microsoft Teams.
You must create a Power Apps app directly from within a Teams channel. The app will be used by
members of the channel to manage sales orders.
You need to create the app by using Dataverse for Teams.
How should you create the app?

    A.  Create a canvas app by using a Power Apps personal app in Teams.
    B.  Create a canvas app by using the App Studio app.
   C. Use the Power Apps web designer.
   D. Create a model-driven app by using the App Studio app.
Answer
   Correct Answer: A

   Explanation:

When building an app directly within Microsoft Teams using Dataverse for Teams, you create a
canvas app from the Power Apps app in Teams.

Dataverse for Teams is designed specifically for:

        •  Teams-based collaboration
        •  Canvas apps
        •  Power Automate flows
        •  Dataverse for Teams tables

Discussion: https://www.examtopics.com/discussions/microsoft/view/82520-exam-pl-200-topic-
2-question-23-discussion/

---

## [Página 101](PL-200%20Q%26A.pdf#page=101) · texto nativo

087 Question.
A company has a portal. Users sign into the portal by using a social media account.
The company wants to replace the existing portal with a Power Apps portal. Users must sign up for
access to the portal by using a Microsoft account and a unique invitation code that will be provided
to the users.
You need to configure authentication for the home page.
Which values should you use? To answer, drag the appropriate values to the appropriate
authentication settings. Each value may be used once, more than once, or not at all. You may need
to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





.
Answer
   Correct Answer:





   Explanation:

    •   External sign in = Yes

      o  Users must sign in using a Microsoft account, which is an external identity provider.
           Therefore, external sign-in must be enabled.

    •  Open registration = No
         o  Users must provide a unique invitation code to gain access.

---

## [Página 102](PL-200%20Q%26A.pdf#page=102) · texto nativo

o  Open registration allows anyone to self-register without an invitation, which does
              not meet the requirement.

Discussion: https://www.examtopics.com/discussions/microsoft/view/81903-exam-pl-200-topic-
2-question-24-discussion/

088 Question.
   You are customizing a model-driven app for a company. You create a Theme template to
   ensure the company logo and colors are properly used within these apps.
   The theme must meet the following requirements:

    •  Updated to add the logo
    •  Downloaded by the makers to create the app

   You need to configure the assets. To answer, drag the appropriate configurations to the correct
   requirements. Each configuration may be used once, more than once, or not at all. You may
   need to drag the split bar between panes or scroll to view content.
   NOTE: Each correct selection is worth one point.
    Select and Place:





Answer
   Correct Answer:





   Explanation:

Update logo → Edit the theme in System settings and upload a jpg file

---

## [Página 103](PL-200%20Q%26A.pdf#page=103) · texto nativo

To add or update the company logo in a Dynamics 365 / model-driven app theme, you edit the
   theme and upload a logo image (typically JPG or PNG) through the theme settings.

Change model-driven app colors → Replace an existing UI item's hexadecimal number

   Theme colors are controlled through hexadecimal color values for UI elements such as the
    navigation bar, links, and accents.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83266-exam-pl-200-topic-
2-question-25-discussion/

089 Question.
A user needs to create a Power Apps portal app.
The user is getting a permission denied error when creating the portal app.
You need to configure permissions to create the portal app.
Which three permissions should you configure? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

    A.  In the Power Platform admin center, ensure that the user account has read-write access.
    B.  In Azure Active Directory, assign the Contributor role to the application at the subscription
       scope.
   C.  In Azure Active Directory, ensure that the user has permission to register an app.
   D.  In the Power Platform admin center, change the portal app owner to the user.
    E.  In the Power Platform admin center, ensure that the user has the System administrator
        security role.
Answer
   Correct Answer: A,C,E

   Explanation:

A. In the Power Platform admin center, ensure that the user account has read-write access.

   The user needs appropriate permissions in the environment, including read-write access to
    create and manage portal components.

C. In Azure Active Directory, ensure that the user has permission to register an app.

    Portal provisioning creates and configures Azure AD applications. If users cannot register
    applications in Azure AD, portal creation can fail with permission errors.

E. In the Power Platform admin center, ensure that the user has the System administrator
security role.

   The System Administrator security role provides the Dataverse permissions required to create
   and configure a portal.

---

## [Página 104](PL-200%20Q%26A.pdf#page=104) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/84248-exam-pl-200-topic-
2-question-26-discussion/

090 Question.
You have a Power Apps portal app that supports a sales community and a service community in the
same environment. The only language configured in the environment is English. The company
wants to add support for two more languages.
The solution must meet the following requirements:

        •  Languages must be for both sales and service functions.
        •  The company logo and colors must be used and apply to all screens.
        •  Communities must be separate with different URLs and access lists.

You need to configure the solution.
What should you configure? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 105](PL-200%20Q%26A.pdf#page=105) · texto nativo

Explanation:

   Languages → Create two portals, one for each community.

   The requirement states:

    •  Sales and Service communities must be separate.
    •  Each must have its own URL and access list.

    Therefore, you need two portals:

    •  Sales Portal
    •   Service Portal

   Each portal can support multiple languages through portal localization and translated content.
   There is no need to create separate portals for each language.

   Company logo and colors → Add themes

   To apply branding consistently across all pages and screens of a portal, use Themes.

   Themes provide:

    •  Logo branding
    •  Colors
    •   Styling applied throughout the portal

Discussion: https://www.examtopics.com/discussions/microsoft/view/82638-exam-pl-200-topic-
2-question-27-discussion/

091 Question.
A company is creating a canvas app and a model-driven app to manage their customer accounts.
The canvas app requires a business rule to set the Business Type column to large if the customer
size is greater than a specific currency value.

---

## [Página 106](PL-200%20Q%26A.pdf#page=106) · texto nativo

The model-driven app requires a business rule to recommend the account rating be re-evaluated
when the account goes on credit hold for this app only.
You need to configure the scope for the business rules.
Which scope should you use? To answer, drag the appropriate scopes to the correct business
rules. Each scope may be used once, more than once, or not at all.
You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





.
Answer
   Correct Answer:





   Explanation:

Business Type column setting for customer size → Table

The rule must work in a canvas app. Business rules that need to apply regardless of the app or
form should use the Table scope, allowing the logic to be enforced at the Dataverse table level.

Account rating re-evaluation → Specific form

The requirement states:

"when the account goes on credit hold for this app only"

Since the rule should apply only to a particular model-driven app form and not everywhere the
table is used, configure the business rule for a Specific form.

Discussion: https://www.examtopics.com/discussions/microsoft/view/79989-exam-pl-200-topic-
2-question-28-discussion/

---

## [Página 107](PL-200%20Q%26A.pdf#page=107) · texto nativo

092 Question.
A company uses a Microsoft Power Platform environment.

The company plans to implement a Power Apps app. The application must meet the following
requirements:

        •   Audit all user activity and only retain the audit logs for one year.
        •   Annually remove products that were created over a year ago.


You need to configure the automated processes.

What should you configure? To answer, drag the appropriate configurations to the correct
requirements. Each configuration may be used once, more than once, or not at all. You may need
to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

---

## [Página 108](PL-200%20Q%26A.pdf#page=108) · texto nativo

Audit log retention → Environment auditing

       Environment-level auditing enables tracking of user activity and manages audit log
retention settings, including keeping audit data for a specified period such as one year.

Product removal → Bulk deletion job

      A Bulk Deletion Job can be scheduled to automatically delete records that meet criteria,
such as products created more than one year ago.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96878-exam-pl-200-topic-
2-question-29-discussion/

093 Question.
A company creates a canvas app.

The app requires users to enter their social security number. The app should only display the last
four digits when the user tabs to a different column.

You need to configure the app.

Which option should you use?

    A.  Business rule
    B. Business process flow
   C. Power BI DAX
   D. Power Fx
Answer
   Correct Answer: D

   Explanation:

In a canvas app, UI behavior and data formatting are implemented using Power Fx formulas.

To display only the last four digits of a Social Security Number after the user leaves the field (for
example, in the control's display logic), you would use a Power Fx expression such as:

        "***-**-" & Right(txtSSN.Text, 4)

Discussion: https://www.examtopics.com/discussions/microsoft/view/96692-exam-pl-200-topic-
2-question-30-discussion/

094 Question.
A company uses Power Apps.

---

## [Página 109](PL-200%20Q%26A.pdf#page=109) · texto nativo

The company plans to create a canvas app that uses a responsive design.

You need to configure the app.

Which two actions should you perform? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

    A.  Disable the Scale to fit setting.
    B.  Configure the height and width properties by using drag handles.
   C. Enable the lock orientation setting.
   D. Configure the height and width properties by using a formula.
Answer
   Correct Answer: A,D

   Explanation:

For a responsive canvas app, Microsoft recommends:

    1.  Disable the Scale to fit setting
       •   This allows the app to adapt dynamically to different screen sizes instead of scaling a
            fixed-size layout.
    2.  Configure the height and width properties by using formulas
       •  Responsive apps use formulas such as Parent.Width, Parent.Height, App.Width, and
          App.Height to automatically resize controls based on the available screen space.

Why the others are incorrect

B. Configure the height and width properties by using drag handles

       •  Drag handles create fixed dimensions and do not support responsive behavior.

C. Enable the lock orientation setting

       •  Locking the orientation restricts responsiveness across device orientations and is
           generally not used for responsive designs.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96694-exam-pl-200-topic-
2-question-31-discussion/

095 Question.
A company uses model-driven apps.

Users in the sales department enter the first name, last name, and phone number of customers in
the app. The users request a single screen in the app to enter the customer data.

---

## [Página 110](PL-200%20Q%26A.pdf#page=110) · texto nativo

You need to configure the app.

What should you do?

    A.  Create a Power Automate flow.
    B. Use a Power Virtual Agents app.
   C. Create a canvas app.
   D. Modify the site map.
Answer
   Correct Answer: C

   Explanation:

The requirement is to provide users with a single screen for entering customer data (first name,
last name, and phone number).

A canvas app is ideal when you need:

    •  A customized user experience
    •  A single-screen data entry interface
    •  Complete control over the layout and user interaction

  Why the other options are incorrect

    •  Create a Power Automate flow
         o  Power Automate automates processes; it does not provide a data entry screen.
    •  Use a Power Virtual Agents app
         o  Power Virtual Agents (Copilot Studio) is used for chatbots, not for creating data
               entry forms.
    •  Modify the site map
         o  The site map controls navigation in a model-driven app and does not create a
            custom single-screen interface.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96695-exam-pl-200-topic-
2-question-32-discussion/

096 Question.
You create a Power Apps app for Microsoft Teams using Microsoft Dataverse for Teams.

Users report that they are unable to view the app in Teams.

You need to ensure that users can access the app.

What should you do?

    A.  Share the app with a security group by using the Maker portal.

---

## [Página 111](PL-200%20Q%26A.pdf#page=111) · texto nativo

B.  Publish the app by using the Maker portal.
   C. Request that a tenant administrator pin the app to the app bar in Teams.
   D. Share the app with a security group in Teams.
    E.  Share the app with individual users by using the Maker portal.
Answer
   Correct Answer: E

   Explanation:

For a Power Apps app built in Microsoft Teams using Dataverse for Teams, users cannot access
the app until it is explicitly shared with them.

The app creator must:

    1. Open the app in the Power Apps Maker portal.
    2.  Select Share.
    3.  Share the app with the required users (or groups, if supported).
    4.  Ensure users have permissions to the underlying Dataverse for Teams tables.

  Why the other options are incorrect

       •  Share the app with a security group by using the Maker portal
           o  Dataverse for Teams apps are typically shared directly with users or Teams
               members; this is not the expected answer for this scenario.
       •  Publish the app by using the Maker portal
           o  Publishing makes the latest version available but does not grant users access.
       •  Request that a tenant administrator pin the app to the app bar in Teams
           o  Pinning improves visibility but does not grant permissions.
       •  Share the app with a security group in Teams
           o  Apps are shared through Power Apps, not by sharing a Teams security group.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96696-exam-pl-200-topic-
2-question-33-discussion/

097 Question.
You create a canvas app.

The app requires access to data that is stored in collections. The app must provide the following
actions:

    •  Create a new collection variable.
    •  Remove table values from a collection.

You need to configure functions for the app.

---

## [Página 112](PL-200%20Q%26A.pdf#page=112) · texto nativo

Which functions should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 113](PL-200%20Q%26A.pdf#page=113) · texto nativo

Explanation:

•  Create a new collection variable

   Use Collect() to create a collection and add records to it.

       Collect(MyCollection, {Name:"Item1"})

•  Remove table values from a collection

   Use Clear() to remove all records from a collection while keeping the collection itself.

       Clear(MyCollection)

•  Why the others are incorrect

      o  Set → Creates/updates a global variable, not a collection.

      o  Select → Triggers the OnSelect behavior of a control.

      o  AddColumns → Adds calculated columns to a table.

      o  Reset → Resets a control to its default value.

      o  Revert → Discards changes to a data source.

      o  DropColumns → Removes columns from a table, not records from a collection.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96697-exam-pl-200-topic-
2-question-34-discussion/

---

## [Página 114](PL-200%20Q%26A.pdf#page=114) · texto nativo

098 Question.
A company creates a canvas app.

The company plans to make the app available in Microsoft Teams. Only employees will be allowed
to use the app.

You need to add the app to Teams.

Which three actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.





Answer
   Correct Answer:





   Explanation:

To make a canvas app available in Microsoft Teams:

        1. Open the Power Apps Maker portal.
        2.  Select the canvas app you want to publish to Teams.
        3. Use Add to Teams to generate and publish the Teams app package

Discussion: https://www.examtopics.com/discussions/microsoft/view/112576-exam-pl-200-
topic-2-question-35-discussion/

099 Question.
A company creates a Microsoft Teams app that stores data in two tables in a Microsoft Dataverse
for Teams environment.

---

## [Página 115](PL-200%20Q%26A.pdf#page=115) · texto nativo

Users require access to the app and the app data.

You need to configure access.

What should you do? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

   Access to the data → Create a security role and assign permissions by table.

    •   In Dataverse for Teams, access to table data is controlled through security roles and
       table permissions.

   Access to the app → Share with users.

    •  Users must be granted access to the Teams app itself.

---

## [Página 116](PL-200%20Q%26A.pdf#page=116) · texto nativo

Why the other options are incorrect

    •  Assign a permission set for each table in the app
         o  Permission sets are associated with Power Pages, not Dataverse for Teams apps.
    •  Share the data and assign permissions
         o  Data access is managed through security roles and table permissions.
    •  Share with a security group
         o  Possible in some Power Apps scenarios, but for a Teams app the expected method
                  is sharing the app with users.
    •  Publish the app to a Teams channel
         o  Publishing makes the app available in Teams but does not grant users app or data
              permissions.

Discussion: https://www.examtopics.com/discussions/microsoft/view/112577-exam-pl-200-
topic-2-question-36-discussion/

100 Question.
A company plans to implement Power Pages.

The company requests that you create demonstration sites based on the following requirements:

    •  A website that supports automated scheduling
    •  A website that supports event registration
    •  A website that can be extended by using the company’s branding


In addition, custom development work must be minimized.

You need to identify the appropriate Power Pages templates to use.

Which templates should you use? To answer, drag the appropriate templates to the correct
requirements. Each template may be used once, more than once, or not at all. You may need to
drag the split between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

---

## [Página 117](PL-200%20Q%26A.pdf#page=117) · texto nativo

Answer
   Correct Answer:





   Explanation:

    •   After school program includes scheduling and registration scenarios, making it the best fit
        for automated scheduling.
    •   Building permit includes forms and registration processes, making it suitable for event
       registration with minimal customization.
    •  Blank page provides a customizable starting point and is the best option when the primary
       requirement is to apply the company's own branding and design.

Discussion: https://www.examtopics.com/discussions/microsoft/view/112656-exam-pl-200-
topic-2-question-37-discussion/

101 Question.
You are modifying a model-driven app. You set up a customer table in Microsoft Power Platform to
retrieve user data.

You set up a form with the following columns for users to enter their data. The form includes the
following columns:





The form must do the following:


    •  The Country/region column must automatically populate with US when English is chosen
      as a language. If the user selects Other for this column, the column must remain blank so
        that user can enter a value.

---

## [Página 118](PL-200%20Q%26A.pdf#page=118) · texto nativo

•  The Passport expiration date column must appear only if the user selects Yes in the
       Passport ownership column.

You need to configure the app with the least amount of effort.

What should you configure? To answer, drag the appropriate solution component to the correct
requirements. Each solution component may be used once, more than once, or not at all. You may
need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





.
Answer
   Correct Answer:





   Explanation:

Both requirements can be implemented with a Business Rule, which is the least-effort solution in
a model-driven app:

Country/region → Business Rule

A Business Rule can:

    •  Check the selected language.
    •   Set Country/region = US when English is selected.
    •  Leave the field editable/blank when "Other" is selected.

Passport expiration date column appears → Business Rule

A Business Rule can:

---

## [Página 119](PL-200%20Q%26A.pdf#page=119) · texto nativo

•   Evaluate the Passport ownership Yes/No field.
    •  Show the Passport expiration date field when the value is Yes.
    •  Hide it when the value is No.

Why not the others?

    •  Power Automate flow → Used for process automation, not real-time form behavior.
    •  Business process flow → Guides users through stages; does not dynamically set field
       values or visibility.
    •  Formula → Not required here because Business Rules provide the functionality with less
         effort.

Discussion: https://www.examtopics.com/discussions/microsoft/view/112062-exam-pl-200-
topic-2-question-38-discussion/

102 Question.
Bo You have a canvas app.

The canvas app must store data in a variable that is available only to the current screen.

You need to create the variable.

Which two functions should you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

    A. UpdateContext
    B.  Navigate
   C. SaveData
   D. Set
    E.  Collect
Answer
   Correct Answer: A,B

   Explanation:

The requirement is for a variable that is available only to the current screen.

In Power Apps, context variables are screen-scoped variables and can be created in two ways:

    •   A. UpdateContext

Creates or updates a context variable for the current screen.

       UpdateContext({MyVar:"Value"})

    •   B. Navigate

---

## [Página 120](PL-200%20Q%26A.pdf#page=120) · texto nativo

Can create/update a context variable when navigating to another screen.

       Navigate(Screen2, None, {MyVar:"Value"})

Why the others are incorrect

   C. SaveData :Stores data locally for offline use, not a screen-scoped variable.

   D. Set: Creates a global variable available throughout the app.

    E. Collect: Creates or modifies a collection, not a screen-scoped variable.

Discussion: https://www.examtopics.com/discussions/microsoft/view/112370-exam-pl-200-
topic-2-question-39-discussion/

103 Question.
You plan to create a canvas app with multiple screens.

The app needs to store temporary data while the app is running. The app has the following data
requirements:

    •  Each screen must maintain a separate copy of data and pass the data to another screen.
    •  The app must be able to update separate rows of a table independently.


You need to configure variables for the data.

Which variable types should you use? To answer, drag the appropriate variable types to the correct
requirements. Each variable type may be used once, more than once, or not at all. You may need to
drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 121](PL-200%20Q%26A.pdf#page=121) · texto nativo

Explanation:

   Screens maintain separate data and pass the data to another screen

   Use a Context variable.

       •  Context variables are scoped to a screen.
       •  They can be passed between screens using the Navigate() function.
       •  They are ideal for temporary data specific to a screen.

   Update separate rows of a table independently

   Use a Collection.

       •   Collections can store multiple records (rows).
       •  Each row can be added, updated, or removed independently.
       •   Collections are commonly used as in-memory tables in canvas apps.

  Why not Global Variable?

       •  A Global variable stores a single value or record and is available throughout the app.
       •    It is not the best choice for maintaining independent table rows.

Discussion: https://www.examtopics.com/discussions/microsoft/view/112652-exam-pl-200-
topic-2-question-40-discussion/

104 Question.
You plan to create a canvas app.

The app must meet the following requirements:

    •  Send an email after a record is saved.
    •   Display the expiration column on a form if the creation date of the record is older than 90
       days.

You need to configure the app.

Which features should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 122](PL-200%20Q%26A.pdf#page=122) · texto nativo

Answer
   Correct Answer:





   Explanation:

Send an email → Power Automate flow

   To send an email after a record is saved, use a Power Automate flow. Power Automate is
   designed for workflow automation and can be triggered when a record is created or updated.

Display the expiration column → Formula

   To show or hide a field based on whether the creation date is older than 90 days, use a Power
   Fx formula on the field's Visible property.

   Example logic:

       DateDiff(CreationDate, Today()) > 90

Discussion: https://www.examtopics.com/discussions/microsoft/view/125068-exam-pl-200-
topic-2-question-41-discussion/

---

## [Página 123](PL-200%20Q%26A.pdf#page=123) · texto nativo

105 Question.
A company plans to create two Microsoft Power Platform applications.

One of the applications requires a custom control layout without using code. The other application
will be used primarily by external users.

You need to create the applications.

Which application types should you use? To answer, drag the appropriate application types to the
correct requirements. Each application type may be used once, more than once, or not at all. You
may need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





                                                                                                                                                 .
Answer
   Correct Answer:





   Explanation:

Custom control layout without coding → Canvas app

   A Canvas app provides complete control over the user interface through a drag-and-drop
    designer and Power Fx formulas, allowing highly customized layouts without traditional coding.

---

## [Página 124](PL-200%20Q%26A.pdf#page=124) · texto nativo

Used by external users → Power Pages portal

   Power Pages (formerly Power Apps Portal) is designed for external users such as customers,
    partners, and vendors, providing secure web access to Dataverse data.

Discussion: https://www.examtopics.com/discussions/microsoft/view/125069-exam-pl-200-
topic-2-question-42-discussion/

106 Question.
You create a Power Apps app.

The app must be able to display a list of records that are sorted by category. The app must also
expand or hide the list by subtopics.

You need to configure the app.

Which tool should you use?

    A.  card
    B.  expression
   C.  gallery
   D. Power BI dashboard
Answer
   Correct Answer: C

   Explanation:

   A Gallery control in a Canvas App is designed to:

        •   Display a list of records.
        •   Sort and filter records.
        •  Show grouped or categorized information.
        •  Support expandable/collapsible layouts (for example, categories and subtopics).

    This makes it the best choice for displaying records sorted by category and allowing users to
   expand or hide subtopics.

  Why the other options are incorrect

    •   A. Card: A card displays a single field or record within a form, not a list of records.

    •   B. Expression: Expressions (Power Fx formulas) define behavior and calculations but are
       not UI controls.

    •  D. Power BI dashboard : Power BI dashboards are for analytics and reporting, not
        interactive record lists within a Power Apps app.

---

## [Página 125](PL-200%20Q%26A.pdf#page=125) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/133850-exam-pl-200-
topic-2-question-43-discussion/

107 Question.
A company is implementing Power Apps and Power Automate.

Several components are created within Power Apps, Microsoft Dataverse, and Power Automate.
These components must be promoted from the development environment to the user acceptance
test environment in a single solution package.

You need to create the solution package for promotion.

Where should you create the package?

    A.  Azure portal
    B.  Microsoft Power Platform admin center
   C. Office 365 admin center
   D. Power Apps maker portal
Answer
   Correct Answer: D

   Explanation:

   To move Power Apps, Dataverse components, and Power Automate flows together between
   environments, you must create a Solution in the Power Apps maker portal.

   Process:

    1. Open the Power Apps maker portal.
    2.  Create a Solution.
    3. Add the app, Dataverse tables, flows, and other components.
    4.  Export the solution (Managed or Unmanaged).
    5.  Import it into the UAT environment.

  Why the others are incorrect

    A. Azure portal: Azure Portal does not create Power Platform solution packages.
    B.  Microsoft Power Platform admin center: Used for environment administration, not
       solution authoring.
   C. Office 365 admin center: Used for Microsoft 365 tenant administration.

Discussion: https://www.examtopics.com/discussions/microsoft/view/144564-exam-pl-200-
topic-2-question-49-discussion/

---

## [Página 126](PL-200%20Q%26A.pdf#page=126) · texto nativo

108 Question.
You are building a model-driven app for a company.

You identify several custom commands that the app must support, including the following
commands:


        •  Save a row.
        •  Move the user to a different row in the application.
        •   Navigate the user to an external webpage.
        •  Show a notification that the user can accept or decline.


You need to identify the formula to use for each requirement.

Which formulas should you identify? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 127](PL-200%20Q%26A.pdf#page=127) · texto nativo

Answer
   Correct Answer:

---

## [Página 128](PL-200%20Q%26A.pdf#page=128) · texto nativo

Explanation:

        •  SubmitForm() – Saves the current form record to the data source.
        •   Navigate() – Moves the user to another screen/page/record within the app.
        •  Launch() – Opens an external URL, website, email, or document.
        •   Confirm() – Displays a confirmation dialog with options such as Accept/Cancel or
          Yes/No.

Discussion: https://www.examtopics.com/discussions/microsoft/view/145199-exam-pl-200-
topic-2-question-50-discussion/

109 Question.
You are building a model-driven app. The environment has Advanced settings enabled.

A form in the app requires a custom interface.

---

## [Página 129](PL-200%20Q%26A.pdf#page=129) · texto nativo

You need to embed the custom interface onto the form without using custom code.

What should you do?

    A.  Modify the model-driven app to use mobile form factor.
    B.  Modify the model-driven app to use tablet form factor.
   C. Create an HTML web resource.
   D. Use the classic experience to add a canvas app.
Answer
   Correct Answer: D

   Explanation:

   The requirement is to:

    •  Embed a custom interface into a model-driven app form.
    •  Do so without using custom code.

   A canvas app embedded in a model-driven form provides a highly customized user
   experience without requiring custom development. In environments with Advanced settings
   enabled, this is configured from the form editor (historically through the classic experience).

    •  Why not the others?

    •   A. Modify the model-driven app to use mobile form factor

         o  Changes the layout for phones but does not embed a custom interface.

    •   B. Modify the model-driven app to use tablet form factor

         o  Changes the layout for tablets but does not provide a custom interface.

    •  C. Create an HTML web resource

         o  Requires custom HTML/JavaScript code, which violates the requirement of without
             using custom code.

   Exam Tip

   When you see:

        •  Custom interface
        •  Model-driven app
        •  No custom code

   The expected answer is typically embedded Canvas App.

Discussion: https://www.examtopics.com/discussions/microsoft/view/316449-exam-pl-200-
topic-2-question-57-discussion/

---

## [Página 130](PL-200%20Q%26A.pdf#page=130) · texto nativo

110 Question.
A company uses model-driven apps.

Users in the sales department enter the first name, last name, and phone number of customers in
the app. The users request a single screen in the app to enter the customer data.

You need to configure the app.

What should you do?

    A.  Create a Power Automate flow.
    B. Use Copilot Studio.
   C. Create a canvas app.
   D. Modify the site map.
Answer
   Correct Answer: C

   Explanation:

   The requirement is:

   "Users request a single screen in the app to enter the customer data."

   A canvas app is the best choice when you need a highly customized data-entry experience on a
    single screen. It allows you to design a streamlined interface containing only the fields users
   need (First Name, Last Name, Phone Number).

  Why not the others?

    •   A. Create a Power Automate flow

         o  Flows automate processes; they do not provide a data-entry screen.

    •   B. Use Copilot Studio

         o  Copilot Studio is used to create conversational agents, not data-entry forms.

    •  D. Modify the site map

         o  The site map controls navigation in a model-driven app and does not create a
               single-screen data-entry experience.

   Exam Tip

   When a question mentions:

    •   Single screen
    •  Custom data entry experience
    •   Simplified user interface

---

## [Página 131](PL-200%20Q%26A.pdf#page=131) · texto nativo

The expected answer is usually Canvas App

Discussion: https://www.examtopics.com/discussions/microsoft/view/326390-exam-pl-200-
topic-2-question-59-discussion/

111 Question.
A company is implementing advanced features for a Power Pages website.

The company hosts documents and lists in several SharePoint environments that are hosted both
on-premises and online. Users of the Power Pages site must be able to view, search for, and filter
this data from a single, intuitive experience.

You need to determine which advanced feature to implement.

What should you implement?

    A.  Virtual tables
    B.  SharePoint Server integration
   C. Power BI embedded
   D. Progressive search
Answer
   Correct Answer: D

   Explanation:

   The requirement is:

    •  Documents and lists exist in multiple SharePoint environments.
    •  Some SharePoint environments are on-premises and some are online.
    •  Users must be able to view, search, and filter information through a single experience in
      Power Pages.

   Progressive search is an advanced Power Pages feature that enables users to search across
    multiple data sources and refine/filter results through a unified interface.

  Why not the others?

    •   A. Virtual tables

         o  Expose external data in Dataverse but do not provide the unified search and filtering
              experience described.

    •   B. SharePoint Server integration

         o   Integrates documents with SharePoint, but it does not provide a consolidated
             search experience across multiple SharePoint environments.

---

## [Página 132](PL-200%20Q%26A.pdf#page=132) · texto nativo

•  C. Power BI embedded

         o  Used for analytics and reporting, not for searching and filtering documents and lists

Discussion: https://www.examtopics.com/discussions/microsoft/view/315255-exam-pl-200-
topic-2-question-60-discussion/

112 Question.
You are implementing a model-driven app for a company.

The company requires the following implementation for the app:

    •  When a user selects a button, a side pane must open that allows the user to upload
      documents.
    •  Documents that are uploaded must be stored within the external document management
       solution configured for the environment.
    •  Use of custom code must be avoided.


You need to implement the requirements.

Which four actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.

---

## [Página 133](PL-200%20Q%26A.pdf#page=133) · texto nativo

Answer
   Correct Answer:





   Explanation:

   The requirements point to using a Custom Page inside a model-driven app:

    •  A side pane can host a custom page.
    •  The custom page is built using the canvas-app experience, without custom code.
    •  Documents must be stored in the external document management system (SharePoint
       Online).
    •   After configuring the page and app, publish the changes.

   Correct sequence

         1.  Connect to SharePoint Online
         2. Add a new custom page
         3.  Use the modern app designer
         4.  Publish changes

Discussion: https://www.examtopics.com/discussions/microsoft/view/315457-exam-pl-200-
topic-2-question-61-discussion/

113 Question.
You are building a model-driven app. The environment has Advanced settings enabled.

---

## [Página 134](PL-200%20Q%26A.pdf#page=134) · texto nativo

A form in the app requires a custom interface.

You need to embed the custom interface onto the form without using custom code.

What should you do?

    A.  Modify the model-driven app to use mobile form factor.
    B.  Modify the model-driven app to use tablet form factor.
   C. Use an IFRAME.
   D. Use the classic experience to add a canvas app.
Answer
   Correct Answer: D

   Explanation:

   The requirement is to:

        •  Embed a custom interface on a model-driven app form.
        •   Avoid custom code.

   An embedded canvas app allows you to create a custom user experience and place it directly
   on a model-driven form without writing code.

  Why not the other options?

    A. Modify the model-driven app to use mobile form factor

         o  Only changes the form layout for phones; it does not provide a custom interface.

    B. Modify the model-driven app to use tablet form factor

         o  Only changes the layout for tablets; it does not embed a custom interface.

   C. Use an IFRAME

         o   Typically requires hosting external content and is considered a custom integration
             approach. It is not the no-code method expected for this scenario.

   Exam tip

   For PL-200/PL-400 style questions, when you see:

        •   Model-driven app
        •  Custom interface
        •  Without custom code

    the correct answer is usually an embedded Canvas App.

Discussion: https://www.examtopics.com/discussions/microsoft/view/316450-exam-pl-200-
topic-2-question-62-discussion/

---

## [Página 135](PL-200%20Q%26A.pdf#page=135) · texto nativo

114 Question.
A company is implementing advanced features for a Power Pages website.

The company hosts documents and lists in several SharePoint environments that are hosted both
on-premises and online. Users of the Power Pages site must be able to view, search for, and filter
this data from a single, intuitive experience.

You need to determine which advanced feature to implement.

What should you implement?

    A.  Faceted search
    B. Content delivery network
   C. Power BI embedded
   D. Progressive search
Answer
   Correct Answer: D

   Explanation:

   The key requirement is:

   Users must be able to view, search, and filter documents and lists that are stored across
   multiple SharePoint environments (both on-premises and online) from a single, intuitive
   experience.

   Progressive search is a Power Pages capability that provides a unified search experience
   across different data sources and allows users to refine and filter search results.

  Why not the others?

    A. Faceted search

         o  Faceted search helps users filter search results, but it does not address the
             requirement to aggregate and search across multiple SharePoint repositories from
            a single experience.

    B. Content delivery network (CDN)

         o  A CDN improves performance for static content delivery and has nothing to do with
              searching documents and lists.

   C. Power BI embedded

         o  Power BI Embedded is used for analytics and reporting, not document discovery,
              search, and filtering.

---

## [Página 136](PL-200%20Q%26A.pdf#page=136) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/315458-exam-pl-200-
topic-2-question-63-discussion/

115 Question.
Body You are building a model-driven app. The environment has Advanced settings enabled.

A form in the app requires a custom interface.

You need to embed the custom interface onto the form without using custom code.

What should you do?

    A.  Create a canvas app and bind its properties to the form.
    B.  Create an HTML web resource.
   C. Create a quick view form.
   D. Create a canvas app and add it to a solution.
Answer
   Correct Answer: A

   Explanation:

   The requirement is to:

        •   Provide a custom interface on a model-driven app form.
        •   Avoid using custom code.
        •  The environment has Advanced settings enabled.

   An embedded canvas app is the recommended no-code/low-code approach for adding a
   custom UI to a model-driven form. The canvas app can be embedded in the form and its
    properties can be bound to fields from the current record.

  Why not the others?

    B. Create an HTML web resource

         o  Requires custom HTML/JavaScript, which violates the requirement to avoid custom
             code.

   C. Create a quick view form

         o  Quick view forms display related data but do not provide a custom interface.

   D. Create a canvas app and add it to a solution

         o  Adding a canvas app to a solution does not embed it on the form. The key
             requirement is to embed and bind it to the form record.

---

## [Página 137](PL-200%20Q%26A.pdf#page=137) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/315459-exam-pl-200-
topic-2-question-64-discussion/

116 Question.
You are customizing a model-driven app view that is used to manage contract approvals by using
Power Fx.

A custom command button must appear only when:

        •  One or more records are selected in the grid view.
        •    All selected records have a RecordStatus field value of Ready.

You need to configure the command to meet the business requirements.

Which Power Fx expressions should you use? To answer, select the appropriate options in the
answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 138](PL-200%20Q%26A.pdf#page=138) · texto nativo

Explanation:

   For a command button that should only be visible when:

         1.  At least one record is selected
         2.  All selected records have RecordStatus = "Ready"

    the correct Power Fx expressions are:

   At least one record is selected

       CountRows(Self.Selected.AllItems) > 0

   Why?

        •   Returns true when one or more records are selected.
        •   CountRows(...) = 1 would only allow exactly one record.
        •   !IsBlank(Self.Selected.AllItems) is not the recommended way to test for selected rows.

    All selected records have a value of Ready

       CountIf(Self.Selected.AllItems, RecordStatus <> "Ready") = 0

   Why?

        •  Counts records that are not Ready.
        •    If the count is 0, then every selected record is Ready.
        •   Self.RecordStatus = "Ready" only checks a single record.
        •   ForAll(...) is not appropriate because ForAll returns a table, not a single Boolean value
           suitable for command visibility.

Discussion: https://www.examtopics.com/discussions/microsoft/view/394312-exam-pl-200-
topic-2-question-68-discussion/

117 Question.
You plan to create user interface (UI) flows to automate several web-based business processes
that you currently perform manually.
You need to ensure that users can create and run web UI flows.
Which three components must you install and configure on user's devices? Each correct answer
presents part of the solution.
NOTE: Each correct selection is worth one point.

    A. Power Automate Desktop
    B.  Latest version of Microsoft Edge
   C. On-premises data gateway
   D. Selenium IDE
    E.  Latest version of Mozilla Firefox

---

## [Página 139](PL-200%20Q%26A.pdf#page=139) · texto nativo

Answer
   Correct Answer: A,B,D

   Explanation:

   To create and run web UI flows (legacy Power Automate UI flows/web automation), users
   need:

    A. Power Automate Desktop

        •  Required to create, record, edit, and run UI flows.

    B. Latest version of Microsoft Edge

        •  Supported browser for web automation and recording.

   D. Selenium IDE

        •  Used by UI flows for web recording and playback capabilities.

  Why not the others?

   C. On-premises data gateway

        •  Used to access on-premises data sources from cloud services.
        •  Not required to create or run web UI flows.

    E. Latest version of Mozilla Firefox

        •  Not a required component for Power Automate web UI flow

Discussion: https://www.examtopics.com/discussions/microsoft/view/60320-exam-pl-200-topic-
3-question-1-discussion/

118 Question.
You are designing a desktop user interface (UI) flow.
The UI flow automates legacy software.
You need to prepare data for transfer to Microsoft SharePoint list.
Which four actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.

---

## [Página 140](PL-200%20Q%26A.pdf#page=140) · texto nativo

Select and Place:





Answer
   Correct Answer:





   Explanation:

   For a desktop UI flow, to extract information from a legacy application and make it available
    for use later (for example, to create SharePoint list items), you first define an output.

   The correct sequence is:

        1.  Start recording the UI flow
        2. On the Outputs menu of the UI flow, choose Select text on screen
        3.  Select information to pass to the SharePoint list
        4.  Enter a name and description for the output

---

## [Página 141](PL-200%20Q%26A.pdf#page=141) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/43262-exam-pl-200-topic-
3-question-2-discussion/

119 Question.
You have a business process flow.
You need to update the business process flow while minimizing administrative and maintenance
efforts.
What should you implement? To answer, drag the appropriate features to the correct
requirements. Each feature may be used once, more than once, or not at all.
You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





Answer
   Correct Answer:





   Explanation:

        •   Classic workflow
         Use this when you need to control business process flow stage navigation, including
         moving users back to a previous stage under specific conditions.
        •  Action step
         Use an action step in a business process flow when users need to manually trigger an
           action from a specific stage, such as creating checklist records on demand.

---

## [Página 142](PL-200%20Q%26A.pdf#page=142) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/41577-exam-pl-200-topic-
3-question-3-discussion/

120 Question.
You are creating a new business process flow to qualify leads.
You create an action. The action is not available inside the Action Step.
You need to make the action available to the Action Step.
Which two steps must you perform? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

    A.  Ensure that the entity for the action matches the corresponding entity for the business
       process flow stage.
    B. Add at least one step to the action.
   C. Select Run as an on-demand process.
   D.  Activate the action.
Answer
   Correct Answer: A,D

   Explanation:

   To make an action available in a Business Process Flow Action Step, you must:

    A. Ensure that the entity for the action matches the corresponding entity for the business
   process flow stage.

   D. Activate the action.

   Why?

   An Action Step in a Business Process Flow can only use actions that:

        •   Are associated with the same table/entity as the stage.
        •   Are activated.

  Why not the others?

    B. Add at least one step to the action

        •  An action does not need a workflow step to appear in the Action Step list.

   C. Select Run as an on-demand process

        •   This setting applies to classic workflows, not actions.

Discussion: https://www.examtopics.com/discussions/microsoft/view/41351-exam-pl-200-topic-
3-question-4-discussion/

---

## [Página 143](PL-200%20Q%26A.pdf#page=143) · texto nativo

121 Question.
You plan to automate several different processes by using Power Automate.
Each process has unique characteristics.
You need to recommend components for each process.
Which components should you recommend? To answer, drag the appropriate components to the
correct processes. Each component may be used once, more than once, or not at all. You may
need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





Answer
   Correct Answer:





   Explanation:

    1. Internally created web application with REST API → Flow that uses a custom connector

        •  The application exposes a REST API.
        •    If there is no existing Power Automate connector, the recommended approach is to
           create a custom connector and use it from a cloud flow.
        •   This is more reliable and maintainable than UI automation.

    2. Public website with no API functionality → Unattended UI flow

        •  No API is available.
        •  The process is triggered from an unmonitored queue, so no user will be present to
            interact with the UI.
        •   Therefore, robotic process automation (RPA) must run without human intervention.

---

## [Página 144](PL-200%20Q%26A.pdf#page=144) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/41579-exam-pl-200-topic-
3-question-5-discussion/

122 Question.
You create workflows to automate business processes.
You need to create a workflow that automatically sends emails based on a mail merge template.
The workflow must contain the following configurations:

        •  Run immediately.
        •   Validate when a condition is met.
        •  Perform an action when a condition is met.

To answer, select the appropriate configuration in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 145](PL-200%20Q%26A.pdf#page=145) · texto nativo

Explanation:

        •  Configure the workflow to run now → Executes the workflow immediately.
        •  Subject contains data → Example of a conditional check/validation within the
          workflow.
        •  Send an email → The action that sends the email (which can use an email template).

Discussion: https://www.examtopics.com/discussions/microsoft/view/60006-exam-pl-200-topic-
3-question-6-discussion/

123 Question.
You are developing a canvas app.
You need to apply business rules to the app without writing code.
Which three actions can you use? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.

    A.  Validate data and show error messages.
    B. Enable or disable fields.
   C. Set field requirement levels.
   D. Set field values.
    E. Show or hide fields

---

## [Página 146](PL-200%20Q%26A.pdf#page=146) · texto nativo

Answer
   Correct Answer: B,D,E

   Explanation:

    In Power Apps, Business Rules can be used to apply logic without writing code. Supported
    actions include:

    B. Enable or disable fields
   D. Set field values
    E. Show or hide fields

  Why not the others?

    A. Validate data and show error messages

        •  Business Rules can validate data in model-driven apps, but this capability is not
          supported in canvas apps in the same way.

   C. Set field requirement levels

        •   Setting a column's required level is a Dataverse/model-driven app capability and isn't
          supported as a Business Rule action in canvas apps.

Discussion: https://www.examtopics.com/discussions/microsoft/view/61021-exam-pl-200-topic-
3-question-7-discussion/

124 Question.
A company plans to use Power Automate to increase employee efficiency.
You need to recommend the types of flows that the company should use.
Which flow type should you recommend? To answer, drag the appropriate flow types to the correct
tasks. Each flow type may be used once, more than once, or not at all. You may need to drag the
split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Hot Area:

---

## [Página 147](PL-200%20Q%26A.pdf#page=147) · texto nativo

Answer
   Correct Answer:





   Explanation:

   The correct mappings are:

    1. Perform repetitive actions in an existing application that does not have an API →
   Desktop flow

   Why?

---

## [Página 148](PL-200%20Q%26A.pdf#page=148) · texto nativo

•  Desktop flows (RPA) automate interactions with legacy applications and systems that
         do not expose APIs.

2. Send an email to a contact on their birthday → Scheduled flow

   Why?

        •  A scheduled flow runs at defined intervals (for example, daily) and can check whether
          today matches a contact's birthday, then send the email automatically.

Discussion: https://www.examtopics.com/discussions/microsoft/view/82598-exam-pl-200-topic-
3-question-8-discussion/

125 Question.
A company is creating a business process flow in Power Automate to analyze the probability that a
customer will buy a specific product.
The company uses ratings from zero to one hundred. The company assigns likelihoods based on
the following table:





You need to define the business process steps. All logic must be included in a single evaluation
statement.
Which step should you use? To answer, drag the appropriate steps to the correct ratings. Each step
may be used once, more than once, or not at all. You may need to drag the split bar between panes
or scroll to view content.
NOTE: Each correct selection is worth one point.

---

## [Página 149](PL-200%20Q%26A.pdf#page=149) · texto nativo

Select and Place:





Answer
   Correct Answer:





   Explanation:

    This question is about Business Process Flow branching logic.

   The requirement states:

    All logic must be included in a single evaluation statement.

    In a Business Process Flow, a Conditional Branch is used to evaluate conditions and create
    different paths. The branches represent the explicit ranges, and the final unmatched path is
   handled by the Default Action

   Why?

   A typical implementation would be:

        1.  Conditional Branch → Rating ≤ 35 → Low

---

## [Página 150](PL-200%20Q%26A.pdf#page=150) · texto nativo

2.  Conditional Branch → Rating ≤ 60 → Medium
        3.  Conditional Branch → Rating ≤ 75 → High
        4.  Default Action → Anything remaining (>75) → Very High

Discussion: https://www.examtopics.com/discussions/microsoft/view/81723-exam-pl-200-topic-
3-question-9-discussion/

126 Question.
You are creating a Power Platform solution.
You need to help end users understand which actions to take next and ensure that user interaction
occurs in manageable steps.
Which actions should you perform? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 151](PL-200%20Q%26A.pdf#page=151) · texto nativo

Explanation:

        •  Business Process Flows (BPFs) are specifically designed to guide users through a
          process and indicate what should be done next.
        •  BPFs break a process into stages, and each stage can contain steps/actions that
          users must complete before moving forward.
        •   Views, charts, timelines, workflows, and insights do not provide the same guided,
          stage-based user experience.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60327-exam-pl-200-topic-
3-question-10-discussion/

127 Question.
You are developing an app.
You must trigger a mobile notification whenever a specific hashtag is posted from Twitter. The
notification will send email to the company's social media teams distribution list.
You need to create a connection to the Twitter service and build a solution.
Which four actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.
Select and Place:





Answer
   Correct Answer:

---

## [Página 152](PL-200%20Q%26A.pdf#page=152) · texto nativo

This is a standard Power Automate Twitter trigger + email action scenario.

   The correct sequence is:

        1.  Sign in to Power Automate and create a new blank flow
        2.  Select the Twitter connector and use the user credentials for the connection
        3.  Create a trigger to search for the new posts with the hashtag
        4.  Create an action to send an email

   Why?

        •  A Power Automate solution starts by creating a flow.
        •  The Twitter connector uses OAuth/user credentials, not a manually generated
           authentication key.
        •  The detection of tweets containing a specific hashtag is the trigger.
        •  Sending the email notification is the action that follows the trigger.


   Explanation:

Discussion: https://www.examtopics.com/discussions/microsoft/view/79717-exam-pl-200-topic-
3-question-11-discussion/

128 Question.
You manage Microsoft Power Platform apps for a company.
You need to hide the Flows button on the user interface.
Which configuration setting should you change?

    A.  the SiteMap
    B.  the Customizations section of System Settings

---

## [Página 153](PL-200%20Q%26A.pdf#page=153) · texto nativo

C. the Entity component of the default solution
   D. the Buttons tab of Flow
Answer
   Correct Answer: B

   Explanation:

    In Dynamics 365 / Power Platform model-driven apps, the Flows button (Power Automate
    integration) can be controlled through:

       Settings → Administration → System Settings → Customization

   There is an option to show or hide the Flow functionality from the user interface.

  Why not the others?

    A. SiteMap

    •   Controls navigation items, not the Flow button displayed on forms and views.

   C. Entity component of the default solution

    •  Used to customize tables/entities and their components, not global Flow visibility.

   D. Buttons tab of Flow

    •  No such configuration exists for hiding the Flow button globally.

Discussion: https://www.examtopics.com/discussions/microsoft/view/62395-exam-pl-200-topic-
3-question-12-discussion/

129 Question.
BYou configure and test a user interface (UI) flow. You plan to run the flow as a scheduled flow.
The UI flow must run on a Windows 10 device. As part of process automation, the UI flow must sign
into the Windows 10 device with the credentials for a user account named User1.
You need to ensure that the flow runs during non-peak hours and requires no physical user
intervention.
What should you do?

    A.  Ensure that the User1 account has an active user session on the device.
    B. Ensure that all user sessions are signed out.
   C. Ensure that there are no active user sessions on the device.
   D. Ensure that all user sessions are signed out except for locked user sessions.
Answer
   Correct Answer: C

   Explanation:

---

## [Página 154](PL-200%20Q%26A.pdf#page=154) · texto nativo

For a scheduled UI flow (unattended RPA):

    •  The flow must run without human intervention.

    •  Power Automate uses the provided credentials (User1) to sign in automatically.

    •  The machine must be available for the automation to establish its own session.

    Therefore, there should be no active user sessions on the device when the unattended UI flow
    starts.

     Why not the others?

    A. Ensure that the User1 account has an active user session on the device.

         o  This is more appropriate for attended automation, not unattended scheduled
              execution.

    B. Ensure that all user sessions are signed out.

         o  Too broad. The recommended condition is specifically that there are no active
              sessions, allowing the unattended flow to create its own session.

   D. Ensure that all user sessions are signed out except for locked user sessions.

         o  Locked sessions can interfere with unattended execution and are not required.

Discussion: https://www.examtopics.com/discussions/microsoft/view/41347-exam-pl-200-topic-
3-question-13-discussion/

130 Question.
A company plans to send escalation emails to all customers with overdue invoices. You are
creating a Microsoft Power Automate flow to determine whether to send an escalation email. The
system must send an alert for all invoices that are seven days or more overdue. You need to
configure the flow. Which expression should you use?

    A.  @GreaterOrEquals(TriggerEmail()?['OverdueDate']: '7')
    B.  'OverdueDate' >= '7'?'TriggerEmail()': false
   C.  TriggerEmail() = 'OverdueDate' >= 7;.
Answer
   Correct Answer: A

   Explanation:

   The requirement is to send an escalation email when an invoice is 7 days or more overdue.

    In Power Automate, the correct way to evaluate this is with the GreaterOrEquals function:

       @GreaterOrEquals(TriggerEmail()?['OverdueDate'], 7)

---

## [Página 155](PL-200%20Q%26A.pdf#page=155) · texto nativo

This returns true when the value of OverdueDate is greater than or equal to 7.

  Why not the others?

   B uses invalid Power Automate expression syntax.

  C is not valid Power Automate expression syntax and performs an assignment rather than a
   comparison.

Discussion: https://www.examtopics.com/discussions/microsoft/view/79991-exam-pl-200-topic-
3-question-14-discussion/

131 Question.
You add a business process flow to the Account table. The flow has three stages.
You need to ensure that a workflow can run when a user completes the final stage.
Which option should you use?

    A.  Start when: Record status changes
    B.  Available to run: Run this workflow in the background
   C. Available to run: As an on-demand process
   D.  Available to run: As a child process


Answer
   Correct Answer: D

   Explanation:

    In a Business Process Flow (BPF), an Action Step can invoke:

        •  A workflow configured as a child process
        •  A custom action

   To run a workflow when the user completes a stage (such as the final stage), the workflow must
   be available to the BPF, which requires it to be configured as a child process.

  Why not the others?

    A. Start when: Record status changes

         o   Triggers based on record status changes, not BPF stage completion.

    B. Available to run: Run this workflow in the background

         o  Controls execution mode, not whether the workflow can be called from a BPF.

   C. Available to run: As an on-demand process

---

## [Página 156](PL-200%20Q%26A.pdf#page=156) · texto nativo

o  Allows manual execution by users, but does not make it available as a BPF child
              workflow.

Discussion: https://www.examtopics.com/discussions/microsoft/view/80316-exam-pl-200-topic-
3-question-15-discussion/

132 Question.
You need to create a Power Automate desktop flow.
What are two possible ways to create the flow? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.

    A. Record mouse and keyboard events.
    B.  Configure a pre-built template.
   C. Use pre-built actions.
   D. Create models by using Microsoft Visio.
Answer
   Correct Answer: A,C

   Explanation:

   Power Automate Desktop flows can be created in two primary ways:

    A. Record mouse and keyboard events

        •  Power Automate Desktop includes a Recorder that captures user interactions such as
        mouse clicks, keyboard input, and UI actions.
        •  The recorded steps are automatically converted into flow actions.

   C. Use pre-built actions

        •  Power Automate Desktop provides hundreds of built-in actions (file operations, web
          automation, Excel, Outlook, loops, conditions, etc.).
        •  You can drag and drop these actions to manually build a desktop flow.

  Why the others are incorrect

    B. Configure a pre-built template

        •   Unlike cloud flows, desktop flows are not created by configuring pre-built templates as
         a primary creation method.

   D. Create models by using Microsoft Visio

        •   Microsoft Visio is not used to create Power Automate Desktop flows

Discussion: https://www.examtopics.com/discussions/microsoft/view/86139-exam-pl-200-topic-
3-question-16-discussion/

---

## [Página 157](PL-200%20Q%26A.pdf#page=157) · texto nativo

133 Question.
You are using Power Automate to create a list of customers from a Microsoft Excel file.
The list must contain customers who meet one of the following criteria:

        •   Sales of less than $500,000.
        •  Customers who are on credit hold.

You need to create a condition to filter the list of customers.
How should you complete the filter condition? To answer, select the appropriate options in the
answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:





   Explanation:

   The requirement is:

    •  Sales < 500,000 OR

    •   Credit Hold = true

    In Power Automate expressions:

        •   less(item()?['sales'], 500000) checks sales less than 500,000.
        •   equals(item()?['credithold'], 'true') checks whether the customer is on credit hold.
        •   Since either condition can be true, use or.

    Therefore, the completed expression is:

   @or(

    less(item()?['sales'], 500000),

---

## [Página 158](PL-200%20Q%26A.pdf#page=158) · texto nativo

equals(item()?['credithold'], 'true')

      )

Discussion: https://www.examtopics.com/discussions/microsoft/view/79811-exam-pl-200-topic-
3-question-17-discussion/

134 Question.
A farm uses a canvas app to manage schedules for planting fields with crop seeds. The farm uses
business intelligence to provide recommendations for schedule changes based on weather data.
You must implement a business rule that changes information for several forms in the canvas app
based on business intelligence data.
You need to configure the business rule.
Which scope should you use?

    A.  Table
    B.  All Forms
   C. Form specific
Answer
   Correct Answer: A

   Explanation:

   Business rules have three possible scopes:

        •   Entity (Table) – applies to all forms, including model-driven apps and data created
          through other methods.
        •   All Forms – applies to all forms of a specific table.
        •   Specific Form – applies only to a selected form.

   The requirement states that the business rule must change information for several forms
   based on business intelligence data. To ensure the rule is applied consistently across the table
   and all its forms, the appropriate scope is Table (Entity).

Discussion: https://www.examtopics.com/discussions/microsoft/view/79812-exam-pl-200-topic-
3-question-18-discussion/

135 Question.
A company uses Power Apps and Power Automate.
There is an issue with the existing flow in the test environment. Development changes are allowed
in the test environment.
You need to troubleshoot the issue with the flow.
Which command should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 159](PL-200%20Q%26A.pdf#page=159) · texto nativo

Hot Area:





Answer
   Correct Answer:





   Explanation:

        •  Remove
                 If a flow is solution-aware and managed by a solution, removing it from the solution
         makes it available for direct modification in the environment.

---

## [Página 160](PL-200%20Q%26A.pdf#page=160) · texto nativo

•  Turn off
        A flow must be turned off before certain edits can be made safely during
           troubleshooting and development.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83287-exam-pl-200-topic-
3-question-19-discussion/

136 Question.
You plan on implementing complex business logic in Microsoft Dataverse tables by using Power
Automate flows.
You realize that the functionality required to implement the business logic is not available in a
Power Automate flow.
The new business logic must work in multiple Dataverse tables. In addition, the operation must
return a value after it finishes and must be able to run from an existing Dataverse action.
You need to recommend the method to implement the missing logic.
What should you recommend?

    A. Bound action
    B. Custom API
   C. Unbound action
   D. Scheduled workflow
Answer
   Correct Answer: B

   Explanation:

   The requirement states:

         1.  The logic is not available in Power Automate.
         2.   It must be reusable across multiple Dataverse tables.
         3.   It must return a value when it finishes.
         4.   It must be callable from an existing Dataverse action.

   A Custom API is specifically designed to extend Dataverse with custom business logic that
   can:

       •  Execute server-side code (plug-ins).
       •  Accept input parameters and return output values.
       •  Be invoked from Power Automate, model-driven apps, JavaScript, and Dataverse
           actions.
       •  Work independently of a specific table (or be associated when needed).

  Why not the others?

---

## [Página 161](PL-200%20Q%26A.pdf#page=161) · texto nativo

•   A. Bound action
      Bound actions are tied to a specific table/row, whereas the requirement is to work across
       multiple tables.

    •  C. Unbound action
       Actions are the older approach. Microsoft recommends Custom APIs for new extensibility
       scenarios because they provide stronger control over parameters, execution, and return
       values.

    •  D. Scheduled workflow
      Workflows do not satisfy the requirement to return a value and are not intended for this type
        of reusable custom business logic.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83453-exam-pl-200-topic-
3-question-20-discussion/

137 Question.
A company plans to automate the following manual processes by using Power Automate.





You need to identify UI flow types for the two business processes.
Which desktop flow type should you use? To answer, drag the appropriate desktop flow types to
the correct business processes. Each desktop flow type may be used once, more than once, or not
at all. You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





Answer
   Correct Answer:

---

## [Página 162](PL-200%20Q%26A.pdf#page=162) · texto nativo

Explanation:

   For Power Automate Desktop:

        •  Attended flow = requires a user session and the machine remains unlocked while the
           flow runs.
        •  Unattended flow = runs automatically without user interaction, typically after hours.

   Process 1 → Attended

   The device must remain unlocked while the process runs, and the user leaves it running while
   doing other work.

   Process 2 → Unattended

   The process must run after normal business hours.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83768-exam-pl-200-topic-
3-question-21-discussion/

138 Question.
You are creating a business process flow for a Power Apps app.

The business process flow must meet the following requirements:

        •  Must be available offline.
        •  Send an email to the team when a record is created.

You need to set up business process flow.

What should you do? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 163](PL-200%20Q%26A.pdf#page=163) · texto nativo

.
Answer
   Correct Answer:





   Explanation:

Make it available offline → Ensure that the business process flow is referencing one table.

   Business Process Flows are available offline only when they reference a single table.

Send an email to the team → Create a step.

   To trigger an action such as sending an email, you add an Action Step to the Business Process
   Flow.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96046-exam-pl-200-topic-
3-question-22-discussion/

139 Question.
A company has a model-driven app.

The app must meet the following requirements:

---

## [Página 164](PL-200%20Q%26A.pdf#page=164) · texto nativo

•   Prevent users from saving a record if validation from a custom action fails.
        •  Query and update a list of records.

You need to configure processes for the app without using code.

Which processes should you use? To answer, drag the appropriate processes to the correct
requirements. Each process may be used once, more than once, or not at all. You may need to
drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

   For the two requirements:

1. Prevent users from saving a record if validation from a custom action fails → Classic
workflow

        •  A real-time (synchronous) classic workflow can run before the record is saved and
          stop the operation if validation fails.
        •  Cloud flows run asynchronously and cannot prevent the save operation.

2. Query and update a list of records → Cloud flow

        •  Cloud flows are designed to query, process, and update multiple records efficiently
           using Dataverse connectors and actions.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96907-exam-pl-200-topic-
3-question-23-discussion/

---

## [Página 165](PL-200%20Q%26A.pdf#page=165) · texto nativo

140 Question.
You plan to create a canvas app.

The app requires a button on the data entry screen that users can select to send an email.

You need to configure the app.

What should you create?

    A.  Classic workflow
    B. Power Automate cloud flow
   C. Azure Logic App
   D. Business process flow
Answer
   Correct Answer: B

   Explanation:

    In a canvas app, if users need to select a button to send an email, the recommended approach
    is to:

        1.  Create a Power Automate cloud flow that sends the email.
        2. Add the flow to the canvas app.
        3.  Configure the button's OnSelect property to run the flow.

  Why not the others?

    •   A. Classic workflow
       Classic workflows run in Dataverse and are not directly invoked by a button in a canvas
       app.

    •  C. Azure Logic App
       While Logic Apps can send emails, the native no-code Power Platform solution for a canvas
      app is a Power Automate cloud flow.

    •  D. Business process flow
       Business process flows guide users through stages of a process; they are not used to send
       emails from a canvas app button.

Discussion: https://www.examtopics.com/discussions/microsoft/view/99701-exam-pl-200-topic-
3-question-24-discussion/

141 Question.
You need to build a Power BI dashboard for sales managers to track opportunities.

---

## [Página 166](PL-200%20Q%26A.pdf#page=166) · texto nativo

When a new sale closes that is greater than $1 million, a notification must pop up and an email
must be sent to the leadership team.

You need to ensure the email is sent without editing the Microsoft Dataverse.

Which two elements should you configure? Each correct answer is part of the solution.

NOTE: Each correct selection is worth one point.

    A. a Power Automate flow
    B. a calculated column in the Dataverse
   C. a paginated report to save to Microsoft OneDrive
   D. a custom connector
    E.  alerts in Power BI
Answer
   Correct Answer: A,E

   Explanation:

   The requirement is:

        •  A Power BI dashboard tracks opportunities.
        •  When a sale exceeds $1 million, a notification must appear.
        •  An email must be sent automatically.
        •  No changes can be made to Dataverse.

   Power BI Alerts can monitor a dashboard tile and trigger when a threshold is exceeded (e.g.,
    sales > $1,000,000).

   Power Automate can be triggered by a Power BI alert and then send an email to the leadership
   team.

  Why not the others?

    •   B. Calculated column in Dataverse
       Requires modifying Dataverse, which is not allowed.

    •  C. Paginated report to OneDrive
      Does not provide real-time alerting and email notification based on dashboard thresholds.

    •  D. Custom connector
      Not needed for standard Power BI alert and email functionality.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96780-exam-pl-200-topic-
3-question-25-discussion/

---

## [Página 167](PL-200%20Q%26A.pdf#page=167) · texto nativo

142 Question.
A company uses a model-driven app for customer support.

The company has the following requirements for the app:

        •  Send an email in real-time to customers when they enter their email address.
        •  Send an email to customers at the same time every day for cases that are open for more
          than 24 hours.

The solution should require the least amount of customization.

You need to configure the model-driven app.

Which components should you use? To answer, drag the appropriate components to the
requirements. Each component may be used once, more than once, or not at all. You may need to
drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 168](PL-200%20Q%26A.pdf#page=168) · texto nativo

Explanation:

   Send email to customer when email address entered

        •   This requires real-time processing when a record is created or updated.
        •  A real-time Classic workflow can trigger immediately when the email field is
          populated and send the email with minimal customization.

   Send email at the same time every day

        •   This is a scheduled process (for cases open more than 24 hours).
        •  A Power Automate flow can run on a recurring schedule (for example, daily at 9:00 AM)
         and send emails for qualifying cases.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96781-exam-pl-200-topic-
3-question-26-discussion/

143 Question.
You have a classic workflow. The workflow updates a custom column on a record when an account
record is created.

The workflow must update the custom column based on the following conditions:

    •  Update the custom column value using the Account Number.
    •    If the Account Number column is blank, update the custom column value using the Ticker
      Symbol.
    •    If the Ticker Symbol column is blank, update the custom column value to N/A.

You need to configure the custom column value by using the update record step.

What should you do?

    A. Add a formula that evaluates the two column values and uses the first populated value or
       else the default value.

---

## [Página 169](PL-200%20Q%26A.pdf#page=169) · texto nativo

B. Add an expression that evaluates the two column values and uses the first populated value
       or else the default value.
   C. Add the two columns with the default value by using the Forms Assistant.
   D. Add check conditions to determine if the two columns contain data.
Answer
   Correct Answer: A

   Explanation:

    In a classic Dataverse workflow, when configuring an Update Record step, you can use the
   Form Assistant and Process Expressions/Formulas to populate a field dynamically.

   The requirement is essentially:

            Account Number

             Else Ticker Symbol

             Else "N/A"

    This can be accomplished with a formula that evaluates the fields and returns the first non-
   empty value, otherwise the default value.

  Why the others are incorrect

    •   B. Add an expression...
       Classic workflows use process formulas rather than Power Automate-style expressions.

    •  C. Add the two columns with the default value by using the Forms Assistant.
       This would concatenate or insert values but would not evaluate which field is populated.

    •  D. Add check conditions to determine if the two columns contain data.
       While possible, it requires multiple conditional branches and does not satisfy the
       requirement to configure the value directly in the Update Record step as efficiently as a
       formula.

Discussion: https://www.examtopics.com/discussions/microsoft/view/95990-exam-pl-200-topic-
3-question-27-discussion/

144 Question.
A company uses a canvas app.

Supervisors must approve transactions when a user from the sales department enters a revenue
amount that is over $1 million.

You need to configure an approval process without using code.

---

## [Página 170](PL-200%20Q%26A.pdf#page=170) · texto nativo

What should you create?

    A. Power Automate cloud flow
    B. Power Apps component framework (PCF) control
   C. Column Expression
   D. Azure Service Bus service
Answer
   Correct Answer: A

   Explanation:

   The requirement is to:

        •   Trigger an approval when a revenue amount exceeds $1 million.
        •  Use a canvas app.
        •  Implement the solution without code.

   Power Automate cloud flows provide built-in Approvals actions that can:

        •   Start and manage approval processes.
        •  Send approval requests to supervisors.
        •  Wait for approval or rejection.
        •   Integrate directly with canvas apps.

  Why not the others?

    •   B. Power Apps component framework (PCF) control
     PCF controls require custom development and are used to extend the UI, not to create
       approval workflows.

    •  C. Column Expression
       Expressions can calculate values but cannot orchestrate approvals.

    •  D. Azure Service Bus service
       Service Bus is a messaging service and would require custom integration; it is not a no-
      code approval solution.

Discussion: https://www.examtopics.com/discussions/microsoft/view/99709-exam-pl-200-topic-
3-question-28-discussion/

145 Question.
A company creates a Power Automate cloud flow for a Power Apps app.

The cloud flow must send a daily email that contains a list of year-to-date (YTD) totals.

You need to configure the flow.

---

## [Página 171](PL-200%20Q%26A.pdf#page=171) · texto nativo

Which feature should you use?

    A. Loop
    B. Wait
   C. Condition
   D.  Parallel branch
Answer
   Correct Answer: A

   Explanation:

   The flow must send a daily email containing a list of YTD totals. When generating a list of
   records (such as YTD totals), Power Automate typically needs to iterate through multiple items
   and build the email content.

   A Loop (Apply to each) is used to process each record in a collection and compile the list that
    will be included in the email.

  Why not the others?

    •   B. Wait
      Pauses execution for a period of time; it does not process lists of records.

    •  C. Condition
       Evaluates true/false logic but does not iterate through multiple YTD records.

    •  D. Parallel branch
      Runs actions simultaneously and is unrelated to creating a list for an email.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96205-exam-pl-200-topic-
3-question-29-discussion/

146 Question.
A company uses a model-driven app. The app uses a workflow to send email. Emails are sent to
new customers that enter an email address for the first time in the app.

Customers report that they do not receive an email after entering an email address.

You need to troubleshoot the issue.

In which order should you perform the actions? To answer, move the appropriate actions from the
list of actions to the answer area and arrange them in the correct order.

---

## [Página 172](PL-200%20Q%26A.pdf#page=172) · texto nativo

Answer
   Correct Answer:





   Explanation:

   To troubleshoot a classic workflow, you should first reproduce the problem, then review the
   workflow execution details, and finally make corrections if needed.

   Correct order:

        •  Run the workflow
        •  Review the tab with the process sessions
        •   Edit the workflow

   Why?

        •  Run the workflow to reproduce the issue and generate a workflow execution record.
        •  Review the Process Sessions to identify errors, failures, or conditions that prevented
           the email from being sent.
        •   Edit the workflow to correct the identified issue.

   Clear the option to delete the workflow retention jobs is not part of the normal
    troubleshooting sequence for this scenario.

Discussion: https://www.examtopics.com/discussions/microsoft/view/114698-exam-pl-200-
topic-3-question-33-discussion/

147 Question.
A company has a Power Apps app.

The app must meet the following requirements:

        •  Managers assign lead records to the sales department. A new phone call record must
         be created if a lead record has no activities.

---

## [Página 173](PL-200%20Q%26A.pdf#page=173) · texto nativo

•  An email must be sent to the manager if the phone call record created is not completed
            after one day.

A classic workflow must run when a lead record is assigned.

You need to configure the check conditions for the workflow.

Which value should you use for each condition? To answer, select the appropriate options in the
answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

   For this classic workflow:

---

## [Página 174](PL-200%20Q%26A.pdf#page=174) · texto nativo

Requirement 1

       Create a new phone call record if a lead record has no activities.

   The check condition should verify that the activity count is 0.

   Number of activities for new phone call record = 0

Requirement 2

      Send an email to the manager if the phone call record is not completed after one day.

   The workflow should wait until 1 day has elapsed before checking whether the phone call is
   completed.

   Duration for email sent to manager = 1 Day

Discussion: https://www.examtopics.com/discussions/microsoft/view/112058-exam-pl-200-
topic-3-question-34-discussion/

148 Question.
You plan to create classic workflows for process automation on the Account table.

The process automation has the following requirements:

        •    If the Account Name column changes, a custom column named Previous Name must
         be updated with the original value.
        •    If the Credit Limit column changes, an email must be sent to the record owner with the
        new value.
        •  Asynchronous processes must be used whenever possible.

You need to implement the process automation.

What is the minimum number of workflows you should use? To answer, select the appropriate
options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 175](PL-200%20Q%26A.pdf#page=175) · texto nativo

.
Answer
   Correct Answer:





   Explanation:

   To satisfy the requirements while using asynchronous processes whenever possible:

   Requirement 1

   Account Name changes → Previous Name must contain the original value

        •  To capture the original value before the change is committed, you need a
         Real-time workflow (runs before/during the update).
        •  A background workflow cannot reliably access the previous value after the
          record has been updated.

   1 Real-time workflow

   Requirement 2

   Credit Limit changes → Send email to record owner with new value

---

## [Página 176](PL-200%20Q%26A.pdf#page=176) · texto nativo

•  Sending an email does not require immediate execution.
        •  The requirement explicitly says to use asynchronous processes whenever possible.

   1 Background workflow

Discussion: https://www.examtopics.com/discussions/microsoft/view/127025-exam-pl-200-
topic-3-question-35-discussion/

149 Question.
A company uses Power Apps to create maintenance requests. The maintenance manager emails
the manager of the department noted in the request.

The maintenance manager wants to automate the email process when a new maintenance request
is created.

You need to build a Power Automate flow to automate the email process.

Which three components should you add to the flow in sequence? To answer, move the
appropriate components from the list of components to the answer area and arrange them in the
correct order.





Answer
   Correct Answer:

---

## [Página 177](PL-200%20Q%26A.pdf#page=177) · texto nativo

Explanation:

    In Power Automate, a flow is built in this sequence:

        •   Trigger – starts the flow when a new maintenance request is created.
        •  Condition – checks which department is associated with the request (to determine the
           correct manager).
        •  Action – sends the email to the manager.

Discussion: https://www.examtopics.com/discussions/microsoft/view/131886-exam-pl-200-
topic-3-question-37-discussion/

150 Question.
You are creating Power Automate automations targeting Dataverse.

The automations must meet the following requirements:

        •  Run a custom API created by a developer. The API performs an action against an
            existing Account row in the system.
        •  Create three rows in Dataverse. If an error occurs when you create the second row, the
               first row must be deleted.
        •  Run several create, update, and delete operations as part of a single transaction
          without writing custom code.
        •  Run several complex operations targeting multiple rows in the system as part of a single
           transaction.


You need to configure the actions.

---

## [Página 178](PL-200%20Q%26A.pdf#page=178) · texto nativo

Which actions should you configure? To answer, move the appropriate actions to the correct
requirements. You may use each action once, more than once, or not at all. You may need to move
the split bar between panes or scroll to view content.





.
Answer
   Correct Answer:





   Explanation:

        •  Perform a bound action
         Use this when the custom API/action is executed against a specific existing row, such
          as an Account row.
        •  Perform a changeset request
         Use this when multiple Dataverse operations must run as a single transaction. If one
           operation fails, the previous operations are rolled back.
        •  Perform an unbound action
         Use this for complex operations that are not tied to one specific row and can target
           multiple rows or broader Dataverse logic.

Discussion: https://www.examtopics.com/discussions/microsoft/view/142354-exam-pl-200-
topic-3-question-40-discussion/

---

## [Página 179](PL-200%20Q%26A.pdf#page=179) · texto nativo

151 Question.
A company has a business process flow that executes on the Contact table.

The company requires that the steps in the flow be executed in real time when users create a new
task and update the status of a Contact row.

You need to implement a solution that automates the steps.

Which three actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.

NOTE: More than one order of answer choices is correct. You will receive credit for any of the
correct orders you select.





Answer
   Correct Answer:





   Explanation:

   To automate steps in a Business Process Flow (BPF) in real time, you use an Action Step that
    calls a Custom Action.

---

## [Página 180](PL-200%20Q%26A.pdf#page=180) · texto nativo

The correct sequence is:

    1.  Create a new custom action with action steps
    2.  Modify the business process flow
    3.  Activate the business process flow

   Why?

        •   First, create the Custom Action that will perform the required operations (create task,
          update contact status, etc.).
        •  Then modify the existing BPF to include an Action Step that invokes the custom
           action.
        •   Finally, activate the BPF so the changes take effect.

Discussion: https://www.examtopics.com/discussions/microsoft/view/139472-exam-pl-200-
topic-3-question-41-discussion/

152 Question.
A company is using the Account table and a main form named Account Main.

The company defines the following requirements for the Account Main form:


        •   Evaluate a single value selected as part of a drop-down list.
        •   Display a message and suggestion based on business intelligence if the drop-down list
          value equals a specific value.
        •   Logic must run against this form only.


You need to implement the logic.

Which four actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.

NOTE: More than one order of answer choices is correct. You will receive credit for any of the
correct orders you select.

---

## [Página 181](PL-200%20Q%26A.pdf#page=181) · texto nativo

Answer
   Correct Answer:





   Explanation:

   The requirements point to a Business Rule because:

        •   Evaluate a value from a drop-down list (Choice column).
        •  Show a message and recommendation when a specific value is selected.
        •  Run only on the Account Main form.

   Correct sequence

    1.  Create a choice column
    2.  Create a business rule
    3. Add a Recommendation action
    4.  Set scope to Account Main form

   Why?

        •  The drop-down list requires a Choice column.
        •  The logic is implemented using a Business Rule.
        •  A Recommendation action displays a message and suggested action based on a
           condition.
        •  The business rule scope must be set to the Account Main form so it runs only on that
           form.

Discussion: https://www.examtopics.com/discussions/microsoft/view/147375-exam-pl-200-
topic-3-question-43-discussion/

153 Question.
A company creates a Power Automate cloud flow for a Power Apps app.

The cloud flow must send an email to each active contact.

You need to configure the flow.

---

## [Página 182](PL-200%20Q%26A.pdf#page=182) · texto nativo

Which feature should you use?

    A.  Condition
    B.  Apply to each
   C. Wait
   D.  Parallel branch
Answer
   Correct Answer: B

   Explanation:

   The flow must send an email to each active contact. When a flow retrieves multiple contact
    records, it must iterate through the collection and perform the email action for every record.

   Apply to each is used to:

    1.  Retrieve the list of active contacts.
    2.  Loop through each contact.
    3. Send an email to each contact individually.

  Why not the others?

    •   A. Condition
       Evaluates true/false logic but does not iterate through multiple contacts.

    •  C. Wait
      Pauses the flow for a specified period.

    •  D. Parallel branch
      Runs actions simultaneously but is not used to process each record in a collection.

Discussion: https://www.examtopics.com/discussions/microsoft/view/149008-exam-pl-200-
topic-3-question-44-discussion/

154 Question.
You are creating a cloud flow for an automation targeting Dataverse.

When a new account is created in Dataverse, the name of the account must be updated based on
the following logic:

        •    If the Account Category Code equals Preferred Customer (1), pre append the value
           Preferred | to the name.
        •    If the Account Category Code equals Standard (2) or is not populated, pre-append
          Standard | to the name.

---

## [Página 183](PL-200%20Q%26A.pdf#page=183) · texto nativo

You need to define the correct formula to use for the automation.

Which formula should you use?

    A.  if(equals(triggerOutputs()?['body/accountcategorycode'), 1), concat('Standard | ',
        triggerOutputs()?['body/name']), concat('Preferred | ', triggerOutputs()?['body/name']))
    B.  if(equals(triggerOutputs()?['body/accountcategorycode'), 2), concat('Standard ',
        |triggerOutputs()?[‘body/name']), concat('Preferred | ', triggerOutputs()?['body/name']))
   C.  if(equals(outputs('trigger')?['body/accountcategorycode'], 1), concat('Standard | ',
        outputs('trigger')?['body/name']), concat('Preferred | ', outputs('trigger')?['body/name']))
   D.  if(equalsfoutputs('trigger')body/accountcategorycode'], 2), concat('Standard | ',
        outputs('trigger')?['body/name']), concat('Preferred | ',outputs('trigger')?['body/name']))
Answer
   Correct Answer: D

   Explanation:

   The logic required is:

           If Account Category Code = 1

        → Preferred | Account Name

       Else

        → Standard | Account Name

   Option D is the only formula that correctly checks for value 2 (Standard) and returns:

      Standard | Name

      ``

   Otherwise, it returns:

       Preferred | Name

      ``

   The expression is:

           if(

           equals(outputs('trigger')?['body/accountcategorycode'], 2),

          concat('Standard | ', outputs('trigger')?['body/name']),

          concat('Preferred | ', outputs('trigger')?['body/name'])

           )

---

## [Página 184](PL-200%20Q%26A.pdf#page=184) · texto nativo

Since the requirement states that Standard (2) or null should result in "Standard | ", and all
    other valid values (specifically 1) should result in "Preferred | ", D is the best match among the
   provided options.

Discussion: https://www.examtopics.com/discussions/microsoft/view/145180-exam-pl-200-
topic-3-question-45-discussion/

155 Question.
A cloud flow you authored failed several times in production due to a transient network issue. The
issue is now resolved.

You need to reprocess the failed flow runs with the least amount of administrative effort.

What should you do?

    A. Resubmit each run individually.
    B. Resubmit all runs in bulk.
   C. Rerun the trigger action.
   D. Turn the flow off and then on.
Answer
   Correct Answer: B

   Explanation:

   Since the flow failures were caused by a transient network issue that has already been
    resolved, the most efficient approach is to resubmit all failed runs in bulk.

    This minimizes administrative effort because:

    •   Multiple failed runs can be retried at once.
    •   There is no need to open and resubmit each run individually.
    •  The original trigger data is reused.

  Why not the others?

    •   A. Resubmit each run individually
      Works, but requires more effort.

    •  C. Rerun the trigger action
      Not all triggers can be rerun, and this does not automatically reprocess the existing failed
       runs.

    •  D. Turn the flow off and then on
       This does not reprocess failed runs.

Discussion: https://www.examtopics.com/discussions/microsoft/view/151211-exam-pl-200-
topic-3-question-46-discussion/

---

## [Página 185](PL-200%20Q%26A.pdf#page=185) · texto nativo

156 Question.
You are creating a Power Automate cloud flow. The cloud flow will create several SharePoint Online
list items based on a variety of conditions.

If any of the dependent SharePoint Online actions fail, you must revert the changes while the
automation runs.

You need to design the cloud flow to meet the requirement.

Which two actions should you implement for the design? Each correct answer presents part of the
solution.

NOTE: Each correct selection is worth one point.

    A. Add a scope.
    B.  Set Run After to Has failed.
   C. Perform a changeset request action.
   D.  Retrigger the flow run.
Answer
   Correct Answer: A,B

   Explanation:

   The requirement is to revert changes if any dependent SharePoint actions fail. Since
   SharePoint does not support transactional rollback like Dataverse changesets, you must
   implement a compensation pattern.

    A. Add a scope

        •  Group the SharePoint create/update operations inside a Scope.
        •   This allows centralized error handling and rollback logic.

    B. Set Run After to Has failed

        •   Configure a second scope (rollback/cleanup scope) to run after the first scope has
            failed.
        •   In the rollback scope, delete or undo any SharePoint items that were created before the
            failure occurred.

  Why not the others?

   C. Perform a changeset request action

        •  Changesets provide transactional behavior for Dataverse operations.
        •  They are not available for SharePoint Online list operations.

   D. Retrigger the flow run

---

## [Página 186](PL-200%20Q%26A.pdf#page=186) · texto nativo

•   Retrying the flow does not revert changes that were already committed.

Discussion: https://www.examtopics.com/discussions/microsoft/view/144030-exam-pl-200-
topic-3-question-47-discussion/

157 Question.
A company has a Power Apps app.

The app must meet the following requirements:

        •   Managers assign lead rows to the sales department. A new phone call row must be
          created if a lead row has no activities.
        •  An email must be sent to the manager if the phone call row created is not completed
            after one day.


A classic workflow must run when a lead row is assigned.

You need to configure the check conditions for the workflow.

Which value should you use for each condition? To answer, select the appropriate options in the
answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 187](PL-200%20Q%26A.pdf#page=187) · texto nativo

Explanation:

   For this workflow:

Condition 1: Number of activities to evaluate for the new phone call row

   The requirement states:

      "A new phone call row must be created if a lead row has no activities."

    Therefore, the workflow should check that the activity count equals 0.

   Value: 0


Condition 2: Duration to delay before sending an email to the manager

   The requirement states:

      "An email must be sent to the manager if the phone call row created is not completed
        after one day."

   Since the workflow runs when the lead is assigned and creates the phone call, the delay should
   be 1 day before checking whether the phone call is completed.

   Value: 1 Day

Discussion: https://www.examtopics.com/discussions/microsoft/view/157182-exam-pl-200-
topic-3-question-51-discussion/

158 Question.
A company uses Power Automate extensively.

---

## [Página 188](PL-200%20Q%26A.pdf#page=188) · texto nativo

The company maintains the following three environments:





You need to recommend a monitoring solution for each environment. The solution must minimize
development effort.

Which tools should you recommend? To answer, move the appropriate tools to the correct
environments. You may use each tool once, more than once, or not at all. You may need to
move the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





.
Answer
   Correct Answer:





   Explanation:

   Environment1 → Power Platform admin center

---

## [Página 189](PL-200%20Q%26A.pdf#page=189) · texto nativo

•  No Dataverse.
    •   Administrators only need to view failed flow run details.
    •  Minimal development effort.

   The Power Platform admin center provides flow monitoring and run history directly, including
    failed runs.

   Environment2 → Application Insights

    •  Dataverse enabled.
    •   Highly sensitive data must remain within the geographical boundary.
    •  Need automatic smart detection alerts.
    •   Retain activity monitoring for auditing.

    Application Insights provides telemetry, monitoring, anomaly detection, and smart detection
    alerts while supporting regional data residency requirements.

   Environment3 → Power Automate Management connector

    •  Dataverse enabled.
    •   Central environment used to store analytical data for cloud flows across the tenant.
    •  Data surfaces in a model-driven app.
    •  No flows execute in this environment.

   The Management connector can collect flow analytics and metadata from multiple
   environments and store/report on them centrally in Dataverse.

Discussion: https://www.examtopics.com/discussions/microsoft/view/394314-exam-pl-200-
topic-3-question-52-discussion/

159 Question.
You are designing a Power Virtual Agents chatbot.
The chatbot must be able to maintain customer information if the conversation topic changes
during a dialog.
You need to configure variables to store customer name and email address.
Which type of variable should you create?

    A.  session
    B.  slot
   C. bot
   D. topic
Answer
   Correct Answer: C

   Explanation:

    In Power Virtual Agents (Copilot Studio):

---

## [Página 190](PL-200%20Q%26A.pdf#page=190) · texto nativo

•  Topic variables are available only within the current topic.
    •  Bot variables persist across topics during the conversation and can be reused if the user
       switches topics.
    •  Session variables and slot variables are not the appropriate choice for sharing
       information across multiple topics in Power Virtual Agents.

   Because the chatbot must maintain customer name and email address when the
   conversation changes topics, you should store them in bot variables.

Discussion: https://www.examtopics.com/discussions/microsoft/view/59930-exam-pl-200-topic-
4-question-2-discussion/

160 Question.
You are designing a Power Virtual Agents chatbot for a store.
You need to teach the chatbot to acknowledge the store's product categories and the variations
within specific categories.
You need to create custom entities to provide the chatbot with the knowledge of the product
categories.
Which features should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:

---

## [Página 191](PL-200%20Q%26A.pdf#page=191) · texto nativo

Answer
   Correct Answer:





   Explanation:

    •  Smart matching

       •  Helps Power Virtual Agents recognize misspellings, grammatical variations, and similar
         meanings when matching custom entity values.

    •  Synonyms

       •  Expand the recognition logic by teaching the bot that different words or phrases
           represent the same category (for example, "TV", "Television", and "Smart TV").

    •   Slot filling

       •   Automatically captures entity values mentioned by the user and stores them in
           variables for later use in the conversation.

Discussion: https://www.examtopics.com/discussions/microsoft/view/62396-exam-pl-200-topic-
4-question-3-discussion/

---

## [Página 192](PL-200%20Q%26A.pdf#page=192) · texto nativo

161 Question.
A customer has a support website that includes FAQ pages, knowledge articles, and support
content.
You plan to leverage an existing Power Virtual Agents bot to enhance and streamline existing
support functionality for the existing support portal.
You need to create topics from existing website content. The process must minimize human errors
during topic creation.
Which three actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.
Select and Place:





Answer
   Correct Answer:





   Explanation:

   For Power Virtual Agents, when creating topics from existing website content (FAQ pages,
   knowledge articles, support content), the Suggested Topics feature is used.

   The correct sequence is:

    1.  Capture suggested topics
    2.  Identify the pre-filled trigger phrases
    3. Add selected topics to the chatbot

   Why?

       •  Capture suggested topics: PVA analyzes the website content and generates suggested
            topics.
       •   Identify the pre-filled trigger phrases: Review the automatically generated trigger
          phrases for each suggested topic.

---

## [Página 193](PL-200%20Q%26A.pdf#page=193) · texto nativo

•  Add selected topics to the chatbot: Accept the useful topics and add them to the bot.

   The other options are not part of the topic-generation workflow:

       •  Hover over the topic and select the Automate icon
       •  Enable the topics (topics are typically available once added and configured).

Discussion: https://www.examtopics.com/discussions/microsoft/view/63914-exam-pl-200-topic-
4-question-4-discussion/

162 Question.
You are creating a Power Virtual Agents chatbot that uses multiple topics.
Each user interaction can reference more than one topic.
You need to be able to capture a value in an initial topic and use it in subsequent topics.
Which type of variable should you create?

    A.  Context
    B. Bot
   C. Topic
Answer
   Correct Answer: B

   Explanation:

    In Power Virtual Agents (Copilot Studio):

       •  Topic variables are available only within the topic where they are created.
       •  Bot variables persist across topics and can be reused throughout the conversation.
       •  Context variables are not the standard variable type used to share data between
            topics.

   Because the requirement is to:

      Capture a value in an initial topic and use it in subsequent topics

   you should store the value in a Bot variable so it remains available when the conversation
   moves from one topic to another.

Discussion: https://www.examtopics.com/discussions/microsoft/view/43269-exam-pl-200-topic-
4-question-5-discussion/

163 Question.
A company has a custom website.
You need to embed a Power Virtual Agents chatbot into the website.
What should you use?

---

## [Página 194](PL-200%20Q%26A.pdf#page=194) · texto nativo

A. Webpage URL
    B. Form ID
   C. Bot ID
   D. Custom web channel
Answer
   Correct Answer: D

   Explanation:

   To embed a Power Virtual Agents (Power Virtual Agents/Copilot Studio) chatbot into a
   custom website, you publish the bot and connect it through a Custom website channel
   (custom web channel).

    This provides the embed code or script that can be added to the website.

  Why not the others?

    •   A. Webpage URL
      A URL alone does not embed the chatbot in the website.

    •   B. Form ID
      Form IDs are unrelated to chatbot embedding.

    •  C. Bot ID
      A Bot ID identifies the bot but is not the mechanism used to publish and embed it on a
       website.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60043-exam-pl-200-topic-
4-question-6-discussion/

164 Question.
A company is developing several Power Virtual Agents chatbots. The company manufactures more
than 1,000 different products.
The chatbots must prompt users to enter or select a product.
You need to store the product information so that it can be reused across all chatbots.
Where should you store the model data?

    A.  Global variables
    B. Custom entities
   C. Topics
   D.  Multiple choice options
Answer
   Correct Answer: B

   Explanation:

---

## [Página 195](PL-200%20Q%26A.pdf#page=195) · texto nativo

The requirement is to:

        •   Store information about more than 1,000 products.
        •  Reuse the information across multiple Power Virtual Agents chatbots.
        •   Allow users to enter or select a product.

   Custom entities are designed to store and recognize lists of values (such as product names,
   product categories, locations, etc.) for use in chatbot conversations. They can be reused
   across topics within a bot and are the appropriate way to model product data for recognition
   and selection.

  Why not the others?

    •   A. Global variables
       Variables store values during a conversation; they are not intended to maintain a reusable
       catalog of 1,000+ products.

    •  C. Topics
       Topics define conversation paths, not reusable product data.

    •  D. Multiple choice options
      Not practical for maintaining or presenting over 1,000 products

Discussion: https://www.examtopics.com/discussions/microsoft/view/60203-exam-pl-200-topic-
4-question-7-discussion/

165 Question.
A company creates a Power Virtual Agents chatbot.
You need to determine when live agents are engaged to provide support.
Which metrics should you use? To answer, drag the appropriate metrics to the correct processes.
Each metric may be used once, more than once, or not at all.
You may need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:

---

## [Página 196](PL-200%20Q%26A.pdf#page=196) · texto nativo

Answer
   Correct Answer:





   Explanation:

    •   Escalation rate drivers
      Shows the topics, issues, or reasons that most frequently cause conversations to be
       escalated to a live agent.
    •   Escalation rate
      Measures how many chatbot sessions are escalated to a live agent and can be tracked over
       time to identify the number of chats transferred each day.

  Why not the others?

    •  Engagement over time
      Measures overall chatbot usage and engagement trends.
    •  Session outcomes over time
      Shows how conversations ended (resolved, abandoned, escalated, etc.) but does not
        specifically identify the topics driving escalations.

Discussion: https://www.examtopics.com/discussions/microsoft/view/43283-exam-pl-200-topic-
4-question-8-discussion/

166 Question.
You create a new Power Virtual Agents chatbot for an organization.
Testing and production deployment of the chatbot are not complete.
You need to ensure that appropriate users can access the chatbot.
Which methods should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 197](PL-200%20Q%26A.pdf#page=197) · texto nativo

Hot Area:





Answer
   Correct Answer:





   Explanation:

    1.  Test the chatbot with unlicensed internal users → Use the demo website

       •  The demo website allows internal users to interact with and test the bot before
         deployment without requiring publication to production channels.

    2.  Allow other licensed internal users to edit the chatbot → Share the chatbot to a security
      group containing all users

       •   Editing a Power Virtual Agents bot requires authoring permissions. Sharing the bot with
         a security group is the most efficient way to grant access to multiple licensed users.

    3.  Deploy the chatbot to production for public consumption → Embed the chatbot code in
      an IFrame on your company's public website

---

## [Página 198](PL-200%20Q%26A.pdf#page=198) · texto nativo

•  For external/public users, the bot should be published and embedded on a public-
           facing website using the provided embed code (iFrame).

Discussion: https://www.examtopics.com/discussions/microsoft/view/54176-exam-pl-200-topic-
4-question-12-discussion/

167 Question.
You are designing a chatbot for a sports outlet.
You need to complete the chatbot.
Which features should you use? To answer, drag the appropriate features to the correct
requirements. Each feature may be used once, more than once, or not at all. You may need to drag
the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





Answer
   Correct Answer:

---

## [Página 199](PL-200%20Q%26A.pdf#page=199) · texto nativo

Explanation:

       •   Entities represent real-world objects, concepts, or topics that the chatbot can
           recognize in user input (for example, sports teams, products, or locations).
       •  Topics define conversation paths and contain trigger phrases that start a conversation
            flow.
       •  Variables store values and can be used with conditions to determine which
           conversational path the bot should follow.
       •  Flows are typically used to call Power Automate processes and are not the best match
            for any of these requirements.

Discussion: https://www.examtopics.com/discussions/microsoft/view/54495-exam-pl-200-topic-
4-question-13-discussion/

168 Question.
A company has marketing teams for different regions.
A user creates and publishes a chatbot within Microsoft Teams for their specific marketing team.
The base metrics retrieved by the chatbot are relevant to all marketing teams.
The other marketing teams request access to the chatbot.
You need to publish the chatbot to the entire company.
What should you do?

    A.  Configure the chatbot to be used with the Teams channel.
    B. Submit the chatbot for admin approval.
   C. Copy the published chatbot link and email it to the other teams.
   D.  Invite the other teams to the team that has the chatbot.
    E.  Export the chatbot and import it into a corporate environment.
Answer
   Correct Answer: B

   Explanation:

   When a chatbot is created in Microsoft Teams using Power Virtual Agents (Copilot Studio for
   Teams), it is initially available only within the scope of that team.

   To make the chatbot available across the entire organization in Teams:

        1.  Publish the bot.
        2.  Submit it for administrator approval.
        3.  The Teams administrator can then make the bot available organization-wide through
           the Teams app catalog.

  Why the other options are incorrect

    •   A. Configure the chatbot to be used with the Teams channel

---

## [Página 200](PL-200%20Q%26A.pdf#page=200) · texto nativo

o  The bot is already running in Teams. This does not make it available company-wide.

    •  C. Copy the published chatbot link and email it to the other teams

         o  This is not a scalable or managed enterprise-wide deployment method.

    •  D. Invite the other teams to the team that has the chatbot

         o  Users would gain access to the Team, not necessarily to an organizationally
             deployed bot.

    •   E. Export the chatbot and import it into a corporate environment

         o  Not required to publish the bot across the organization from Teams.

Discussion: https://www.examtopics.com/discussions/microsoft/view/85542-exam-pl-200-topic-
4-question-14-discussion/

169 Question.
You create a Power Virtual Agents chatbot to reduce the number of incoming support calls that
require a live person.
The chatbot does not direct users to the correct information. You determine that this is because
the chatbot is not able to identify which product a user is referring to in a conversation.
You need to present a list of products so that users can select the correct product.
What should you create?

    A.  Table
    B.  Variable
   C.  Slot filling
   D.  Entity
Answer
   Correct Answer:

   Explanation:

    In Power Virtual Agents (Copilot Studio), an Entity is used to identify and recognize specific
    items, concepts, or categories in a user's input.

   Since the chatbot must recognize which product the user is referring to and present a list of
    valid products for selection, you should create a custom Entity that contains the product
   names.

    Entities define the valid products and allow users to select or reference them consistently
   throughout the conversation.

Why not the others?

---

## [Página 201](PL-200%20Q%26A.pdf#page=201) · texto nativo

•   A. Table
          Tables are not used by Power Virtual Agents to identify products in a conversation.
        •   B. Variable
           Variables store values during a conversation but do not define the list of products to
           recognize.
        •  C. Slot filling
            Slot filling is a technique for collecting missing information, but it relies on entities to
            identify and validate the values being collected.

Discussion: https://www.examtopics.com/discussions/microsoft/view/80997-exam-pl-200-topic-
4-question-15-discussion/

170 Question.
You are creating a Power Virtual Agents chatbot for a Microsoft Power Platform power apps portal
app.
The job title of users must be stored automatically when users log in. The job title must always
appear in the chatbot.
You need to configure the job title functionality.
Which mechanism should you use?

    A.  artificial intelligence
    B.  variable
   C.  entity
   D. topic
Answer
   Correct Answer: B

   Explanation:

    In Power Virtual Agents, variables are used to store and retain information during a
    conversation. User attributes such as a job title can be stored in a variable and then referenced
   throughout the chatbot conversation.

       •  Variable → Stores and reuses values (such as Job Title, Name, Department).
       •   Entity → Identifies and extracts information from user input.
       •  Topic → Defines a conversation path.
       •   Artificial intelligence → Helps with intent recognition and conversational capabilities,
          but does not store user-specific data.

   Since the requirement is to automatically store the user's job title when they log in and
   make it available throughout the chatbot, a variable is the appropriate mechanism.

Discussion: https://www.examtopics.com/discussions/microsoft/view/85544-exam-pl-200-topic-
4-question-16-discussion/

---

## [Página 202](PL-200%20Q%26A.pdf#page=202) · texto nativo

171 Question.
You are designing a Power Virtual Agents chatbot.
The environment you plan to use does not appear as an option in the Power Virtual Agents user
interface.
You need to ensure that you can create the chatbot in the environment.
What should you do?

    A. Change the region for the environment.
    B.  Convert the environment to a sandbox environment.
   C. Create an environment in a supported region.
Answer
   Correct Answer: C

   Explanation:

   Power Virtual Agents (now Microsoft Copilot Studio) is available only in certain supported
    regions. If an environment does not appear in the environment list when creating a chatbot, it is
    typically because the environment is hosted in an unsupported region.

    •   A. Change the region for the environment – Not possible. An environment's region
      cannot be changed after it is created.

    •   B. Convert the environment to a sandbox environment – Environment type
       (Production/Sandbox) does not determine whether it appears for Power Virtual Agents.

    •   C. Create an environment in a supported region – Correct. Creating a new environment
        in a region supported by Power Virtual Agents makes it available for chatbot creation.

Discussion: https://www.examtopics.com/discussions/microsoft/view/86799-exam-pl-200-topic-
4-question-17-discussion/

172 Question.
You are a system administrator for a company with locations in Mexico, United States, and France.
The company has both fulltime employees and contractors in all regions. Fulltime employees use a
mobile app. The company has two security groups: fulltime employees and contractors.

The company requests a chatbot in Microsoft Teams to answer employee benefit questions. The
chatbot must meet the following requirements:

    •    It must be in the local language.
    •  Only fulltime employees may access the chatbot.

You need to configure the chatbot.

What should you do? To answer, select the appropriate options in the answer area.

---

## [Página 203](PL-200%20Q%26A.pdf#page=203) · texto nativo

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

   Chatbot in local language

       •  Power Virtual Agents bots are created for a specific language.
       •  To support users in Spanish (Mexico), English (United States), and French (France),
         you should create three separate chatbots, one for each language.

   Employee access

       •  Access can be restricted by sharing the bot only with the appropriate Microsoft Entra ID
           (Azure AD) security group.
       •  Since only fulltime employees should use the bot, share it with the Fulltime
         Employees security group.

Discussion: https://www.examtopics.com/discussions/microsoft/view/98026-exam-pl-200-topic-
4-question-18-discussion/

---

## [Página 204](PL-200%20Q%26A.pdf#page=204) · texto nativo

173 Question.
A company sells all types of bicycles, bicycle parts, and accessories. You are creating a chatbot by
using Microsoft Power Virtual Agent for the bicycle shop.

When someone types in a bicycle brand name or terms such as helmet or shoes, the chatbot must
automatically go to the accessories section of the chatbot.

You need to configure the chatbot functions.

Which two functions should you configure? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

    A.  Entities
    B.  Fallback topic
   C. Smart matching
   D. Synonyms
    E.  Slot filling
Answer
   Correct Answer: A.D

   Explanation:

   The chatbot must recognize various bicycle brand names and accessory-related terms (such as
   helmet or shoes) and route the conversation to the accessories topic.

•   A. Entities: Entities are used to identify and categorize information entered by users. You can
    create an entity for bicycle brands and accessories so the bot recognizes these values.

•  D. Synonyms: Synonyms allow multiple words or phrases to map to the same entity value. For
   example:

       •  Accessory
           o  Helmet
           o  Bike helmet
           o  Cycling helmet
       •  Shoes
           o  Cycling shoes
           o  Bike shoes

    This enables the bot to understand different terms and direct users to the appropriate topic.

  Why the others are incorrect

    •   B. Fallback topic
      Used when the bot cannot determine the user's intent.

---

## [Página 205](PL-200%20Q%26A.pdf#page=205) · texto nativo

•  C. Smart matching
      Helps match similar phrases but does not specifically categorize product names and
       accessory terms.

    •   E. Slot filling
      Used to collect required information during a conversation, not to recognize brands or
       accessory terms.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96480-exam-pl-200-topic-
4-question-19-discussion/

174 Question.
You plan to create a Power Virtual Agents bot.

The bot must support single sign-on.

You need to publish the bot.

Which two locations should you use? Each correct answer presents a complete solution.

NOTE: Each correct selection is worth one point.

    A.  Mobile app developed for iOS and Android
    B. Website developed using pro developer tools
   C. Microsoft Teams
   D. Azure Bot Service channels
Answer
   Correct Answer: C, D

   Explanation:

   Power Virtual Agents supports Single Sign-On (SSO) when published to specific channels:

    •   Microsoft Teams – Supports SSO using Microsoft Entra ID (Azure AD), allowing users to be
       authenticated automatically.

    •  Azure Bot Service channels – Support SSO when configured appropriately with Azure AD
       authentication.

  Why the others are incorrect

    •   A. Mobile app developed for iOS and Android

         o  Custom mobile apps do not automatically support Power Virtual Agents SSO unless
               additional development and authentication configuration are implemented.

    •   B. Website developed using pro developer tools

---

## [Página 206](PL-200%20Q%26A.pdf#page=206) · texto nativo

o  A website alone does not provide built-in SSO support for a Power Virtual Agents
               bot. Additional custom authentication would be required.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96621-exam-pl-200-topic-
4-question-20-discussion/

175 Question.
A company is planning to create a Power Virtual Agents bot.

The bot has the following requirements:

        •  The bot must provide address information for the company.
        •  The bot must be available from Microsoft Teams and from the internet website of the
         company.

You need to configure the bot.

Which component should you use?

    A. Channel
    B. Template
   C. Composer
   D.  Skill
Answer
   Correct Answer: A

   Explanation:

   The bot must be available in Microsoft Teams and on the company's internet website. In
   Power Virtual Agents (now Microsoft Copilot Studio), availability across different platforms is
    configured through Channels.

   Channels allow you to publish the same bot to multiple endpoints, including:

    •   Microsoft Teams
    •  Custom websites
    •  Facebook Messenger
    •   Mobile apps
    •   Direct Line and other supported platforms

  Why the other options are incorrect

    •   B. Template – Provides a starting point for bot creation but does not determine where the
       bot is available.

    •  C. Composer – Used to create more advanced conversational experiences and dialogs.

---

## [Página 207](PL-200%20Q%26A.pdf#page=207) · texto nativo

•  D. Skill – A reusable capability that can be called by another bot; it does not publish the bot
       to Teams or websites.

Discussion: https://www.examtopics.com/discussions/microsoft/view/98276-exam-pl-200-topic-
4-question-21-discussion/

176 Question.
A company plans to implement a voice-enabled Power Virtual Agents bot.

The company has the following requirements for the bot:

• Recognize when a caller states Tennis or any variation of the word.
• Provide options when a caller states the name of a sport.

You need to configure the bot.

Which features should you use? To answer, select the appropriate options in the answer area.





Answer
   Correct Answer:

---

## [Página 208](PL-200%20Q%26A.pdf#page=208) · texto nativo

Explanation:

    •   Entity
        Entities are used to recognize specific words, phrases, and their variations (synonyms). For
       example, an entity could contain:
         o  Tennis
         o  Lawn tennis
         o  Tennis game

    This allows the bot to recognize different ways users may refer to the same sport.

    •  Topic
       Topics define the conversation flow and responses. Once the bot identifies the sport
       through the entity, it can trigger the appropriate topic and provide options related to that
        sport.
    •   Variable (incorrect)
       Variables store information during a conversation but do not recognize words or control
       conversation topics.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96623-exam-pl-200-topic-
4-question-22-discussion/

---

## [Página 209](PL-200%20Q%26A.pdf#page=209) · texto nativo

177 Question.
A company plans to implement chatbots by using Power Virtual Agents.

The company has the following requirements for the bots:

    •  Users in the accounting department must be able to create a bot for frequently asked
       questions.
    •  The support desk users must be able to use the bot.


The users must not be able to change environment parameters in the Microsoft Power Platform
environment.

You need to configure the permissions for the bots.

Which actions should you implement? To answer, select the appropriate options in the answer
area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 210](PL-200%20Q%26A.pdf#page=210) · texto nativo

Explanation:

    •  Assign users the Maker permissions
         o  Makers can create and manage Power Virtual Agents bots.
         o  This grants bot creation capabilities without giving environment administration
                 rights.
         o  The requirement specifically states users must not be able to change environment
              parameters.
    •  Share the bot with a security group
         o  Allows support desk users to access and use the bot.
         o  Permissions can be managed centrally through the security group.
    •  System Administrator role (Incorrect)
         o  Too much privilege because it allows management of environment settings.
    •  Assign users to a security role (Incorrect)
         o  Security roles control Dataverse access but do not specifically enable bot creation.

Discussion: https://www.examtopics.com/discussions/microsoft/view/97522-exam-pl-200-topic-
4-question-23-discussion/

178 Question.
You use Power Virtual Agents to create a bot that will answer and transfer help desk calls.

You create topics that contain nodes and functions. The company has the following requirements
for the bot:

---

## [Página 211](PL-200%20Q%26A.pdf#page=211) · texto nativo

•  When a caller states the word issue, help, or problem, the bot must respond with the
       question, “How can we help you today?”
    •  When the bot responds with the question, “How can we help you today?”, the bot must
       provide the caller with the choices of hardware, software, or other.
    •  When the caller asks a question, the bot must save the response so that it can perform an
       action on the response.

You need to configure the bot.

Which nodes or functions should you use? To answer, select the appropriate options in the answer
area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 212](PL-200%20Q%26A.pdf#page=212) · texto nativo

Explanation:

Trigger phrase

•   Trigger phrases determine when a topic starts.
•  Words such as issue, help, and problem would be configured as trigger phrases for the
    topic.

Question

•  A Question node can present multiple-choice options such as:
      o  Hardware
      o  Software
      o  Other

•    It also captures the user's selection.

Variable

•   Variables store user responses temporarily during a conversation so they can be used later
    in conditions, actions, or other dialog steps.

---

## [Página 213](PL-200%20Q%26A.pdf#page=213) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/96065-exam-pl-200-topic-
4-question-24-discussion/

179 Question.
A company creates a bot by using Power Virtual Agents.

The company requires the bot to transfer callers to an agent if the bot is unable to recognize a
customer’s request.

You need to configure the bot for the unrecognized information from the customer.

Which feature should you use?

    A.  Fallback skill
    B.  Fallback topic
   C. Fallback workstream
   D. Fallback entity
    E.  Fallback queue
Answer
   Correct Answer: B

   Explanation:

   n Power Virtual Agents, a Fallback topic is triggered when the bot cannot match a user's input
    to any existing topic or intent.

   For this scenario:

    1.  The customer asks something the bot does not understand.
    2.  The Fallback topic is activated.
    3.  Within the fallback topic, you can configure actions such as:
         o  Escalating to a live agent
         o   Transferring the conversation to customer support
         o  Collecting additional information

Why the other options are incorrect

    •   A. Fallback skill – Not a Power Virtual Agents feature for handling unrecognized input.

    •  C. Fallback workstream – Workstreams are used in Dynamics 365 Customer Service
        routing, not for intent recognition.

    •  D. Fallback entity – Entities are used to recognize and extract data from user input.

    •   E. Fallback queue – Queues can receive escalations, but they are not triggered directly by
       unrecognized utterances.

---

## [Página 214](PL-200%20Q%26A.pdf#page=214) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/96067-exam-pl-200-topic-
4-question-25-discussion/

180 Question.
A company plans to create a Power Virtual Agents chatbot.

The bot has the following requirements:

        •  Prompt for a location of the customer and the call must be routed to a support agent for
           the location.
        •   Transfer support calls at each location to a support bot that uses the Bot Framework.

You need to configure the bot.

Which components should you use? To answer, drag the appropriate components to the correct
requirements. Each component may be used once, more than once, or not at all. You may need to
drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 215](PL-200%20Q%26A.pdf#page=215) · texto nativo

Explanation:

    Entities → Route to location

        •   Entities capture and recognize information provided by the user, such as a location
              (e.g., Madrid, Paris, New York).
        •  The chatbot can use the identified location to determine which support agent or queue
          should handle the request.

    Skills → Route to support bot

        •   Skills allow a Power Virtual Agents bot to hand off or integrate with a Bot Framework
           bot.
        •  They enable reuse of capabilities and routing conversations to specialized bots.

  Why not the others?

        •   Variables: Store values temporarily but do not perform routing.
        •   Topics: Define conversation flows but are not specifically used to identify locations or
          connect to Bot Framework bots.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96624-exam-pl-200-topic-
4-question-26-discussion/

181 Question.
A company is building a Power Virtual Agents chatbot.

Users in the accounting department require access to collaborate with the building of the bot.
Users in the sales department require access to only chat with the bot.

---

## [Página 216](PL-200%20Q%26A.pdf#page=216) · texto nativo

You need to configure the bot.

Which sharing options should you use? To answer, drag the appropriate sharing options to the
correct requirements. Each sharing option may be used once, more than once, or not at all. You
may need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

        •  Accounting department → Users
          These users need to collaborate in building the bot. Bot collaboration/authoring is
            typically shared with specific users who need edit/manage access.
        •  Sales department → Active Directory security groups
          These users only need to chat with the bot. For chat access, the bot can be shared with
         an Azure Active Directory / Microsoft Entra security group, which is recommended
            for department-based access control. Microsoft documentation states that Copilot
          Studio agents can be shared for chat with individual users, security groups, or
         everyone in the organization, while collaboration is handled by inviting users to
           collaborate on the agent project.

Discussion: https://www.examtopics.com/discussions/microsoft/view/116273-exam-pl-200-
topic-4-question-27-discussion/

---

## [Página 217](PL-200%20Q%26A.pdf#page=217) · texto nativo

182 Question.
BodyYou create a Power Virtual Agents bot.

You observe that the bot is not able to recognize input from some users.

You need to configure the bot response for unrecognized input from users.

What are two possible ways to achieve this goal? Each correct answer presents a complete
solution.

NOTE: Each correct selection is worth one point.

    A. Connect to a different channel.
    B.  Display a system-defined error message.
   C. Use a fallback topic.
   D. Transfer to an agent.
Answer
   Correct Answer: C,D

   Explanation:

   When Power Virtual Agents (Microsoft Copilot Studio) cannot recognize a user's input, you can
   handle the situation by:

    •  C. Use a fallback topic
      A fallback topic is triggered when the bot cannot match the user's utterance to any existing
        topic. You can customize the response and guide the user to the appropriate next step.

    •  D. Transfer to an agent
      From the fallback topic, you can escalate the conversation to a live agent when the bot is
       unable to understand or resolve the customer's request.

  Why the other options are incorrect

    •   A. Connect to a different channel
      Channels determine where the bot is available (Teams, website, Facebook, etc.) and do not
        affect handling of unrecognized input.

    •   B. Display a system-defined error message
      Power Virtual Agents uses fallback topics rather than configurable system-defined error
      messages as the primary mechanism for handling unrecognized utterances.

Discussion: https://www.examtopics.com/discussions/microsoft/view/116274-exam-pl-200-
topic-4-question-28-discussion/

---

## [Página 218](PL-200%20Q%26A.pdf#page=218) · texto nativo

183 Question.
You plan to create a Power Virtual Agents bot.

The bot has the following requirements:

        •  Ensure that user responses are available to any topic.
        •  Recognize a list of words from spoken language of users.


You need to configure the bot.

Which features should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

        •  Global variable

---

## [Página 219](PL-200%20Q%26A.pdf#page=219) · texto nativo

o  Global variables can be accessed across multiple topics in the bot.

                o  This allows user responses collected in one topic to be available in any
                         other topic.

        •   Entity

                o   Entities are used to recognize and extract information from user input.

                o  They can represent a list of words, phrases, or synonyms (for example,
                         sport names, locations, product names, etc.).

Discussion: https://www.examtopics.com/discussions/microsoft/view/127101-exam-pl-200-
topic-4-question-29-discussion/

184 Question.
You deploy a Power Virtual Agents chatbot that integrates with Dynamics 365 Omnichannel for
Customer Service.

You observe that the chatbot is not able to recognize the questions asked by users.

You need to ensure that the chatbot can respond to unrecognized questions. The solution must
minimize administrative effort.

What should you do?

    A. Add a fallback topic.
    B.  Create new topics.
   C. Create an entity.
   D. Modify the Escalate system topic.
Answer
   Correct Answer: A

   Explanation:

   A fallback topic is specifically designed to handle situations where the chatbot cannot
    recognize or match a user's question to an existing topic. When an unrecognized question is
    received, the fallback topic is triggered automatically and can provide a response, ask clarifying
    questions, or route the user to an agent.

   Why the other options are incorrect:

    •   B. Create new topics
       This would require creating topics for every possible unrecognized question and does not
      minimize administrative effort.

---

## [Página 220](PL-200%20Q%26A.pdf#page=220) · texto nativo

•  C. Create an entity
        Entities help recognize and extract information from user input but do not handle
      unmatched intents.

    •  D. Modify the Escalate system topic
      The Escalate topic handles handoff scenarios, but unrecognized input is first handled by
       the fallback topic.

Discussion: https://www.examtopics.com/discussions/microsoft/view/130187-exam-pl-200-
topic-4-question-30-discussion/

185 Question.
A company deploys a chatbot that is embedded in a Power Pages website.

The company has the following requirements for the chatbot:


        •   Microsoft Entra ID users only must be able to use the chatbot when accessing sensitive
           data.
        •  The chatbot must be accessible only from the Power Pages website.


You need to recommend a solution that meets the requirements.

Which two options should you recommend? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

    A.  Enable Only for Teams authentication.
    B.  Configure a data loss prevention policy.
   C. Set up a new channel for the chatbot.
   D. Enable Manual authentication.
    E.  Enable web channel security.
Answer
   Correct Answer: D,E

   Explanation:

   D. Enable Manual authentication

        •  The requirement states that only Microsoft Entra ID users can use the chatbot when
          accessing sensitive data.
        •  Manual authentication allows the bot to authenticate users through Microsoft Entra ID
          (Azure AD) and identify authenticated users before granting access.

    E. Enable web channel security

---

## [Página 221](PL-200%20Q%26A.pdf#page=221) · texto nativo

•  The chatbot must be accessible only from the Power Pages website.
        •  Web channel security restricts where the bot can be embedded and accessed, helping
          prevent unauthorized use of the web channel from other sites.

  Why the other options are incorrect

    •   A. Enable Only for Teams authentication

         o  The chatbot is embedded in a Power Pages website, not limited to Microsoft
            Teams.

    •   B. Configure a data loss prevention policy

         o  DLP policies control connector usage and data movement, not chatbot
              authentication or website access restrictions.

    •  C. Set up a new channel for the chatbot

         o  Creating a channel does not enforce Entra ID authentication or restrict access to a
               specific website.

Discussion: https://www.examtopics.com/discussions/microsoft/view/132073-exam-pl-200-
topic-4-question-31-discussion/

186 Question
Exam PL-200 topic 5 question 1 discussion

Actual exam question from Microsoft's PL-200

Question #: 1
Topic #: 5

You are a Dynamics Sales administrator for a car dealership. The dealership uses only out-of-the-
box functionality. When a new car is sold, the salesperson uses a Word template to generate a
letter from the quote to thank the customer.
You need to determine if you can revise the template.
Which Word template change can you make?

    A. Add the Discount field conditionally.
    B. Format the table to have alternating color rows.
   C. Format the Created On field to a long date format.
   D. Add the address of the customer.

Answer
   Correct Answer: B

   Explanation:

For Dynamics 365 Sales Word templates (out-of-the-box functionality):

---

## [Página 222](PL-200%20Q%26A.pdf#page=222) · texto nativo

•   B. Format the table to have alternating color rows
      Word formatting changes such as table styles, fonts, colors, headers, and alternating row
       shading can be applied directly in the Word template.

   Wrong Answers:

    •   A. Add the Discount field conditionally
       Conditional logic (IF statements based on Dynamics data) is not supported through
      Dynamics 365 Word templates in the way required here.

    •  C. Format the Created On field to a long date format
      Date formatting is controlled by the data returned from Dynamics. Word templates do not
       support changing Dynamics date fields to custom formats such as "Friday, July 17, 2026".

    •  D. Add the address of the customer
      The template can only use fields included in the entity relationships selected when the
       template was created. Revising an existing template cannot add new related data sources
      such as a customer's address if it was not included originally.

Discussion: https://www.examtopics.com/discussions/microsoft/view/43014-exam-pl-200-topic-
5-question-1-discussion/

187 Question
Exam PL-200 topic 5 question 2 discussion

Actual exam question from Microsoft's PL-200

Question #: 2
Topic #: 5

You manage the Dynamics 365 Customer Service environment for an organization.
Microsoft SharePoint will not be deployed in the environment for a year.
You need to integrate Microsoft Office 365 solutions with the Dynamics 365 instance to help the
sales team with internal collaboration efforts.
Which three solutions can you currently implement? Each correct answer presents part of the
solution.
NOTE: Each correct selection is worth one point.

    A.  Microsoft Skype for Business
    B.  Microsoft Exchange Online
   C. Microsoft OneNote
   D. Microsoft Yammer
    E.  Microsoft OneDrive for Business

Answer
   Correct Answer: B,C,D

---

## [Página 223](PL-200%20Q%26A.pdf#page=223) · texto nativo

Explanation:

B. Microsoft Exchange Online

       •  Dynamics 365 integrates with Exchange Online for email, appointments, contacts, and
           tasks synchronization.
       •  SharePoint is not required.

C. Microsoft OneNote

       •  Dynamics 365 can integrate with OneNote to allow users to create and manage notes
          associated with records.
       •  The integration does not require SharePoint deployment.

D. Microsoft Yammer

       •  Yammer can be embedded within Dynamics 365 records to support collaboration and
          discussions around customer records.
       •  SharePoint is not required.

  Why the others are incorrect

A. Microsoft Skype for Business

       •  Skype for Business integration existed historically but was not considered a standard
         Dynamics 365 collaboration solution in this context and is not one of the supported
          answers.

E. Microsoft OneDrive for Business

       •  Document management and storage integration scenarios traditionally rely on
          SharePoint configuration. Since SharePoint will not be deployed for a year, this is not a
           current solution for the requirement.

Discussion: https://www.examtopics.com/discussions/microsoft/view/42420-exam-pl-200-topic-
5-question-2-discussion/

188 Question
Exam PL-200 topic 5 question 3 discussion

Actual exam question from Microsoft's PL-200

Question #: 3
Topic #: 5

HOTSPOT -
A company plans to implement AI Builder to add intelligence to several business processes.
Each business process uses different sources and produces different outputs.
You need to determine which AI Builder model types to use.

---

## [Página 224](PL-200%20Q%26A.pdf#page=224) · texto nativo

Which model types should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 225](PL-200%20Q%26A.pdf#page=225) · texto nativo

Explanation:

    1.  Entity extraction

       •  Used to identify and extract specific pieces of information (entities) from text.

       •  An age expressed as "twenty years old" is an entity that can be extracted from a
          paragraph.

    2. Form processing

           •  Designed to extract structured data from documents such as invoices, receipts, tax
              forms, and purchase orders.

           •    It can identify fields such as item names, quantities, and prices from invoices.

Discussion: https://www.examtopics.com/discussions/microsoft/view/42219-exam-pl-200-topic-
5-question-3-discussion/

189 Question
Exam PL-200 topic 5 question 4 discussion

Actual exam question from Microsoft's PL-200

Question #: 4
Topic #: 5

You create and publish a Power BI report that contains an embedded canvas app. The report will be
used by multiple people.
The canvas app has an issue that must be corrected.
You update the canvas app.
You need to ensure that the updated canvas app is available in the published Power BI report.
What should you do?

    A.  Manually refresh the data source on the published Power BI report
    B.  Publish the canvas app
   C. Publish the Power BI report from Power BI Desktop and reshare to any users
   D. Publish the Power BI report from Power BI Desktop

Answer
   Correct Answer: B

   Explanation:

When a canvas app is embedded in a Power BI report, the Power BI report references the app by
its App ID. If you make changes to the canvas app, those changes are not available to users until
the app is republished.

---

## [Página 226](PL-200%20Q%26A.pdf#page=226) · texto nativo

Once you publish the updated canvas app, the embedded version in the Power BI report
automatically uses the latest published version. There is no need to republish the Power BI report
or refresh its data source.

  Why the other options are incorrect

    •   A. Manually refresh the data source on the published Power BI report

         o  Refreshing data does not update the embedded canvas app.

    •  C. Publish the Power BI report from Power BI Desktop and reshare to any users

         o  Unnecessary. The report itself has not changed.

    •  D. Publish the Power BI report from Power BI Desktop

         o  Also unnecessary because only the canvas app was modified.

Discussion: https://www.examtopics.com/discussions/microsoft/view/54428-exam-pl-200-topic-
5-question-4-discussion/

190 Question
Exam PL-200 topic 5 question 5 discussion

Actual exam question from Microsoft's PL-200

Question #: 5
Topic #: 5

DRAG DROP -
You create a report by using Power BI Desktop and publish the report to the Power BI service. You
enable Power BI visualization embedding in a model-driven app.
You need to configure the model-driven app to display a Power BI tile.
Which three actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.

---

## [Página 227](PL-200%20Q%26A.pdf#page=227) · texto nativo

Select and Place:





Answer
   Correct Answer:





   Explanation:

To display a Power BI tile in a model-driven app:

---

## [Página 228](PL-200%20Q%26A.pdf#page=228) · texto nativo

•  A Power BI report visualization must first be pinned to a Power BI dashboard in the
      Power BI service.
    •   In the model-driven app (Dynamics 365), create a personal dashboard.
    •  Add a Power BI tile component and select the Power BI dashboard that contains the
       pinned tile.

The options "Share the dashboard with the appropriate user in the app" and "Ensure the
dashboard is available to the appropriate security roles" are not part of the required
configuration sequence for embedding the Power BI tile.

Discussion: https://www.examtopics.com/discussions/microsoft/view/54951-exam-pl-200-topic-
5-question-5-discussion/

191 Question
Exam PL-200 topic 5 question 6 discussion

Actual exam question from Microsoft's PL-200

Question #: 6
Topic #: 5

You use Power BI Desktop to configure Power BI reports.
You need to create a canvas app that displays user account information and include the app in a
Power BI report.
Which three actions should you perform? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

    A. From the Power Apps Insert menu, add a Power BI tile
    B. From the Power BI Desktop menu, insert a Power Apps visual and include the required
        fields in the Power Apps data
   C. Publish the report to the Power BI service
   D. Connect to Common Data Service from Power BI Desktop

Answer
   Correct Answer: B,C,D

   Explanation:

To embed a canvas app in a Power BI report, the process is:

    1.  D: Connect to Common Data Service (Dataverse) from Power BI Desktop to access the
       user account data.

    2.  B: Insert a Power Apps visual in Power BI Desktop and add the fields that will be passed
       to the app.

---

## [Página 229](PL-200%20Q%26A.pdf#page=229) · texto nativo

3. C : Publish the report to the Power BI service so the embedded Power Apps visual can be
      used and shared.

Discussion: https://www.examtopics.com/discussions/microsoft/view/54206-exam-pl-200-topic-
5-question-6-discussion/

192 Question
Exam PL-200 topic 5 question 7 discussion

Actual exam question from Microsoft's PL-200

Question #: 7
Topic #: 5

DRAG DROP -
A company uses Microsoft Dataverse to store sales data.
For the past few quarters, the company has experienced a decrease in sales revenue. The company
wants to improve sales forecasting.
The company plans to use AI Builder to implement the solution. You select fields that will be used
for prediction.
Which three actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.
Select and Place:

---

## [Página 230](PL-200%20Q%26A.pdf#page=230) · texto nativo

Answer
   Correct Answer:





   Explanation:

The requirement is to improve sales forecasting, which is a Prediction scenario in AI Builder.

After selecting the prediction fields:

        •   Train the Prediction model using the data stored in Dataverse.
        •   Publish the model so it is available for use.
        •  Consume the published model in Power Apps (or Power Automate) to generate
           predictions.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83456-exam-pl-200-topic-
5-question-7-discussion/

193 Question
Exam PL-200 topic 5 question 9 discussion

Actual exam question from Microsoft's PL-200

---

## [Página 231](PL-200%20Q%26A.pdf#page=231) · texto nativo

Question #: 9
Topic #: 5

You have a business process flow (BPF) that interacts with the Account entity.
You modify the BPF and add a new stage at the beginning.
You need to identify the impact of the new version on the existing account records.
What is the outcome in each scenario? To answer, select the appropriate options in the answer
area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:





   Explanation:

When you modify and activate a new version of a Business Process Flow (BPF):

        •   Existing records that are already associated with an active BPF instance continue to
         use the version they started with. They do not automatically switch to the new version.
        •  New records created after the new BPF version is activated use the new version of the
          BPF, including the newly added stage.

---

## [Página 232](PL-200%20Q%26A.pdf#page=232) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/60165-exam-pl-200-topic-
5-question-9-discussion/

194 Question
Exam PL-200 topic 5 question 10 discussion

Actual exam question from Microsoft's PL-200

Question #: 10
Topic #: 5


You are examining several processes to determine if you can automate the processes by using
Power Automate.
The processes must run without human intervention when possible.
You need to determine which flow type should be used for each process.
Which flow type should you use? To answer, drag the appropriate processes to the correct flow
types. Each process may be used once, more than once, or not at all. You may need to drag the
split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.
Select and Place:





Answer
   Correct Answer:





   Explanation:

        •  Attended desktop flow is used when a user is present and interacting with the
          process. In the leave request scenario, the automation interacts with a web page used
          by employees and involves a supervisor's approval process.

---

## [Página 233](PL-200%20Q%26A.pdf#page=233) · texto nativo

•  Unattended desktop flow is used when the process can run entirely without human
            intervention, using saved credentials to access applications and execute tasks
           automatically.

Scheduled cloud flow is not the best choice for either scenario because both require desktop/web
UI automation, which is handled by desktop flows rather than cloud flows.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60846-exam-pl-200-topic-
5-question-10-discussion/

195 Question
Exam PL-200 topic 5 question 11 discussion

Actual exam question from Microsoft's PL-200

Question #: 11
Topic #: 5

A company uses Microsoft Teams. You plan to create a Power Apps app for Microsoft Teams.
You need to determine the environment that will used by the app.
Which environment will the app use?

    A. An existing Dataverse environment that you select.
    B. An existing Dataverse for Teams environment that you select.
   C. A Dataverse environment that is automatically created for the team.
   D. A Dataverse for Teams environment that is automatically created for the team.

Answer
   Correct Answer: D

   Explanation:

When you create a Power Apps app directly within Microsoft Teams, Power Platform uses
Dataverse for Teams as the data platform.

    •    If the team does not already have a Dataverse for Teams environment, one is automatically
      created for that specific team.
    •  The app is then stored and managed within that Dataverse for Teams environment.

  Why the other options are incorrect

    •   A. An existing Dataverse environment that you select
      Apps created in Teams do not use a standard Dataverse environment selected manually.

    •   B. An existing Dataverse for Teams environment that you select
      The environment is associated with the Team and is not manually selected.

---

## [Página 234](PL-200%20Q%26A.pdf#page=234) · texto nativo

•  C. A Dataverse environment that is automatically created for the team
      The automatically created environment is Dataverse for Teams, not a full Dataverse
       environment.

Discussion: https://www.examtopics.com/discussions/microsoft/view/61546-exam-pl-200-topic-
5-question-11-discussion/

196 Question
Exam PL-200 topic 5 question 12 discussion

Actual exam question from Microsoft's PL-200

Question #: 12
Topic #: 5

You create a canvas app for a sales team. The app has an embedded Power BI tile that shows year-
to-date sales. Sales users do not have access to the data source that the tile uses.
Sales team users must be able to see data in the Power BI tile. You must minimize the level of
permissions that you grant and minimize administrative overhead.
You need to share another Power BI component to make the data visible.
What should you share?

    A. The Power BI dataset the tile uses as a data source.
    B. The Power BI workspace that includes the tile.
   C. The Power BI dashboard that includes the tile.

Answer
   Correct Answer: C

   Explanation:

When a Power BI tile is embedded in a canvas app, users must have access to the Power BI
content that contains the tile.

To provide access with the least privilege and minimal administrative overhead, share the
dashboard containing the tile:

        •  Users can view the tile.
        •  No need to grant broader access to the entire workspace.
        •   Simpler than managing dataset permissions directly.

  Why the other options are incorrect

    •   A. The Power BI dataset the tile uses as a data source

         o  Grants access to the underlying data, which is more permission than necessary.

    •   B. The Power BI workspace that includes the tile

---

## [Página 235](PL-200%20Q%26A.pdf#page=235) · texto nativo

o  Workspace access provides broader permissions and creates unnecessary
               administrative overhead.

Discussion: https://www.examtopics.com/discussions/microsoft/view/62989-exam-pl-200-topic-
5-question-12-discussion/

197 Question
Exam PL-200 topic 5 question 13 discussion

Actual exam question from Microsoft's PL-200

Question #: 13
Topic #: 5

You have a model-driven app. You create five Microsoft Excel templates for analyzing customer
data.
Four of the templates must be available to all users. The remaining template must be available only
to you. You configure the appropriate security roles for users.
You need to determine how to upload the Excel templates.
Which method should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 236](PL-200%20Q%26A.pdf#page=236) · texto nativo

Explanation:

Organization-wide Excel templates

    •  Uploaded through Settings → Templates → Document Templates.
    •   Available to all users who have the appropriate security permissions.

Personal Excel templates

    •  Created or uploaded from an entity view using Excel Templates.
    •   Available only to the user who creates them.

Discussion: https://www.examtopics.com/discussions/microsoft/view/63960-exam-pl-200-topic-
5-question-13-discussion/

198 Question
Exam PL-200 topic 5 question 14 discussion

Actual exam question from Microsoft's PL-200

Question #: 14
Topic #: 5

You configure an alert in Power BI.
You need to alert users when the value of a tile exceeds a threshold. To answer, select the
appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 237](PL-200%20Q%26A.pdf#page=237) · texto nativo

Hot Area:





Answer
   Correct Answer:





   Explanation:

    •  Power BI data alerts can be used as triggers for flows in Power Automate. When a
      dashboard tile exceeds a configured threshold, Power Automate can start a process
       automatically.
    •  Data alerts are personal. An alert is visible only to the user who creates it, even if other
       users have access to the same dashboard.

Discussion: https://www.examtopics.com/discussions/microsoft/view/43126-exam-pl-200-topic-
5-question-14-discussion/

199 Question
Exam PL-200 topic 5 question 15 discussion

---

## [Página 238](PL-200%20Q%26A.pdf#page=238) · texto nativo

Actual exam question from Microsoft's PL-200

Question #: 15
Topic #: 5

You are using Power BI to build a dashboard for a company.
You must make the dashboard available to a specific set of users, including employees and five
external users. The number of employees that require access to the dashboard varies, but is
usually less than 100.
Employees and external users must not be permitted to share the dashboard with other users.
You need to share the dashboard with the employees and external users.
Which three actions should you perform? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

    A. Create a dynamic distribution list. Add all users to the distribution list and use the list to
   share the dashboard.

    B. Sign into the Power BI service. Open the dashboard and select Share.

   C. Enter the individual email address of internal and external users.

   D. Sign into Power BI Desktop. Open the dashboard and select Share.

    E. Clear the Allow recipients to share your dashboard (or report) option.

    F. Create a distribution list. Add all users to the distribution list and use the list to share the
   dashboard.

Answer
   Correct Answer: B,C,E

   Explanation:

To share a Power BI dashboard with a specific set of internal and external users while preventing
further sharing:

    B. Sign into the Power BI service. Open the dashboard and select Share.

         o  Dashboards are shared from the Power BI Service, not from Power BI Desktop.

   C. Enter the individual email address of internal and external users.

         o  Since the audience is relatively small (usually fewer than 100 users plus 5 external
               users), directly specifying users is appropriate.

    E. Clear the Allow recipients to share your dashboard (or report) option.

         o  This prevents recipients from sharing the dashboard with other users.

  Why the other options are incorrect

---

## [Página 239](PL-200%20Q%26A.pdf#page=239) · texto nativo

•   A. Create a dynamic distribution list

         o  Not required and may not properly handle external users.

    •  D. Sign into Power BI Desktop. Open the dashboard and select Share

         o  Dashboards are shared from the Power BI Service, not Power BI Desktop.

    •   F. Create a distribution list

         o  Adds administration overhead and is unnecessary for a relatively small audience,
               especially when external users are involved.

Discussion: https://www.examtopics.com/discussions/microsoft/view/41809-exam-pl-200-topic-
5-question-15-discussion/

200 Question
Exam PL-200 topic 5 question 16 discussion

Actual exam question from Microsoft's PL-200

Question #: 16
Topic #: 5

You create a report by using Power BI Desktop and a Power BI dataset that is connected to Azure
SQL Database.
Multiple groups of employees will use the report.
You need to ensure that each group of employees can see only data that pertains to their group.
What should you do?

    A.  Create and assign field security profiles.
    B.  Create and assign Common Data Service security roles.
   C. Create and assign roles by using row-level security.

Answer
   Correct Answer: C

   Explanation:

Row-Level Security (RLS) in Power BI restricts data access for specific users. You can create roles
that filter the data returned from the Azure SQL Database dataset so that each employee group
sees only its own data.

For example:

    •   Sales East sees only East region data.
    •   Sales West sees only West region data.
    •  Management can see all data.

---

## [Página 240](PL-200%20Q%26A.pdf#page=240) · texto nativo

Why the other options are incorrect

    •   A. Create and assign field security profiles

         o   Field Security Profiles are a Dataverse feature used to secure specific columns, not
            Power BI report data.

    •   B. Create and assign Common Data Service security roles

         o  Dataverse (formerly Common Data Service) security roles control access to
             Dataverse data, not data displayed in a Power BI report sourced from Azure SQL
             Database

Discussion: https://www.examtopics.com/discussions/microsoft/view/43129-exam-pl-200-topic-
5-question-16-discussion/

201 Question
Exam PL-200 topic 5 question 17 discussion

Actual exam question from Microsoft's PL-200

Question #: 17
Topic #: 5

A company uses Microsoft Dataverse manage account and contact information.
The company plans to use the AI Builder model to make key business decisions.
You need to integrate prebuilt AI Builder models with Power Automate flows.
Which models should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 241](PL-200%20Q%26A.pdf#page=241) · texto nativo

Explanation:

    •   Extract key phrases from a PDF document → Text recognition model and key phrase
       extraction model
         o  A PDF must first be converted into text using Text Recognition (OCR). After the text
                  is extracted, the Key Phrase Extraction model identifies important phrases and
              concepts.
    •  Determine the likelihood that customers will purchase additional products →
       Prediction model
         o  This is a forecasting/probability scenario where AI Builder predicts a future outcome
            based on historical data.

Discussion: https://www.examtopics.com/discussions/microsoft/view/42138-exam-pl-200-topic-
5-question-17-discussion/

202 Question
Exam PL-200 topic 5 question 18 discussion

Actual exam question from Microsoft's PL-200

Question #: 18
Topic #: 5

The sales manager receives a list of leads from a partner company monthly. The field names that
are provided do not match the fields in Microsoft Dataverse tables. A data map does not exist.
You need to import the leads without changing the data from the partner company.
What should you do?

    A.  Create a data map on the first import by using the Import Data wizard.
    B. Add a template for Import Data.
   C. Use Import Field Translations.
   D. Create a data map in Data Management.

---

## [Página 242](PL-200%20Q%26A.pdf#page=242) · texto nativo

Answer
   Correct Answer: A

   Explanation:

The partner company provides the lead file every month, but the field names do not match the
Dataverse fields.

A data map allows you to map the source file columns to the corresponding Dataverse fields.
When you create the data map during the first import using the Import Data Wizard, the mapping
can be saved and reused for future imports, eliminating the need to modify the partner's file.

  Why the other options are incorrect

    •   B. Add a template for Import Data
       Import templates help users prepare data but do not solve the field name mismatch
       problem.

    •  C. Use Import Field Translations
        Field translations are for multilingual labels, not data import mapping.

    •  D. Create a data map in Data Management
      Data maps are typically created and saved during the import process using the Import Data
       Wizard. The scenario specifically starts without an existing data map.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60497-exam-pl-200-topic-
5-question-18-discussion/

203 Question
Exam PL-200 topic 5 question 22 discussion

Actual exam question from Microsoft's PL-200

Question #: 22
Topic #: 5

You are creating Power BI reports for a company.
A company that has a model-driven app wants to use Power BI reports within the app. You create
the reports.
You need to ensure that these reports are available within the app.
Which two actions should you perform? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.

    A.  Share the Power BI report to all users.
    B. Add the Power BI report to the Site Map dashboards.
   C. Create a PCF file.
   D. Use the native reports in model-driven apps.

---

## [Página 243](PL-200%20Q%26A.pdf#page=243) · texto nativo

E. Add the Power BI report to a dashboard in the model-driven app.

Answer
   Correct Answer: B,E

   Explanation:

There are two supported ways to make Power BI reports available within a model-driven app:

        •   B: Add the Power BI report to the Site Map dashboards
                o  This enables users to access the Power BI report directly from the
                        model-driven app navigation.
        •   E: Add the Power BI report to a dashboard in the model-driven app
                o  Power BI reports can be embedded in model-driven app dashboards.

  Why the other options are incorrect

    A. Share the Power BI report to all users

       •  Users need permission to view the report, but sharing alone does not make it appear
           within the model-driven app.

   C. Create a PCF file

       •  PCF controls are not required to embed standard Power BI reports in model-driven
          apps.

   D. Use the native reports in model-driven apps

       •   Native Dynamics reports are different from Power BI reports.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83457-exam-pl-200-topic-
5-question-22-discussion/

204 Question
Exam PL-200 topic 5 question 23 discussion

Actual exam question from Microsoft's PL-200

Question #: 23
Topic #: 5

A company is training an Al model using a custom table to determine the amount of time it takes to
deliver a package based on several key fields.
The testing data used to train the model is used for all training and regression testing scenarios and
is considered complete data.
The trained model predicts a 2 percent variance between the estimated delivery time and the
actual delivery time of packages.
The executive sponsors reject the model because the actual variance is at 15 percent.

---

## [Página 244](PL-200%20Q%26A.pdf#page=244) · texto nativo

You need to address the sponsors' concern.
What should you do?

    A.  Replace the training data with real-world data.
    B. Reduce the size of the data used within the model.
   C. Increase the size of the data used with the model.
   D. Use sample training data from Microsoft.

Answer
   Correct Answer: A

   Explanation:

The key issue is that the model was trained and tested using the same complete testing dataset,
resulting in a predicted variance of only 2%, while the actual real-world variance is 15%.

This indicates that the model is not generalizing well to real-world conditions and may be
overfitting to the training/testing data.

To address the executives' concern, you should train and validate the model using real-world
historical data that accurately reflects actual delivery conditions and variability.

  Why the other options are incorrect

    •   B. Reduce the size of the data used within the model

         o  Less data generally reduces model accuracy.

    •  C. Increase the size of the data used with the model

         o  More data can help, but the main problem is that the data is not representative of
               real-world outcomes.

    •  D. Use sample training data from Microsoft

         o  Sample data is generic and would not reflect the company's delivery processes.

Discussion: https://www.examtopics.com/discussions/microsoft/view/80222-exam-pl-200-topic-
5-question-23-discussion/

205 Question
Exam PL-200 topic 5 question 24 discussion

Actual exam question from Microsoft's PL-200

Question #: 24
Topic #: 5

A bank uses Power BI visualizations to help determine whether they should loan money to a
customer. The bank has three different visuals that are part of a

---

## [Página 245](PL-200%20Q%26A.pdf#page=245) · texto nativo

Power BI report. The bank uses a set of four risk variables that indicate whether the customer is
creditworthy.
You must create a mechanism so that bank employees can change the values of the four risk
variables. Changes to the value of any variable must cause the three visualizations to update.
You need to create the solution.
Which action should you perform? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:





   Explanation:

To allow users to change input values directly from a Power BI report and have the related
visuals update, you use the Power Apps visual in Power BI. A canvas app can be embedded in the
Power BI report and used to write/update values in the underlying data source; the Power BI visuals
can then refresh based on those changes.

Discussion: https://www.examtopics.com/discussions/microsoft/view/84805-exam-pl-200-topic-
5-question-24-discussion/

---

## [Página 246](PL-200%20Q%26A.pdf#page=246) · texto nativo

206 Question
Exam PL-200 topic 5 question 25 discussion

Actual exam question from Microsoft's PL-200

Question #: 25
Topic #: 5

You create a JavaScript web resource named MyBusinessLogic. The code it contains uses
functionality from a third-party JavaScript library.
You notice that an independent software vendor (ISV) solution uses the same third-party library in
their managed solution.
You plan to deploy your solution to other environments by using a managed solution. The ISV
solution might not be installed in the other environments.
You need to package the solution for deployment
What are two ways to achieve this goal? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.

    A.  Create a new JavaScript web resource by using the code from the third-party library. Add
       the new JavaScript web resource along with MyBusinessLogic to the solution.
    B. Add a copy of the JavaScript library from the ISV to the solution along with
       MyBusinessLogic.
   C. Add the code from the third-party JavaScript library to MyBusinessLogic. Add
       MyBusinessLogic to the solution.
   D. Add only the third-party JavaScript web resource to the solution.

Answer
   Correct Answer: A,C

   Explanation:

Your managed solution must be self-contained because the ISV solution (which contains the
third-party library) may not exist in the target environments.

    •   A. Create a new JavaScript web resource by using the code from the third-party library.
     Add the new JavaScript web resource along with MyBusinessLogic to the solution.

        •   This ensures the third-party library is deployed with your solution.

        •  MyBusinessLogic can reference the library web resource.

        •   This is a best practice because it keeps the library separate and reusable.

    •  C. Add the code from the third-party JavaScript library to MyBusinessLogic. Add
      MyBusinessLogic to the solution.

        •   This also makes the solution self-contained.

---

## [Página 247](PL-200%20Q%26A.pdf#page=247) · texto nativo

•  The library code is packaged directly within the custom JavaScript file.

  Why the others are incorrect

    •   B. Add a copy of the JavaScript library from the ISV to the solution along with
      MyBusinessLogic.

        •  You cannot reliably package components owned by another managed solution.

        •  The ISV solution may not be present in the target environment.

    •  D. Add only the third-party JavaScript web resource to the solution.

        •  MyBusinessLogic is also required because it contains the custom business logic.

        •   Deploying only the library would not provide the required functionality.

Discussion: https://www.examtopics.com/discussions/microsoft/view/84806-exam-pl-200-topic-
5-question-25-discussion/

207 Question
Exam PL-200 topic 5 question 26 discussion

Actual exam question from Microsoft's PL-200

Question #: 26
Topic #: 5

A company creates a canvas app.

The app requires near real-time data from an accounting system that resides in a customer's data
center.

You need to implement a solution for the app.

What should you create?

    A. On-premises data gateway
    B.  Azure DevOps pipeline
   C. Data integration project
   D. Power Pages

Answer
   Correct Answer: A

   Explanation:

The canvas app requires near real-time access to data that resides in a customer's on-
premises data center.

---

## [Página 248](PL-200%20Q%26A.pdf#page=248) · texto nativo

An On-premises Data Gateway enables Power Apps, Power Automate, and Power BI to securely
connect to on-premises data sources without moving the data to the cloud.

  Why the other options are incorrect

    •   B. Azure DevOps pipeline

         o  Used for application lifecycle management (ALM) and deployments, not data
               connectivity.

    •  C. Data integration project

         o  Used for data migration and synchronization scenarios, not direct near real-time
             access from a canvas app.

    •  D. Power Pages

         o  Used to build external-facing websites, not to connect Power Apps to on-premises
               data.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96979-exam-pl-200-topic-
5-question-26-discussion/

208 Question
Exam PL-200 topic 5 question 27 discussion

Actual exam question from Microsoft's PL-200

Question #: 27
Topic #: 5

You create a canvas app that uses data from a Microsoft SQL Server database.

You use a dataflow to move some of the data from the database to Microsoft Dataverse. Users will
filter the data by using the app.

You need to filter data in the dataflow and in the canvas app.

Which tools should you use? To answer, drag the appropriate tools to the correct requirements.
Each tool may be used once, more than once, or not at all. You may need to drag the split bar
between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

---

## [Página 249](PL-200%20Q%26A.pdf#page=249) · texto nativo

Answer
   Correct Answer:





   Explanation:

        •  Power Query is used in dataflows to transform, shape, and filter data before loading it
            into Dataverse.
        •  Power Fx is the formula language used in canvas apps to filter, sort, and manipulate
          data displayed to users.

  Why the others are incorrect

        •  T-SQL: Used for querying SQL Server directly, not for filtering data within a Power
           Platform dataflow or canvas app.
        •  Kusto: Used with Azure Data Explorer, Log Analytics, and Microsoft Fabric/Kusto
          databases, not canvas apps or Dataverse dataflows.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96144-exam-pl-200-topic-
5-question-27-discussion/

---

## [Página 250](PL-200%20Q%26A.pdf#page=250) · texto nativo

209 Question
Exam PL-200 topic 5 question 28 discussion

Actual exam question from Microsoft's PL-200

Question #: 28
Topic #: 5

You have a canvas app with an embedded Power BI tile.

You share the canvas app. Users report that they are unable to access the Power BI content.

You need to determine why users are unable to access the content.

What is the cause of the user's problems?

    A. The Power BI dashboard is not shared.
    B. The Power BI connection is not shared.
   C. The Power BI Display mode property on the Power BI tiles is set to Disabled.
   D. The Power BI interactions property on the Power BI tiles is set to Off.

Answer
   Correct Answer: A

   Explanation:

When a Power BI tile is embedded in a canvas app, sharing the canvas app alone does not grant
access to the underlying Power BI content.

Users must also have permission to the Power BI content (dashboard/report) that contains the tile.
If the Power BI dashboard has not been shared, users will be unable to view the embedded Power
BI data.

  Why the other options are incorrect

    •   B. The Power BI connection is not shared

         o  Power BI connections are not typically the cause of users being unable to see
           embedded Power BI tiles.

    •  C. The Power BI Display mode property on the Power BI tiles is set to Disabled

         o  This affects interaction with the control, not user authorization to view the content.

    •  D. The Power BI interactions property on the Power BI tiles is set to Off

         o  This disables interaction with the tile but does not prevent users from accessing the
            Power BI content.

---

## [Página 251](PL-200%20Q%26A.pdf#page=251) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/96036-exam-pl-200-topic-
5-question-28-discussion/

210 Question
Exam PL-200 topic 5 question 29 discussion

Actual exam question from Microsoft's PL-200

Question #: 29
Topic #: 5

You plan to create a Power BI dataflow.

The Power BI dataflow has the following requirements:


       •  Be able to create a copy of the dataflow to separate Power BI workspaces.
       •  Schedule the dataflow to update every day at 11:00 AM.


You need to configure the dataflow.

What should you do? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 252](PL-200%20Q%26A.pdf#page=252) · texto nativo

Answer
   Correct Answer:

---

## [Página 253](PL-200%20Q%26A.pdf#page=253) · texto nativo

Explanation:

       •  Export the JSON file enables you to copy and reuse a Power BI dataflow in another
         workspace by importing the dataflow definition.
       •  To run the dataflow every day at 11:00 AM, configure automatic refresh (scheduled
            refresh) in the dataflow settings.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96037-exam-pl-200-topic-
5-question-29-discussion/

211 Question
Exam PL-200 topic 5 question 30 discussion

Actual exam question from Microsoft's PL-200

Question #: 30
Topic #: 5

You plan to create a dataflow to import data into Microsoft Dataverse by using Power Query.

The dataflow has the following requirements:

    •  A table of aggregated data must be created in dataflow storage.
    •  A unique identifier must be created for the table.


You need to configure the dataflow.

Which solutions should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 254](PL-200%20Q%26A.pdf#page=254) · texto nativo

Answer
   Correct Answer:





   Explanation:

    •  Computed entity: Used in Power BI/Dataflows to create derived or aggregated data based
      on other entities stored in the dataflow. It performs transformations and aggregations in
       dataflow storage.
    •   Alternate key: Provides a unique identifier for records in Dataverse besides the primary
      GUID. It can be used to uniquely identify rows during imports and integrations.

---

## [Página 255](PL-200%20Q%26A.pdf#page=255) · texto nativo

Why the other options are incorrect

    •  Fact table
         o  A data warehousing concept, not a specific dataflow feature for creating aggregated
               data.
    •  Merge query
         o  Combines data from multiple queries but does not specifically create an
              aggregated table in dataflow storage.
    •  Linked entity
         o  References another entity and does not create a new aggregated dataset.
    •  Key column
         o  Not the Dataverse mechanism used to define a unique identifier for integration
              scenarios.

Discussion: https://www.examtopics.com/discussions/microsoft/view/114076-exam-pl-200-
topic-5-question-30-discussion/

212 Question
Exam PL-200 topic 5 question 31 discussion

Actual exam question from Microsoft's PL-200

Question #: 31
Topic #: 5

You plan to create a dataflow by using Power Query to transform the data.

You observe that some cells display an error instead of the expected data.

You need to obtain more details about the errors.

What should you do?

    A. Use the App Checker.
    B.  Select the cell with the error.
   C. Use the Flow Checker.
   D. Select the row that includes the cell with the error.
    E. Use the Advanced Editor.

Answer
   Correct Answer: B

   Explanation:

In Power Query, when a cell contains an error value, you can click/select that specific error cell to
view detailed information about the error, including:

---

## [Página 256](PL-200%20Q%26A.pdf#page=256) · texto nativo

•   Error type
    •   Error message
    •   Details about the failed transformation step

  Why the other options are incorrect

    •   A. Use the App Checker

         o  App Checker is used in Power Apps, not Power Query.

    •  C. Use the Flow Checker

         o  Flow Checker is used in Power Automate.

    •  D. Select the row that includes the cell with the error

         o   Error details are associated with the specific cell, not the entire row.

    •   E. Use the Advanced Editor

         o  Advanced Editor shows the M code but is not the primary tool for viewing details of a
               specific cell error.

Discussion: https://www.examtopics.com/discussions/microsoft/view/118068-exam-pl-200-
topic-5-question-31-discussion/

213 Question
Exam PL-200 topic 5 question 32 discussion

Actual exam question from Microsoft's PL-200

Question #: 32
Topic #: 5

A company creates a model-driven app.

Users require access to a Power BI report that is embedded in the app.

You need to configure the app.

Where should you add the report?

    A. XML report
    B. Dashboard
   C. Business rule
   D. Power Automate cloud flow

Answer
   Correct Answer: B

---

## [Página 257](PL-200%20Q%26A.pdf#page=257) · texto nativo

Explanation:

In a model-driven app, Power BI reports are typically surfaced by embedding them in a
dashboard.

        •  You can add a Power BI report or Power BI tile to a model-driven app dashboard.
        •  Users can then view the report directly within the app.

  Why the other options are incorrect

    •   A. XML report
      Used for legacy SQL Server Reporting Services (SSRS) reports, not Power BI reports.

    •  C. Business rule
       Business rules enforce logic and validation, not report display.

    •  D. Power Automate cloud flow
      Flows automate processes and do not host Power BI reports.

Discussion: https://www.examtopics.com/discussions/microsoft/view/120590-exam-pl-200-
topic-5-question-32-discussion/

214 Question
Exam PL-200 topic 5 question 33 discussion

Actual exam question from Microsoft's PL-200

Question #: 33
Topic #: 5

A company is implementing Microsoft Power Platform solutions.

The company requests information on the features that are supported by Power Fx.

You need to identify the features of Power Fx.

What should you identify?

    A.   It uses imperative and declarative logic.
    B.   It uses an undefined value for uninitialized variables.
   C.  It uses a plug-in.
   D.  It uses the model-driven app formula language.

Answer
   Correct Answer: A

   Explanation:

---

## [Página 258](PL-200%20Q%26A.pdf#page=258) · texto nativo

Power Fx is the low-code formula language used across Microsoft Power Platform, especially in
canvas apps. It supports:

        •   Declarative logic for defining what a control should display (similar to Excel formulas).
        •  Imperative logic for actions and behavior, such as button selections and data updates.

  Why the other options are incorrect

    •   B. It uses an undefined value for uninitialized variables.
      Power Fx uses Blank(), not an undefined value concept like some programming languages.

    •  C. It uses a plug-in.
       Plug-ins are Dataverse server-side extensions written in .NET and are unrelated to Power
        Fx.

    •  D. It uses the model-driven app formula language.
      Power Fx originated in canvas apps and is now expanding across Power Platform, but it is
       not specifically "the model-driven app formula language."

Discussion: https://www.examtopics.com/discussions/microsoft/view/123772-exam-pl-200-
topic-5-question-33-discussion/

215 Question
Exam PL-200 topic 5 question 34 discussion

Actual exam question from Microsoft's PL-200

Question #: 34
Topic #: 5

You use a dataflow to import data into Microsoft Dataverse.

The data uses the following schema:





The data must load in the least amount of time.

You need to configure the incremental refresh settings for the dataflow.

Which columns should you use? To answer, select the appropriate options in the answer area.

---

## [Página 259](PL-200%20Q%26A.pdf#page=259) · texto nativo

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

For the fastest incremental refresh:

•   Filter field = createdon
           o  Incremental refresh partitions data based on a date/time column.
           o  createdon is the appropriate Date and Time field for identifying new records.
•  Detect data changes = versionnumber
           o  versionnumber is a Big Integer that changes whenever a record is updated.
           o  Using it is more efficient than scanning date columns and provides optimal
               change detection performance.

---

## [Página 260](PL-200%20Q%26A.pdf#page=260) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/128082-exam-pl-200-
topic-5-question-34-discussion/

216 Question
Exam PL-200 topic 5 question 35 discussion

Actual exam question from Microsoft's PL-200

Question #: 35
Topic #: 5

A company uses Dataverse to store the names of contacts. The company uses a shared Microsoft
Excel file to collect the data.

The company requires that the contacts be added to Dataverse automatically every day.

You need to identify which tools are required to create and perform the import.

What should you use? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 261](PL-200%20Q%26A.pdf#page=261) · texto nativo

Explanation:

•  Dataflows are used to create repeatable, scheduled imports into Dataverse from sources such
   as Excel files stored in OneDrive or SharePoint.
•  Power Query is used within the dataflow to connect to the shared Excel file, transform the
    data, and load it into Dataverse.
•  Because the import must run automatically every day, a Dataflow is the appropriate
   mechanism rather than a one-time Import Wizard or Import from Excel.

Discussion: https://www.examtopics.com/discussions/microsoft/view/123812-exam-pl-200-
topic-5-question-35-discussion/

217 Question
Exam PL-200 topic 5 question 36 discussion

Actual exam question from Microsoft's PL-200

Question #: 36
Topic #: 5

A company is implementing Microsoft Power Platform solutions.

The company requests information on the features that are supported by Power Fx.

You need to identify the features of Power Fx.

What should you identify?

    A.   It is available for purchase through a Microsoft reseller.
    B.   It uses an undefined value for uninitialized variables.
   C.  It uses formulas that are similar to Microsoft Excel formulas.
   D.  It uses synchronous data operations.

---

## [Página 262](PL-200%20Q%26A.pdf#page=262) · texto nativo

Answer
   Correct Answer: C

   Explanation:

Power Fx is the low-code formula language used in Microsoft Power Platform, especially in Canvas
Apps. Its syntax and behavior are intentionally designed to be familiar to users of Microsoft Excel.

Examples:

        •  Sum()
        •   Filter()
        •    If()
        •  LookUp()

These formulas closely resemble Excel functions and make app development easier for business
users.

  Why the other options are incorrect

    •   A. It is available for purchase through a Microsoft reseller.
      Power Fx is a language, not a licensable product.

    •   B. It uses an undefined value for uninitialized variables.
      Power Fx uses Blank() to represent no value.

    •  D. It uses synchronous data operations.
      Power Fx supports asynchronous behavior and does not rely exclusively on synchronous
       operations.

Discussion: https://www.examtopics.com/discussions/microsoft/view/148698-exam-pl-200-
topic-5-question-36-discussion/

218 Question
Exam PL-200 topic 5 question 37 discussion

Actual exam question from Microsoft's PL-200

Question #: 37
Topic #: 5

A company is implementing Microsoft Power Platform solutions.

The company requests information on the features that are supported by Power Fx.

You need to identify the features of Power Fx.

What should you identify?

---

## [Página 263](PL-200%20Q%26A.pdf#page=263) · texto nativo

A.   It uses imperative and declarative logic.
    B.   It is available for purchase through a Microsoft reseller.
   C.  It uses an undefined value for uninitialized variables.
   D.  It provides a manual compiler.

Answer
   Correct Answer: A

   Explanation:

Power Fx supports both:

        •   Declarative logic: Similar to Excel formulas, where you describe what a value should
           be.
        •  Imperative logic: Used in behavior formulas such as button actions (OnSelect), where
         you specify a sequence of actions to perform.

  Why the other options are incorrect

    •   B. It is available for purchase through a Microsoft reseller.
      Power Fx is a programming language within Power Platform, not a product that is
      purchased separately.

    •  C. It uses an undefined value for uninitialized variables.
      Power Fx uses Blank() to represent a missing or uninitialized value rather than an undefined
       value.

    •  D. It provides a manual compiler.
      Power Fx does not provide a manual compiler feature.

Discussion: https://www.examtopics.com/discussions/microsoft/view/150235-exam-pl-200-
topic-5-question-37-discussion/


219 Question
Exam PL-200 topic 6 question 1 discussion

Actual exam question from Microsoft's PL-200

Question #: 1
Topic #: 6

HOTSPOT -
You create a Power Platform help Desk solution.
You need to create a dashboard that displays information on help desk cases that are handled
each week.
Which dashboard components should you use? To answer, select the appropriate options in the

---

## [Página 264](PL-200%20Q%26A.pdf#page=264) · texto nativo

answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:

---

## [Página 265](PL-200%20Q%26A.pdf#page=265) · texto nativo

Explanation:

    •  System charts are organization-wide and can be shared with all users. They support chart
       types such as tag charts, stacked column charts, and doughnut charts.
    •  Personal dashboards can include Power BI visualizations and can display charts based
      on personal views created by users.
    •  A chart based on a user-created (personal) view cannot be a system chart because system
       charts require system views.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60492-exam-pl-200-topic-
6-question-1-discussion/

220 Question
Exam PL-200 topic 6 question 2 discussion

Actual exam question from Microsoft's PL-200

---

## [Página 266](PL-200%20Q%26A.pdf#page=266) · texto nativo

Question #: 2
Topic #: 6

You create a Power Automate flow as part of a managed solution. The flow alerts users when files
are uploaded to a SharePoint location.
Files are uploaded to SharePoint at a much higher rate than expected. Users report that they
receive too many notifications about uploaded files.
You need to stop the flow and correct the issue.
What should you do? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer
   Correct Answer:





   Explanation:

Disable the flow from the Power Automate solution

       •  Because the flow is part of a managed solution, it should be managed from the
          Solutions area in Power Automate rather than from Azure.
       •  Azure portal is not used to enable/disable Power Automate cloud flows.

Run the Flow checker and then use the Test feature on the updated flow

       •  Flow checker validates the flow for errors and warnings.

---

## [Página 267](PL-200%20Q%26A.pdf#page=267) · texto nativo

•  Test verifies that the updated flow behaves correctly before it is turned back on.
       •  The flow should remain disabled while testing and validation are performed.

Discussion: https://www.examtopics.com/discussions/microsoft/view/85754-exam-pl-200-topic-
6-question-2-discussion/

221 Question
Exam PL-200 topic 6 question 3 discussion

Actual exam question from Microsoft's PL-200

Question #: 3
Topic #: 6

You create a new independent software vendor (ISV) solution for a Power Apps app.
The Power Apps solution will be imported into multiple customer environments. The environments
will have a large variety of solutions and publishers.
You need to avoid naming conflicts during solution import.
Which element should you configure?

    A. Package type
    B.  Configuration page
   C. Marketplace
   D.  Prefix
    E.  Version

Answer
   Correct Answer: D

   Explanation:

In Power Apps and Dataverse solutions, the publisher prefix is used as part of the schema name
for components such as:

       •  Tables (entities)
       •  Columns (attributes)
       •  Choices
       •  Forms
       •  Views
       •  Other solution components

Using a unique prefix (for example, contoso_ or isv_) helps prevent naming conflicts when the
solution is imported into customer environments that may already contain solutions from other
publishers.

---

## [Página 268](PL-200%20Q%26A.pdf#page=268) · texto nativo

For an ISV solution deployed to many customers, defining a unique publisher prefix is a best
practice.

Discussion: https://www.examtopics.com/discussions/microsoft/view/80526-exam-pl-200-topic-
6-question-3-discussion/

222 Question
Exam PL-200 topic 6 question 4 discussion

Actual exam question from Microsoft's PL-200

Question #: 4
Topic #: 6

A company has employees in France, Mexico, and the United States. You are creating a Power
Apps app to allow users to add client records to Microsoft
Dataverse. The default language for the company is English.
The company wants the app to display each local language.
You need to add the Spanish and French languages.
Which four actions should you perform in sequence for each language? To answer, move the
appropriate actions from the list of actions to the answer area and arrange them in the correct
order.
Select and Place:





Answer
   Correct Answer:

---

## [Página 269](PL-200%20Q%26A.pdf#page=269) · texto nativo

Explanation:

To localize a Power Apps/Dataverse solution:

       •   Translation export/import is performed on an unmanaged solution.
       •  Export translations generates the translation file.
       •  Add the new language (Spanish or French) by adding a language code column and the
          translated text to the CrmTranslations.xml file.
       •  Import translations back into the solution to apply the localized labels.

Discussion: https://www.examtopics.com/discussions/microsoft/view/80527-exam-pl-200-topic-
6-question-4-discussion/

223 Question
Exam PL-200 topic 6 question 5 discussion

Actual exam question from Microsoft's PL-200

Question #: 5
Topic #: 6

A company uses a model-driven Power Apps app in a new environment. The base language is
English.
You need to configure French and Spanish.
Which configuration component should you use? To answer, select the appropriate options in the
answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 270](PL-200%20Q%26A.pdf#page=270) · texto nativo

Hot Area:





Answer
   Correct Answer:





   Explanation:

Language packs

       •  Language packs must be installed to make additional languages (such as French and
          Spanish) available in Dataverse and model-driven apps.

Environment

       •   After the language packs are available, the languages are enabled at the environment
            level through Power Platform environment settings.

---

## [Página 271](PL-200%20Q%26A.pdf#page=271) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/83030-exam-pl-200-topic-
6-question-5-discussion/

224 Question
Exam PL-200 topic 6 question 6 discussion

Actual exam question from Microsoft's PL-200

Question #: 6
Topic #: 6

A company creates a Microsoft Power Apps app through the Power Apps designer portal for use in
Microsoft Teams.
This app needs to be promoted to the user acceptance testing environment.
You need to complete the Microsoft recommended actions before you export the solution.
Which two actions should you complete? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

    A. Run the solution checker.
    B.  Set the Optimized embedding appearance field to true.
   C. Clone a solution.
   D. Write validation tests.
    E.  Publish all changes.

Answer
   Correct Answer: A,E

   Explanation:

    A. Run the solution checker

    •   Microsoft recommends running Solution Checker before exporting a solution.
    •    It analyzes the solution for performance, reliability, security, and supportability issues.

    E. Publish all changes

    •   Before exporting, all customizations must be published to ensure the latest changes are
       included in the exported solution.

  Why not the others?

    •   B. Set the Optimized embedding appearance field to true – Not related to solution export
       or deployment.

    •  C. Clone a solution – Used in certain ALM scenarios but is not a recommended
        prerequisite for every export.

---

## [Página 272](PL-200%20Q%26A.pdf#page=272) · texto nativo

•  D. Write validation tests – A good practice, but not a specific Microsoft-recommended
       action required before exporting a solution.

Discussion: https://www.examtopics.com/discussions/microsoft/view/79352-exam-pl-200-topic-
6-question-6-discussion/

225 Question
Exam PL-200 topic 6 question 7 discussion

Actual exam question from Microsoft's PL-200

Question #: 7
Topic #: 6

You create functionality for a company. The functionality includes a Microsoft Dataverse table with
a form for data entry. The functionality will be distributed to other lines of business in the company,
each with its own Dataverse environment.
New forms must not be created in order for updates to the functionality to work correctly.
You need to package the new functionality for distribution.
What should you do?

    A. Use a patch solution and disable the ability to create new forms for the table.
    B. Use a managed solution and include only the needed form.
   C. Use an unmanaged solution and include only the needed form.
   D. Use a managed solution and disable the ability to create new forms for the table.

Answer
   Correct Answer: B

   Explanation:

The functionality will be distributed to multiple business units and environments, so it should be
packaged as a managed solution. Managed solutions are the Microsoft-recommended approach
for distributing applications and customizations to production environments.

Including only the required form helps ensure that updates to the solution can be applied
consistently and avoids conflicts with additional forms.

Why the other options are incorrect:

    •   A. Patch solution – Patches are used to update an existing solution, not as the initial
        distribution package.

    •  C. Unmanaged solution – Unmanaged solutions are intended for development and can be
       modified directly in the target environment, which can complicate future updates.

    •  D. Managed solution and disable the ability to create new forms – There is no
       requirement or standard approach to disable form creation to support solution updates.

---

## [Página 273](PL-200%20Q%26A.pdf#page=273) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/79350-exam-pl-200-topic-
6-question-7-discussion/

226 Question
Exam PL-200 topic 6 question 8 discussion

Actual exam question from Microsoft's PL-200

Question #: 8
Topic #: 6

You are using a development environment to add a new column to a system table. You plan to
move the changes to a test environment when they are complete.
The changes must meet the following requirements:

    •  Must be clearly identified so that they are not confused with system components and
      components from other solutions.
    •  Must not affect any existing components in the test environment.

You need to prepare a solution for deployment to the test environment.
Which four actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.
Select and Place:





Answer
   Correct Answer:





   Explanation:

    •  Create a new publisher: Ensures a unique prefix so the custom column is clearly identified
      and not confused with system components or other solutions.

---

## [Página 274](PL-200%20Q%26A.pdf#page=274) · texto nativo

•  Create a new unmanaged solution and select the correct publisher: Development is
      performed in an unmanaged solution.
    •  Add the table to the solution and add the new column: Include only the required
      components to minimize impact on the target environment.
    •  Run the solution checker on the solution: Validate the solution before deployment.

Discussion: https://www.examtopics.com/discussions/microsoft/view/79353-exam-pl-200-topic-
6-question-8-discussion/

227 Question
Exam PL-200 topic 6 question 9 discussion

Actual exam question from Microsoft's PL-200

Question #: 9
Topic #: 6

A company uses Power BI dashboards.

A manager wants to understand the raw data in one of the charts.

You need to present the data.

What should you do?

    A.  Export the dashboard to Microsoft PowerPoint.
    B.  Export the dashboard to Microsoft Excel.
   C. Change to focus mode.
   D.  Drill down in the dashboard controls.

Answer
   Correct Answer: B

   Explanation:

If a manager wants to view the raw data behind a chart in a Power BI dashboard, the appropriate
action is to export the data to Excel.

    •  Export to Excel provides access to the underlying or summarized data used by the
        visualization.
    •  Export to PowerPoint only exports the visual representation, not the raw data.
    •  Focus mode enlarges the visualization but does not expose the raw data.
    •   Drill down shows data at a lower level of aggregation but not the complete raw dataset.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96042-exam-pl-200-topic-
6-question-9-discussion/

---

## [Página 275](PL-200%20Q%26A.pdf#page=275) · texto nativo

228 Question
Exam PL-200 topic 6 question 10 discussion

Actual exam question from Microsoft's PL-200

Question #: 10
Topic #: 6


You are a consultant. A client asks you to remove several solutions in one of their Microsoft
Dataverse environments.

The client wants to know what effect removing the solutions will have on the rest of the system.

You need to explain the results of removing the solutions.

Which components will be affected? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 276](PL-200%20Q%26A.pdf#page=276) · texto nativo

Explanation:

    •  Unmanaged solution → The solution only
         o  Deleting an unmanaged solution removes only the solution container.
         o  Components remain in the environment.
    •  Managed solution patch → The solution and the updated column label
         o  Removing a managed patch rolls back the changes made by the patch.
         o  The updated label is removed/restored to its previous value.
    •  Managed ISV solution → The solution, the table, and any data in the table
         o   Uninstalling a managed solution removes the components introduced by that
               solution, including custom tables and their data.
         o   Site map customizations are also removed as part of the uninstall.

Discussion: https://www.examtopics.com/discussions/microsoft/view/95993-exam-pl-200-topic-
6-question-10-discussion/

229 Question
Exam PL-200 topic 6 question 11 discussion

Actual exam question from Microsoft's PL-200

Question #: 11
Topic #: 6

You are creating tables for use with Microsoft Power Platform components.

The display names of the tables must not be changed when the solution is promoted to the user
acceptance testing environment.

You need to apply this restriction to the solution.

---

## [Página 277](PL-200%20Q%26A.pdf#page=277) · texto nativo

Where should you make the changes?

    A. Segmented solution
    B.  Default solution
   C. Power Apps
   D. Unmanaged solution
    E. Managed solution

Answer
   Correct Answer: E

   Explanation:

A managed solution is used when distributing a solution to downstream environments such as
UAT or Production and you want to prevent users from modifying components, including table
display names.

Managed solutions allow solution authors to control customizations and protect components from
being changed in the target environment.

  Why not the others?

    •   A. Segmented solution – Controls which components are included, not whether they can
      be modified.

    •   B. Default solution – Contains all components in an environment and does not enforce
        restrictions.

    •  C. Power Apps – The platform itself, not a deployment mechanism.

    •  D. Unmanaged solution – Allows customization in the target environment, so display
      names could be changed.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96044-exam-pl-200-topic-
6-question-11-discussion/

230 Question
Exam PL-200 topic 6 question 12 discussion

Actual exam question from Microsoft's PL-200

Question #: 12
Topic #: 6

A company uses a model-driven app with Microsoft Dataverse in a single environment.

The company requires a canvas app that includes the same data as the model-driven app.

---

## [Página 278](PL-200%20Q%26A.pdf#page=278) · texto nativo

You need to create the canvas app.

Which three actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.





Answer
   Correct Answer:





   Explanation:

Since the model-driven app already uses Microsoft Dataverse, the quickest way to create a
canvas app with the same data is:

       •  Open the Power Apps Maker portal.
       •  Choose Dataverse as the data source.
       •   Select the required tables and generate/save the canvas app.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96132-exam-pl-200-topic-
6-question-12-discussion/

231 Question
Exam PL-200 topic 6 question 13 discussion

Actual exam question from Microsoft's PL-200

Question #: 13
Topic #: 6

---

## [Página 279](PL-200%20Q%26A.pdf#page=279) · texto nativo

A company that manufactures medical devices uses Power Apps to manage their sales and device
maintenance.

A table named Devices in Microsoft Dataverse has a column named Status. The Status column
must have a new status value of Review added to the existing Choice values of Active and Inactive.

The table must be added to a solution to be promoted once the change is made.

Only this change must be promoted to the test environment. The changes must not be able to be
changed once promoted.

You need to add the change to a solution for promotion.





Answer
   Correct Answer:





   Explanation:

       •  Add existing is used to add the existing Devices table to the solution.
       •  To promote only the Status column change (the new Choice value Review) and not the
            entire table with all its components, use Add subcomponent and select the specific
          column.
       •  The requirement that changes must not be changed once promoted indicates the
           solution should ultimately be deployed as a managed solution, but for the selections
         shown in the image, the correct options are those above.

---

## [Página 280](PL-200%20Q%26A.pdf#page=280) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/95994-exam-pl-200-topic-
6-question-13-discussion/

232 Question
Exam PL-200 topic 6 question 14 discussion

Actual exam question from Microsoft's PL-200

Question #: 14
Topic #: 6

A company is updating a Power Apps solution that contains two tables named Services and
Equipment.

The company is creating a new solution to update the current solution for the following
requirements:

    •  The Services table must be updated to include change tracking.
    •  The Equipment table must be updated to include four new columns.
    •  The solution must update only the components that need to be added or changed.

You need to create the solution.

Which table option should you use? To answer, drag the appropriate options to the correct tables.
Each option may be used once, more than once, or not at all. You may need to drag the split bar
between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 281](PL-200%20Q%26A.pdf#page=281) · texto nativo

The requirement says:

       •  Services table: enable Change Tracking → this is a table-level setting (metadata
          change).
       •  Equipment table: add 4 new columns → only specific components need to be
           included.
       •  Only the components that need to be added or changed should be updated.

   Explanation:

       •  Include entity metadata is used when changing table properties such as Change
           Tracking, auditing, ownership, etc.
       •  Select components allows you to include only the four new columns instead of the
            entire table and all its components.
       •  Include all components would bring unnecessary components and does not meet the
          requirement to update only what changed.

Discussion: https://www.examtopics.com/discussions/microsoft/view/96133-exam-pl-200-topic-
6-question-14-discussion/

233 Question
Exam PL-200 topic 6 question 15 discussion

Actual exam question from Microsoft's PL-200

Question #: 15
Topic #: 6

A company uses a model-driven app. The app uses a Power Virtual Agents chatbot.

The company has two locations in different countries/regions with separate environments for each
location. Each location has a development environment, a testing environment, and a production
environment. The company uses the Application Lifecycle Management (ALM) process for the
environments.

---

## [Página 282](PL-200%20Q%26A.pdf#page=282) · texto nativo

You need to create the different Power Virtual Agents bot environments.

How many Power Virtual Agents bot environments are required?

    A. 1
    B. 2
   C. 3
   D. 6

Answer
   Correct Answer: D

   Explanation:

Power Virtual Agents bots are created within a Power Platform environment and are managed
through the ALM process.

The company has:

        •  2 locations
        •  Each location has:
                o  1 Development environment
                o  1 Testing environment
                o  1 Production environment

Therefore:

        •   Location 1: Dev + Test + Prod = 3 bot environments
        •   Location 2: Dev + Test + Prod = 3 bot environments

Total: 2 × 3 = 6

Discussion: https://www.examtopics.com/discussions/microsoft/view/96285-exam-pl-200-topic-
6-question-15-discussion/

234 Question
Exam PL-200 topic 6 question 16 discussion

Actual exam question from Microsoft's PL-200

Question #: 16
Topic #: 6

A company plans to create an app by using Power Apps.

The company has the following requirements:

---

## [Página 283](PL-200%20Q%26A.pdf#page=283) · texto nativo

•  The app must be able to enter data into Microsoft SharePoint.
        •  Users must be able to add the app into Microsoft Teams.


You need to recommend which app to create.

Which type of app should you recommend?

    A.  model-driven app as a personal app
    B.  model-driven app as a tab app
   C. canvas app as a personal app
   D. Canvas app as a tab app

Answer
   Correct Answer: D

   Explanation:

The requirements are:

    1.  Enter data into Microsoft SharePoint
         o  Canvas apps can connect directly to SharePoint lists and libraries through built-in
              connectors.
         o  Model-driven apps are primarily built on Dataverse and are not the recommended
              option for SharePoint-based data entry.
    2.  Users must be able to add the app into Microsoft Teams
         o  Canvas apps can be embedded in Teams as a tab app.

    •   Therefore: D. Canvas app as a tab app

         o  Supports SharePoint as a data source and can be added directly as a Teams tab.

  Why not the others?

    •   A. Model-driven app as a personal app

         o  Not ideal for SharePoint data sources.

    •   B. Model-driven app as a tab app

         o  Model-driven apps require Dataverse and are not the best fit for SharePoint-based
             data entry.

    •  C. Canvas app as a personal app

         o  A personal app appears in the Teams app rail, but the requirement is to add the app
                into Teams, typically as a tab within a team or channel.

Discussion: https://www.examtopics.com/discussions/microsoft/view/112236-exam-pl-200-
topic-6-question-16-discussion/

---

## [Página 284](PL-200%20Q%26A.pdf#page=284) · texto nativo

235 Question
Exam PL-200 topic 6 question 17 discussion

Actual exam question from Microsoft's PL-200

Question #: 17
Topic #: 6

A company records data in Microsoft SharePoint Online. The company is creating a mobile app by
using Microsoft Power Platform only.

The company requires the app to connect directly to SharePoint Online to collect data.

You need to recommend which Microsoft Power Platform product or feature to implement.

What should you recommend?

    A. Power Automate
    B. Power Pages
   C. Canvas app
   D. Model-driven app

Answer
   Correct Answer: C

   Explanation:

The requirements are:

    •  Create a mobile app.
    •  Connect directly to SharePoint Online.
    •  Use Microsoft Power Platform only.
    •   Collect and enter data into SharePoint.

A Canvas app is the recommended Power Platform app type for direct connections to SharePoint
lists and libraries. It is optimized for mobile experiences and allows users to create, edit, and view
SharePoint data.

  Why not the others?

    •   A. Power Automate
      Automates processes and workflows but is not used to build mobile data-entry
        applications.

---

## [Página 285](PL-200%20Q%26A.pdf#page=285) · texto nativo

•   B. Power Pages
      Used for external-facing websites and portals, not primarily for mobile apps connected
        directly to SharePoint.

    •  D. Model-driven app
       Requires Dataverse as the primary data source and does not directly use SharePoint as its
       data platform.

Discussion: https://www.examtopics.com/discussions/microsoft/view/112391-exam-pl-200-
topic-6-question-17-discussion/

236 Question
Exam PL-200 topic 6 question 20 discussion

Actual exam question from Microsoft's PL-200

Question #: 20
Topic #: 6

A company has implemented server-side synchronization in Dataverse.

Users have the following synchronization requirements:

    •  As emails are moved to specific locations within an inbox, the emails must relate back to a
        specific record in Dataverse.
    •   Information about key individuals must sync automatically to Outlook.
    •  Tagged appointments in Outlook must sync automatically to Dataverse.

You need to recommend a solution for each requirement.

What should you recommend? To answer, move the appropriate features to the correct
requirements. You may use each feature once, more than once, or not at all. You may need to
move the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

---

## [Página 286](PL-200%20Q%26A.pdf#page=286) · texto nativo

Answer
   Correct Answer:





   Explanation:

    •   Folder-level tracking: Tracks emails automatically when they are moved to specific
       Outlook folders and links them to Dataverse records.
    •  Appointments, contacts, and tasks synchronization: Synchronizes contacts (key
        individuals) between Dataverse and Outlook.
    •  Outlook category tracking: Tracks Outlook items, including appointments, when users
       assign the configured Dataverse category.

Discussion: https://www.examtopics.com/discussions/microsoft/view/143772-exam-pl-200-
topic-6-question-20-discussion/

237 Question
Exam PL-200 topic 6 question 21 discussion

Actual exam question from Microsoft's PL-200

Question #: 21
Topic #: 6

You are creating a model-driven app that has an embedded Power BI report. Another functional
consultant set up an environment variable for the report.

You add the dashboard to a solution in the development environment and then import the changes
to a production environment as a managed solution.

When you test the report, the data appears the same as it did in the development environment.
You delete the solution in production.

You need to resolve the development environment issue before redeploying the solution.

What should you do?

---

## [Página 287](PL-200%20Q%26A.pdf#page=287) · texto nativo

A. Update the environment variable current value
    B. Remove the environment variable current value.
   C. Update the environment variable default value.
   D. Create a new environment variable.

Answer
   Correct Answer: B

   Explanation:

Environment variables have:

    •   Default Value – stored in the solution and moved between environments.
    •  Current Value – environment-specific and should be configured separately in each
       environment.

In this scenario, after importing the managed solution into Production, the report still points to the
Development data. This commonly occurs because the environment variable's Current Value was
included in the solution.

To ensure the Production environment prompts for or uses its own value during deployment, you
should remove the Current Value from the environment variable in Development before exporting
the solution again.

  Why not the others?

    •   A. Update the environment variable current value
      The issue is that the current value should not be carried from Development.

    •  C. Update the environment variable default value
       Default values are intended as a fallback and are packaged in the solution.

    •  D. Create a new environment variable
       Unnecessary; the existing environment variable can be used correctly.

Discussion: https://www.examtopics.com/discussions/microsoft/view/145182-exam-pl-200-
topic-6-question-21-discussion/

238 Question
Exam PL-200 topic 6 question 22 discussion

Actual exam question from Microsoft's PL-200

Question #: 22
Topic #: 6

You are creating tables for use with Microsoft Power Platform components.

---

## [Página 288](PL-200%20Q%26A.pdf#page=288) · texto nativo

The display names of the tables must not be changed when the solution is promoted to the user
acceptance testing environment.

You need to apply this restriction to the solution.

Where should you make the changes?

    A. Segmented solution
    B.  Default solution
   C. Unmanaged solution
   D. Managed solution

Answer
   Correct Answer: D

   Explanation:

A managed solution is used when moving customizations from Development to UAT/Production
and you want to prevent users from modifying solution components.

Since the requirement states:

"The display names of the tables must not be changed when the solution is promoted to the
user acceptance testing environment."

you should deploy the solution as a managed solution. Managed solutions enforce restrictions on
customizations in the target environment.

  Why not the others?

    •   A. Segmented solution
       Controls which components are included in a solution, not whether they can be modified.

    •   B. Default solution
       Contains all environment customizations and does not provide protection against changes.

    •  C. Unmanaged solution
       Allows direct modification of components in the target environment.

Discussion: https://www.examtopics.com/discussions/microsoft/view/145204-exam-pl-200-
topic-6-question-22-discussion/

239 Question
Exam PL-200 topic 6 question 23 discussion

Actual exam question from Microsoft's PL-200

---

## [Página 289](PL-200%20Q%26A.pdf#page=289) · texto nativo

Question #: 23
Topic #: 6

A company is using Dataverse with a custom table named Prospects. The Prospects table has a
lookup to the Account table.

SharePoint document management is configured in the environment but is not configured for the
Prospects table. All documents saved as part of the integration must be accessed by using an
Account row linked to the Prospects table.

Based on new requirements from end users, the Prospects table must be reconfigured for use with
the document management feature.

You need to configure the integration.

Which four actions should you perform in sequence? To answer, move the appropriate actions
from the list of actions to the answer area and arrange them in the correct order.





Answer
   Correct Answer:

---

## [Página 290](PL-200%20Q%26A.pdf#page=290) · texto nativo

Explanation:

The requirement states:

        •   SharePoint document management is already configured in the environment.
        •  The Prospects table is not yet enabled.
        •  Documents for a Prospect must be accessed through the related Account record.

To achieve this, when enabling document management for the Prospects table, configure it to be
based on the Account entity so documents are stored and accessed through the associated
Account's SharePoint location.

Discussion: https://www.examtopics.com/discussions/microsoft/view/148699-exam-pl-200-
topic-6-question-23-discussion/

240 Question
Exam PL-200 topic 6 question 24 discussion

Actual exam question from Microsoft's PL-200

Question #: 24
Topic #: 6

A company is using a model-driven app in a production environment.

You must set up server-side synchronization for all users to connect with the company’s Exchange
Online instance.

You need to determine the locations to use to complete the configuration.

Where should you navigate to? To answer, select the appropriate options in the answer area.

---

## [Página 291](PL-200%20Q%26A.pdf#page=291) · texto nativo

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 292](PL-200%20Q%26A.pdf#page=292) · texto nativo

Explanation:

        •  Server Profile (Exchange Online profile) is configured in the Microsoft Power Platform
         admin center.
        •   Default processing (server-side synchronization settings for email, appointments,
           contacts, and tasks) is configured in System Settings.
        •  Approve Email is performed on the Mailbox record for the user in Dataverse.
        •   Test & Enable Mailbox is also performed from the Mailbox record in Dataverse.

Discussion: https://www.examtopics.com/discussions/microsoft/view/145200-exam-pl-200-
topic-6-question-24-discussion/

241 Question
Exam PL-200 topic 6 question 26 discussion

Actual exam question from Microsoft's PL-200

Question #: 26
Topic #: 6

A company is using Dataverse.

Users require a mechanism to manually track emails against specific row types in the system from
within Outlook.

You need to recommend a solution.

---

## [Página 293](PL-200%20Q%26A.pdf#page=293) · texto nativo

Which solution should you recommend?

    A. Custom page
    B. Cloud flow
   C. Canvas app
   D. Dynamics 365 App for Outlook

Answer
   Correct Answer: D

   Explanation:

The requirement is:

Users require a mechanism to manually track emails against specific row types in the system
from within Outlook.

The Dynamics 365 App for Outlook allows users to:

    •   Track emails directly from Outlook to Dataverse/Dynamics 365.
    •   Set Regarding records (specific rows such as Contacts, Accounts, Opportunities, custom
        tables, etc.).
    •  Create and link records without leaving Outlook.
    •  Manually track emails, appointments, and contacts.

   Therefore: D. Dynamics 365 App for Outlook Specifically designed for tracking Outlook items
    to Dataverse/Dynamics 365 records.

  Why not the others?

    •   A. Custom page: Not used for Outlook email tracking.

    •   B. Cloud flow: Automates processes but does not provide manual tracking from Outlook.

    •  C. Canvas app: Can interact with Dataverse but cannot directly provide Outlook email
        tracking functionality.

Discussion: https://www.examtopics.com/discussions/microsoft/view/316426-exam-pl-200-
topic-6-question-26-discussion/

242 Question
Exam PL-200 topic 6 question 27 discussion

Actual exam question from Microsoft's PL-200

Question #: 27
Topic #: 6

---

## [Página 294](PL-200%20Q%26A.pdf#page=294) · texto nativo

You are implementing server-side synchronization for a company. The company uses Exchange
Online with no permissions delegated. All users are assigned the Approve Email Addresses for
Users or Queues privilege.

You set up the server profile and configure the mailboxes. You encounter an issue when you
attempt to approve mailboxes for other users.

You need to identify who can approve the mailbox.

Who should you identify?

    A.  All users
    B.  Microsoft Power Platform Administrator
   C. Any system administrator
   D. User who owns the mailbox

Answer
   Correct Answer: C

   Explanation:

For server-side synchronization in Dataverse/Dynamics 365, approving a mailbox is a privileged
action.

Even if users are assigned the Approve Email Addresses for Users or Queues privilege, users
cannot approve their own email addresses/mailboxes. Approval must be performed by another
user with sufficient administrative privileges.

A System Administrator security role has the required permissions to approve email addresses
and mailboxes for other users.

  Why not the others?

    •   A. All users
       Regular users cannot approve mailboxes.

    •   B. Microsoft Power Platform Administrator
       This role manages environments but mailbox approval is typically performed by a
      Dataverse/Dynamics 365 System Administrator.

    •  D. User who owns the mailbox
       Users cannot approve their own mailbox.

Discussion: https://www.examtopics.com/discussions/microsoft/view/394315-exam-pl-200-
topic-6-question-27-discussion/

---

## [Página 295](PL-200%20Q%26A.pdf#page=295) · texto nativo

243 Question
Exam PL-200 topic 6 question 28 discussion

Actual exam question from Microsoft's PL-200

Question #: 28
Topic #: 6

You develop a model-driven app that has an embedded Power BI report in the development
environment.

Another environment has a Power BI workspace that corresponds to the development
environment.

All deployments must take place by using the maker portal.

When you manually deploy changes to the other environment, you observe that the report from the
development workspace is displayed.

You need to resolve the issue.

Which two actions should you perform? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

    A. Use a solution settings file.
    B. Replace the Report component with a Power BI Dashboard component.
   C. Add an environment variable.
   D. Include the current value in the solution.
    E. Remove the current value in the solution.

Answer
   Correct Answer: C,E

   Explanation:

The issue occurs because the embedded Power BI report is still using the values from the
Development environment.

To support deployment through the Maker portal, Microsoft recommends using environment
variables for items that differ between environments, such as Power BI workspace IDs and report
IDs.

    •  C. Add an environment variable

Use an environment variable to store the Power BI report/workspace reference. This allows each
environment to have its own value.

---

## [Página 296](PL-200%20Q%26A.pdf#page=296) · texto nativo

•   E. Remove the current value in the solution

When exporting the solution, remove the Current Value so that the target environment can provide
its own environment-specific value during import. Otherwise, the Development value is carried
over and the report continues to point to the Development workspace.

  Why not the others?

    •   A. Use a solution settings file
      Used with ALM pipelines and deployment automation, not manual deployment through the
      Maker portal.

    •   B. Replace the Report component with a Power BI Dashboard component
      Does not address environment-specific workspace references.

    •  D. Include the current value in the solution
       This is what causes the Development workspace value to be deployed to other
       environments.

Discussion: https://www.examtopics.com/discussions/microsoft/view/394316-exam-pl-200-
topic-6-question-28-discussion/

244 Question
Exam PL-200 topic 6 question 29 discussion

Actual exam question from Microsoft's PL-200

Question #: 29
Topic #: 6

You are exporting a solution from a development environment that contains a form and a view for a
custom table.

When you attempt to import the solution into another environment, the import fails due to missing
dependencies.

You need to ensure that the solution can be imported successfully.

What should you do to resolve the dependency errors?

    A.  Select Export as Unmanaged when exporting the solution.
    B.  Publish all customizations in the environment before exporting the solution.
   C. Select Include all objects when adding the table to the solution.
   D. Select Export as Managed when exporting the solution.

Answer
   Correct Answer: C

---

## [Página 297](PL-200%20Q%26A.pdf#page=297) · texto nativo

Explanation:

The import is failing because the form and view have dependencies on other table components
(columns, relationships, charts, etc.) that were not included in the solution.

When adding a table to a solution, selecting Include all objects ensures that all dependent
components required by the form and view are included in the export package, preventing missing
dependency errors during import.

  Why not the others?

    •   A. Export as Unmanaged
      Managed vs. unmanaged does not resolve missing dependencies.

    •   B. Publish all customizations
       This is a good practice before export but does not automatically include missing dependent
      components.

    •  D. Export as Managed
      Managed solutions can still fail due to missing dependencies.

Discussion: https://www.examtopics.com/discussions/microsoft/view/394317-exam-pl-200-
topic-6-question-29-discussion/
