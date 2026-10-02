# Transcripción: PL-200-MULTI.pdf

- PDF original: [PL-200-MULTI.pdf](PL-200-MULTI.pdf)
- Cada encabezado de página enlaza a la página correspondiente del PDF.


- Archivo fuente: `PL-200-MULTI.pdf`
- Páginas del archivo: 20
- Páginas incluidas: `1-20`
- Extracción: 2026-10-02T11:18+02:00
- Aviso: resultado automático; cotejar cifras e identificadores con el original.

## [Página 1](PL-200-MULTI.pdf#page=1) · texto nativo

MULTI 01
You administer the Microsoft 365 and Power Platform environments for Contoso, Ltd. The company has
a model-driven app that is used to track customer interactions with employees. The app uses standard
table types for customers. A user named Elisabeth Rice signs in to the app by using the following sign in
name: Elisabeth.Rice@contoso.com.

After marriage, Elisabeth changes her legal name to Elisabeth Mueller.

You need to update the sign in name for the user without losing any application history.

Option 1:
Solution: Change Elizabeth's username in the user record for the app.
Does this meet the goal?

    A.  Yes
    B. No


Dynamics 365 and Dataverse, a user's sign-in name is synchronized from Microsoft Entra ID (Azure AD).
You do not change the sign-in name directly in the app's user record.

To preserve all ownership, history, activities, and audit records:

         1.  Change the user's name and User Principal Name (UPN) in Microsoft Entra ID / Microsoft
           365.
         2.  Synchronization updates the corresponding Dynamics 365 user record.
         3.  The same user account is retained, so application history remains intact.

Changing the username in the Dynamics 365 app user record itself is not the correct method for
changing the sign-in identity.

Option 2:
Solution: Ask the Microsoft 365 administrator to sign in to the admin portal and change the
username.
Does this meet the goal?

    A.  Yes
    B. No

Dynamics 365 and Dataverse, user accounts are linked to Microsoft Entra ID (Azure AD) / Microsoft 365
identities. To change a user's sign-in name (UPN) while preserving ownership, activities, audit history,
and record associations:
         1. A Microsoft 365 administrator changes the user's username (UPN) in the Microsoft 365
         Admin Center.
         2.  The change synchronizes to Dynamics 365.
         3.  The user continues to use the same underlying account, so all application history is retained.
For example:

---

## [Página 2](PL-200-MULTI.pdf#page=2) · texto nativo

•   Before: Elisabeth.Rice@contoso.com
       •   After: Elisabeth.Mueller@contoso.com
The Dynamics 365 user record remains associated with the same identity, preserving all historical data.
Option 3:
Solution: Delete the user account in the Power Platform admin portal and recreate the account
by using the new name.
Does this meet the goal?

    A.  Yes
    B. No

The goal is to:
    •  Update the user's sign-in name from Elisabeth.Rice@contoso.com to
       Elisabeth.Mueller@contoso.com.
    •   Preserve all application history, including:
        o  Record ownership
        o   Activities
        o  Audit history
        o  Assignments
        o  Relationships
Deleting the user account and recreating it would create a new identity in Microsoft Entra ID (Azure AD)
and Dataverse. The new account would not be associated with the original user's history and ownership
records.
The correct approach is to change the username (UPN) in Microsoft 365 / Microsoft Entra ID, which
keeps the same user identity and preserves all history.
Option 4:

Solution: From Dynamics 365 Settings, select Email Configuration. In the active mailbox for the
user, update the name.
Does this meet the goal?

    C.  Yes
    D. No

The proposed solution does not meet the goal.
Changing information in Dynamics 365 Settings → Email Configuration → Mailbox only affects the
mailbox configuration used for email synchronization. It does not change the user's sign-in name (User
Principal Name/UPN) in Microsoft Entra ID (Azure AD) or Dynamics 365.

MULTI 02
On a Contact record, a user creates a Note record that contains the word running.

One week later, the user reports that they cannot find the Contact record associated with the Note
record.

You need to find the Note record.

---

## [Página 3](PL-200-MULTI.pdf#page=3) · texto nativo

Option 1:
Solution: Use Categorized Search to search for the word run.
Does this meet the goal?

    A.  Yes
    B. No

Categorized Search does not perform stemming or linguistic matching in a way that guarantees that
searching for "run" will return records containing "running".

To find the Note record reliably, the user should search for the actual indexed term "running" (or use
Relevance Search/Dataverse Search configured for Notes).

