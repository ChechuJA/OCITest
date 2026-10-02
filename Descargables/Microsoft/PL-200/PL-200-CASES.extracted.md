# Transcripción: PL-200-CASES.pdf

- PDF original: [PL-200-CASES.pdf](PL-200-CASES.pdf)
- Cada encabezado de página enlaza a la página correspondiente del PDF.


- Archivo fuente: `PL-200-CASES.pdf`
- Páginas del archivo: 67
- Páginas incluidas: `1-67`
- Extracción: 2026-10-02T11:18+02:00
- Aviso: resultado automático; cotejar cifras e identificadores con el original.

## [Página 1](PL-200-CASES.pdf#page=1) · texto nativo

CASE 01 CONTOSO
Contoso Suites is an animal shelter that specializes in finding homes for dogs that have been given up by
their owners. The shelter can house up to 20 dogs.


The shelter is implementing one model-driven Power Apps app to track the dogs and schedule meetings
with potential adopters. No other apps will be created.


The model-driven app uses Dataverse with out-of-the-box functionality when possible. Dataverse is set
up with the following configuration:

    •  The solution prefix “cs” is used for all new components.
    •   Only the root business unit is used.
    •   All tables are stored in Dataverse and do not require rapid scaling.
    •  Exchange server-side sync is not configured.

Adopters

    •  Adopter information is stored in a Contact table.
    •   Contacts are considered to be duplicates if they have the same email address and last name.
    •   Adopters are often late to meetings, so a reminder email is sent to them two hours before their
       meeting.
    •  The email reminders must not be tracked in the system.

Dogs

    •  Dog information is stored in a Dog table, which is organization owned.
    •   Breed, size, and weight are fields in the table..

Dog residency


    •  A Resident table tracks the stay of each dog.
    •  Each resident record has a lookup for the dog and its food.
    •  The food type and amount are logged on each resident record. Auto-posting is not configured
        for changes to food type and amount.
    •  A fee of $120 is in a currency column named Adoption Fee. This fee can be changed depending
      on the adoption circumstances.
    •  A formula column named Deposit is automatically populated with 20% of the adoption fee.
    •  A resident record is generated automatically when a dog record is created. This is the only way a
        resident record can be created.


Exercise and feedings

    •   Exercise for the dogs is tracked in an Exercise table.
    •   Feedings are tracked in a Feeding table.

---

## [Página 2](PL-200-CASES.pdf#page=2) · texto nativo

•   Exercise and feeding records appear in a resident record timeline.


Care staff

    •  The care staff must be able to view who changed the food type and the amount that was given,
        for up to three months ago.
    •  The staff must be able to update the weight of a dog on the resident record.
    •  The staff report that the buttons are too small on the touch screen they use to log exercise and
        feeding.
    •  The staff must be able to view who the adopters are for upcoming meetings. The staff must not
      be able to update adopter information.

Administrative staff

    •   Administrative staff must receive a weekly list of duplicate contacts. Duplicate alerts must not
       appear when a staff member saves a new contact.
    •  When an adopter wants to adopt a dog, the staff must perform a series of adoption duties in
        order. The following duty list must be displayed on the screen:
        o  Commitment:
                     - Obtain adopter signature in a commitment document.
                     - Collect deposit.
        o  Pre-pickup:
                     - Document spay or neutering date.
                     - Perform spay or neutering.
                     - Document pickup date.
        o  Pickup:
                     - Collect full payment.
                     - Verify dog is picked up.
        o  A dog must be picked up no sooner than two days after spaying or neutering.
        o  A pop-up window must appear with an error message if the Pickup date is too soon.
        o  Only administrative staff must be able to add new adopters and dogs.

Question 01 - 01


You need to set up the capability to view the change history for the food type and amount.

