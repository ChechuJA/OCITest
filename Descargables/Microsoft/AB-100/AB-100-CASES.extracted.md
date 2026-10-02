# Transcripción: AB-100-CASES.pdf

- Archivo fuente: `AB-100-CASES.pdf`
- Páginas del archivo: 19
- Páginas incluidas: `1-19`
- Extracción: 2026-10-02T11:15+02:00
- Aviso: resultado automático; cotejar cifras e identificadores con el original.

## [Página 1](AB-100-CASES.pdf#page=1) · texto nativo

CASE 01 FABRIKAM
Fabrikam, Inc., is a global consumer goods company that is undergoing a digital transformation initiative
to migrate its entire infrastructure to the Microsoft cloud. As a key element of this cloud migration, the
company will implement Microsoft Dynamics 365 Sales, moving away from the current on-premises
proprietary technologies used by its business-to-business (B2B) sales team.

As part of the cloud migration, Fabrikam will adopt an AI-first approach to its business solutions and
implement AI solutions, wherever possible, to streamline operations.



Problem Statements -

Fabrikam's infrastructure currently relies on various on-premises systems that require sales executives
to use corporate computers with physical keyboards to access business information during customer
interactions. Mobile phones cannot be used for these purposes, as the systems depend on keyboard
input. As a result, the sales executives spend a lot of time using keyboards to search for data on several
disparate systems and file servers, rather than focusing on the customers. This affects the customer
experience.

Fabrikam stakeholders are concerned that users will be hesitant to adopt AI. If the AI initiatives are NOT
adopted, cost savings will never be realized. Additionally, funding for future AI initiatives will depend on
demonstrating an increase in AI adoption month over month. As the AI agent initiative for the sales
team will be the first for Fabrikam, the rapid adoption of the agent is a high priority.



Planned Initiatives -



General -

Fabrikam management has prioritized AI-driven projects to improve efficiency, customer engagement,
and responsible AI adoption. The current application infrastructure is on-premises and must be migrated
to the cloud to support the adoption of these technologies.



Infrastructure Migration -

Fabrikam plans to migrate from its current on-premises infrastructure to a completely cloud-based
topology; this will include user authentication, the security framework, and, primarily, the adoption of
the services by end users.

All the data from the different systems will be consolidated into a single data source - a common data
model that will use a Microsoft Dataverse environment as a single source of truth (SSOT) for the sales
team.

---

## [Página 2](AB-100-CASES.pdf#page=2) · texto nativo

Sales Cycle Enablement -

To achieve the company's objectives, Fabrikam intends to implement the following strategies to
enhance the sales cycle:

Use low-code development to create a single AI agent that has Dataverse as its core component.

Ensure that sales managers can access unanswered correspondence from prospects and intervene as
appropriate.

Replace the previous proprietary software with Dynamics 365 Sales to track sales cycles and customer
interactions.

Have the sales executives use Dynamics 365 Sales to track interactions for open opportunities and send
follow-up communications to prospects.

Have the sales executives use handsfree headsets to interact with an AI agent when they have questions
about internal policies or customer data.



Requirements -



Infrastructure Migration -

Fabrikam has identified the following infrastructure migration requirements:

Azure must be used for all future infrastructure workloads.

The company must follow Microsoft-recommended methodologies for infrastructure migration to the
cloud.

Any created AI agents must have their return on investment (ROI) calculated to ensure that the solution
will save the company money.



Sales Cycle Enablement -

Fabrikam has identified the following requirements for sales cycle enablement:

The final AI agent must follow Microsoft recommendations for a conversational user experience.

A designated checklist must be reviewed to ensure that the AI agent follows Microsoft deployment
recommendations for a compliant solution.

Detailed telemetry must be logged for the first created AI agent to help troubleshoot and optimize the
agent during the initial AI agent adoption process.

Unexpected AI agent actions must end in an escalation to a live representative. For example, a sales
executive must be rerouted to a representative if the agent cannot answer a question after two failed
attempts.

---

## [Página 3](AB-100-CASES.pdf#page=3) · texto nativo