Because the note contains the word "running", searching for "run" with Categorized Search is not
guaranteed to return the Note record.

Therefore, the proposed solution does not meet the goal.

Option 2:
Solution: Use Relevance Search to search for the word run.
Does this meet the goal?

    A.  Yes
    B. No

Relevance Search (now Dataverse Search) uses Azure Cognitive Search technology and supports
linguistic analysis, including:

    •  Word stemming

    •   Inflectional forms

    •   Relevance ranking

   Because the Note contains the word: running
   a search for: run

   can return results containing related word forms such as running, runs, and ran.

    Therefore, using Relevance Search to search for "run" can locate the Note record and,
    consequently, the associated Contact record.

Option 3:
Solution: Use Quick Find search on the Notes list to search for the word run.
Does this meet the goal?

    A.  Yes
    B. No

---

## [Página 4](PL-200-MULTI.pdf#page=4) · texto nativo

Quick Find performs keyword matching but does not support the linguistic analysis and stemming
capabilities of Relevance Search (Dataverse Search).

The Note contains the word: running

The proposed search term is: run

Quick Find does not automatically treat run and running as equivalent terms. Therefore, searching for
run is not guaranteed to find a Note that contains running.

To reliably find the Note, you would need to:

    •   Search for running using Quick Find, or

    •  Use Relevance Search, which supports word stemming and related word forms.

Therefore, the solution does not meet the goal.

Option 4:
Solution: Use Dataverse Search to search for the word run.
Does this meet the goal?

    A.  Yes
    B. No

Dataverse Search (formerly Relevance Search) supports linguistic search and word stemming.
Stemming allows the search engine to match variations of a word based on its root.

For example:

    •   Stored word: running

    •   Search term: run

Dataverse Search can return records containing running, runs, or ran when searching for run.

Since Notes (annotations) are searchable by Dataverse Search, searching for run can locate the Note
containing running, which in turn helps identify the associated Contact record.

MULTI 03
A company uses Dataverse. The company plans to store and manage documents and data in the
environment.

The company requires a solution that minimizes Dataverse storage consumption.

You need to recommend a solution.

Option 1:
Solution: Configure SharePoint on-premises integration..
Does this meet the goal?

    A.  Yes

---

## [Página 5](PL-200-MULTI.pdf#page=5) · texto nativo

B. No

    Configuring SharePoint integration with Dataverse is the correct approach to minimize
    Dataverse storage consumption because documents are stored in SharePoint while only
   metadata and links are stored in Dataverse.

   However, the solution specifies SharePoint on-premises integration. Dataverse supports
   document management integration with SharePoint Online, and the recommended approach
    for minimizing storage in Power Platform environments is to store documents in SharePoint
    Online rather than in Dataverse file storage.

    Therefore, the proposed solution does not meet the goal.

Option 2:
Solution: Enable attachments for a table..


Does this meet the goal?

    A.  Yes
    B. No

    Enabling attachments for a Dataverse table stores the attached files in Dataverse file storage, which
    increases Dataverse storage consumption rather than minimizing it.

   The requirement is:

    "Store and manage documents and data while minimizing Dataverse storage consumption."

   The recommended approach would be to integrate Dataverse with SharePoint document
   management, where documents are stored in SharePoint and only references are maintained in
    Dataverse.

    Therefore:

       •  Documents can be stored as attachments.
       •   Storage consumption is not minimized.
       •  The solution does not meet the goal.

Option 3:
Solution: Configure SharePoint Online integration.


Does this meet the goal?

    A.  Yes
    B. No

---

## [Página 6](PL-200-MULTI.pdf#page=6) · texto nativo

Configuring SharePoint Online integration is the recommended approach when a company needs to
store and manage documents while minimizing Dataverse storage consumption.

With SharePoint integration:

       •  Documents are stored in SharePoint Online instead of Dataverse file storage.
       •   Dataverse stores only references/links to the documents.
       •   Users can manage documents directly from model-driven apps.
       •   SharePoint storage is typically more cost-effective for document management.

Therefore, configuring SharePoint Online integration meets the goal of minimizing Dataverse storage
usage

Option 4:
Solution: Add a File column to a table.


Does this meet the goal?

    C.  Yes
    D. No

   A File column stores files directly in Dataverse file storage. While it provides a convenient way
    to associate documents with records, it increases Dataverse storage consumption.

   The requirement is to:

   Minimize Dataverse storage consumption.

   The recommended approach is SharePoint Online integration, where documents are stored in
    SharePoint and only linked to Dataverse records.