What should you set up? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 3](PL-200-CASES.pdf#page=3) · texto nativo

.



Answer 01 - 01
    Correct Answer:





Scenario:

You The requirement states:

"The care staff must be able to view who changed the food type and the amount that was given, for up
to three months ago."

---

## [Página 4](PL-200-CASES.pdf#page=4) · texto nativo

To track:

       •  Who made the change
       •  What value changed
       •  When the change occurred

you must enable Auditing on the table and the relevant columns.

The fields Food Type and Amount are stored on the Resident table:

"The food type and amount are logged on each resident record."

Therefore, auditing must be configured on the Resident table.

Reference: https://www.examtopics.com/discussions/microsoft/view/156860-exam-pl-200-topic-1-
question-72-discussion/


Question 01 – 02
You need to configure the Deposit column.


How should you write the formula?

    A.  Decimal(‘Adoption Fee’) * 0.20
    B.  ‘Adoption Fee’ * 0.20
    C.  Decimal(‘Adoption Fee’ * 20%)
    D.  ‘Adoption Fee’ * 20%

Answer 01 - 02
    Correct Answer: A

   The scenario states:

       •  Adoption Fee is a Currency column.
       •   Deposit is a Formula column.
       •   Deposit must automatically contain 20% of the Adoption Fee.

    In Dataverse formula columns, you can directly reference a currency column and multiply it by a
    percentage:

       •   'Adoption Fee' * 20%

Reference: https://www.examtopics.com/discussions/microsoft/view/156861-exam-pl-200-topic-1-
question-73-discussion/

---

## [Página 5](PL-200-CASES.pdf#page=5) · texto nativo

Question 01 - 03


You need to set up a security role for the care staff.

Which privileges should you set? To answer, move the appropriate privileges to the correct create, read,
write tables. You may use each create, read, write privileges once, more than once, or not at all. You
may need to move the split bar between panes or scroll to view content.





Answer 01 - 03
    Correct Answer:





   From the scenario:

       •  Care staff must be able to view upcoming meeting adopters but must not update adopter
           information.
       •  Care staff must be able to update the weight of a dog on the resident record.
       •  Only administrative staff can add new adopters and dogs.
       •  There is only the root business unit, so organization-level access is appropriate.

   Why

    •   Adopters: Care staff only need to view adopter information for upcoming meetings; they must
       not create or modify adopters.
         o  None – Organization – None

---

## [Página 6](PL-200-CASES.pdf#page=6) · texto nativo

•   Dogs: Care staff must update dog weight, but only administrative staff can create dogs.
         o  None – Organization – Organization
    •   Residents: Care staff need to update resident-related information, but resident records are
       created automatically when a dog is created.
         o  None – Organization – Organization

Reference: https://www.examtopics.com/discussions/microsoft/view/157045-exam-pl-200-topic-1-
question-74-discussion/


Question 01 – 04
You need to define the table types for Contoso Suites.


Which table type should you define for each requirement? To answer, move the appropriate table types
to the correct tables. You may use each table type once, more than once, or not at all. You may need to
move the split bar between panes or scroll to view content.





Answer 01 - 04
    Correct Answer:

---

## [Página 7](PL-200-CASES.pdf#page=7) · texto nativo

Based on the scenario:

    •   Adopters are stored in the existing Contact table and do not require special scaling or external
       data → Standard.
    •  Dogs are stored in Dataverse, do not require rapid scaling, and are organization-owned →
       Standard.
    •   Exercise records appear in the Resident timeline. Timeline entries must use an Activity table.
    •   Feeding records also appear in the Resident timeline. Timeline entries must use an Activity
        table.

Reference: https://www.examtopics.com/discussions/microsoft/view/157046-exam-pl-200-topic-1-
question-75-discussion/


Question 01 – 05
You need to improve the user experience for the care staff to log exercise and feeding.


What should you create?

    A.  Custom page in a model-driven app
    B.  Model-driven app form
    C.  Power BI report
    D.  Canvas app

Answer 01 - 05
    Correct Answer: D

   The requirement is:

   "The staff report that the buttons are too small on the touch screen they use to log exercise and
    feeding."

---

## [Página 8](PL-200-CASES.pdf#page=8) · texto nativo

Canvas apps are designed for task-focused, touch-friendly user experiences and allow complete
    control over:

    •   Button size
    •   Layout
    •   Screen design
    •   Mobile and tablet usability

    This makes them ideal for care staff who need to quickly record exercise and feeding activities on a
   touch screen.

   Why not the others?

    •   A. Custom page in a model-driven app

         o  Can improve the experience, but the standard Microsoft recommendation for highly
              customized touch-friendly data-entry scenarios is a canvas app.

    •   B. Model-driven app form

         o  Forms provide limited control over the UI and button sizing.
         o  They would not adequately address the touch-screen usability issue.

    •   C. Power BI report

         o  Used for analytics and reporting, not for entering exercise and feeding records.

   Exam Tip

   When a scenario mentions:

    •  Touch screens
    •   Mobile-friendly data entry
    •   Large buttons
    •   Highly customized user experience

   The expected Power Platform answer is usually Canvas App.

Reference: https://www.examtopics.com/discussions/microsoft/view/157034-exam-pl-200-topic-2-
question-55-discussion/

Question 01 – 06
You need to enable the care staff to update a dog's weight.


Which three actions should you perform in sequence? To answer, move the appropriate actions from
the list of actions to the answer area and arrange them in the correct order.

---

## [Página 9](PL-200-CASES.pdf#page=9) · texto nativo

Answer 01 - 06
    Correct Answer:





   To allow care staff to update the Dog Weight from the Resident record, you need to display fields
   from the related Dog table on the Resident form.

   The correct sequence is:

---

## [Página 10](PL-200-CASES.pdf#page=10) · texto nativo

1.  Edit the resident form
         2.  Select the lookup
         3.  Add a form component

    Explanation

    •  The weight field belongs to the Dog table, not the Resident table.
    •  The Resident table contains a lookup to Dog.
    •   In a model-driven app, you can expose and edit fields from a related record by adding a Form
      Component Control to the lookup on the parent form

Reference: https://www.examtopics.com/discussions/microsoft/view/157035-exam-pl-200-topic-2-
question-56-discussion/

Question 01 – 07
You need to create adoption duties for the administrative staff.


What should you create?

    A.  business unit
    B.  business process flow
    C.  business rule

Answer 01 - 07
    Correct Answer: B

    Explanation

The requirements describe a series of adoption duties that must be completed in order:

       •  Commitment
           o  Obtain adopter signature
           o   Collect deposit
       •   Pre-pickup
           o  Document spay/neuter date
           o  Perform spay/neuter
           o  Document pickup date
       •   Pickup
           o   Collect full payment
           o   Verify dog is picked up

A Business Process Flow (BPF) is specifically designed to:

       •  Guide users through a sequence of stages and steps.
       •   Enforce a consistent process.
       •   Display the required activities on the form.
       •   Ensure users complete tasks in the proper order.

---

## [Página 11](PL-200-CASES.pdf#page=11) · texto nativo

Why not the others?

    •   A. Business unit
      Used for security and organizational structure, not process guidance.

    •   C. Business rule
      Used for field validation, visibility, requirements, and calculations, but not for guiding users
       through multiple stages of a process.

Reference: https://www.examtopics.com/discussions/microsoft/view/157030-exam-pl-200-topic-3-
question-48-discussion/

Question 01 – 08
You need to manage contact duplicates for the administrative staff.


What should you do?

    A.  Create two duplicate detection rules and two duplicate detection jobs, and update duplicate
        detection settings.
    B.  Create two duplicate detection rules and one duplicate detection job.
    C.  Create one duplicate detection rule and one duplicate detection job, and update duplicate
        detection settings.


Answer 01 - 08
    Correct Answer: C

    Explanation

   The scenario states:

       •   Contacts are duplicates when they have the same Email Address and Last Name.
       •   Administrative staff must receive a weekly list of duplicate contacts.
       •   Duplicate alerts must not appear when a user saves a new contact.

   To satisfy this:

     1.  Create one duplicate detection rule on the Contact table:
           •   Email Address = Exact Match
           •   Last Name = Exact Match
     2.  Create one duplicate detection job:
           •  Run weekly to identify duplicates and provide the list to administrative staff.
     3.  Update duplicate detection settings:
           •   Disable duplicate detection during create/update operations so users do not receive
                duplicate warnings when saving contacts.

   Why not the others?

---

## [Página 12](PL-200-CASES.pdf#page=12) · texto nativo

•   A. Two duplicate detection rules and two duplicate detection jobs
       Only one duplicate definition exists (Email + Last Name), so a single rule and job are sufficient.
    •   B. Two duplicate detection rules and one duplicate detection job
        Multiple rules are unnecessary because the duplicate criteria are clearly defined as a single
       combination.

Reference: https://www.examtopics.com/discussions/microsoft/view/157031-exam-pl-200-topic-3-
question-49-discussion/

Question 01 – 09
You need to ensure that an appropriate date is selected for dog pickup.


What should you configure? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point.





Answer 01 - 09
    Correct Answer:

---

## [Página 13](PL-200-CASES.pdf#page=13) · texto nativo

Component: Business rule

   Formula (Condition):

        (Pickup date Is more than [Spay or neuter date + 2])

   Why?

   The requirement states:

      "A dog must be picked up no sooner than two days after spaying or neutering."

      "A pop-up window must appear with an error message if the Pickup date is too soon."

   A Business Rule is the correct component because it can:

       •   Validate data on the form in real time.
       •  Show an error message to the user.
       •   Prevent invalid data entry without code.

   The condition should verify that the Pickup date is at least 2 days after the Spay or neuter date.

Reference: https://www.examtopics.com/discussions/microsoft/view/157032-exam-pl-200-topic-3-
question-50-discussion/

Question 01 – 10
You need to create reminders for the adopters.


What should you use for each requirement? To answer, select the appropriate options in the answer
area.

---

## [Página 14](PL-200-CASES.pdf#page=14) · texto nativo

Answer 01 - 10
    Correct Answer:

---

## [Página 15](PL-200-CASES.pdf#page=15) · texto nativo

The reminder email must:

    •  Be sent 2 hours before a meeting.
    •  Be sent automatically.
    •  Not be tracked in Dataverse.
    •   Exchange server-side synchronization is not configured.

   A Scheduled Power Automate flow can run periodically, identify upcoming meetings, and send
   reminder emails at the appropriate time.

    Using the Outlook connector sends the email directly through Outlook and avoids creating/tracking
    email activities in Dataverse.

Reference: https://www.examtopics.com/discussions/microsoft/view/157027-exam-pl-200-topic-6-
question-25-discussion/

CASE 02 BELLOWS COLLEGE
   Background -


    Bellows College is a post-secondary school that wants to start a football team. The college uses
    Microsoft Power Platform to manage its recruiting efforts. The registration team and assistants use
    model-driven apps. The coaches use canvas apps on their mobile devices.


    Prospects are considered underage if they are younger than 18 years old at the time of registration.



    Current environment -


   Environment -


    •  Custom code is not allowed in the system.
    •   Server-side synchronization is configured for emails, appointments, contacts, and tasks.
    •  The database and file storage of Dataverse must be minimized to keep costs low.


    Contact table -


    •   Birthdate is a custom date and time field.
    •  Age at Registration is a calculated field that displays the age of the prospect at the time of
         registration.
    •   Current Age is a calculated field that displays the age of the prospect based on the current date
      and time.


    Evaluation table -

---

## [Página 16](PL-200-CASES.pdf#page=16) · texto nativo

•  The Evaluation table is a custom table used to track evaluation criteria.
    •   Evaluation records cannot be manually created.
    •   Users must not be able to continue until an evaluation record is created automatically for the
        prospect.

   Consent table –

    •  The consent forms completed by the parents are stored as records in the Consent table.
    •   Occasionally, a parent cannot complete the consent online and a paper copy must be printed.
      The signed copy must be scanned and stored with the consent record.


   Team website –

    •  The team website is created by using Power Pages.
    •  A starter layout template was used to create the site.
    •  The site consists of five pages:
         o  Home: A page open to everyone to view the announcements from the team.
         o  Schedule: A page open to everyone to view the tryout and game schedule.
         o   Evaluations: A page that displays tracking from the evaluation table. Prospects are able
               to view their own information only.
         o  Forms: A page that displays the consent form.
         o  Contact Us: A page for anyone to submit questions and comments.
    •  Two web roles for authenticated users are created: Primary Contact User and Prospect User.
         o    All primary contacts and prospects are assigned to their respective roles.


Requirements –

   Registration –

    •   Parents and prospects are created as contacts and must be linked.
    •  The registration team must be able to rapidly create prospects without navigating away from
       the Parents form. Only the First Name, Last Name, and Birthdate fields should be displayed for
       the team.
    •   Assistants must be able to update prospect information and add teams that the prospect has
        previously played on to a subgrid.

    Parental consent -


    •  When a prospect is underage, a Primary Contact field will appear. The field must be populated
       before the prospect record can be saved.
    •  A view named Underage Prospects that lists all underaged prospects is required.
    •  The Underage Prospects view must run once a week without requiring modifications to display
        correct information.
    •  A consent email must meet the following requirements:
         o  be sent to the primary contact of each new underage prospect

---

## [Página 17](PL-200-CASES.pdf#page=17) · texto nativo

o   contain a link to the team website o be automatically sent weekly and tracked to the
               contact record in Dataverse
         o   include the current date using the full month name, date, and year


    Evaluations -


    •   Coaches rate prospects each day on a scale of 1-10 in three categories: endurance, coordination,
      and skill.
    •  The total of the three categories is displayed at the bottom of the form. If the total for the day is
        greater than 25, the number should appear green.


Question 02 - 01
You need to view website questions and comments.


Where should you view this information?

    A.  Evaluations
    B.  Lead
    C.  Contact
    D.  Feedback

Answer 02 - 01
    Correct Answer: D

In Power Pages (formerly Power Apps Portals), the Feedback table is used to capture feedback,
comments, and ratings submitted by users through portal pages.

The scenario includes:

Contact Us: A page for anyone to submit questions and comments.

Questions and comments submitted from a portal's Contact Us page are typically stored and viewed
as Feedback records.

Why the other options are incorrect

    •   A. Evaluations – Used to track prospect evaluation scores, not website inquiries.
    •   B. Lead – Used for prospective customers/sales opportunities, not portal comments.
    •   C. Contact – Stores person records (parents, prospects, etc.), not the submitted
       questions/comments themselves


    Reference: https://www.examtopics.com/discussions/microsoft/view/139464-exam-pl-200-topic-2-
    question-44-discussion/

---

## [Página 18](PL-200-CASES.pdf#page=18) · texto nativo

Question 02 - 02
You need to set up webpage permissions.


Which permissions must you set? To answer, move the appropriate permissions to the correct page. You
may use each permission once, more than once, or not at all. You may need to move the split bar
between panes or scroll to view content.


NOTE: Each correct selection is worth one point.





Answer 02 - 02
    Correct Answer:





Based on the scenario:

    •  Home: "A page open to everyone to view the announcements from the team."
    •   Schedule: "A page open to everyone to view the tryout and game schedule."
    •   Evaluations: "Prospects are able to view their own information only."

---

## [Página 19](PL-200-CASES.pdf#page=19) · texto nativo

•  Forms: Displays the parental consent form. This is intended for the parent (Primary Contact)
       to complete.


Reference: https://www.examtopics.com/discussions/microsoft/view/140625-exam-pl-200-topic-2-
question-45-discussion/


Question 02 - 03
You need to create forms required for the registration team and assistants.


Which form types should you create? To answer, move the appropriate form types to the correct roles.
You may use each form type once, more than once, or not at all. You may need to move the split bar
between panes or scroll to view content.


NOTE: Each correct selection is worth one point.





Answer 02 - 03
    Correct Answer:

---

## [Página 20](PL-200-CASES.pdf#page=20) · texto nativo

Based on the requirements:

Registration team

"Must be able to rapidly create prospects without navigating away from the Parents form. Only the
First Name, Last Name, and Birthdate fields should be displayed."

This is exactly the purpose of a Quick Create form.

Registration team → Quick create



Assistants

"Must be able to update prospect information and add teams that the prospect has previously played
on to a subgrid."

Subgrids and full record editing require a Main form.

Assistants → Main

Reference: https://www.examtopics.com/discussions/microsoft/view/140626-exam-pl-200-topic-2-
question-46-discussion/


Question 02 - 04


You need to configure the Total field on the Evaluation form.

Which property should you select for the formula? To answer, move the appropriate property to the
correct formula. You may use each property once, more than once, or not at all. You may need to move
the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

---

## [Página 21](PL-200-CASES.pdf#page=21) · texto nativo

Answer 02 - 04
    Correct Answer:





The Total field needs to:

    1.  Display the sum of Endurance, Coordination, and Skill.

         o  The result shown in the label/control is controlled by the Text property.

    2.  Turn green when the total is greater than 25.

         o  The text color is controlled by the Color property.

 Reference: https://www.examtopics.com/discussions/microsoft/view/140627-exam-pl-200-topic-2-
question-47-discussion/


Question 02 - 05


You need to create the evaluation record for a prospect.

What should you use?

---

## [Página 22](PL-200-CASES.pdf#page=22) · texto nativo

A.  a classic Dataverse workflow
    B.  a cloud flow
    C.  a plug-in
    D.  a quick create form

Answer 02 - 05
    Correct Answer: B

      The scenario states:

    •   Evaluation records cannot be manually created.
    •   Users must not be able to continue until an evaluation record is created automatically for the
        prospect.
    •  Custom code is not allowed in the system.



         Let's evaluate the options:

    •   Classic Dataverse workflow (Incorrect): Classic workflows are legacy functionality. While they
       can create records, Microsoft's recommended approach for new automation is Power Automate
        (cloud flows).
    •   Cloud flow (Correct): A Power Automate cloud flow can trigger when a Prospect record is
       created and automatically create the corresponding Evaluation record without custom code.
    •   Plug-in (Incorrect): A plug-in could enforce synchronous creation, but the scenario explicitly
        states custom code is not allowed.
    •   Quick create form (Incorrect): A Quick Create form facilitates manual record creation, which
        contradicts the requirement that Evaluation records be created automatically.


Reference: https://www.examtopics.com/discussions/microsoft/view/139467-exam-pl-200-topic-2-
question-48-discussion/


Question 02 - 06


You need to create a filter for the Underage Prospects view.

How should you set up the expression for the filter? To answer, select the appropriate options in the
answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 23](PL-200-CASES.pdf#page=23) · texto nativo

Answer 02 - 06
    Correct Answer:





   The requirement is:

       •  A prospect is underage if younger than 18 at the time of registration.
       •  The Underage Prospects view must automatically remain correct over time and run without
          manual updates.
       •  The table already contains a calculated field Age at Registration, which stores the age when
           the prospect registered.

    Since the rule is based on age at registration, not current age, the view should filter on Age at
    Registration

Reference: https://www.examtopics.com/discussions/microsoft/view/140220-exam-pl-200-topic-3-
question-38-discussion/

---

## [Página 24](PL-200-CASES.pdf#page=24) · texto nativo

Question 02 - 07


You need to create a flow to send an email to the primary contacts.

Which action should you configure? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.





Answer 02 - 07
    Correct Answer:

---

## [Página 25](PL-200-CASES.pdf#page=25) · texto nativo

For the consent email requirement:

       •    It must be automatically sent weekly → use a Recurrence trigger.
       •    It must be sent to the primary contact of each underage prospect → retrieve matching
           records with List rows.
       •    It must be tracked to the contact record in Dataverse → create an Email activity record
            rather than sending an untracked notification, so use Add a new row (Email table)

    Reference: https://www.examtopics.com/discussions/microsoft/view/140629-exam-pl-200-topic-3-
    question-39-discussion/


Question 02 - 08


You need to configure the Primary Contact field.

What should you configure? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 26](PL-200-CASES.pdf#page=26) · texto nativo

Answer 02 - 08
    Correct Answer:





       Primary Contact data type = Lookup

           •   Parents and prospects are both stored as Contact records and must be linked.
           •   Therefore, the Primary Contact field should be a Lookup to the Contact table.

         Visibility = Business rule where Set Visibility = Yes

---

## [Página 27](PL-200-CASES.pdf#page=27) · texto nativo

•   Requirement: "When a prospect is underage, a Primary Contact field will appear."
           •  Use a Business Rule that checks the prospect's age and sets the field visibility to Yes
            when the prospect is under 18.

       Requirement = Business rule where Business Required = Business Required

           •   Requirement: "The field must be populated before the prospect record can be saved."
           •  Use the same Business Rule to make the field Business Required when the prospect is
              underage.

    Reference: https://www.examtopics.com/discussions/microsoft/view/139474-exam-pl-200-topic-4-
    question-32-discussion/

Question 02 - 09
You need to format the Current Date field for parental consent.


What should you use?

    A.  switch
     B.  dynamic content
     C.  expression
    D.  condition


Answer 02 - 09
    Correct Answer: C

The requirement is to include the current date in the consent email using the format:

         Full month name, day, and year
       Example: July 20, 2026

In Power Automate, custom date formatting is done by using an Expression, such as:

      formatDateTime(utcNow(),'MMMM dd, yyyy')

       •   Expression (Correct) Used to format dates and manipulate values.
       •  Dynamic content (Incorrect) Inserts values, but by itself does not provide custom
            formatting.
       •   Condition (Incorrect) Used for branching logic.
       •   Switch (Incorrect) Used for multiple branching scenarios.

    Reference: https://www.examtopics.com/discussions/microsoft/view/140634-exam-pl-200-topic-6-
    question-18-discussion/


Question 02 - 10
You need to store scanned consent forms.

---

## [Página 28](PL-200-CASES.pdf#page=28) · texto nativo

Where should you store the forms?

    A.  Attachment
     B.  Column
     C.  Notes
    D.  SharePoint

Answer 02 - 10
    Correct Answer: D

The case explicitly states:

"The database and file storage of Dataverse must be minimized to keep costs low."

Scanned consent forms are documents that can consume significant storage. Microsoft best practice
is to store documents in SharePoint and link them to Dataverse records through SharePoint
integration.

Why not the others?

    •   A. Attachment (Incorrect)  Uses Dataverse storage.
    •   B. Column (Incorrect)  File/Image columns consume Dataverse file storage.
    •   C. Notes (Incorrect)  Attachments in notes are stored in Dataverse and increase storage
        costs.
    •  SharePoint (Correct) Optimizes storage costs and is the recommended document
        repository for Dataverse apps.


    Reference: https://www.examtopics.com/discussions/microsoft/view/140635-exam-pl-200-topic-6-
    question-19-discussion/


CASE 03 CITY POWER & LIGHT
   Background -


    City Power & Light is an energy and utilities company that has offices in Europe. The company
    subsidizes home improvements for domestic customers, to improve energy efficiency and to meet
    environmental commitments. The company also distributes and generates electricity for domestic
   and commercial customers. The company has 2,000 employees in multiple offices and in work-from-
   home locations.


    City Power & Light uses a team of schedulers, assessors, field engineers, and customer support
    agents for home improvements in a program named Get Energy Fit.



    Current environment -

---

## [Página 29](PL-200-CASES.pdf#page=29) · texto nativo

Get Energy Fit Program-



    City Power & Light uses the following to manage the Get Energy Fit program:

    •  The company uses a Microsoft Excel spreadsheet named Planning Hub on Microsoft SharePoint
       Online to store information about customer appointments, customer details, and customer
          eligibility in the program.
    •  The company records sensitive customer information that includes the document identification
      numbers and the customer's financial information.
    •  The company uses an assessor to verify customer eligibility in the program and to perform a
         suitability assessment. The assessor completes the suitability assessment by using a paper and
        clipboard at the customer property and enters the data to the Planning Hub after the
       assessment is completed. The assessor also uploads photographs to an on-premises document
         library. The assessor completes the eligibility assessment by using an application written in
        React.
    •   Schedulers use Microsoft Outlook to schedule engineers and assessors for home improvement
       appointments. About 200 appointments are scheduled daily.
    •  Employees for the company submit funding claims on behalf of the customer by uploading
       evidence and compliance checks information to an application named the Claim Submission
        Portal.

    Technical Environment -



    •   Schedulers use Windows 11 desktop and laptop computers with the latest version of Microsoft
       Edge.
    •   Assessors use iOS and Android tablet devices.
    •  The Claim Submission Portal uses REST-based APIs for all operations and a dedicated testing
       environment. Authentication to the API is provided by using the following example header key
      and value pair:
         o   Authentication: 2C8D41431415E429C7FC7A74D8315
    •  The company uses Microsoft Azure for hosting multiple applications..


Requirements –

   Overview-


    City Power & Light plans to implement Microsoft Power Platform to improve the customer
    experience and increase delivery for the Get Energy Fit program.


    Business Requirements-


   • Only team leaders and senior managers should have access to read personally identifiable

---

## [Página 30](PL-200-CASES.pdf#page=30) · texto nativo

information (PII).
   • All development changes must be tested in a separate environment.
   • The company requires out-of-the-box solutions, when possible.
   • Sensitive credentials, such as user passwords and API secrets, must be stored securely.
   • The Claim Submission Portal must allow citizen developers to create automated solutions.
   • Customer and appointment information must be accessible to all applications.

Planning Hub Application-


The company is planning to replace the Planning Hub spreadsheet with a new application. The new
application has the following requirements:

    •  The application must support a component design that provides rapid changes requested by the
        schedulers.
    •  The data model for the application must capture the following information:
        o  Information about customers such as name, address, and other PII.
        o  The data and time for an assessor's or engineer's appointment. Schedulers must be able
               to view all appointments without filters.
        o  Records the details of the home improvements installed for the customer.
        o  Contains all the information and evidence for submission to the Claim Submission
                 Portal.
    •   After an assessor uploads the funding application and all evidence after a home improvement
       has been complete, the company requires that the status of the application is set to Submit and
       should run the following:
        o  Retrieve the details about the customer and the improvement installed.
        o  Send an approval to a senior manager to review and approve in Microsoft Teams.
        o  Upload the information to the API endpoint.
        o    If the upload fails to complete, it should retry after a delay of 30 seconds up to three
                times. If an error occurs after three times, the application should send an email
                 notification to the application support team.
        o  Must record the status on the funding application.

Suitability Assessment Tool-


The company plans to implement a new application named the Suitability Assessment Tool for the
assessors. The new application has the following requirements:


    •  Must integrate with Microsoft Power Platform.
    •   Assessors must be able to complete the eligibility assessment by using the Suitability
       Assessment Tool. The assessors must be able to upload photographs to the on-premises file
        share.
    •  Must be developed by using modular components that can be used by other applications.
    •  Must be optimized for use on tablet devices.
    •   All changes to the application must be completed in the Suitability Assessment Tool solution.

---

## [Página 31](PL-200-CASES.pdf#page=31) · texto nativo

Reporting-


The company has the following requirements for a reporting solution:

    •  The data source for the reporting solution must support incremental refreshes.
    •   The solution must report accurate data if an error occurs.



Issues-


    •  A recent audit identified that all users can access the PII in the Planning Hub spreadsheet.
    •   After a developer deploys a change to the production environment, a user reports information is
       loaded incorrectly to the test system when processing a funding application.
    •   After deploying a change to the new eligibility assessment tool in the development
       environment, you observe that the changes do not appear in the development environment.
    •   After removing a column from the Planning Hub application and deploying the changes to the
       production environment, you observe that the column is still present.
    •  You deploy the customizations for the data model. Users report that the email address of the
       user who created the appointment is missing and that searches on the description information
      do not return any results.

Question 03 - 01
You need to deploy the changes and resolve the issue with the Planning Hub application.


What should you use? To answer, select the appropriate options in the answer area.


NOTE: Each correct selection is worth one point.

---

## [Página 32](PL-200-CASES.pdf#page=32) · texto nativo

Answer 03 - 01
    Correct Answer:





For the Planning Hub application:

1. Solution to deploy → Appointment data

The issue mentions:

---

## [Página 33](PL-200-CASES.pdf#page=33) · texto nativo

"After removing a column from the Planning Hub application and deploying the changes to
the production environment, you observe that the column is still present."

To support ALM and deployment to production, the Planning Hub should be deployed as a
managed solution.

(The Planning Hub application contains customer, appointment, and improvement data.)

2. How to export → Export the unmanaged solution as managed

Production deployments should use a managed solution.

3. Remove the column after deployment → Stage for Upgrade

When a component (such as a column) is removed from a managed solution, the correct approach is
to use Stage for Upgrade and then apply the upgrade. This removes deleted components from the
target environment.

Reference: https://www.examtopics.com/discussions/microsoft/view/307896-exam-pl-400-topic-2-
question-58-discussion/


CASE 04 ADATUM
   Background -


   ADatum Corporation provides verification and investigation services that are used by insurance
    companies, law firms, and other organizations in the public sector. Services include verifying an
    individual’s background, qualifications, and specific scenarios that require onsite visit.


   The thorough work ADatum Corporation performs results in highly accurate cases with minimal
     critical information missing. Because of these high-quality results, ADatum Corporation is quickly
    proving itself as one of the best in the industry. In recent months, business has significantly
    increased, with most new business coming from high-profile companies and individuals.


   Management has decided to create a new qualification verification (QV) role to help ensure that
    clients get the most accurate results. This role examines completed work to ensure that nothing is
    missed.



    Current environment -


   Data storage and retention –

       •   All information sent by clients for services is stored in Microsoft Dataverse with a model-
           driven app as the interface.
       •   Clients enter their data in a website, which then uses a service account to create the records
             in the Dataverse database.

---

## [Página 34](PL-200-CASES.pdf#page=34) · texto nativo

•  Team members currently have full access to all Service Request records..


Service Requests –

    •  The Service Request table includes header information about the individual or organization
        that is the subject of verification.
    •  New Service Request records are assigned to a queue. All potential users who will be
        performing the verifications have access to these records.
    •  A service request is assigned to a single user who will ensure that all qualifications are
         verified. This single user is the only one able to process Qualification records related to their
      own service requests.
    •  Many required tasks when performing verification services are currently done by using
       manual processes.
    •  To keep up with demand, ADatum Corporation identifies several processes that can be
        replaced by using Power Automate flows to hire fewer new staff and keep costs down.




 Qualification verification –

    •  The qualification table contains details about an individual school degree, professional
         qualifications, and other qualifications that must be verified.
    •  A service request can have one or more Qualification records associated with it.
    •  Record status is pending verification until the initial team member finishes, at which point
        the member changes the status to Complete.
    •  When all qualification records related to a service request are verified either by manual or
       automated processes, the results are made available to ADatum Corporation’s client.
    •   In the rare event that results are questioned, a new service request is created and verified
        independently of the previous work that took place.
    •  To complete a service request, users perform the following actions: o Send a templated
        email by using Microsoft Outlook to the client after all qualifications for a service request
        are checked. o Change the service request status to Completed. Currently, service requests
       do not indicate when all Qualification records are addressed.




Microsoft Power platform environment

    •  The following environments exist: development, testing, user acceptance testing (UAT), and
        production.
    •  Managed solutions are used to move customizations from the development environment to
       other higher-level environments. These solutions are created and maintained by the power
        users and provided to internal IT for deployment when they are ready.
    •  Two managed solutions, Verification Process Automation and Onsite Visit, share several
       components.

---

## [Página 35](PL-200-CASES.pdf#page=35) · texto nativo

•   All customizations to Power Platform components are performed by several power users
      who have received training and are certified as subject matter experts.
    •  Power users have been granted the System Administrator security role in the development
       environment.
    •   Corporate policy prohibits power users from writing code due to lack of a formal code
       review process.
    •   Internal IT will not be able to supply any development resources for this project due to a
        lack of staff. This means that any customizations and automation created for this project
      must be low-code/no-code for the power users to implement them.

Customizations created by power users are deployed by internal IT.



Requirements -


Process automation –

ADatum Corporation plans to establish a new QV department to verify completed work so that the
quality of work is maintained. The new process for verifying professional qualifications must
automate the following:

    •   Enter data and navigate the authority’s website. The authority website UI changes
        frequently because the company constantly improves the user experience.
    •   Search page contents for a specified value to determine validity.
    •  Update the corresponding Qualification record in Dataverse.


The new process for completing a service request must automate the following:

    •   Set the Service Request record status to Complete when work on all Qualification records is
        finished.
    •  Send an email to the client with the results when the service request is completed. The
       email must list each qualification as either Valid or Not Valid, depending on the verification.

    Qualification verification -


   • Service request results will not be released to clients until all related Qualification records are
    set to a Complete status.
   • To check work done by a wide array of users, 10 percent of Qualification records must be
   double checked.
   • Qualification records must be automatically assigned to a queue.
   • Qualification records must be flagged with a new status field named Assigned to ensure that
    records are rechecked.
   • Ensure that only QV team members can change the status from Assigned to In Progress to
   Complete.
   • Record the name of the QV team member who performed the work and the date completed.

---

## [Página 36](PL-200-CASES.pdf#page=36) · texto nativo

Governance and security –

    •   All components required for the verification process must be included in a new solution.
    •   Corporate security requires that deployments to non-development environments must be
       automated using service accounts.
    •  User security and data access must also be consistent across environments, except for the
       elevated access of the power users in the development environment.
    •  The Onsite Visit managed solution has a table that is not in the Verification Process Automation
      managed solution. This table must be upgraded prior to the go-live date without the other
       shared components.
    •  A VP of sales requires a test environment to demonstrate to potential clients the security
         policies that are included in their initial offering.


Issues -

    •  More employees than are required can access individual client information and continue to have
        access after a service request is completed.
    •  When users go on vacation, all their outstanding Service Request records are assigned to a
        substitute employee. The substitute employees are unable to see all the qualifications related to
        their service requests.
    •   Currently, testing the new QV functionality outside the development environment is not
        possible due to corporate security policies requiring the same security role across all
       environments.
    •   Internal IT reports that the solution import to the test environment failed because of missing
       dependencies related to the flow for completing service requests.

Question 04 - 01
You need to create the automation for the qualification verification process.


Which two actions should you perform? Each correct answer presents a complete solution.


NOTE: Each correct selection is worth one point.

                    A. Add a Dataverse connector.
                    B.  Add an Outlook connector.
                     C.  Create an on-premises data gateway reference.
                   D.  Update the Qualification records to finished.
                      E.  Create a Service Request record.



Answer 04 - 01
    Correct Answer: A,C

---

## [Página 37](PL-200-CASES.pdf#page=37) · texto nativo

A. Add a Dataverse connector

       •  The automation must update the corresponding Qualification record in Dataverse.

       •  Use the Dataverse connector to update the Qualification status/result.

C. Create an on-premises data gateway reference

       •  The process must interact with an external authority website by entering data, navigating
           pages, and reading page contents.

       •   This type of UI automation typically requires a desktop/UI flow connection through a
          gateway or machine connection so the automation can run against the website.

Why the others are not correct

    •   B. Add an Outlook connector
       Outlook is needed for sending client emails when the service request is completed, not for
        qualification verification.

    •   D. Update the Qualification records to finished
       Updating the record is the result of the automation, but the required configuration action is
       to use the Dataverse connector.

    •   E. Create a Service Request record
     A new service request is only created if results are questioned later, not during normal
        qualification verification.

Reference: https://www.examtopics.com/discussions/microsoft/view/145216-exam-pl-200-topic-3-
question-42-discussion/

Question 04 - 02
You need to address the executive's concerns regarding unnecessary data access.
Which security changes should you make? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 38](PL-200-CASES.pdf#page=38) · texto nativo

Hot Area:





                                                                                                                                                                  .

Answer 04 - 02
    Correct Answer:





   Concern — Unnecessary user access to client data during verification

    •   Security Measure: → Assign records to a service account and add the team member doing the
        verification by using an access team.

   Why?

    •   Access Teams provide temporary, record-level access.
    •  The verifier only gets access to the specific Service Request being worked on.
    •  The record remains owned by the service account, minimizing unnecessary exposure.

   Concern — Unnecessary user access to client data after the request is completed

---

## [Página 39](PL-200-CASES.pdf#page=39) · texto nativo

Security Measure: → Assign records to a service account when the service request is completed.

   Why?

       •   Returning ownership to the service account removes access that was granted through
           assignment.
       •   This ensures employees do not retain access after their work is finished.

Reference: https://www.examtopics.com/discussions/microsoft/view/83377-exam-pl-200-topic-7-
question-1-discussion/

Question 04 - 03
You need to resolve the issue reported by substitute employees after they are assigned service requests.
How should you configure the system? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer 04 - 03
    Correct Answer:

---

## [Página 40](PL-200-CASES.pdf#page=40) · texto nativo

The issue states:

      "When users go on vacation, all their outstanding Service Request records are assigned to a
        substitute employee. The substitute employees are unable to see all the qualifications related to
         their service requests."

A Service Request can have one or more Qualification records, so the relationship is:

Service Request 1:N Qualification:

When ownership of a Service Request changes, the related Qualification records must also transfer
ownership/access to the substitute employee.

Cascade All:

This ensures that assign, share, reparent, and other ownership-related actions are cascaded from the
Service Request to its associated Qualification records.

Reference: https://www.examtopics.com/discussions/microsoft/view/83459-exam-pl-200-topic-7-
question-2-discussion/

---

## [Página 41](PL-200-CASES.pdf#page=41) · texto nativo

Question 04 - 04
You need to implement the requirement for the VP of sales.
What should you do?

    A.  Use a test account with a base security role with QV security added.
    B.  Add the System Administrator security role to your user account.
    C.  Use a test account with only QV security added.
    D. Add QV security to your user account.

Answer 04 - 04
    Correct Answer: A

The requirement is:

"A VP of sales requires a test environment to demonstrate to potential clients the security policies that
are included in their initial offering."

And the issue states:

"Testing the new QV functionality outside the development environment is not possible due to
corporate security policies requiring the same security role across all environments."

To demonstrate the security model properly, you should test with a representative user account, not
with an administrator account.

    •  A base security role provides the normal user permissions.
    •  The QV security role adds the permissions specific to Qualification Verification.
    •   Using a test account accurately reflects how an end user would experience the system.

Why not the others?

    •   B. Add the System Administrator security role to your user account
       System Administrator bypasses security restrictions and would not demonstrate the actual
        security model.

    •   C. Use a test account with only QV security added
      The QV role would typically supplement a base role rather than replace standard access.

    •   D. Add QV security to your user account
       Your existing account likely has elevated privileges, making it unsuitable for validating user-level
        security.

Reference: https://www.examtopics.com/discussions/microsoft/view/83460-exam-pl-200-topic-7-
question-3-discussion/

Question 04 - 05


You create a desktop flow to interact with a certification authority's website.

---

## [Página 42](PL-200-CASES.pdf#page=42) · texto nativo

You need to get data in and out of the desktop flow.
How should you set up the input and output parameters? To answer, select the appropriate options in
the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer 04 - 05
    Correct Answer:





    Explanation:

For a Power Automate Desktop flow, the recommended pattern is:

    •  A cloud flow retrieves the Dataverse record and passes values into the desktop flow using input
       parameters.
    •  The desktop flow returns results using output parameters to the cloud flow.
    •  The cloud flow then updates Dataverse.



Why?

    •  Desktop flows do not typically access Dataverse directly for ALM and governance scenarios.
    •  The standard RPA pattern is Cloud Flow → Desktop Flow → Cloud Flow → Dataverse.
    •   This keeps connections, security, and Dataverse updates centralized in the cloud flow.


Discussion: https://www.examtopics.com/discussions/microsoft/view/83393-exam-pl-200-topic-9-
question-2-discussion/

---

## [Página 43](PL-200-CASES.pdf#page=43) · texto nativo

Question 04 - 06

You need to configure a Power Automate flow to send the email with the results to the client.
What should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.





Answer 04 - 06
    Correct Answer:





For this requirement, the flow must:

         1.  Loop through all Qualification records related to a Service Request to build the email
           content.
         2.  Check whether each qualification is Valid or Not Valid.

---

## [Página 44](PL-200-CASES.pdf#page=44) · texto nativo

Explanation:

    •   • Apply to Each is used to iterate through the collection of Qualification records associated
       with the Service Request.
    •   • Condition is used inside the loop to determine whether the qualification result is Valid or
      Not Valid and append the appropriate text to the email.


Discussion: https://www.examtopics.com/discussions/microsoft/view/83392-exam-pl-200-topic-9-
question-3-discussion/

Question 04 – 07

You need to capture the Date Completed value from the website using a desktop flow.
Which method should you use?

    A.  Use optical character recognition (OCR) on the screen to locate and extract the value.
     B.  Display an input dialog and prompt the user to enter the value.
     C.  Extract the value from the window the browser is using.
    D.  Retrieve the value from the HTML element in the webpage.

Answer 04 - 07
    Correct Answer: D

The requirement is to capture a Date Completed value from a website using Power Automate Desktop.

    •   Retrieve details of a web page / web element is the most reliable and accurate method
       because it reads the value directly from the webpage's HTML/DOM.
    •  OCR should only be used when the value cannot be accessed as a web element (for example, an
       image or remote desktop session).
    •   Input dialog requires manual entry and does not automate the process.
    •   Extracting from the browser window is less precise than reading the specific HTML element.

Additionally, the scenario mentions that the website UI changes frequently. Power Automate Desktop's
web automation and element selectors are designed for interacting with webpage elements, making
them more robust than screen-based techniques such as OCR.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83396-exam-pl-200-topic-9-
question-4-discussion/

Question 04 – 08

You need to assign 10 percent of the Qualification records to the QV queue through table configuration
by using a Power Automate flow.
What should you do?

    A.  Create an autonumber column on the Qualification table and assign its qualification records if
       the number cleanly divides by 10.

---

## [Página 45](PL-200-CASES.pdf#page=45) · texto nativo

B.  Create a calculated column on the Service Request table that sums the number of qualification
        records, generates a random number between zero and the number from the new field, and
        assigns each qualification record if the number generated is 10 percent or less of the value of
       the new field.
    C.  Create a roll-up column on the Service Request table that is the count of qualification records,
       generates a random number between zero and the number from the new field, and assigns each
        qualification record if the number generated is 10 percent or less of the value of the new field.
    D.  Create an autonumber column on the Service Request table and assign its qualification records
            if the number cleanly divides by 10.

Answer 04 - 08
    Correct Answer: A

The requirement is to assign 10% of Qualification records for rechecking by the QV team using a low-
code/no-code approach.

Using an Autonumber column on the Qualification table provides a predictable sequence of values. A
Power Automate flow can evaluate the autonumber and assign records where:

      Autonumber MOD 10 = 0

This selects approximately 1 out of every 10 Qualification records (10%).

Why not the others?

    •  B and C rely on generating random values and counts from Service Requests. This does not
       guarantee a consistent 10% selection of Qualification records and adds unnecessary complexity.

    •  D uses an autonumber on the Service Request table, which would assign all qualifications under
        selected service requests rather than 10% of the Qualification records themselves.

Discussion: https://www.examtopics.com/discussions/microsoft/view/80543-exam-pl-200-topic-9-
question-5-discussion/

Question 04 – 09

You need to configure a Power Automate flow to send the email with the results to the client.
What should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 46](PL-200-CASES.pdf#page=46) · texto nativo

Hot Area:





Answer 04 - 09
    Correct Answer:





For this scenario, the email should be sent when Qualification records are completed, because the
Service Request is only completed after verifying that all related Qualification records are Complete

Why?

    •   statuscode tracks the specific status values (Pending Verification, Complete, etc.), making it the
        correct column to monitor.
    •  When a Qualification record changes to Complete, the flow should check all related
        Qualification records for the Service Request.
    •   Only if all related Qualification records are Complete should the Service Request be marked
       Complete and the email sent to the client.

Discussion: https://www.examtopics.com/discussions/microsoft/view/80545-exam-pl-200-topic-9-
question-6-discussion/

---

## [Página 47](PL-200-CASES.pdf#page=47) · texto nativo

Question 04 - 10
You need to set up the new service request completion process.
Which two components should you include in the solution? Each correct answer presents a complete
solution.
NOTE: Each correct selection is worth one point.

    A.  connection reference
    B.  business process flow
    C.  Power Automate flow
    D.  connection

Answer 04 - 10
    Correct Answer: A,C

    Explanation

   The new service request completion process must:

    •   Detect when all related Qualification records are completed.
    •  Update the Service Request status to Complete.
    •  Send an email to the client with the qualification results.
    •  Be deployed through managed solutions across environments.

    C. Power Automate flow

   A Power Automate flow is required to automate the business process:

    •   Check related Qualification records.
    •  Update the Service Request record.
    •  Send the completion email.

    A. Connection reference

   The scenario mentions that solution imports failed because of missing dependencies related to the
    flow and that deployments must be automated across environments. Connection references are the
    ALM-friendly way to manage connectors inside solutions and allow connections to be configured per
   environment during deployment.

   Why not the others?

    •   B. Business process flow
      A business process flow guides users through stages but does not automate sending emails or
       updating records based on related records.
    •   D. Connection
       Connections themselves are environment-specific and are not included in solutions. A
       connection reference should be used instead..

Discussion: https://www.examtopics.com/discussions/microsoft/view/79404-exam-pl-200-topic-11-
question-1-discussion/

---

## [Página 48](PL-200-CASES.pdf#page=48) · texto nativo

Question 04 - 11
You need to add the missing components to the Verification Process Automation solution.
Which two components should you add? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.

    A.  Service Request statuscode field
    B.  Dataverse connection reference
    C.  Qualification statuscode field
    D.  On-premises data gateway reference
    E.  Outlook connection reference

Answer 04 - 11
    Correct Answer: B,E

    Explanation

   The issue states:

        "Internal IT reports that the solution import to the test environment failed because of missing
       dependencies related to the flow for completing service requests."

   The service request completion flow must:

          1.  Read and update Dataverse records (Service Request and Qualification tables).
          2.  Send emails through Outlook.

   When a flow is included in a solution, the associated connectors must be represented by connection
    references so they can be configured in each environment during deployment.

   Why the others are incorrect

    •   A. Service Request statuscode field
      The status field is part of the table schema and not typically the missing dependency causing
       flow import failures.

    •   C. Qualification statuscode field
      Same reasoning as A; fields are not the connector dependencies referenced by the flow.

•   D. On-premises data gateway reference
   The scenario uses Dataverse and Outlook cloud services, not on-premises data sources.

Discussion: https://www.examtopics.com/discussions/microsoft/view/79413-exam-pl-200-topic-13-
question-1-discussion/

Question 04 - 12
Exam PL-200 topic 13 question 2 discussion

Actual exam question from Microsoft's PL-200

---

## [Página 49](PL-200-CASES.pdf#page=49) · texto nativo

Question #: 2
Topic #: 13

HOTSPOT -
You need to coordinate updates and deployment for managed solutions containing completed work
without disrupting the system.
What should you do? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer 04 - 12
    Correct Answer:





    Explanation

   The key clue is:

   "The Onsite Visit managed solution has a table that is not in the Verification Process Automation
   managed solution. This table must be upgraded prior to the go-live date without the other shared
   components."

    This means a patch should be used for a small change affecting an unrelated table, while
   automation enhancements that affect shared components should be deployed as a full solution
    upgrade.

   Why?

---

## [Página 50](PL-200-CASES.pdf#page=50) · texto nativo

•   Patch = small, targeted updates to existing managed solutions without affecting unrelated
          components.
        •  Upgrade = used when introducing enhancements and changes to solution components
           while ensuring proper removal of obsolete components and maintaining managed solution
             integrity.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83463-exam-pl-200-topic-13-
question-2-discussion/

CASE 5: ALPINE SKI HOUSE
   Background -


    Alpine SKi House is a boutique mountain resort that offers year-round spa and outdoor activities
   such as snow sports, hiking, mountain biking, and more. The resort has been family owned and
   operated for more than 50 years. The company has been able to remain profitable while not
   needing to adopt new technologies.

    Current environment. General -


   Booking at the resort have decreased. The company has decided to focus on creating a tailored,
     first- class experience for guest. The company also plans to target corporate meetings and events.

    The company recently purchased a chatbot named FAQbot from AppSoure. The chatbot uses the
    resort's existing FAQS

    Current environment. Communication -

       •  Communication between staff members is primarily conducted through email and SMS text
           messages.
       •   Conversations between staff members and guest often lost.
       •   Conference calls are used for all group meeting

    Current environment. Event Registration -

        •   Corporate customers can reserve a meeting room at the resort to host meetings. The
           meetings will include lunch and choice of either an inside-spa experience or a seasonally
            appropriate outdoor activity.
        •   Event registration is conducted three weeks prior to start of the event. lt is assumed that
                all event attendees will attend the meeting.

    Current environment. Check-in process -
        •   Guests wait in lines to check in and obtain name badges. At this time, guests can specify any
            dietary restrictions and select their activity preference. This can result in long wait times
          and crowding at the front desk.
        •   For health and compliance reasons, guests must answer a series of questions with a yes or
          no answer during check-in. The front desk will ask and record these answers for the resort's
            records.
    Current environment. Marketing –

---

## [Página 51](PL-200-CASES.pdf#page=51) · texto nativo

At the check-in counter, the guests can drop their business cards into a bowl for a chance to win an
all-inclusive weekend stay at the resort. The resort uses the business card information to send
announcements about promotions and upcoming events.

Current environment. Resort policies and event inquiries –

    •  A guest can call or send an email to the event coordinator at the resort to get information
       about hotel policies, snow conditions, or to pre-select their after-meeting event;
    •   Guests can also go to the website to view the extensive list of frequently asked questions
       (FAQ) compiled over the years. Many of the answers to the FAQs are out of date.


Requirements. General –

Alpine Ski House does not employ technical staff and does not have the budget to hire an external
firm to develop solutions. There are two team members who are proficient at Microsoft Excel
formulas. Any solution created must use the capabilities of current team members.

All solutions must be simple to use, easy to maintain, and represent the brand of the resort.

You must implement the following solutions:

    •  a centrally managed communication solution
    •  a customer service solution
    •  a resort portal
    •  a chat solution
    •  a check-in solution

Requirements. Communication -


    •  Communication between team members must be centrally managed and unified in
        Microsoft Teams.
    •  When the company confirms an event, they must provide a list of guest's names and email
        addresses.
    •  You must send guests a welcome email that includes a unique registration number for
        authentication with the resort's portal.
    •   Guests must receive a separate email to verify proof of ownership for their registration.

Requirements. Event attendance  -

    •   Guests must create an account and sign into resort portal to confirm their attendance to an
       event and preselect an after-meeting event.
    •   Prior to the event, guests must be able to identify any personal dietary restrictions.

Requirements. Check-in processes -


    •   Check-in processes must be self-service. Each screen must ask for specific data from the
        guest. The check-in solution Will use some data that is stored in Microsoft Excel.

---

## [Página 52](PL-200-CASES.pdf#page=52) · texto nativo

•  The check-in solution must continue to function if there are internet issues. If the self-
             service kiosks are not available, staff must be able to use the check-in solution from within
             their communication solution.
        •  The check-in solution must have a screen where the guest Will select either yes or no to
            health and wellness questions. Guests must physically interact with each answer before
           proceeding to the next screen.
        •   Guests must be able to confirm any dietary restrictions they may have entered from the
            portal or add new ones at this time.
        •   Data must be entered in each screen before users move on to the next screen.

   Requirements. Marketing -

        •  To eliminate the handling of business cards, the check-in solution must be able to translate
           the contents of the business cards into Alpine Ski House's marketing system.
        •  The solution must not require any effort or manual entry from the guest to prevent any
           mistyped information and to make it more appealing to the guest to participate.

   Requirements. Hotel policies and event inquiries -

The portal must allow the guest to ask questions about hotel policies, event information, weather
reports, and current weather condition at the resort.

   Requirements. Chat solution -

The chat solution must specifically address the following key words. NO additional key words Will be
added until a later implementation phase:

        •  Snow reports
        •  Weather conditions
        •   Start time
        •  End time
        •   Event date
        •  Outdoor activities
        •   Indoor activities
        •  Most popular

The chat solution must be available always and not require staff to answer all of the questions. If a
question does require a staff member's attention, the solution must determine which staff member
is best to assist the customer with the question.

The information in the FAQ on the legacy website must be used in the chat solution but retyping all
the data from the website should not be required. If quests ask about topics that are not listed in the
FAQ the chat solution must identify the issue and escalate to a staff member.

Team members must be able to ask their own questions through a centrally managed
communication solution instead of using the guest portal. Team members must be able to access the
same FAQ across multiple solutions.

---

## [Página 53](PL-200-CASES.pdf#page=53) · texto nativo

Issue:

Guest1 inquires about snow conditions several times each day of their stay.


Question 05 - 01
You need to embed the check-in solution into the communication solution. To answer, select the
appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer 05 - 01
    Correct Answer:





    Explanation:

The communication solution is Microsoft Teams. The requirement states:

          "If the self-service kiosks are not available, staff must be able to use the check-in solution from
        within their communication solution."

---

## [Página 54](PL-200-CASES.pdf#page=54) · texto nativo

The recommended approach is to embed the Power Apps check-in application in Microsoft Teams as a
tab.

    •  Power Apps Web Studio is used to configure and publish the app for Teams integration.
    •  A Teams tab provides direct access to the app within the centrally managed communication
        solution.

Discussion: https://www.examtopics.com/discussions/microsoft/view/65986-exam-pl-200-topic-8-
question-1-discussion/

Question 05 - 01
You need to add controls to the check-in solution for the health and wellness questions.
Which form control should you use?

    A.  Drop down
    B.  Check box
    C.  Text input

Answer 05 - 02
    Correct Answer: B

    Explanation:

The case states:
       "The check-in solution must have a screen where the guest will select either yes or no to health
      and wellness questions."
       "Guests must physically interact with each answer before proceeding to the next screen."
A Check box is the most appropriate control for capturing Yes/No responses and requiring user
interaction before continuing.


Why not the others?

    •   A. Drop down
         o  Requires opening a list and selecting a value.
         o  Not ideal for quick health-screening questions.

    •   C. Text input

         o  Allows free-form text and does not enforce a Yes/No response.

Discussion: https://www.examtopics.com/discussions/microsoft/view/62057-exam-pl-200-topic-8-
question-2-discussion/

Question 05 - 03
You need to design the resort portal to meet the business requirements.
Which data source should you use?

---

## [Página 55](PL-200-CASES.pdf#page=55) · texto nativo

A.  Microsoft Dataverse
    B.  Microsoft Excel
    C.  Azure SQL Database
    D. SQL Server

Answer 05 - 03
    Correct Answer: A

    Explanation:

   The resort portal is a Power Pages solution where guests must:

    •   Create accounts and authenticate.
    •   Confirm event attendance.
    •   Select activities.
    •   Maintain dietary restrictions.
    •   Interact with the chatbot and portal data.

    Microsoft Dataverse is the native and recommended data source for Power Pages because it
    provides:

    •   Built-in security and authentication
    •   Integration with Power Pages
    •   Support for contacts, registrations, and portal users
    •  Low-code administration suitable for a company without developers
    •   Easy integration with Power Apps, Power Automate, and Power Virtual Agents

   Why not the others?

    •   B. Microsoft Excel

         o  Appropriate for some check-in data, but not as the primary data source for a secure
              customer portal

    •   C. Azure SQL Database

         o  Requires more technical expertise and maintenance than Dataverse.

    •   D. SQL Server

         o  Not the recommended backend for a Power Pages portal and would increase
               complexity.

Discussion: https://www.examtopics.com/discussions/microsoft/view/81451-exam-pl-200-topic-8-
question-3-discussion/

Question 05 - 04
You need to design the resort portal's email registration process.
Which solutions should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 56](PL-200-CASES.pdf#page=56) · texto nativo

Hot Area:





Answer 05 - 04
    Correct Answer:





    Explanation:

Implement the invitation code redemption process → Embed the invitation code in the email link URL

    •   Allows the invited user to redeem the invitation automatically when following the registration
          link.

Validate the user's email → Invitation code sign-up

    •  The Invitation code sign-up mechanism validates that the user owns the invitation associated
       with the email address and allows secure registration.

Discussion: https://www.examtopics.com/discussions/microsoft/view/60816-exam-pl-200-topic-8-
question-4-discussion/

---

## [Página 57](PL-200-CASES.pdf#page=57) · texto nativo

Question 05 - 05

You need to design the resort portal's email registration process.
Which solution should you use?

    A.  Default the invitation code from the email upon logging into the portal
    B.  Auto-populate the invitation code field on the sign in screen from the email link
    C. Embed the invitation code in the email link URL
    D.  Send the customer their username and temporary password in the email link

Answer 05 - 05
    Correct Answer: C

    Explanation:

In Power Pages/Power Apps Portals, the standard invitation redemption process includes sending the
user a link that contains the invitation code. When the user clicks the link, the portal can automatically
process the invitation and validate the registration flow.

    •   Threfore: C. Embed the invitation code in the email link URL

         o   This is the standard invitation redemption mechanism.

Why the other options are incorrect:

    •   A. Default the invitation code from the email upon logging into the portal

         o   Invitation codes are not typically defaulted after login.

    •   B. Auto-populate the invitation code field on the sign-in screen from the email link

         o  The invitation code can be auto-populated, but the recommended design is to embed
              the code in the URL itself.

    •   D. Send the customer their username and temporary password in the email link

         o  Sending usernames and temporary passwords in the URL is insecure and not a portal
                 invitation feature.

Discussion: https://www.examtopics.com/discussions/microsoft/view/87333-exam-pl-200-topic-8-
question-5-discussion/

Question 05 - 06

You need to be able to move a Power Automate desktop flow used in the verification process to the
testing environment.
What should you do?

    A.  Share a copy of the desktop flow with a member of internal IT.
    B.  Use the Export option in the flow to get the flow identifier and provide it to internal IT.
    C.  Send a copy of the desktop flow to a member of internal IT.

---

## [Página 58](PL-200-CASES.pdf#page=58) · texto nativo

D.  Create the desktop flow in a solution and provide it to internal IT.

Answer 05 - 06
    Correct Answer: D

    Explanation:

For ALM (Application Lifecycle Management), Power Automate desktop flows must be added to a
solution to be moved between environments (Development → Test → Production). The solution can
then be exported and imported into the target environment.

Therefore D: placing the desktop flow in a solution enables transport to the testing environment.

    •  A Sharing does not move the flow between environments.

    •  B Exporting only a flow identifier is not a deployment method.

    •  C Sending a copy is not the recommended ALM approach and does not support environment
       deployment.

Discussion: https://www.examtopics.com/discussions/microsoft/view/83461-exam-pl-200-topic-9-
question-1-discussion/

Question 05 - 07

You need to design the FAQ solution to handle unknown responses.
Which component should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:

---

## [Página 59](PL-200-CASES.pdf#page=59) · texto nativo

Answer 05 - 07
    Correct Answer:





    Explanation:

    •   Fallback topic is triggered when the bot cannot match the user's question to an existing topic
        (such as snow reports, weather conditions, event dates, etc.). It handles unknown or
       unrecognized utterances.
    •  Omnichannel for Dynamics 365 Customer Service enables escalation from the chatbot to a live
        agent/staff member and can route the conversation to the most appropriate staff member.

Discussion: https://www.examtopics.com/discussions/microsoft/view/62640-exam-pl-200-topic-10-
question-1-discussion/

Question 05 - 08

You need to embed the FAQbot into the communication solution.
Which actions should you perform? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 60](PL-200-CASES.pdf#page=60) · texto nativo

Hot Area:





Answer 05 - 08
    Correct Answer:





    Explanation:

    •   Since FAQbot already exists, you do not create a new app or new chatbot.
    •  To add an existing Power Virtual Agents/Copilot Studio solution into Teams, you import the
       existing app.

---

## [Página 61](PL-200-CASES.pdf#page=61) · texto nativo

•  Then you import the chatbot into Microsoft Teams so users can interact with it from the
        centralized communication solution.
Discussion: https://www.examtopics.com/discussions/microsoft/view/64137-exam-pl-200-topic-10-
question-2-discussion/


Question 05 - 09
Exam PL-200 topic 10 question 3 discussion

Actual exam question from Microsoft's PL-200

Question #: 3
Topic #: 10

HOTSPOT -
A guest asks about the start time of a specific scheduled event and wants to know what the snow
conditions will be like during their stay.
You need to determine how to design the chat solution to answer those questions.
What should you do? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer 05 - 09
    Correct Answer:

---

## [Página 62](PL-200-CASES.pdf#page=62) · texto nativo

Explanation:

    •  To identify a specific event mentioned by the guest (for example, a corporate event name),
       use an entity and enable smart matching so the bot can recognize variations of the event
      name and pass the value into the topic.
    •  Snow conditions involve specific values or attributes (powder, icy, groomed, fresh snow,
       depth, etc.). These are best modeled as a custom entity that the chatbot can recognize and
       use in conversation.
Discussion: https://www.examtopics.com/discussions/microsoft/view/62202-exam-pl-200-topic-10-
question-3-discussion/

Question 05 - 10
You need to design the chat solution to answer the inquiry from Guest1.
Which three components can you use? Each correct answer presents a complete solution.
NOTE: Each correct selection is worth one point.

    A.  Variables
    B.  Escalations
    C.  Smart match
    D. Synonyms
    E.  Topics

Answer 05 - 10
    Correct Answer: C,D,E

    Explanation:

The inquiry is about snow conditions, which is one of the predefined keywords for the chatbot. To
answer such questions effectively in Power Virtual Agents/Copilot Studio, you need:
    •  A Topic to handle the snow conditions conversation.
    •  Synonyms so different phrases such as "snow report", "snow conditions", "ski conditions",
         etc. trigger the same topic.

---

## [Página 63](PL-200-CASES.pdf#page=63) · texto nativo

•  Smart match to recognize variations in how guests ask the question.
You do not need:
    •   Variables (not required just to identify and answer the inquiry).
    •   Escalations (used when the bot cannot answer or needs a human agent).


Discussion: https://www.examtopics.com/discussions/microsoft/view/62448-exam-pl-200-topic-10-
question-4-discussion/

Question 05 - 11
Guest1 inquires about snow conditions several times during each day of their stay.

You need to create the FAQ solution content.
What should you do first?

    A.  AI Builder
     B.  Automate
     C.  Suggest topics
    D.  Trigger phrases

Answer 05 - 11
    Correct Answer: C

    Explanation:

The inquiry is about snow conditions, which is one of the predefined keywords for the chatbot. To
answer such questions effectively in Power Virtual Agents/Copilot Studio, you need:
    •  A Topic to handle the snow conditions conversation.
    •  Synonyms so different phrases such as "snow report", "snow conditions", "ski conditions",
         etc. trigger the same topic.
    •  Smart match to recognize variations in how guests ask the question.
You do not need:
    •   Variables (not required just to identify and answer the inquiry).
    •   Escalations (used when the bot cannot answer or needs a human agent).


Discussion: https://www.examtopics.com/discussions/microsoft/view/64138-exam-pl-200-topic-10-
question-5-discussion/

Question 05 - 12
Guest1 inquires about snow conditions several times during each day of their stay.


You need to design and create the solution for gathering contact information from guests for marketing
purposes.
What should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 64](PL-200-CASES.pdf#page=64) · texto nativo

Hot Area:





Answer 05 - 12
    Correct Answer:





    Explanation:

For this requirement:
    •  The resort wants to capture information from business cards automatically.
    •   Guests should not manually enter data.
    •   Alpine Ski House has limited technical skills and requires a low-code solution.
Why?

---

## [Página 65](PL-200-CASES.pdf#page=65) · texto nativo

•  AI Builder includes a Business Card Reader prebuilt model that extracts contact details
          such as name, company, phone number, email address, and job title from a photo of a
           business card.
       •  Using a prebuilt AI model satisfies the low-code/no-code requirement and avoids the
         need to build custom AI models or integrate external services.


Discussion: https://www.examtopics.com/discussions/microsoft/view/66708-exam-pl-200-topic-12-
question-1-discussion/

Question 05 - 13
You need to embed the business card solution in the check-in app.
What should you use?

    A.  Input control
    B.  Custom component
    C.  Button control
    D.  AI Builder component

Answer 05 - 12
    Correct Answer: D

    Explanation:

The requirement is to embed the business card reader functionality directly into the check-in
app.
Power Apps provides an AI Builder Business Card Reader component that can be added to a
canvas app. This component allows users to scan a business card and automatically extract contact
information (name, email, phone number, company, etc.) without manual entry.
    •   A. Input control (Incorrect) – Used for manual data entry.
    •   B. Custom component (Incorrect) – Unnecessary because a built-in AI Builder component
       already exists.
    •   C. Button control (Incorrect) – Can trigger actions but does not provide business card
        recognition.
    •   D. AI Builder component (Correct) – Specifically designed for business card scanning and
       data extraction.


Discussion: https://www.examtopics.com/discussions/microsoft/view/65376-exam-pl-200-topic-12-
question-2-discussion/

Question 05 - 13
Exam PL-200 topic 12 question 3 discussion

Actual exam question from Microsoft's PL-200

---

## [Página 66](PL-200-CASES.pdf#page=66) · texto nativo

Question #: 3
Topic #: 12

HOTSPOT -
You need to design the guest check-in solution.
Which technologies should you use? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.
Hot Area:





Answer 05 - 13
    Correct Answer:

---

## [Página 67](PL-200-CASES.pdf#page=67) · texto nativo

Explanation:

    For the guest check-in solution:
   Requirement 1: Develop the base check-in solution → Canvas app
   Why?
       •  The check-in process requires multiple custom screens.
       •   Users must enter data on each screen before proceeding.
       •  The solution must work on kiosks and be easy to customize.
       •  Canvas apps support offline capabilities and AI Builder components.
   Requirement 2: Access the check-in solution on the check-in devices → Power Apps
   mobile app
   Why?
       •  The requirement states the solution must continue to function during internet issues.
       •  Canvas apps can be run through the Power Apps mobile app, which supports offline
            scenarios.
       •   This is the standard approach for kiosk/tablet-based Power Apps solutions.


Discussion: https://www.examtopics.com/discussions/microsoft/view/61518-exam-pl-200-topic-12-
question-3-discussion/