The return on investment (ROI) of switching from the current process to the future process is required
for stakeholder sign off.

The sales team must use Dynamics 365 Sales to correspond with prospects more quickly and efficiently
than currently.

Sales managers must report on the adoption of the AI agent to key Fabrikam stakeholders on a monthly
basis.

Any sensitive information, such as user IDs and names, shared via the AI agent must be tracked for
future auditing.

Question 01 - 01


Which framework should you use to meet the AI agent requirements for the sales cycle enablement? To
answer, select the appropriate options in the answer area.





Answer 01 - 01
    Correct Answer:

---

## [Página 4](AB-100-CASES.pdf#page=4) · texto nativo

Scenario:

You must select the “Azure Virtual Desktop” app so the policy applies whenever a user connects to AVD
resources.

To “force reauthentication if the session lasts more than eight hours,” you configure a sign‐in frequency
(for example, every 8 hours) in the Session controls.

Reference: Exam AB-100 topic 1 question 1 discussion - ExamTopics


Question 01 – 02
Which framework should you use for the infrastructure migration?

    A.  Microsoft Cloud Adoption Framework for Azure
    B.  Success by Design
    C.  Microsoft Power Platform Center of Excellence (CoE)
    D.  Microsoft Power Platform Project Setup Wizard

Answer 01 - 02
    Correct Answer: A

   CAF is Microsoft’s official, end-to-end methodology for: - Migrating on-premises infrastructure to
   Azure - Modernizing identity, security, networking, and governance - Establishing cloud landing
   zones - Guiding organizations through strategy → plan → ready → adopt → govern → manage
    Fabrikam’s requirements explicitly state: - “Azure must be used for all future infrastructure
    workloads.” - “The company must follow Microsoft-recommended methodologies for infrastructure
    migration to the cloud.”

Reference:

---

## [Página 5](AB-100-CASES.pdf#page=5) · texto nativo

Question 01 - 03


Which tool should you recommend to address the sensitive information concerns in the sales process?

    A.  the Analytics tab in Microsoft Copilot Studio
    B.  Model Context Protocol (MCP)
    C.  Application Insights
    D.  Microsoft Foundry Tracing UI
    E.  Monitoring in Microsoft Foundry

Answer 01 - 03
    Correct Answer: C

   The case study outlines a specific requirement: "Detailed telemetry must be logged for the first
    created AI agent to help troubleshoot and optimize... Any sensitive information, such as user IDs and
   names, shared via the AI agent must be tracked for future auditing."

Reference: https://www.examtopics.com/discussions/microsoft/view/384055-exam-ab-100-topic-3-
question-1-discussion/


Question 01 – 04


Which existing tool and data should you use to gather the required metrics for stakeholder signoff for
the AI agents? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.





Answer 01 - 04
    Correct Answer:

---

## [Página 6](AB-100-CASES.pdf#page=6) · texto nativo

1 - Tool: Microsoft Copilot Studio The ROI calculation for AI agents is done using: - Telemetry from
    Copilot Studio - Task duration metrics - Usage analytics This aligns with the requirement to
   measure how long tasks currently take so the organization can compare: - Before AI agent vs.
    After AI agent Foundry, ARM, and Dynamics 365 Sales do not provide the required task-level
    timing metrics for ROI.

   2 - Data required for the tool: the current time to complete the task today per instance ROI
    requires a baseline: - How long does the task take right now? - How much time will the AI agent
   save per instance? This is the only data point in the list that directly supports ROI modeling for AI
   agent adoption.

Reference: https://www.examtopics.com/discussions/microsoft/view/384056-exam-ab-100-topic-3-
question-2-discussion/


Question 01 - 05


Which template should you use for the AI agent to meet the requirements for the sales executives?

    A.  IT Helpdesk in Microsoft Copilot Studio
    B.  AI agents in Microsoft Foundry
    C.  Voice in Microsoft Copilot Studio
    D.  AI chat in Microsoft Foundry

Answer 01 - 05

    Correct Answer: C