MULTI 04
A company uses a Dataverse environment. The environment is accessed from canvas and model-driven
apps.

The Dataverse environment contains a table that has the following columns:

       •  Name
       •  Company
       •   Contacted On

The company requires that the table not contain any duplicate rows when users create data in the
environment.

You need to implement a solution that meets the requirement.

---

## [Página 7](PL-200-MULTI.pdf#page=7) · texto nativo

Option 1:
Solution: Create an alternate key for the columns.
Does this meet the goal?

    A.  Yes
    B. No

   An alternate key in Dataverse enforces uniqueness across one or more columns. By creating an
    alternate key using the columns:

       •  Name
       •  Company
       •  Contacted On

    Dataverse will prevent users from creating another row with the same combination of values in
    those columns.

    Since the requirement is that the table must not contain duplicate rows, an alternate key is an
    appropriate solution because it enforces uniqueness at the database level for all apps accessing
    Dataverse (both canvas apps and model-driven apps).

Option 2:
Solution: Create an alternate key for the columns.
Does this meet the goal?

    A.  Yes
    B. No

   A Power Fx formula can be used to validate data or provide logic within an app, but it does not
   enforce uniqueness at the Dataverse table level across all ways data can be be created or
   updated.

   The requirement is:

   "The table must not contain any duplicate rows when users create data in the environment."

   To guarantee uniqueness in Dataverse, you should use an alternate key or duplicate detection
    rules. A Power Fx formula only works within the specific app where it is implemented and does
   not prevent duplicates coming from other apps, imports, workflows, or APIs.

    Therefore, creating a Power Fx formula does not fully meet the requirement.

---

## [Página 8](PL-200-MULTI.pdf#page=8) · texto nativo

Option 3:
Solution: Create a duplicate detection rule for the columns.
Does this meet the goal?

    A.  Yes
    B. No

   A duplicate detection rule can identify potential duplicates and warn users, but it does not
   guarantee that duplicates will never be created.

   The requirement states:

   "The table must not contain any duplicate rows."

   To enforce uniqueness at the database level, you should use an alternate key. Alternate keys
    prevent duplicate records from being created with the same key values, regardless of whether
    the data is entered through a canvas app, model-driven app, import, or API.

    Duplicate detection rules:

       •   Detect duplicate records.
       •  Can warn users during create/update/import operations.
       •  Do not enforce uniqueness in all scenarios.
       •  Do not guarantee that duplicates cannot exist.

    Therefore, the solution does not meet the goal.

Option 4:
Solution: Create a business rule for the columns.
Does this meet the goal?

    A.  Yes
    B. No

   A business rule can validate data, show error messages, set field values, or enforce field
    requirements within Dataverse forms and apps. However, it does not enforce uniqueness across
    records in a table.

   The requirement is:

   "The table must not contain any duplicate rows when users create data in the environment."

   A business rule cannot reliably prevent duplicate records from being created, especially through
    different entry methods (canvas apps, model-driven apps, imports, APIs, flows, etc.).

---

## [Página 9](PL-200-MULTI.pdf#page=9) · texto nativo

To guarantee no duplicates, you should use an alternate key, which enforces uniqueness at the
    Dataverse database level..

    Therefore, the solution does not meet the goal.

MULTI 05
You are building a Power Pages site for a supermarket chain.

The company plans to have the managers of individual stores use the site. Managers will authenticate
on the site each week by using their corporate identity to update stock information for their store.
Managers must be able to add and update stock information for their store only.

You need to configure the site security.

Option 1:
Solution: Configure table permissions.
Does this meet the goal?

    C.  Yes
    D. No

   Table permissions are the correct security mechanism in Power Pages for controlling access to
    Dataverse data.

    In this scenario, managers must:

       •   Authenticate using their corporate identity.
       •  Add stock information.
       •  Update stock information.
       •   Access only the records for their own store.

   By configuring table permissions (with the appropriate access type such as Contact, Account,
    or a relationship-based permission), you can grant Create and Write privileges while restricting
   each manager to only the records associated with their store.

    Therefore, the solution meets the goal.

Option 2:
Solution: Use local authentication.
Does this meet the goal?

    A.  Yes
    B. No

---

## [Página 10](PL-200-MULTI.pdf#page=10) · texto nativo

The scenario states that managers must authenticate using their corporate identity. In Power
    Pages, this requires an external identity provider such as Microsoft Entra ID (Azure AD), not
    local authentication.

    Local authentication:

       •  Uses username/password accounts stored for the website.
       •  Does not authenticate users with their corporate identity.
       •  Does not provide record-level access control by itself.

   To meet the requirements, you would need:

         1.  Corporate authentication (for example, Microsoft Entra ID).
         2.  Table permissions to restrict managers so they can add and update stock information
           only for their own store.

Option 3:
Solution: Use Microsoft Entra ID authentication.
Does this meet the goal?

    A.  Yes
    B. No

   Using Microsoft Entra ID authentication satisfies only one requirement:

       •  Managers authenticate using their corporate identity.

   However, it does not by itself ensure that managers can:

       •  Add and update stock information.
       •   Access only their own store's records.

   To enforce record-level access in Power Pages, you must configure table permissions (and
    appropriate web roles/relationships).

    Since Microsoft Entra ID authentication alone does not provide the required authorization and
    data access restrictions, the solution does not fully meet the goal.

Option 4:
Solution: Configure page permissions.
Does this meet the goal?

    A.  Yes
    B. No

---

## [Página 11](PL-200-MULTI.pdf#page=11) · texto nativo

Page permissions control access to web pages in a Power Pages site, but they do not control
    access to Dataverse records.

   The requirement is that managers must:

       •   Sign in with their corporate identity.
       •  Add and update stock information.
       •   Access only the stock information for their own store.

   To achieve record-level security, you must use table permissions (often together with web roles
   and Entra ID authentication).

    Therefore, configuring page permissions alone does not meet the goal.

MULTI 06
Support agents use a model-driven app while working on customer cases.



Agents currently switch between multiple systems to locate help content. The need to switch systems
makes it difficult to find relevant information.



You need to provide an efficient way to display contextual knowledge directly within the case form
without requiring the agent to refresh the record.



Option 1:
Solution: Call an instant flow to update article information on the Dataverse record..
Does this meet the goal?

    A.  Yes
    B. No

   The requirement is to:

       •   Display contextual knowledge directly within the case form.
       •  Avoid requiring the agent to refresh the record.
       •  Help agents find relevant information without switching systems.

    Calling an instant flow to update article information on a Dataverse record does not satisfy the
   requirement because:

---

## [Página 12](PL-200-MULTI.pdf#page=12) · texto nativo

•  The flow updates data in the background, but the form would typically need to be
           refreshed to display the updated information.
       •    It does not provide an embedded, contextual knowledge experience within the form.

   A better approach would be to use capabilities such as:

       •  Knowledge articles integrated into Customer Service
       •  Knowledge search control
       •  A custom page or embedded component that displays knowledge content dynamically
            within the form

    Therefore, the proposed solution does not meet the goal

 Option2:
Solution: Add a custom page that has a knowledge article lookup and link it by using a navigation
button in the app..
Does this meet the goal?

    C.  Yes
    D. No

   The requirement is to:

       •   Display contextual knowledge directly within the case form.
       •  Avoid requiring the agent to refresh the record.
       •  Reduce switching between systems.

   A custom page linked from a navigation button does provide access to knowledge articles,
   but it does not display the knowledge directly within the case form. The agent must navigate
   away from the form (or open another page), which does not fully satisfy the requirement for
    contextual information embedded in the case experience.

   A better solution would be to embed the knowledge experience directly in the form (for example,
    using a side pane or embedded component that displays contextual knowledge based on the
    current case).

    Therefore, the proposed solution does not meet the goal

Option3:
Solution: In the case form, embed a canvas app that dynamically displays knowledge articles
based on the case category.
Does this meet the goal?

    A.  Yes
    B. No

---

## [Página 13](PL-200-MULTI.pdf#page=13) · texto nativo

The requirement is to:

       •   Display contextual knowledge directly within the case form.
       •  Avoid switching to other systems.
       •  Avoid requiring the agent to refresh the record.

   By embedding a canvas app in the case form, you can:

       •   Pass the current case information (such as case category) to the canvas app.
       •   Dynamically retrieve and display relevant knowledge articles.
       •  Show the information directly within the form.
       •  Update the displayed content without requiring the user to refresh the case record.

    This provides an integrated and contextual user experience that meets the stated requirements