Scenario:

---

## [Página 7](AB-100-CASES.pdf#page=7) · texto nativo

The case study states that sales executives will use hands-free headsets to interact with the AI
    agent. This template is specifically designed for:

       •   Voice-enabled conversational agents
       •  Headset or microphone-based interaction
       •   Real-time Q&A
       •   Hands-free workflows for field or sales scenarios

    Exactly what Fabrikam’s sales executives need.

Reference: https://www.examtopics.com/discussions/microsoft/view/384389-exam-ab-100-topic-2-
question-1-discussion/

Question 01 - 06


Which tool should you use for the prospect communication requirements in Dynamics 365 Sales?

    A.  Azure AI Search
    B.  Copilot email assist
    C.  the Voice template Microsoft Copilot Studio
    D. Deep Research in Microsoft Foundry Agent Service

Answer 01 - 06
    Correct Answer: B

Scenario:
Copilot email assist is built specifically for Dynamics 365 Sales and provides:

       •   AI-generated email drafts
       •   Follow-up suggestions
       •   Context-aware responses based on opportunity and lead data
       •   Faster prospect communication directly inside the Sales workflow.

This aligns perfectly with the requirement

Reference: https://www.examtopics.com/discussions/microsoft/view/384390-exam-ab-100-topic-2-
question-2-discussion/


Question 01 - 07


Which components should you use to meet the sales cycle enablement requirements? To answer, select
the appropriate options in the answer area.

---

## [Página 8](AB-100-CASES.pdf#page=8) · texto nativo

NOTE: Each correct selection is worth one point.





Answer 01 - 07
    Correct Answer:





Scenario:

1. Microsoft Copilot Studio → AI agent creation The case study requires:

       •  A low-code AI agent

---

## [Página 9](AB-100-CASES.pdf#page=9) · texto nativo

•   Built on Dataverse
       •  Used by sales executives through voice/headset
       •  With telemetry, governance, and adoption tracking

This is exactly what Copilot Studio is designed for.

Foundry is code-first and not aligned with the low-code requirement.

2. Fallback topic → Unexpected AI agent actions The requirements state:

       •    If the agent fails twice, it must escalate to a live representative
       •  Unexpected actions must be handled gracefully

In Copilot Studio, the Fallback topic is the built-in mechanism for:

       •   Handling unrecognized intents
       •  Managing repeated failures
       •   Triggering escalation workflows

  Reference: https://www.examtopics.com/discussions/microsoft/view/384391-exam-ab-100-topic-2-
question-3-discussion/


Question 01 - 08


Which tool should you recommend to help secure funding for future AI agent development?

    A.  Evaluations in Microsoft Foundry
    B.  the Azure Cost Optimization workbook
    C.  Azure Operator Insights
    D.  the Analytics tab in Microsoft Copilot Studio
    E.  Direct Preference Optimization (DPO)

Answer 01 - 08
    Correct Answer: D

   The Analytics tab in Copilot Studio provides:

       •  Usage metrics (how often the agent is used)
       •  Adoption trends (month-over-month usage)
       •   Conversation volume
       •   Success vs. failure rates
       •   Insights needed to justify ROI

   These metrics are exactly what stakeholders need to approve future funding.

Reference: https://www.examtopics.com/discussions/microsoft/view/384403-exam-ab-100-topic-3-
question-3-discussion/

---

## [Página 10](AB-100-CASES.pdf#page=10) · texto nativo