Option4:
Solution: In the case form, add a subgrid that points to a custom table storing external article
links.
Does this meet the goal?

    C.  Yes
    D. No

   The requirement is to provide:

       •  Contextual knowledge directly within the case form
       •  An efficient experience for agents
       •  No need to refresh the record
       •  Reduced switching between systems

   A subgrid that displays records from a custom table containing external article links can show
    related links, but it does not dynamically display contextual knowledge articles based on the
    current case. Agents would still need to open the links and navigate elsewhere to read the
    content.

    Therefore, this solution does not fully meet the goal of displaying contextual knowledge directly
    within the case form.

   The better solution remains:

   Embed a canvas app that dynamically displays knowledge articles based on the case
    category.

MULTI 07
A company uses a model-driven app.

---

## [Página 14](PL-200-MULTI.pdf#page=14) · texto nativo

The company needs to automatically update the Status column in real time.

You need to configure this feature.

Option 1:
Solution: Create a flow that has an Update item action.
Does this meet the goal?

    A.  Yes
    B. No


The requirement is to update the Status column in real time.

A Power Automate cloud flow with an Update item action runs asynchronously after the triggering
event occurs. It cannot guarantee real-time processing before the record is saved or immediately during
the transaction.

To achieve real-time updates in a model-driven app, you would typically use:

       •  A real-time classic workflow
       •  A business rule (if the logic is simple enough)
       •  A plug-in (if custom code is allowed)

Therefore, creating a cloud flow with an Update item action does not meet the requirement for real-
time updates.

Option 2:
Solution: Create a workflow that has an Update Record step.
Does this meet the goal?

    A.  Yes
    B. No


A workflow with an Update Record step can be configured as a real-time (synchronous) classic
workflow in a model-driven app.

Because the requirement is to automatically update the Status column in real time, a real-time
workflow can:

       •  Run immediately when the triggering event occurs.
       •  Update the record using the Update Record step.
       •   Apply the change as part of the transaction.

Therefore, the proposed solution does meet the goal

Option 3:
Solution: Create a flow that has an Update a row action.
Does this meet the goal?

---

## [Página 15](PL-200-MULTI.pdf#page=15) · texto nativo

A.  Yes
    B. No


The requirement is to automatically update the Status column in real time.

A flow with an "Update a row" action refers to a Power Automate cloud flow using the Dataverse
connector. Cloud flows run asynchronously and do not execute in real time as part of the Dataverse
transaction.

Therefore, although the flow can update the Status column, it does not satisfy the requirement for a
real-time update.

To achieve real-time behavior, you would typically use:

       •  A real-time classic workflow
       •  A business rule (for simple logic)
       •  A plug-in (for more complex logic).

Option 4:
Solution: Create a workflow that has a Change Status step.
Does this meet the goal?

    A.  Yes
    B. No


The requirement is to automatically update the Status column in real time.

A real-time workflow can include a Change Status step, which is specifically designed to change the
status of a record immediately as part of the workflow execution.

Because the workflow can be configured to run synchronously (real time), the status update occurs
immediately when the triggering event happens.

MULTI 08
You are creating Power Virtual Agents chatbot that captures demographic information about customers.
The chatbot must determine the group a customer belongs to based on their age. The age groups are:

          •  0 - 17
          •  18 - 25
          •  26 - 35
          •  36 - 55
          •  55 - 100

You need to configure the chatbot to ask a question that can be used to determine the correct age
group.

---

## [Página 16](PL-200-MULTI.pdf#page=16) · texto nativo

Option 1:
Solution: Use age for Identify in the question and then add branches for each group that use
conditional logic.
Does this meet the goal?

    A.  Yes
    B. No


In Power Virtual Agents, you can:

    1.  Ask the user for their age and store it in a variable (for example, Age).

    2.  Use conditional branches to evaluate the age ranges:

              •  0–17
              •  18–25
              •  26–35
              •  36–55
              •  55–100

    3.  Route the conversation based on the matching condition.

Using Age as the identified value in the question and then adding conditional logic branches for each
age range is a valid approach and meets the requirement.

Option 2:
Solution: Use Date and time for Identify in the question and then add branches that use
conditional logic to determine the age group.
Does this meet the goal?

    A.  Yes
    B. No


The requirement is to determine a customer's age group based on their age:

       •  0–17
       •  18–25
       •  26–35
       •  36–55
       •  55–100

The proposed solution uses Date and time for Identify and then conditional logic.

This does not meet the goal because the chatbot needs to capture either:

       •  The customer's age directly (Number), or
       •  The customer's birth date and then calculate the age.

---

## [Página 17](PL-200-MULTI.pdf#page=17) · texto nativo

Using Date and time alone does not inherently provide the customer's age and is not the appropriate
entity type for determining age groups in this scenario.

A correct approach would be to:

         1.  Ask for the customer's age (Number).
         2.  Use conditional branches to place the customer into the appropriate age group.

Therefore, the proposed solution does not meet the goal

Option 3:
Solution: Use multiple choice options for Identify in the question and create options that
represent each of the age groups.
Does this meet the goal?

    A.  Yes
    B. No


The requirement is for the chatbot to determine which age group a customer belongs to.

Using a question with Multiple choice options such as:

       •  0–17
       •  18–25
       •  26–35
       •  36–55
       •  55–100

allows the user to directly select their age group. The chatbot can then use the selected option without
needing additional calculations or conditional logic.

Therefore, the solution does meet the goal.

Option 4:
Solution: Create a custom Age group entity and synonyms for each individual age in the
corresponding item. Use Age group for Identify in the question.
Does this meet the goal?

    A.  Yes
    B. No


A custom entity named Age Group can be created with values such as:

       •  0–17
       •  18–25
       •  26–35
       •  36–55

---

## [Página 18](PL-200-MULTI.pdf#page=18) · texto nativo

•  55–100

By adding synonyms for each entity value (for example, mapping ages 18 through 25 to the "18–25"
group), Power Virtual Agents can recognize an age entered by the user and match it to the correct age
group.

Then, using Age Group for Identify in the question allows the chatbot to determine the appropriate
group.

Therefore, the solution meets the goal.

MULTI 09
The sales team at a software company wants to attach a large number of supporting documents to
customer records, but management does not want to incur the cost of additional storage.
The company does not have any Office 365 application integrations enabled.
You need to recommend a storage solution that keeps storage costs low..

Option 1:
Solution: Enable Outlook integration.
Does this meet the goal?

    A.  Yes
    B. No


In Enabling Outlook integration does not provide a low-cost document storage solution for attaching
large numbers of supporting documents to customer records. Outlook integration is used primarily for
email tracking, synchronization, and accessing Dynamics 365 data from Outlook.

To store a large volume of documents while minimizing Dataverse storage consumption and cost, the
recommended solution is typically to integrate with SharePoint. Documents are stored in SharePoint
rather than in Dataverse, which significantly reduces Dataverse storage requirements.

Since the proposed solution only enables Outlook integration and does not address document storage
costs:

Option 2:
Solution: Enable server-based SharePoint integration..
Does this meet the goal?

    A.  Yes
    B. No

Server-based SharePoint integration is the recommended solution when users need to store a large
number of documents related to Dataverse/Dynamics 365 records while minimizing storage costs.

Benefits include:

---

## [Página 19](PL-200-MULTI.pdf#page=19) · texto nativo

•  Documents are stored in SharePoint rather than consuming expensive Dataverse
            database/file storage.
       •  Documents remain linked to customer records (Accounts, Contacts, Opportunities, etc.).
       •   Users can access and manage documents directly from within Dynamics 365/Dataverse.
       •    It provides a scalable and cost-effective document management solution.

Since the goal is to attach many supporting documents while keeping storage costs low, enabling
server-based SharePoint integration meets the requirement.

Option 3:
Solution: Enable OneNote integration.
Does this meet the goal?

    A.  Yes
    B. No


OneNote integration is designed for capturing and organizing notes related to records in Dynamics
365/Dataverse. It is not intended as a document management solution for storing large numbers of
supporting documents.

The requirement is to:

       •   Attach a large number of documents to customer records.
       •  Keep storage costs low.

The recommended solution for this scenario is server-based SharePoint integration, because
documents are stored in SharePoint rather than consuming Dataverse storage.

Therefore, enabling OneNote integration does not meet the goal

.

Option 4:
Solution: Enable OneDrive for Business.
Does this meet the goal?

    A.  Yes
    B. No


OneDrive for Business is intended for personal or team file storage and collaboration, but it is not the
recommended document management integration for Dynamics 365/Dataverse customer records.

The requirement is to:

    •   Attach a large number of supporting documents to customer records.

    •  Keep storage costs low.

---

## [Página 20](PL-200-MULTI.pdf#page=20) · texto nativo

•   Provide an integrated document management solution linked to records.

The correct solution is server-based SharePoint integration, which stores documents in SharePoint
while maintaining links to Dataverse/Dynamics 365 records.

Therefore, enabling OneDrive for Business does not meet the goal.