CASE 02 CONTOSO
   Overview -


    Contoso, Ltd. is a high-tech manufacturing company that uses Microsoft Dynamics 365 Finance.
   Dynamics 365 Supply Chain Management, and Dynamics 365 Commerce for its North American
    operations. The company designs and develops innovative products that have many patents and
    proprietary technologies. The patents and engineering designs are closely guarded secrets.


   Contoso executives want to integrate and adopt AI solutions to help scale the company in
    preparation for an anticipated period of rapid growth.


   The company has multiple legal entities and Azure subscriptions that will be used in the adopted AI
    solutions.

   Requirements -



    AI Adoption -


   The following executives will have specific responsibilities in the overall AI adoption:


   • Chief Technology Officer (CTO): Select one Dynamics 365 Finance, Dynamics 365 Supply Chain
   Management or Dynamics 365 Commerce prebuilt AI agent and one custom Microsoft Copilot
    Studio AI agent to prioritize and deploy during the initial AI adoption phase.
   • Chief Information Officer (CIO): Ensure that appropriate security labels are assigned to the data
   used by the AI agents.
   • Chief Financial Officer (CFO): Analyze the return on investment (ROI) for the AI agents being
    deployed.
   • Chief Information Security Officer (CISO): Discover and inventory AI resources for auditing.
   • Chief Executive Officer (CEO): Ensure that all solutions adhere to industry-standard responsible AI
    practices.


     All AI initiatives and agents will have a detailed business use case, a defined audience profile, and an
    estimated ROI that will compare the cost savings of the current process against the estimated costs
    of using the new AI solutions.


   The company's research and development (R&D) department already has a custom Model Context
    Protocol (MCP) server that contains comprehensive product specifications and compliance data.



    Prebuilt AI Agent -


   The CTO has NOT yet selected which prebuilt AI agent to use in Dynamics 365 Supply Chain

---

## [Página 11](AB-100-CASES.pdf#page=11) · texto nativo

Management. The CTO wants to view available agent templates to identify which agent will add the
most business value.

Depending on which high-priority AI agents are identified, its agent capabilities must be previewed
in a discovery meeting with the relevant business operation stakeholders.



Custom AI Agent -


Contoso has identified the following custom AI agent requirements:
• The custom AI agent will use data from Dynamics 365 Supply Chain Management to answer
questions for the manufacturing team as a low-code solution.
• The custom AI agent will be accessible from within Microsoft Teams.
• The custom AI agent must be designed to eventually connect to other agents that can be selected
based on their description.
• The topics used in the custom AI agent will be selected based NOT on a trigger phrase, but on a
description of the purpose of the query, to make the interactions more conversational.
• The custom AI agent must be able to answer questions about product specifications by using
existing technologies. The product specifications are maintained by the R&D department.
• The custom AI agent must be integrated with and accessible from Dynamics 365 Supply Chain
Management.
• The custom AI agent must be able to use Dynamics 365 Supply Chain Management business logic
that is stored outside of the application.


Analysis, Reporting, and Troubleshooting


Contoso has identified the following analysis, reporting, and troubleshooting requirements:
• The CISO will audit all the AI solutions monthly for compliance and security.
• The CFO will analyze all the AI solutions quarterly to compare the estimated ROI against actual
measured efficiencies and adoption. The CFO will use the Copilot Studio agent usage estimator to
perform this analysis.
• The CISO wants to identify how much sensitive data was accessed for a given AI agent run and who
accessed the data. Too much sensitive data accessed by a single user might indicate a high security
risk.
• The CTO wants to track user feedback on the quality of the AI agent responses during user
interactions with the agents. Consistently poor feedback will trigger an escalated reengineering
discussion.
• The CEO wants a quarterly assessment of all the required metrics for their specific responsibilities.
The tools used for the assessments must be Microsoft-recommended and must verify reliability,
interpretability, fairness, and compliance.
• The CFO wants to identify how many interactions with the AI agents are abandoned on a given day
as compared to resolved conversations. Too many abandoned sessions might indicate that Copilot
Studio credits are being used inefficiently by end users.

---

## [Página 12](AB-100-CASES.pdf#page=12) · texto nativo

Question 02 - 01
Which two components in the custom AI agent design should the CFO evaluate in the quarterly agent
analysis? Each correct answer presents part of the solution.


NOTE: Each correct selection is worth one point.

    A.  the GPT models used for the agent
    B.  the average characters in a chat message
    C.  the agent orchestration method
    D.  the average session time per agent

Answer 02 - 01
    Correct Answer: C

C. generative orchestration

    •   C. the agent orchestration method This affects how many model calls, how complex the
       reasoning steps are, and how many credits are consumed per interaction.
                -   Multi-agent orchestration, tool calls, and reasoning depth all impact cost.
                -   The usage estimator explicitly evaluates orchestration patterns because they change the
                 total cost per session.
    •   D. the average session time per agent Session duration is a direct cost driver because longer
        sessions typically involve:
                -  More turns
                -  More model calls
                -  More grounding queries
                -  More tool invocations.

    Reference: https://www.examtopics.com/discussions/microsoft/view/406238-exam-ab-100-topic-
    1-question-31-discussion/


Question 02 - 01
What should you configure for the custom AI agent?

    A.  AI-assisted evaluators
    B.  classic orchestration
    C.  generative orchestration
    D.  Azure OpenAI reasoning models

Answer 02 - 01
    Correct Answer: C

C. generative orchestration

    •  Use topics selected based on a description, not a trigger phrase → this is a generative topic
        router capability.

---

## [Página 13](AB-100-CASES.pdf#page=13) · texto nativo

•  Be conversational, selecting topics based on the purpose of the query → this is only supported
       by generative orchestration.
    •  Connect to other agents selected by description → again, generative orchestration.
    •  Use Dynamics 365 Supply Chain Management business logic stored outside the application →
        generative orchestration can call actions, connectors, and external logic.
    •  Answer questions using existing R&D product specifications → generative orchestration
       supports grounding and multi-source reasoning.

Reference: https://www.examtopics.com/discussions/microsoft/view/406239-exam-ab-100-topic-1-
question-32-discussion/


Question 02 - 02
What should you recommend to assist the CTO with the prebuilt agent selection process?

    A.  Agent management
    B.  Copilot Studio
    C.  Lifecycle Services (LCS)
    D.  Immersive Home

Answer 02 - 02
    Correct Answer: D

Immersive Home Takeaway: To help the CTO view available prebuilt AI agent templates in Dynamics 365
Supply Chain Management and preview their capabilities, the correct recommendation is Immersive
Home.

The case study states:

•  The CTO wants to view available prebuilt AI agent templates.
•  The CTO also wants to preview agent capabilities during discovery meetings.

Reference: https://www.examtopics.com/discussions/microsoft/view/406250-exam-ab-100-topic-2-
question-28-discussion/


Question 02 - 03


What should you include in the custom AI agent design to meet the R&D product specifications and the
compliance information requirements? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 14](AB-100-CASES.pdf#page=14) · texto nativo

Answer 02 - 03
    Correct Answer:

    1.  Custom connector → Expose R&D product specifications + compliance data

The case study states:

       •  R&D already has a custom MCP server containing product specifications and compliance
            data.
       •  The custom AI agent must be able to answer questions using existing technologies.
       •  The agent must access Dynamics 365 Supply Chain Management business logic stored
           outside the application.
    2.  Add the MCP server → Provide product specifications + compliance data

The R&D department already maintains:

       •  A Model Context Protocol (MCP) server
       •   Containing product specifications
       •  And compliance information

To make this data available to the agent, you must add the MCP server as a data source/tool inside the
agent.

 Reference: https://www.examtopics.com/discussions/microsoft/view/406251-exam-ab-100-topic-2-
question-29-discussion/

---

## [Página 15](AB-100-CASES.pdf#page=15) · texto nativo

Question 02 - 04


Which two components for the custom AI agent should you include in the application lifecycle
management (AIM) process? Each correct answer presents part of the solution.

NOTE: Each correct selection is worth one point.

    A.  an Azure package
    B.  a ZIP package
    C.  a Microsoft Power Platform solution
    D.  a Cloud Scale Unit (CSU) package
    E.  an X++model

Answer 02 - 04
    Correct Answer: B,C

Scenario:

B. a ZIP package This is required because Copilot Studio exports agents as ZIP files when:

       •  Moving between tenants
       •   Backing up agents
       •   Importing into another environment
       •   Packaging custom connectors (OpenAPI definitions are also ZIP-based)

C. Microsoft Power Platform solution This is mandatory for ALM of Copilot Studio agents. Copilot Studio
agents are packaged and moved between environments only through Power Platform solutions.
Solutions provide:

       •   Versioning
       •  Dependency tracking
       •  Managed/unmanaged deployment
       •  Environment promotion (Dev → Test → Prod)

Reference: https://www.examtopics.com/discussions/microsoft/view/406265-exam-ab-100-topic-3-
question-39-discussion/


Question 02 - 05


Which tools should you recommend to assist the CISO and the CIO with their specific responsibilities? To
answer, drag the appropriate tools to the correct executives. Each tool may be used once, more than
once, or not at all. You may need to drag the split bar between panes or scroll to view content.


NOTE: Each correct selection is worth one point.

---

## [Página 16](AB-100-CASES.pdf#page=16) · texto nativo

Answer 02 - 05
    Correct Answer:





Scenario:

 1. CISO → Microsoft Purview The CISO must:

       •   Discover and inventory AI resources for auditing
       •   Identify how much sensitive data was accessed
       •  See who accessed sensitive data
       •  Perform monthly compliance and security audits

These responsibilities align exactly with Microsoft Purview.

2. CIO → Copilot Studio The CIO must:

- Ensure appropriate security labels are assigned to the data used by AI agents Security labels for AI
agents are configured within Copilot Studio, where the CIO can:

       •   Assign data classifications
       •   Configure data access policies
       •  Manage connectors and data sources
       •   Apply environment-level governance

Copilot Studio is the correct tool for managing data labeling and governance for AI agents.

---

## [Página 17](AB-100-CASES.pdf#page=17) · texto nativo

Reference: https://www.examtopics.com/discussions/microsoft/view/406266-exam-ab-100-topic-3-
question-40-discussion/


Question 02 - 06



What should you recommend to assist the CEO with their specific responsibilities?

            A.  the Microsoft Service Trust Portal
            B.  Microsoft Foundry Tools
            C.  Microsoft Purview
           D.  the Responsible AI dashboard
             E.  Compliance Center

Answer 02 - 06
    Correct Answer: D

Scenario:

The Responsible AI dashboard is the only option that provides:

       •  Model fairness analysis
       •   Error and bias detection
       •   Explainability and interpretability reports
       •   Safety and reliability evaluations
       •   Compliance-aligned assessments
       •  A unified view of responsible AI metrics across agents and models

This aligns perfectly with the CEO’s responsibilities..

Reference: https://www.examtopics.com/discussions/microsoft/view/406267-exam-ab-100-topic-3-
question-41-discussion/


Question 02 - 07


Which Copilot Studio analytics metrics should you recommend to assist the executives with their specific
responsibilities? To answer, drag the appropriate metrics to the correct executives. Each metric may be
used once, more than once, or not at all. You may need to drag the split bar between panes or scroll to
view content.

NOTE: Each correct selection is worth one point.

---

## [Página 18](AB-100-CASES.pdf#page=18) · texto nativo

Answer 02 - 07
    Correct Answer:





    1.  CFO → Use The CFO wants to analyze:
       •  How many interactions are abandoned vs. resolved
       •  Whether Copilot Studio credits are being used efficiently
       •   Actual usage vs. estimated ROI These insights come from the Use metric, which includes:
       •   Session counts
       •  Abandonment rate
       •   Resolution rate
       •   Daily/weekly/monthly usage trends

This directly reflects credit consumption efficiency.

2. CTO → Satisfaction The CTO wants to:

       •   Track user feedback on the quality of AI agent responses
       •   Trigger reengineering discussions when feedback is consistently poor

This is exactly what the Satisfaction metric measures:

       •  User thumbs-up / thumbs-down
       •  Feedback comments
       •   Quality perception trends

This is the only metric tied to response quality.

---

## [Página 19](AB-100-CASES.pdf#page=19) · texto nativo

Reference: https://www.examtopics.com/discussions/microsoft/view/406268-exam-ab-100-topic-3-
question-42-discussion/
