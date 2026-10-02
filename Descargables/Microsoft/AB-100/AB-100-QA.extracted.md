# Transcripción: AB-100 Q&A.pdf
- PDF original: [AB-100 Q&A.pdf](AB-100%20Q%26A.pdf)
- Referencias: cada encabezado `Página N` corresponde a la página de origen p. N.
- Sin texto utilizable: p. 83 (aparentemente vacía; OCR no ejecutado).

- Archivo fuente: `AB-100 Q&A.pdf`
- Páginas del archivo: 83
- Páginas incluidas: `1-83`
- Extracción: 2026-10-02T11:12+02:00
- Aviso: resultado automático; cotejar cifras e identificadores con el original.

## [Página 1](AB-100%20Q%26A.pdf#page=1) · texto nativo

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
A company uses Microsoft Dynamics 365 Sales to manage leads that are stored in a Microsoft
Dataverse table named Lead and use non-standard terminology and custom columns.

You need to configure business terms in the Lead table so that Microsoft Copilot controls can
summarize the leads efficiently. The solution must minimize administrative effort.

How should you configure the business terms?

    A. Combine all the fields into one custom field.
    B. Map the field display names as business terms.
   C. Add the schema names as business terms.
   D. Create new business terms for each field.

---

## [Página 2](AB-100%20Q%26A.pdf#page=2) · texto nativo

Answer
   Correct Answer: B

   Explanation:

To let Microsoft Copilot summarize leads effectively with the least administrative effort, you should
map the existing display names of the Lead table’s fields to business terms. This avoids creating
new terms manually and aligns Copilot with the terminology already used in Dynamics 365 Sales.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384378-exam-ab-100-
topic-1-question-3-discussion/

002 Question.
You are designing two Microsoft Copilot Studio agents named Agent1 and Agent2. Each agent must
meet the following requirements:

    •  Each agent must use a standard model.
    •  Each agent must NOT use generative orchestration.
    •  Agent1 must support simple and short phrases for a given topic.
    •  Agent2 must integrate with Microsoft Dynamics 365 Contact Center voice channel.

You need to recommend language models for the agents.
What should you recommend for each agent? To answer, drag the appropriate language models to
the correct agents. Each language model may be used once, more than once, or not at all. You may
need to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 3](AB-100%20Q%26A.pdf#page=3) · texto nativo

Explanation:

    •  Agent1

   Requirements:

       •  Standard model
       •  No generative orchestration
       •  Handles simple, short phrases

Answer: Natural language understanding (NLU)

   Why: NLU is the classic intent-based model in Copilot Studio. It is optimized for short
   utterances and deterministic topic triggering.

    A.  Agent2

   Requirements:

       •  Standard model
       •  No generative orchestration
       •  Must integrate with Dynamics 365 Contact Center voice channel

Answer: Conversational language understanding (CLU)

   Why: CLU is the only standard model that supports speech-to-intent scenarios and is required
    for voice channel integration.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384379-exam-ab-100-
topic-1-question-4-discussion/

003 Question.
A company uses Microsoft Dynamics 365 finance and operations apps.

The company plans to use Microsoft Copilot in-app help and guidance to generate responses for
internal business processes.

You need to add an additional knowledge source for the business processes. The solution must
NOT add new topics to the Copilot agent for the finance and operations apps.

---

## [Página 4](AB-100%20Q%26A.pdf#page=4) · texto nativo

Which knowledge source should you add?

    A.  Microsoft Dataverse
    B. a public website
   C. Azure AI Search
   D. a file upload
Answer
   Correct Answer: B

   Explanation:

   You can add knowledge to the Copilot help and guidance feature by uploading files to Copilot
   Studio (in file formats such as PDF, RTF, or Word). If you want to add other types of knowledge
   (such as from SharePoint or other data sources), then you must add your own topic in the
    Copilot for Finance and Operations apps agent in Copilot Studio. Reference article
    https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/copilot/extend-
    copilot-generative-help

Discussion: https://www.examtopics.com/discussions/microsoft/view/384053-exam-ab-100-
topic-1-question-5-discussion/

004 Question.
A company has an AI business solution.
You need to extend the solution so that Microsoft 365 Copilot can invoke external logic hosted in
Azure services.
What should you include in the solution?

    A.  Microsoft Copilot Studio skills
    B.  Microsoft Power Platform connectors
   C. custom engine agents
Answer
   Correct Answer: A

   Explanation:

    Microsoft 365 Copilot can call Copilot Studio skills, which act as extensions that connect
    Copilot to:

       •  Azure Functions
       •  Azure API Management
       •  Custom REST APIs
       •  Power Platform connectors
       •  Other external services

---

## [Página 5](AB-100%20Q%26A.pdf#page=5) · texto nativo

These skills allow Copilot to execute external logic and return results directly into the user’s
    Microsoft 365 experience.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384380-exam-ab-100-
topic-1-question-6-discussion/

005 Question.
You need to design a shared prompt library that will be used across multiple business units. The
solution must meet the following requirements:

    •  Ensure consistent AI responses with reusable formats.
    •  Support governance and version control.
    •  Minimize administrative effort.
    •  Minimize ongoing costs.

What should you recommend for each requirement? To answer, select the appropriate options in
the answer area.
NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 6](AB-100%20Q%26A.pdf#page=6) · texto nativo

Explanation:

   Ensure consistent AI responses: → Define standardized prompt templates Standardized
   templates give every business unit the same structure, tone, and expectations. This is the only
    option that guarantees consistent responses across teams.

   Support governance and version control: → Store prompts in a Git repository - A Git repo
    provides: - Full version history - Branching and approvals - Governance workflows - Minimal
   cost (often free with existing DevOps/GitHub).

Discussion: https://www.examtopics.com/discussions/microsoft/view/384381-exam-ab-100-
topic-1-question-7-discussion/

006 Question.
A company has a Microsoft Foundry project that uses a single agent and a single prompt to
complete a series of tasks.

    •  The agent encounters the following issues:
    •    It frequently produces incomplete results.
    •    It struggles with domain-specific reasoning.
    •  Agent response times are remarkably slow.

You need to recommend a solution to improve the overall performance and accuracy of the agent.
What should you include in the recommendation? To answer, drag the appropriate actions to the
correct requirements. Each action may be used once, more than once, or not at all. You may need
to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.

---

## [Página 7](AB-100%20Q%26A.pdf#page=7) · texto nativo

Answer
   Correct Answer:





   Explanation:

   To improve performance: → Move to a multi-agent architecture: A multi-agent architecture
    distributes tasks across specialized agents. This reduces cognitive load on a single model and
    dramatically improves speed, task completion, and parallelization.

   To improve accuracy: → Add a grounding data source: Adding a grounding data source (Azure
    AI Search, SharePoint, Dataverse, etc.) gives the agent authoritative domain knowledge. This
   improves precision, reasoning, and completeness.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384382-exam-ab-100-
topic-1-question-8-discussion/

007 Question.
A financial services company uses Microsoft Dynamics 365 Finance.
Currently, the company's support staff manually reviews customer transaction histories to detect
potential fraud cases before escalating the cases.
You need to recommend an automation solution for the review process. The solution must ensure
that escalations reach a human analyst for final decision making. What should you recommend?

    A. Deploy an autonomous agent that closes non-fraud cases automatically.
    B. Use Microsoft 365 Copilot in Word to automatically finalize fraud detection policies.
   C. Configure a task agent to generate fraud risk scores for the human analyst to review.
   D. Export the data to a data lake for analysis in Microsoft Power BI.

---

## [Página 8](AB-100%20Q%26A.pdf#page=8) · texto nativo

Answer
   Correct Answer: C

   Explanation:

   The company needs automation, but not full autonomy. The requirement explicitly states:

              •   Escalations must still reach a human analyst
              •  The system should assist, not replace, human decision-making
              •  The process involves structured, repeatable analysis (transaction review → risk
                  scoring → human review)

Discussion: https://www.examtopics.com/discussions/microsoft/view/384383-exam-ab-100-
topic-1-question-9-discussion/

008 Question.
A company plans to deploy a Microsoft Copilot Studio agent that will analyze historical business
data to predict customer behavior.
The data is currently stored in an Azure SQL database, flat files, APIs, and logs.
You need to organize the data into a format that can be used as a knowledge source in Copilot
Studio.
What should you include in the solution?

    A.  Azure AI Search
    B.  Azure Data Lake Storage
   C. Azure Cosmos DB
   D. Azure Translator in Foundry Tools
Answer
   Correct Answer: A

   Explanation:

   Azure AI Search is the correct choice. It’s the only option in the list that can index, chunk, and
    vectorize heterogeneous data (SQL tables, flat files, APIs, logs) into a searchable knowledge
   source that Copilot Studio can ground its responses on.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384384-exam-ab-100-
topic-1-question-10-discussion/

009 Question.
A retail company plans to deploy Microsoft Copilot Studio agents to support:
Microsoft Dynamics 365 Commerce scenarios.
A Microsoft Power Apps inventory management solution.

---

## [Página 9](AB-100%20Q%26A.pdf#page=9) · texto nativo

You need to recommend a solution to organize product catalog data as a consistent source for
multiple AI systems.
What should you recommend?

    A.  Let each agent scrape product details from Microsoft SharePoint Online libraries.
    B.  Store the product catalog data in a separate custom table for each agent.
   C. Configure prompts to pull product details from the PDFs of external vendors.
   D. Centralize the product catalog data in Microsoft Dataverse and expose the data to both
       agents.
Answer
   Correct Answer: D

   Explanation:
    Centralizing the catalog in Dataverse gives you a single source of truth that every Copilot Studio
    agent, Power Apps solution, and Dynamics 365 Commerce integration can reliably consume.
    This avoids duplication, drift, and inconsistent product attributes across systems.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384385-exam-ab-100-
topic-1-question-11-discussion/

010 Question.
A company has a portfolio of AI initiatives at different stages of development.
You need to recommend a structured approach to evaluating the return on AI investment (ROAI)
across all the initiatives. The solution must balance immediate results with long-term values and
strategic innovations.
What should you include in the recommendation?

    A. a simple cost and benefit analysis
    B. a horizon-based framework
   C. the internal rate of return (IRR) function
   D. a prioritization grid
Answer
   Correct Answer: B

   Explanation:

   When a company has multiple AI initiatives at different maturity levels, you need a framework
    that:

              •   Evaluates short-term ROI
              •  Captures long-term strategic value
              •  Encourages innovation without ignoring immediate business impact
              •   Provides a structured, portfolio-level view

---

## [Página 10](AB-100%20Q%26A.pdf#page=10) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/384386-exam-ab-100-
topic-1-question-12-discussion/

011 Question.
You need to recommend a Microsoft Power Platform business solution that consolidates data from
multiple internal and external data sources. The solution must meet the following requirements:
Provide the data as a centralized source for multiple AI systems, including Microsoft Copilot Studio
agents, Dynamics 365 applications, and external AI models.
Support built-in data classification and protection policies.
Provide data for grounding and analytics.
What should you include in the recommendation?

    A.  Microsoft Dataverse
    B.  Azure Data Lake Storage
   C. a Microsoft Power BI semantic model
   D. Azure Cosmos DB
Answer
   Correct Answer: A

   Explanation:

   You need a centralized, governed, secure data platform that can:

              •  Consolidate internal + external data sources
              •  Serve as a single source of truth for multiple AI systems
              •   Provide built-in data classification, DLP, and security
              •  Support grounding for Copilot Studio, Dynamics 365, and external AI models
              •  Enable analytics across the organization

   Only Microsoft Dataverse satisfies all of these requirements.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384387-exam-ab-100-
topic-1-question-13-discussion/

012 Question.
A company plans to deploy an AI-based customer service app that will autonomously manage
interactions, escalate complex cases, and learn from historical ticket data.
You need to perform a return on AI investment (ROAI) analysis of the app deployment. The solution
must ensure that the analysis is accurate.
What should you do first?

    A.  Establish the AI performance metrics.
    B. Conduct an AI market benchmarking study.

---

## [Página 11](AB-100%20Q%26A.pdf#page=11) · texto nativo

C. Model the customer experience.
   D.  Identify and quantify all the development, deployment, and operating costs.
Answer
   Correct Answer: D

   Explanation:

   A Return on AI Investment (ROAI) analysis must begin with a baseline financial understanding.
   Before you can measure value, performance, or customer impact, you must know:

              •  What the AI solution will cost to build
              •  What it will cost to run
              •  What it will cost to maintain
              •  What existing processes cost today

   Without this foundation, any ROI calculation would be incomplete or misleading.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384388-exam-ab-100-
topic-1-question-14-discussion/

013 Question.
You are designing end-to-end test scenarios for a business solution that uses Microsoft Dynamics
365 Sales and Dynamics 365 Finance.

You need to ensure that the business solution meets the following test requirements:

    •   Properly exchanges data between the Dynamics 365 apps
    •   Aligns with defined user workflows and business processes


Which type of testing should you use for each requirement? To answer, drag the appropriate testing
types to the correct requirements. Each testing type may be used once, more than once, or not at
all. You may need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.

---

## [Página 12](AB-100%20Q%26A.pdf#page=12) · texto nativo

Answer
   Correct Answer:





   Explanation:

   → Integration testing Integration testing validates that data flows correctly between
   systems—in this case, Dynamics 365 Sales and Dynamics 365 Finance. It ensures APIs,
    plugins, dual-write, and synchronization behave as expected.

   → User acceptance testing (UAT) User acceptance testing ensures the solution matches
    real-world business workflows, user expectations, and process requirements. It is the final
    validation before production.


Discussion: https://www.examtopics.com/discussions/microsoft/view/406222-exam-ab-100-
topic-1-question-15-discussion/

014 Question.
A company has a Microsoft 365 tenant in Canada and multiple Microsoft Power Platform
environments in Canada and the United States.

---

## [Página 13](AB-100%20Q%26A.pdf#page=13) · texto nativo

The company plans to deploy a Microsoft Copilot Studio agent to the Canadian environment that
will use:

    •   Microsoft Dataverse data stored in Canada
    •  A connector that connects to an Azure OpenAI instance in the United States


You need to ensure that the agent adheres to data residency and data movement policies before
being deployed.

What should you do?

    A.  Ensure that the data processed by Azure OpenAI is stored in the United States.
    B. From the Microsoft Purview portal, validate the Data loss prevention settings.
   C. Migrate the tenant to the United States.
   D. Ensure that cross-region data movement is enabled for the Canadian environment and
       connector dependencies.
Answer
   Correct Answer: d

   Explanation:

   Correct answer: D. Ensure that cross-region data movement is enabled for the Canadian
   environment and connector dependencies. Your Copilot Studio agent will run in Canada, but
   one of its dependencies—the Azure OpenAI connector—is located in the United States.

    This means the agent will send data across regions, which triggers Microsoft’s data residency
   and data movement policies.

   Before deploying the agent, you must explicitly enable cross-region data movement for:

       •  The Canadian Copilot Studio environment
       •  The connector that calls Azure OpenAI in the U.S.

    This is the only option that ensures the solution is compliant before deployment.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406223-exam-ab-100-
topic-1-question-16-discussion/

015 Question.
A company has a Microsoft Copilot Studio agent for customer support.

You are reviewing and validating the following prompts:

    •  A prompt that has instructions to "help the customer as best you can"
    •  A prompt that helps retrieve product information from a knowledge base

---

## [Página 14](AB-100%20Q%26A.pdf#page=14) · texto nativo

You need to ensure that the agent delivers consistent and accurate responses.

What should you do for each prompt? To answer, select the appropriate options in the answer
area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

   Prompt: “help the customer as best you can” → Rewrite the prompt with clear and
    task-specific instructions.

   A vague instruction like “help the customer as best you can” leads to inconsistent,
    unpredictable model behavior. Clear, scoped, task-specific instructions produce repeatable,
    controlled, and aligned responses

   Prompt: Retrieve product information from a knowledge base → Use responses with only
   reference sources and limit the response scope.

     - When grounding to a knowledge base, the model must:

     - Stay within the retrieved content - Avoid hallucinating

     - Cite or reference the source

     - Limit the scope to the product information retrieved

---

## [Página 15](AB-100%20Q%26A.pdf#page=15) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/406224-exam-ab-100-
topic-1-question-17-discussion/

016 Question.
You are designing a testing solution for Microsoft Copilot Studio agents.

You need to validate prompt engineering best practices to ensure that the agents generate
accurate and contextually relevant responses.

Which prompt validation techniques and metrics should you include in the solution? To answer,
select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 16](AB-100%20Q%26A.pdf#page=16) · texto nativo

Explanation:

   Prompt validation techniques: → Use prompts that have varied phrasing This is the correct
   technique because varied phrasing helps you test whether the agent responds consistently
   even when users express the same intent in different ways. It validates robustness,
    generalization, and prompt stability.

    Metrics: → Response relevance and accuracy This is the key metric for evaluating whether the
   agent is producing correct, contextually grounded, and useful responses. It directly measures
    the success of prompt engineering.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406225-exam-ab-100-
topic-1-question-18-discussion/

017 Question.
A company has two Microsoft Power Platform environments named Dev1 and Prod1. A Microsoft
Copilot Studio agent named Agent1 is built into a solution in the Dev1 environment.

You plan to deploy Agent1 to Prod1.

You need to make Agent1 available to the users in Prod1. The solution must minimize
administrative effort.

What should you do?

    A.  Share Agent1 with the users in Prod1.
    B.  Export the solution as an unmanaged solution and import the solution into Prod1.
   C. Export the solution as a managed solution and import the solution into Prod1.
   D. Create a new Copilot Studio agent in Prod1 by replicating the configuration of Agent1.

---

## [Página 17](AB-100%20Q%26A.pdf#page=17) · texto nativo

Answer
   Correct Answer: C

   Explanation:

   The correct answer is: C. Export the solution as a managed solution and import the
   solution into Prod1.

   To move a Copilot Studio agent (or any Power Platform component) from Dev to Prod, the
   recommended and lowest-effort approach is:

       •  Package the agent inside a managed solution
       •  Import that managed solution into Prod1 This ensures:
       •  Proper ALM (Application Lifecycle Management)
       •   Controlled, locked-down components in production
       •  Easy updates through solution versioning
       •  Minimal administrative overhead
       •  No need to manually recreate or re-share anything

    This is exactly how Microsoft expects Copilot Studio agents to be deployed across
   environments.

   Discussion: https://www.examtopics.com/discussions/microsoft/view/406226-exam-ab-100-
    topic-1-question-19-discussion/

018 Question.
A company has a Microsoft Power Platform environment that contains Microsoft Dataverse data.

You create a Microsoft Copilot Studio agent named Agent1 that processes the Dataverse data.

You discover that Agent1 fails to return relevant or accurate results.

You need to improve the quality and reliability of data grounding.

What should you do?

    A.  Retrain Agent1.
    B.  Verify and cleanse the Dataverse data.
   C. Use an adaptive card in Agent1.
   D. Add example user inputs to the training data of Agent1.
Answer
   Correct Answer: B

   Explanation:

---

## [Página 18](AB-100%20Q%26A.pdf#page=18) · texto nativo

The right first step is B. Verify and cleanse the Dataverse data.

   When a Copilot Studio agent returns irrelevant or inaccurate results, the most common root
   cause is poor grounding data quality. Grounding only works if the underlying Dataverse tables
    contain:

       •  Clean
       •  Complete
       •  Accurate
       •   Well-structured information.

      If the data is inconsistent, outdated, duplicated, or missing key fields, the agent will hallucinate
    or produce unreliable answers—even if the prompts and model are correct.

   So before retraining, rewriting prompts, or adding examples, you must fix the data.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406227-exam-ab-100-
topic-1-question-20-discussion/

019 Question.
A company plans to deploy a Microsoft Copilot Studio agent to enhance customer support.

The company stores customer data across ServiceNow, Microsoft Dynamics 365 Finance,
Dynamics 365 Supply Chain Management, and Excel files in SharePoint Online.

You need to recommend a solution to ensure that the agent can deliver accurate and timely
responses.

What should you recommend?

    A. Implement a model router for query handling.
    B.  Create custom prompts.
   C. Implement Microsoft Power Platform connectors.
   D. Enable incremental indexing in Azure AI Search.
Answer
   Correct Answer: C

   Explanation:

   The correct recommendation is: C. Implement Microsoft Power Platform connectors.
   Power Platform connectors allow the agent to securely and reliably access each system’s data
   without custom integration work. This ensures:

       •   Real-time data retrieval
       •  Consistent grounding

---

## [Página 19](AB-100%20Q%26A.pdf#page=19) · texto nativo

•  Minimal development effort
       •  Compliance with Power Platform governance
       •  Seamless integration across all systems

Discussion: https://www.examtopics.com/discussions/microsoft/view/406228-exam-ab-100-
topic-1-question-21-discussion/

020 Question.
A manufacturing company wants to deploy an agent that will automate supplier invoice
processing.

You are designing a solution to evaluate the financial implications of the deployment. The company
is especially concerned about budget overruns.

You need to ensure that the solution considers the total cost of ownership (TCO), the expected
savings from using automation, and whether to extend the existing AI capabilities.

What should you include in the design?

    A. a break-even analysis only
    B.  adopting prebuilt agents to reduce the deployment time
   C.  training a custom model
   D. a return on AI investment (ROAI) analysis
Answer
   Correct Answer: D

   Explanation:

   The correct answer is: D. a return on AI investment (ROAI) analysis

   The company wants to evaluate:

       •   Total cost of ownership (TCO)
       •  Expected savings from automation
       •  Whether extending AI capabilities is financially justified
       •   Risk of budget overruns

   A return on AI investment (ROAI) analysis is the only framework that covers all of these
   dimensions.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406229-exam-ab-100-
topic-1-question-22-discussion/

---

## [Página 20](AB-100%20Q%26A.pdf#page=20) · texto nativo

021 Question.
A company has a Microsoft Power Platform solution that contains the following components:

    •   Microsoft Dataverse tables
    •  A Microsoft Power BI workspace named WS1
    •  A canvas app named App1 that uses Dataverse
    •  A Power BI semantic model that connects to Dataverse by using DirectQuery

You plan to use generative AI to provide answers to queries based on a subset of corporate data.

You need to ensure that the data is available as a grounding data source for AI systems.

What should you do?

    A.  Populate a Dataverse table.
    B. Share WS1.
   C. Endorse the semantic model.
   D. Export the semantic model.
Answer
   Correct Answer: A

   Explanation:

   The correct answer is: A. Populate a Dataverse table.

    To make data available as a grounding data source for generative AI systems (including Copilot
    Studio, Microsoft 365 Copilot, and other AI experiences), the data must live in a supported
   grounding store. From the options provided, the only store that AI systems can directly ground
   on is:

    Microsoft Dataverse The scenario already includes Dataverse, so the correct action is to
   populate a Dataverse table with the subset of corporate data you want to expose to AI.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406230-exam-ab-100-
topic-1-question-23-discussion/

022 Question.
A company plans to implement an AI business solution for a consumer goods company.

You need to create agents that meet the following requirements:

• Orchestrate the sales order fulfillment and shipping of goods to customers.
• Analyze historical data and trends to replenish stock.

---

## [Página 21](AB-100%20Q%26A.pdf#page=21) · texto nativo

Which type of agent should you use for each requirement? To answer, drag the appropriate agent
types to the correct requirements. Each agent type may be used once, more than once, or not at
all. You may need to drag the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

   Orchestrate the sales order fulfillment and shipping → Autonomous agent

    This scenario requires an agent that can coordinate multi-step workflows, make decisions,
    trigger actions across systems, and manage an end-to-end operational process.

   That is exactly what an autonomous agent is designed for.

   Analyze historical data and trends to replenish stock → Task agent

   Task agents are built for bounded, well-defined analytical or computational tasks, not ongoing
    orchestration.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406231-exam-ab-100-
topic-1-question-24-discussion/

023 Question.
A company has an AI agent that automates the review of customer feedback stored in a cloud
database.

You plan to generate monthly reports from the agent's output to provide insights into customer
sentiment and guide product development and marketing.

---

## [Página 22](AB-100%20Q%26A.pdf#page=22) · texto nativo

You need to ensure that the data ingested by the agent is clean and suitable for the intended use.

What should you do to prepare the data?

    A.  Create a workflow in Microsoft Power Automate.
    B.  Identify and address biased data.
   C. Create an agent flow in Microsoft Copilot Studio.
   D. Sort the database by customer last name.
Answer
   Correct Answer: B

   Explanation:

   The correct answer is B. Identify and address biased data. Before generating monthly
   sentiment reports, the company must ensure that the customer feedback data is clean,
    representative, and free of bias. This is a core requirement in responsible AI and data
    preparation. This step is explicitly emphasized in Microsoft’s AI readiness and data preparation
   guidance.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406232-exam-ab-100-
topic-1-question-25-discussion/

024 Question.
A company is designing a Microsoft Power Platform solution to reduce the manual steps of a
business process by deploying an existing AI model.

You need to calculate the return on AI investment (ROAI) by identifying the metadata and telemetry
of the solution.

What should you use?

    A.  Microsoft Power Platform admin center
    B. Success by Design
   C. the Business value toolkit
   D. Microsoft Cloud Adoption Framework for Azure
Answer
   Correct Answer: C

   Explanation:

   The correct answer is: C. the Business value toolkit The Business value toolkit is the only
    Microsoft tool designed specifically to:

---

## [Página 23](AB-100%20Q%26A.pdf#page=23) · texto nativo

•  Capture telemetry and metadata from Power Platform solutions
       •  Model ROI and ROAI
       •  Estimate TCO
       •   Quantify expected savings
       •  Support build vs buy vs extend decisions
       •   Provide financial modeling templates for AI adoption

Discussion: https://www.examtopics.com/discussions/microsoft/view/406233-exam-ab-100-
topic-1-question-26-discussion/

025 Question.
A company has a Microsoft Power Platform environment.

You need to build two agents named Agent1 and Agent2. The solution must meet the following
requirements:

• Agent1 must be extendable by using the Semantic Kernel and must connect to multiple business
apps and APIs.
• Agent2 must connect directly to data stored in Microsoft Dataverse and must be embeddable in a
Microsoft Power Apps canvas app.

What should you use to build each agent? To answer, select the appropriate options in the answer
area.

NOTE: Each correct selection is worth one point.

---

## [Página 24](AB-100%20Q%26A.pdf#page=24) · texto nativo

Answer
   Correct Answer:

   Explanation:

   Agent1 → Microsoft Foundry Agent1 must:

       •  Be extendable using Semantic Kernel
       •  Connect to multiple business apps and APIs
       •  Support complex orchestration and multi-agent patterns

   These are exactly the capabilities of Microsoft Foundry, which is designed for enterprise-grade,
    extensible, multi-agent AI systems with deep integration into Semantic Kernel.

   Agent2 → Copilot in Power Apps Why: Agent2 must:

       •  Connect directly to Dataverse
       •  Be embeddable in a Power Apps canvas app

    This is precisely what Copilot in Power Apps is built for.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406234-exam-ab-100-
topic-1-question-27-discussion/

026 Question.
A company has an Azure environment that supports multiple business units.

The company plans to implement an AI solution that will perform sentiment analysis on customer
product reviews.

You need to evaluate the potential cost of the solution to support return on AI investment (ROAI)
analysis.

What should you use?

    A. Cost Management + Billing
    B.  Microsoft Fabric SKU Estimator
   C.  Total Cost of Ownership (TCO) Calculator
   D. Azure Reservations
Answer
   Correct Answer:

   Explanation:

    A. Cost Management + Billing To evaluate the potential cost of an AI solution running in Azure
  — especially for ROAI (Return on AI Investment) — you need visibility into:

---

## [Página 25](AB-100%20Q%26A.pdf#page=25) · texto nativo

•  Current Azure resource consumption
       •  Forecasted costs
       •  Cost trends
       •   Service-level spending
       •  Budget alerts
       •  Cost allocation by business unit

   Cost Management + Billing is the Azure-native tool that provides exactly this.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406235-exam-ab-100-
topic-1-question-28-discussion/

027 Question.
You need to recommend a Microsoft Power Platform solution for customer support. The solution
must include AI capabilities in Microsoft Power Automate and must meet the following
requirements:

    •  Use a centralized workspace for AI models.
    •  Generate short overviews from large amounts of unstructured text, such as case notes or
        transcripts, without requiring additional training or coding.

What should you include in the recommendation for each requirement? To answer, select the
appropriate options in the answer area.

NOTE: Each correct selection is worth one point.

---

## [Página 26](AB-100%20Q%26A.pdf#page=26) · texto nativo

Answer
   Correct Answer:





   Explanation:

   Use a centralized workspace → Microsoft Dataverse In Power Platform, the AI Hub is built on
   Dataverse and acts as the centralized workspace for:

       •  Managing AI models
       •  Managing AI Builder models
       •  Managing prompts
       •  Managing AI assets used in Power Automate and Power Apps

    Neither Foundry option is part of Power Platform, and Copilot Studio is for agents, not
    centralized AI model management.

   Generate short overviews → AI Builder prebuilt prompt The requirement is:

       •  Generate short overviews
       •  From large unstructured text (case notes, transcripts)
       •  Without training
       •  Without coding

    This is exactly what AI Builder prebuilt prompts are designed for.


Discussion: https://www.examtopics.com/discussions/microsoft/view/406236-exam-ab-100-
topic-1-question-29-discussion/

---

## [Página 27](AB-100%20Q%26A.pdf#page=27) · texto nativo

028 Question.
Body A company uses Microsoft Dynamics 365 Finance for accounts payable and customer debt
recovery.

You are designing an AI finance process that meets the following requirements:

• Provides AI-driven details to help staff identify overdue vendor invoices and outstanding balances
• Helps staff reduce how long it takes to review overdue invoices and payment history

You need to recommend which Microsoft Copilot features to include in the design.

What should you recommend for each requirement? To answer, select the appropriate options in
the answer area.

NOTE: Each correct selection is worth one point.





.
Answer
   Correct Answer:

---

## [Página 28](AB-100%20Q%26A.pdf#page=28) · texto nativo

Explanation:

    1. Help identify vendor overdue invoices and outstanding balances → The Supplier
   Communication agent This agent is designed for vendor-facing processes in Dynamics 365
   Finance.

       •   Identify overdue vendor invoices
       •  Track outstanding balances
       •  Communicate with suppliers
       •  Automate follow-ups

    2. Reduce how long it takes to review overdue invoices and payment history → Collections
   coordinator summary The Collections Coordinator Copilot feature provides:

       •   AI-generated summaries of customer payment history
       •  Overdue invoice insights
       •  Quick review of aging and collection status
       •   Faster decision-making for debt recovery

Discussion: https://www.examtopics.com/discussions/microsoft/view/406237-exam-ab-100-
topic-1-question-30-discussion/

029 Question.
A company has an AI agent that automates the review of customer feedback stored in a cloud
database.

You plan to generate monthly reports from the agent's output to provide insights into customer
sentiment and guide product development and marketing.

You need to ensure that the data ingested by the agent is clean and suitable for the intended use.

What should you do to prepare the data?

---

## [Página 29](AB-100%20Q%26A.pdf#page=29) · texto nativo

A.  Ensure that the size of the database does not exceed 100 GB.
    B.  Translate the data into a single language.
   C.  Identify and address biased data.
   D. Sort the database by customer last name.
Answer
   Correct Answer: C

   Explanation:

   The correct answer is C. Identify and address biased data.

   For an AI agent performing sentiment analysis on customer feedback, the most important
    data-quality step is ensuring that the dataset is:

       •   Representative
       •  Unbiased
       •   Fair
       •   Suitable for downstream analytics

Discussion: https://www.examtopics.com/discussions/microsoft/view/411611-exam-ab-100-
topic-1-question-33-discussion/

030 Question.
A company has an Azure environment that supports multiple business units.

The company plans to implement an AI solution that will perform sentiment analysis on customer
product reviews.

You need to evaluate the potential cost of the solution to support return on AI investment (ROAI)
analysis.

What should you use?

    A.  Total Cost of Ownership (TCO) Calculator
    B.  Azure Reservations
   C. Azure pricing calculator
   D. Azure Monitor
Answer
   Correct Answer: C

   Explanation:

   C. Azure pricing calculator To evaluate the potential cost of a new AI workload — before
   deployment — you need a tool that can:

---

## [Página 30](AB-100%20Q%26A.pdf#page=30) · texto nativo

•  Estimate the cost of Azure services you plan to use
       •  Model different configurations
       •  Forecast monthly and annual spend
       •  Support early-stage ROAI calculations

   The Azure pricing calculator is specifically designed for pre-deployment cost estimation.

Discussion: https://www.examtopics.com/discussions/microsoft/view/411612-exam-ab-100-
topic-1-question-34-discussion/

031 Question.
A company has an Azure environment that supports multiple business units.

The company plans to implement an AI solution that will perform sentiment analysis on customer
product reviews.

You need to evaluate the potential cost of the solution to support return on AI investment (ROAI)
analysis.

What should you use?

    A.  Azure savings plans
    B.  Microsoft Fabric SKU Estimator
   C. Cost Management + Billing
   D. Azure Monitor
Answer
   Correct Answer: C

   Explanation:

   Correct Answer: Cost Management + Billing To evaluate potential cost for an AI workload
    (sentiment analysis on product reviews) across multiple business units, you need:

       •  Forecasted Azure spend
       •  Cost breakdown by resource, tag, or business unit
       •  Budget alerts
       •  Usage analytics
       •  Chargeback/showback support

   Cost Management + Billing is the only option that provides all of this. It is specifically used for
   ongoing and projected Azure cost analysis, which is essential for ROAI.

Discussion: https://www.examtopics.com/discussions/microsoft/view/411613-exam-ab-100-
topic-1-question-35-discussion/

---

## [Página 31](AB-100%20Q%26A.pdf#page=31) · texto nativo

032 Question.
A company has an Azure environment that supports multiple business units.

The company plans to implement an AI solution that will perform sentiment analysis on customer
product reviews.

You need to evaluate the potential cost of the solution to support return on AI investment (ROAI)
analysis.

What should you use?

    A.  Azure Reservations
    B.  Microsoft Fabric SKU Estimator
   C. Anomaly Detection in Azure Cost Management
   D. Azure pricing calculator
Answer
   Correct Answer: D

   Explanation:

   Azure pricing calculator.

   To evaluate the potential cost of a new AI workload (sentiment analysis on product reviews),
   you need a tool that:

       •  Estimates future Azure service costs
       •  Models different configurations (compute, storage, AI services)
       •  Supports pre-deployment ROAI calculations
       •  Works across multiple business units

   The Azure pricing calculator is the only option designed specifically for forecasting the cost of
   planned Azure services before you deploy anything. This is exactly what ROAI requires.

Discussion: https://www.examtopics.com/discussions/microsoft/view/411614-exam-ab-100-
topic-1-question-36-discussion/

033 Question.
You need to design a Microsoft 365 Copilot solution to optimize employee productivity. The
solution must meet the following requirements:
Ensure that the employees can query content stored in a subset of Microsoft SharePoint Online
sites and in Teams by using natural language-based prompt actions.
Ensure that employees receive contextually relevant responses in Microsoft 365 Copilot.
What should you include in the design?

---

## [Página 32](AB-100%20Q%26A.pdf#page=32) · texto nativo

A.  Build a Microsoft Power Automate desktop flow to read the SharePoint content and post
       the responses to Teams.
    B.  Modify SharePoint settings.
   C. Create a custom REST API that crawls the SharePoint content.
   D. Configure Microsoft Graph access.
Answer
   Correct Answer: D

   Explanation:

   To let Microsoft 365 Copilot query specific SharePoint Online sites and Teams content using
    natural language—and return contextually grounded responses—you must configure Microsoft
   Graph access. This is the mechanism Copilot uses to read organizational content securely and
    selectively.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384392-exam-ab-100-
topic-2-question-4-discussion/

034 Question.
A company uses Microsoft Dynamics 365 Finance to manage accounts payable.
You are designing an AI invoice processing solution.
You need to recommend the prerequisites to configure a prebuilt copilot for accounts payable.
What should you recommend?

    A. From Microsoft Copilot Studio, create an accounts payable agent.
    B. Extend Microsoft 365 Copilot for Sales to an accounts payable agent.
   C. Build an AI tool in Microsoft Foundry.
   D. From the Power Platform admin center, assign the Finance and Operations AI security role
       to users.
Answer
   Correct Answer: D

   Explanation:

   To enable the prebuilt Copilot for Accounts Payable in Dynamics 365 Finance, users must be
   assigned the Finance and Operations AI security role. This is the documented prerequisite
   before the AP Copilot can access invoice data and perform AI-assisted processing.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384393-exam-ab-100-
topic-2-question-5-discussion/

---

## [Página 33](AB-100%20Q%26A.pdf#page=33) · texto nativo

035 Question.
A company plans to deploy a Microsoft Dynamics 365 Contact Center agent.
You need to ensure that the agent can transfer the conversation to a live customer service
representative.
Which two components should you include in the solution? Each correct answer presents part of
the solution.
NOTE: Each correct selection is worth one point.

    A.  Microsoft Foundry
    B.  Microsoft Copilot Studio
   C. Microsoft 365 Agents Toolkit
   D. an Azure AI Bot Service skill
    E. Customer engagement hub
Answer
   Correct Answer: BE

    B. Microsoft Copilot Studio Dynamics 365 Contact Center uses Copilot Studio to build and
    configure the conversational agent. The live-agent transfer capability is implemented through:

       •  handoff nodes
       •  Omnichannel/Customer Service integration
       •   routing rules

    E. Customer engagement hub The Customer Service workspace / Customer Engagement Hub
    is where human agents receive escalated conversations. The Contact Center agent must be
   able to:

       •   transfer the session to a queue
       •   route it to a human agent
       •   allow the human agent to pick up the conversation in the Customer Engagement Hub

Discussion: https://www.examtopics.com/discussions/microsoft/view/384394-exam-ab-100-
topic-2-question-6-discussion/

036 Question.
A company uses Microsoft Dynamics 365 Supply Chain Management.
You are designing an AI supply chain process that meets the following requirements:
Provides managers with AI-driven insights that surface key information from customer orders
Helps planners use AI to anticipate future product needs more accurately
You need to recommend which Microsoft Copilot features to include in the design.
What should you recommend for each requirement? To answer, select the appropriate options in
the answer area.

---

## [Página 34](AB-100%20Q%26A.pdf#page=34) · texto nativo

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

        1.  Provide AI-driven insights from customer orders: ➡ AI Summaries with Copilot

   Reason: AI Summaries in Supply Chain Management surface key information from operational
   records—such as customer orders, shipments, delays, exceptions, and fulfillment issues. They
    are designed to give managers quick, AI-generated overviews of order activity.

        2.  Anticipate future product needs: ➡ Generative insights for Demand planning

   Reason: This Copilot feature uses AI to analyze historical demand, seasonality, supply
    constraints, and forecast signals to help planners predict future product needs more
    accurately.

---

## [Página 35](AB-100%20Q%26A.pdf#page=35) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/384395-exam-ab-100-
topic-2-question-7-discussion/

037 Question.
A company has a Microsoft 365 E5 subscription and uses Microsoft Copilot Studio.
The company has a Microsoft SharePoint Online library that contains 10,000 policy PDFs from
various departments. The library contains a populated column named Department for each PDF.
You need to design a Copilot Studio agent that will use the SharePoint library as a knowledge
source. The solution must meet the following requirements:

    •  Enable the agent to answer user questions about company policies.
    •  Ensure that the agent can identify which departments and policies are connected.

What should you include in the design for each requirement? To answer, select the appropriate
options in the answer area.
NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

---

## [Página 36](AB-100%20Q%26A.pdf#page=36) · texto nativo

1. From Copilot Studio, add SharePoint as a knowledge source.

Copilot Studio can directly index a SharePoint library (including PDFs) as a knowledge source,
enabling natural-language Q&A over the content. No custom models, Dataverse imports, or AI
Builder pipelines are required.

            2.  Create a Microsoft Dataverse table for the departments.

The agent must understand relationships between departments and policies. - A Dataverse table
allows you to: - Represent departments as structured entities - Link policies to departments -
Enable the agent to reason over relationships (e.g., “Which policies belong to HR?”)

Discussion: https://www.examtopics.com/discussions/microsoft/view/384527-exam-ab-100-
topic-2-question-8-discussion/

038 Question.
You need to design a Microsoft Copilot Studio agent that meets the following requirements:
Supports interactive speech responses
Optimizes decision-making and the accuracy of responses
What should you include in the design for each requirement? To answer, drag the appropriate
options to the correct requirements. Each option may be used once, more than once, or not at all.
You may need to drag the split bar between panes or scroll to view content.





Answer
   Correct Answer:





   Explanation:

   Copilot Studio voice features → Interactive speech responses

    Copilot Studio includes built-in voice capabilities that allow an agent to:

---

## [Página 37](AB-100%20Q%26A.pdf#page=37) · texto nativo

•   Listen to user speech
       •  Generate spoken responses
       •  Support natural, interactive voice conversations

    This is the only option designed specifically for speech interaction.

   Deep reasoning model → Decision-making & accuracy

   Deep reasoning models (like GPT-4-class reasoning models) are used in Copilot Studio to:

              •  Improve multi-step reasoning
              •   Increase accuracy of responses
              •  Handle complex decision logic
              •  Produce more reliable, grounded answers

    This directly satisfies the requirement to optimize decision-making and accuracy.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384070-exam-ab-100-
topic-2-question-9-discussion/

039 Question.
You are designing a low-code AI business solution by using Microsoft Copilot Studio.
The solution must include an agent that automates tasks by simulating user interactions across
third-party apps and websites, such as clicking buttons, entering text, and extracting information
from screens.
You need to recommend what to include in the agent.
What should you recommend?

    A. Model Context Protocol (MCP)
    B. a natural language understanding + (NLU+) model in Copilot Studio
   C. Computer Use in Copilot Studio
   D. Copilot skills
Answer
   Correct Answer: C

   Explanation:

   Computer Use enables a Copilot Studio agent to:

       •   Control a computer like a human
       •   Click, type, scroll, select, and navigate
       •  Read information from screens
       •  Automate workflows across any app (web or desktop)
       •  Handle UI automation without building custom connectors It is the low-code way to
            give your agent real “hands-on-keyboard” abilities.

---

## [Página 38](AB-100%20Q%26A.pdf#page=38) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/384396-exam-ab-100-
topic-2-question-10-discussion/

040 Question.
You need to recommend a solution to integrate a Microsoft Copilot agent with a Microsoft
Dynamics 365 Contact Center chat channel.
The agent must respond to customer questions and hand off the conversation to a live customer
service representative when the customer requests an escalation.
What should you recommend?

    A.  Build an agent flow.
    B.  Configure the Conversation Start topic.
   C. Configure a skill.
   D.  Call a Microsoft Power Automate connector.
    E.  Configure the Escalate topic.
Answer
   Correct Answer: E

   Explanation:

    In Copilot Studio, the Escalate topic is the built-in mechanism that:

       •  Detects when a customer asks for a human
       •   Triggers the handoff flow
       •  Connects to Dynamics 365 Customer Service / Contact Center queues
       •   Transfers the conversation to a live representative

    This is the only option that directly supports the required escalation behavior.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384397-exam-ab-100-
topic-2-question-11-discussion/

041 Question.
A company has a customer order system that creates sales orders manually.
You need to design an AI solution to automate the following tasks as part of the system:
Save the order details to a database.
Update the order status in the database.
Extract the order details from an order file.
Prepare and send a confirmation email to customers.
The solution must minimize development effort and support intelligent automation and solution
integration.
What should you include in the design?

---

## [Página 39](AB-100%20Q%26A.pdf#page=39) · texto nativo

A. a workflow in Azure Logic Apps
    B. a multi-agent solution that uses the Semantic Kernel SDK
   C. a multi-agent solution that uses Microsoft Foundry Agent Service
   D. a Microsoft Copilot Studio agent that uses Microsoft Power Automate workflows
Answer
   Correct Answer: D

   Explanation:

   D. A Microsoft Copilot Studio agent that uses Microsoft Power Automate workflows. Your
   requirements are:

       •  Save order details to a database
       •  Update order status
       •   Extract order details from an order file
       •  Prepare and send confirmation emails
       •  Minimize development effort
       •  Support intelligent automation
       •  Support integration across systems

    This is a textbook case for Copilot Studio + Power Automate.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384398-exam-ab-100-
topic-2-question-12-discussion/

042 Question.
You are designing an AI strategy for Microsoft Dynamics 365 finance and operations apps. You are
evaluating the use of Microsoft Copilot Studio to provide in-app help and guidance based on
generative AI general knowledge.
You need to recommend which knowledge sources to include in the generative help and guidance
agent. The solution must minimize the risk of generating inaccurate responses.
What should you recommend? To answer, select the appropriate options in the answer area.
NOTE: Each correct selection is worth one point.

---

## [Página 40](AB-100%20Q%26A.pdf#page=40) · texto nativo

Answer
   Correct Answer:





   Explanation:

    1. Custom knowledge sources → Must be uploaded to the agent To minimize hallucinations,
       Copilot Studio agents used for in-app help and guidance in Dynamics 365 must rely on
        trusted, organization-controlled content. This includes: - Product documentation - Internal
       process guides - Policy documents - Standard operating procedures
    2.  AI general knowledge → Must be disabled for the agent General knowledge models can
       introduce: - Hallucinations - Non-compliant or inaccurate answers - Content unrelated to
      Dynamics 365 processes

Discussion: https://www.examtopics.com/discussions/microsoft/view/384054-exam-ab-100-
topic-2-question-13-discussion/

043 Question.
You need to design a multi-agent solution that will include a custom agent. The solution must meet
the following requirements:
Define the rules and constraints that the agent must follow.
Automate a backend process that involves data movement between services and runs

---

## [Página 41](AB-100%20Q%26A.pdf#page=41) · texto nativo

independently of the agent's reasoning steps.
What should you include in the design for each requirement? To answer, select the appropriate
options in the answer area.
NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

    1. Rules and constraints → Agent flows Agent flows are the mechanism used in Copilot Studio
    to:

       •  Define policies, constraints, and guardrails
       •   Control how the agent reasons
       •  Enforce rules such as allowed actions, restricted topics, or required steps

---

## [Página 42](AB-100%20Q%26A.pdf#page=42) · texto nativo

•  Shape the agent’s decision-making and behavior They are part of the agent’s internal
           orchestration, not external automation.

    2. Backend automation → Power Automate cloud flow A backend process that:

       •  Moves data between services
       •  Runs independently of the agent’s reasoning
       •  Executes reliably and asynchronously

    Is exactly what Power Automate cloud flows are designed for.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384399-exam-ab-100-
topic-2-question-14-discussion/

044 Question.
You are designing a Microsoft Copilot Studio agent that uses a custom Microsoft Foundry model to
generate responses.
You need to ensure that the agent can securely connect to and invoke the custom model during
user interactions.
What should you include in the design?

    A.  Configure the agent to use classic orchestration.
    B.  Create a connection to Microsoft Foundry in the agent.
   C. Add the Microsoft Foundry model as a Copilot Studio skill.
   D. Create a custom engine agent.
Answer
   Correct Answer: B

   Explanation:

   The key requirement in your scenario is securely connecting a Copilot Studio agent to a custom
    Microsoft Foundry model so the agent can invoke it during user interactions. That capability is
   enabled through connections, not orchestration modes, skills, or custom engine agents. To
    securely invoke a custom Microsoft Foundry model from a Copilot Studio agent, you must
    create a Foundry connection inside the agent.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384404-exam-ab-100-
topic-3-question-4-discussion/

045 Question.
You need to design an application lifecycle management (ALM) process for a Microsoft Power
Platform environment that contains a solution named Solution1.
Solution1 must include a custom connector for Copilot in Microsoft Dynamics 365 Customer
Service. Solution1 must meet the following requirements:

---

## [Página 43](AB-100%20Q%26A.pdf#page=43) · texto nativo

•  Ensure that the custom connector can be deployed consistently across environments as
       part of the ALM process.
    •   Allow the custom connector to be edited only in the development environment.



What should you include in the design?

    A. Add the custom connector to GitHub.
    B. Share the custom connector.
   C. Create the custom connector in the default solution.
   D. Add the custom connector to Solution1.
Answer
   Correct Answer: D

   Explanation:

   Custom connectors must be included inside a solution so they can be:

       •  exported from Dev
       •  -imported into Test/Prod
       •  versioned and transported through pipelines

   When a solution is exported as managed, all components—including the custom connector—
   become:

       •  locked
       •   read-only
       •  not editable in Test/Prod

Discussion: https://www.examtopics.com/discussions/microsoft/view/406240-exam-ab-100-
topic-2-question-18-discussion/

046 Question.
A company uses a Microsoft Copilot Studio agent to automate tasks in a web app.

During testing, you discover that the automation sometimes fails because of frequent changes to
the app's user interface.

You need to recommend a solution to ensure that the agent successfully automates the tasks. The
solution must minimize changes to the agent.

What should you include in the recommendation?

    A. Computer Use in Copilot Studio

---

## [Página 44](AB-100%20Q%26A.pdf#page=44) · texto nativo

B. custom models in Azure AI Studio
   C. conversation topics in Copilot Studio
   D. an agent flow in Copilot Studio
Answer
   Correct Answer: A

   Your scenario describes:

       •  A Copilot Studio agent automating tasks in a web app
       •  Automation failing because the UI changes frequently
       •  You want a solution that minimizes changes to the agent

    This is exactly the problem Computer Use is designed to solve.

Discussion: h https://www.examtopics.com/discussions/microsoft/view/406241-exam-ab-100-
topic-2-question-19-discussion/

047 Question.
A company processes invoices stored across multiple systems in multiple formats.

You need to implement an AI solution to automate the invoice processing. The solution must meet
the following requirements:

    •  Automate multi-step invoice processing tasks, including document analysis, data
        validation, and approval routing.
    •  Enable users to interact directly via Microsoft Teams to review and approve invoices.
    •  Minimize development efforts to define and customize approval workflows.


What should you include in the solution?

    A.  Azure Document Intelligence in Foundry Tools and Azure Logic Apps
    B. a SharePoint agent
   C. Microsoft Copilot Studio and AI Builder
   D. Azure OpenAI and Azure Functions
Answer
   Correct Answer: C

   Explanation:

    Microsoft Copilot Studio and AI Builder AI Builder provides prebuilt and customizable
   document processing models (Invoice Processing, Form Processing) that can extract
    structured data from invoices across formats and systems. Copilot Studio can orchestrate
    multi-step workflows using:

---

## [Página 45](AB-100%20Q%26A.pdf#page=45) · texto nativo

•  Agent flows
       •  Power Automate integration
       •  Reasoning steps
       •   Conditional logic

    This gives you intelligent automation with minimal custom code.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406242-exam-ab-100-
topic-2-question-20-discussion/

048 Question.
You need to design a Microsoft Copilot Studio agent for customer support.

The agent must securely retrieve product warranty data from a REST API. The solution must
minimize development effort.

What should you include in the design?

    A.  Export the agent as a managed solution and customize the agent in Power Apps.
    B.  Create a custom connector in Copilot Studio and use the connector to call the API.
   C. Use a Microsoft Power Automate desktop flow to screen scrape the warranty data.
   D. Add the warranty data to the Fallback topic.
Answer
   Correct Answer: B

   Explanation:

   Create a custom connector in Copilot Studio To securely retrieve product warranty data from a
   REST API, the agent needs:

       •  A secure authentication mechanism
       •  A reusable, governed integration component
       •  Low-code configuration
       •   ALM-friendly deployment

   A custom connector provides exactly that.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406243-exam-ab-100-
topic-2-question-21-discussion/

049 Question.
A company has an ecommerce support portal that uses Microsoft Dataverse.

---

## [Página 46](AB-100%20Q%26A.pdf#page=46) · texto nativo

You are designing a Microsoft Copilot Studio agent for the portal. The agent must meet the
following requirements:

    •  Respond with a default help message when the user input is unclear.
    •   Initiate external processes, such as retrieving the order status, when users make specific
       requests.


Generative orchestration will be enabled for the solution.

You need to recommend a feature for each requirement.

What should you recommend? To answer, drag the appropriate features to the correct
requirements. Each feature may be used once, more than once, or not at all. You may need to drag
the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

   Explanation:

    1.  Fallback topic → Default help message

When user input is unclear, incomplete, or outside the agent’s scope, the Fallback topic is the
built-in mechanism that:

       •  Detects unrecognized intents
       •  Responds with a default help or clarification message
       •   Redirects the user back into a supported Flow
    2.  Tool (connector) → Initiate external processes

To retrieve order status or trigger any external system action, the agent must call a tool, which in
Copilot Studio means:

       •  A connector (custom or standard)
       •  A Power Automate flow exposed as a tool

---

## [Página 47](AB-100%20Q%26A.pdf#page=47) · texto nativo

•  Any external API wrapped as a tool

Discussion: https://www.examtopics.com/discussions/microsoft/view/406244-exam-ab-100-
topic-2-question-22-discussion/

050 Question.
A company uses Microsoft Dynamics 365 to manage service operations. Dispatchers coordinate
service requests, and technicians perform scheduled on-site work.

You need to design a solution that will use Microsoft Copilot to improve the efficiency of the service
operations. The solution must meet the following requirements:

    •   Provide AI-driven assistance to help staff organize and resolve work orders.
    •   Deliver contextual AI support to frontline workers as they prepare for and complete
      customer appointments.

Which two components should you include in the design? Each correct answer presents part of the
solution.

NOTE: Each correct selection is worth one point.

    A.  Copilot Service workspace
    B.  Copilot in Outlook
   C. Dynamics 365 Customer Service
   D. Copilot in Customer Service
    E.  Copilot in Field Service
    F.  the Dynamics 365 Field Service mobile app
Answer
   Correct Answer:

   Explanation:

    E. Copilot in Field Service →This provides:

     - AI-driven insights for work orders

     - Assistance with scheduling, dispatching, and resolving service tasks

     - Summaries, recommendations, and automated updates for service operatives

    This directly supports dispatchers and back-office service staff.

    F. Dynamics 365 Field Service mobile app → This gives frontline technicians:

     - Contextual AI assistance during appointments

     - Work order summaries

---

## [Página 48](AB-100%20Q%26A.pdf#page=48) · texto nativo

- Step-by-step guidance

     - Real-time updates

     - Integrated Copilot experiences in the mobile workflow

    This is the only option that delivers AI support to technicians in the field.


Discussion: https://www.examtopics.com/discussions/microsoft/view/406245-exam-ab-100-
topic-2-question-23-discussion/

051 Question.
A company uses Microsoft Foundry agents.

You need to ensure that an agent can dynamically use external tools at runtime without updating
the agent.

What should you include in the solution?

    A. a Microsoft Foundry hub
    B. a Model Context Protocol (MCP) server
   C. Azure AI Search
   D. Microsoft Copilot Studio
Answer
   Correct Answer: B

   Explanation:

   The right choice is B. a Model Context Protocol (MCP) server.

   You need the agent to:

       •  Dynamically use external tools at runtime
       •  Without updating or redeploying the agent

   That is exactly what Model Context Protocol (MCP) is designed for.

  MCP allows a Foundry agent to:

       •  Discover tools dynamically
       •  Load new tools without modifying the agent
       •   Call external capabilities exposed by MCP servers

     - Extend functionality at runtime This is the only mechanism in Foundry that supports dynamic
    tool availability.

---

## [Página 49](AB-100%20Q%26A.pdf#page=49) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/406246-exam-ab-100-
topic-2-question-24-discussion/

052 Question.
You are designing an AI business solution that contains the following components:

    •  A Microsoft Power Automate workflow
    •  A Microsoft Copilot Studio agent
    •  A Microsoft Dataverse database
    •  A Microsoft Power Apps app

As part of the application lifecycle management (ALM) process, you plan to package the
components, so that they can be deployed to other environments as a group.
You need to recommend a solution that supports versioning, dependencies, and deployments.
What should you include in the recommendation?

    A. GitHub Actions
    B.  Azure DevOps
   C. Microsoft Power Platform solutions
Answer
   Correct Answer: C

   Why GitHub Actions and Azure DevOps are not the primary answer Both GitHub Actions and
   Azure DevOps can automate ALM pipelines, but they rely on solutions as the underlying
   deployment artifact.

    •  They orchestrate CI/CD.
    •  They do not provide versioning, dependency management, or packaging by themselves.
    •  They require solutions to function in Power Platform ALM.

   So they are optional enhancements—not the core ALM mechanism.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384405-exam-ab-100-
topic-3-question-5-discussion/

053 Question.
A company has Microsoft 365 Copilot agents.
You need to design a security solution for the agents. The solution must meet the following
requirements:

    •   Identify and mitigate potential risks that relate to AI use.
    •   Protect AI apps and the sensitive data processed or generated by the agents.

---

## [Página 50](AB-100%20Q%26A.pdf#page=50) · texto nativo

•  Support responsible AI governance by retaining and logging interactions, detecting policy
        violations, and investigating incidents.

Which two components should you include in the design? Each correct answer presents part of the
solution.
NOTE: Each correct selection is worth one point.

    A.  Microsoft Purview
    B.  Azure AI Content Safety
   C. role-based access control (RBAC) in Microsoft Foundry
   D. Microsoft Defender
Answer
   Correct Answer: A,B

   Explanation:

   Correct answers: A. Microsoft Purview and B. Azure AI Content Safety

   These are the only two components that together satisfy all three requirements:

    risk identification, sensitive-data protection, and responsible AI governance for Microsoft 365
    Copilot agents.

   Purview provides the governance, auditing, and data-protection controls that Copilot agents
    rely on. Purview is the only Microsoft product that logs Copilot interactions and enforces
    data-protection policies across the Microsoft 365 ecosystem. Azure AI Content Safety provides
    AI-specific risk detection. This directly satisfies the requirement to identify and mitigate
    AI-related risks.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384406-exam-ab-100-
topic-3-question-6-discussion/

054 Question.
You are creating validation criteria for a custom generative AI model that produces business
reports based on internal enterprise data.
You need to assess whether the model's outputs are appropriate and meaningful for the business
reports.
Which metric should you use?

    A.  the number of active users interacting with the model
    B.  alignment of the output to domain-specific tasks
   C. the average system resource usage during inference
   D. the model training duration

---

## [Página 51](AB-100%20Q%26A.pdf#page=51) · texto nativo

Answer
   Correct Answer: B

   Explanation:

   The metric that determines whether a custom generative AI model produces appropriate and
   meaningful business reports is how well the model’s output aligns with the specific business
    tasks and domain requirements.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384407-exam-ab-100-
topic-3-question-7-discussion/

055 Question.
A company has Microsoft Foundry agents that generate responses by using Azure OpenAI
resources. The agents are deployed to both the United States and Europe.
A company mandate states that the agents and their grounding data must adhere to data residency
and movement regulations.
You need to recommend a governance solution for the agents.
What should you include in the recommendation?

    A.  Microsoft Defender for Cloud
    B.  Azure Policy
   C. Azure Monitor
   D. Microsoft Purview
Answer
   Correct Answer: D

   Explanation:

   For Microsoft Foundry agents and Azure OpenAI resources deployed across multiple regions
    (U.S. and Europe), the company must enforce data residency, data movement controls,
   governance, and auditing. Only Microsoft Purview provides the governance capabilities
    required for this scenario.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384408-exam-ab-100-
topic-3-question-8-discussion/

056 Question.
A company has a Microsoft Copilot Studio agent that uses custom connectors to interact with
enterprise APIs.
You need to recommend an application lifecycle management (ALM) process to ensure that the
connectors are deployed consistently across development, test, and production environments and

---

## [Página 52](AB-100%20Q%26A.pdf#page=52) · texto nativo

meet governance and traceability requirements.
What should you recommend?

    A. Deploy the APIs as Azure Functions.
    B. Manage the connectors as solution components and deploy the components by using ALM
        pipelines.
   C. Maintain connector definitions in environment variables.
   D. Export and import the connectors between the environments as unmanaged solutions.
Answer
   Correct Answer: B

   Explanation:

   For Copilot Studio / Power Platform ALM, the recommended best practice is:

Use Solutions + ALM pipelines

    •  Custom connectors are solution-aware components

    •  They should be:

         o  Stored inside managed solutions

         o  Version-controlled

         o  Deployed using ALM pipelines (Power Platform Pipelines or Azure DevOps)

This ensures:

    •  Consistency across Dev / Test / Prod

    •  Governance (controlled promotion of changes)

    •   Traceability (who changed what, when)

    •   Repeatability (automated deployments)

   Discussion: https://www.examtopics.com/discussions/microsoft/view/384057-exam-ab-100-
    topic-3-question-9-discussion/

057 Question.
A company plans to implement an AI solution that will contain a Microsoft Copilot Studio agent and
a Microsoft Foundry agent. The solution will be stored in a source code repository.
You need to recommend a deployment method for each agent. The solution must meet the
following requirements:

    •  A test environment must be used before a deployment to production.
    •  Production must be isolated from development and testing.
    •  The deployment must be repeatable and fully automated.

---

## [Página 53](AB-100%20Q%26A.pdf#page=53) · texto nativo

•  The solution must NOT require manual intervention.

Which deployment method should you recommend for each agent? To answer, select the
appropriate options in the answer area.
NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

    1) Copilot Studio agent → Use a Microsoft Power Platform deployment pipeline:

   Power Platform deployment pipelines are the official ALM mechanism for Copilot Studio
    agents. They support:

       •  Dev → Test → Prod stages - Managed solution deployment
       •  Automated, repeatable deployments
       •   Isolation between environments
       •  No manual steps once configured

    2) Microsoft Foundry agent → Use an Azure DevOps pipeline

    Microsoft Foundry agents are deployed like Azure resources. To automate deployments from a
   source code repository with:

---

## [Página 54](AB-100%20Q%26A.pdf#page=54) · texto nativo

•   Infrastructure-as-code
       •  CI/CD
       •   Multi-environment promotion
       •  No manual intervention

    the correct choice is Azure DevOps pipelines (or GitHub Actions, but that option is not available
    in the answer list).

Discussion: https://www.examtopics.com/discussions/microsoft/view/384071-exam-ab-100-
topic-3-question-10-discussion/

058 Question.
A company has a Microsoft Copilot Studio prompt-and-response agent.
You need to ensure that the agent meets the following requirements:
Provides effective and relevant responses
Provides conversational outcomes
Which metric should you use for each requirement? To answer, select the appropriate options in
the answer area.
NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 55](AB-100%20Q%26A.pdf#page=55) · texto nativo

Explanation:

Discussion: https://www.examtopics.com/discussions/microsoft/view/384058-exam-ab-100-
topic-3-question-11-discussion/

059 Question.
A company extends Copilot in Microsoft Dynamics 365 Customer Service.
You need to recommend an automated application lifecycle management (ALM) process so that
the Copilot components can be safely developed, tested, and promoted to production.
Which two actions should you include in the ALM process? Each correct answer presents part of
the solution.
NOTE: Each correct selection is worth one point.

    A. Use an unmanaged solution in production.
    B.  Rebuild the agents in each environment.
   C. Use Microsoft Power Platform pipelines.
   D. Include the components in a solution.
    E.  Store the agent transcripts in source control.
Answer
   Correct Answer:

   Explanation: C, D

   D. Include the components in a solution All Copilot extensions for Dynamics 365 Customer
   Service—custom actions, plugins, connectors, prompts, and Copilot Studio agents—must be
   packaged inside a Power Platform solution to support:

       •   Versioning
       •  Dependency tracking
       •  Environment isolation

---

## [Página 56](AB-100%20Q%26A.pdf#page=56) · texto nativo

•  Managed deployments to Test/Prod

   C. Use Microsoft Power Platform pipelines Deployment pipelines provide:

       •  Automated Dev → Test → Prod promotion
       •  No manual intervention
       •  Governance and approvals
       •  Repeatable deployments
       •  Managed solution enforcement in production

Discussion: https://www.examtopics.com/discussions/microsoft/view/384484-exam-ab-100-
topic-3-question-12-discussion/

060 Question.
You are designing a testing solution for a Microsoft Copilot Studio agent that integrates with
Microsoft Dynamics 365 Customer Service and Dynamics 365 Sales.
You need to design end-to-end scenarios to test the agent's ability to perform the following actions:
Coordinate tasks and data interactions across both Dynamics 365 apps.
Interpret user input and provide contextually relevant outputs.
Which test scenario and metric should you include in the design? To answer, select the appropriate
options in the answer area.
NOTE: Each correct selection is worth one point.





.
Answer
   Correct Answer:

---

## [Página 57](AB-100%20Q%26A.pdf#page=57) · texto nativo

Explanation:

            1)  Test scenario: Run task-based scenarios that involve both apps You must
              simulate end-to-end workflows that span Customer Service and Sales—such as
               creating a case, updating an opportunity, or retrieving customer history across
             systems.

           This is exactly what task-based scenarios involving both apps are designed for.

            2)  Metric: Track the successful completion of cross-app tasks The best metric is
             whether the agent can successfully complete the multi-app tasks it was asked to
              perform. This validates:
              •  Correct interpretation of user intent
              •  Correct grounding
              •  Correct orchestration across systems
              •  Correct data retrieval and updates

Discussion: https://www.examtopics.com/discussions/microsoft/view/384485-exam-ab-100-
topic-3-question-13-discussion/

061 Question.
A company has multiple AI models that support generation of sales transactions.
Each release of the models must be reviewed by a security and compliance team before being
deployed to the production environment. The security and compliance team must have access to
prior versions to properly determine potential exposures introduced.
You need to recommend a solution to evaluate the impact of each deployment to production. The
solution must enhance business continuity.
What should you recommend?

    A.  Create a central model registry that uses version history.
    B.  Establish a promotion process by using a quality gate.

---

## [Página 58](AB-100%20Q%26A.pdf#page=58) · texto nativo

C. Implement version control for all the AI system components.
   D. Track model retirement schedules to prevent service disruptions.
Answer
   Correct Answer: A

   Explanation:

    A. Create a central model registry that uses version history. You described three key
   requirements: - Every model release must be reviewed by security and compliance before
    production. - Security must have access to prior versions to compare changes and detect new
    risks. - Business continuity must be protected — meaning controlled, traceable, reversible
   deployments. This is exactly the problem that a central model registry with versioning is
   designed to solve.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384059-exam-ab-100-
topic-3-question-14-discussion/

062 Question.
DRAG DROP -
A company has an AI solution that uses a Microsoft Copilot Studio agent.
You need to monitor the agent's performance. The solution must meet the following requirements:
Monitor the agent's telemetry in near-real-time (NRT).
Download transcripts of full conversations.
Monitor the agent's usage and performance.
What should you use for each requirement? To answer, drag the appropriate options to the correct
requirements. Each option may be used once, more than once, or not at all. You may need to drag
the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 59](AB-100%20Q%26A.pdf#page=59) · texto nativo

Explanation:

   Near-real-time telemetry → Application Insights Application Insights is the only option that
    provides live metrics, NRT telemetry, and deep diagnostics (requests, dependencies,
    exceptions, traces). Copilot Studio can surface analytics, but not true NRT telemetry.

    Full conversation transcripts → Copilot Studio Copilot Studio includes the Transcripts area
   where you can export full conversations. Application Insights only stores event-level telemetry,
   not full transcripts.

   Usage & performance monitoring → Copilot Studio Copilot Studio provides built-in analytics
   dashboards for:

          •  Session counts
          •   Escalations
          •  Resolution rates
          •  Channel usage
          •  CSAT
          •  Topic performance These are the standard usage/performance KPIs for Copilot
              Studio agents.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384060-exam-ab-100-
topic-3-question-15-discussion/

063 Question.
A company deploys a Microsoft Copilot Studio agent that integrates with a Microsoft Power
Automate desktop flow.
You need to recommend a testing solution that meets the following requirements:
Test cases must validate the most recent changes to the agent before the agent is released.
The flow must be validated as part of the agent's orchestration.
What should you recommend for each requirement? To answer, select the appropriate options in
the answer area.

---

## [Página 60](AB-100%20Q%26A.pdf#page=60) · texto nativo

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

    The correct pair is:

       •   Validate the most recent changes to the agent before release: Run tests against the
           latest unpublished version of the agent. This is the only option that ensures you are
            validating new changes before publishing. Testing on production or live users would not
         meet the requirement.
       •   Validate the flow as part of the agent’s orchestration: Add the flow to the agent as a
            tool. A Power Automate desktop flow must be exposed to Copilot Studio as a tool so
           the agent can call it during orchestration. Canvas apps and the PAD console do not
           integrate with Copilot Studio orchestration.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384061-exam-ab-100-
topic-3-question-16-discussion/

064 Question.
A company has a Microsoft Copilot Studio agent that provides answers based on a knowledge base
for customer support.

---

## [Página 61](AB-100%20Q%26A.pdf#page=61) · texto nativo

Users report that, occasionally, the agent provides inaccurate answers.
You need to use metrics from the Analytics tab in Copilot Studio to identify the cause of the
inaccuracies.
Which two options should you use? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

    A.  survey results
    B.  session information and session outcomes
   C. topic usage and topics with low resolution
   D. engagement, resolution, and escalation rates
    E.  quality of generated answers
Answer
   Correct Answer: B, C

   Explanation:

    B. Session information and session outcomes

       •  These metrics show:
       •  How conversations flow
       •  Where users get stuck
       •  Whether sessions end in success, abandonment, or escalation
       •  They help you pinpoint where the bot misunderstood the user or failed to resolve an
           issue.

   C. Topic usage and topics with low resolution

       •  These metrics reveal:
       •  Which topics are triggered most often
       •  Which topics fail to resolve successfully
       •  Where the bot may be matching the wrong topic or lacking knowledge

    Low-resolution topics are a strong indicator of inaccurate or incomplete answers.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384062-exam-ab-100-
topic-3-question-17-discussion/

065 Question.
A company uses a fine-tuned Microsoft Foundry model that requires frequent updates as new
customer feedback becomes available.
You need to design an application lifecycle management (ALM) process that meets the following
requirements:
Data changes must be tracked and versioned.
The model must be retrained consistently by using approved training data.
Which two actions should you include in the design? Each correct answer presents part of the

---

## [Página 62](AB-100%20Q%26A.pdf#page=62) · texto nativo

solution.
NOTE: Each correct selection is worth one point.

    A.  Associate the storage location to the fine-tuning job.
    B.  Create a content filter.
   C. Store the training data in Azure Files.
   D. Upload the training data to Microsoft Foundry data files
    E.  Store the training data in Azure Blob Storage that has version control enabled.
Answer
   Correct Answer:

   Explanation:

    A. Associate the storage location to the fine-tuning job Foundry fine-tuning jobs support
    referencing a storage location (Blob Storage or Foundry data files). This ensures:

       •  The model is always trained on the approved dataset
       •   Retraining is consistent and repeatable
       •  The job pulls data from a controlled, governed location

    This is essential for ALM.

    E. Store the training data in Azure Blob Storage with version control Blob Storage with
    versioning provides:

       •  Automatic version history of every dataset change
       •   Ability to roll back to prior versions
       •   Full traceability for compliance and audits
       •  A single source of truth for training data

Discussion: https://www.examtopics.com/discussions/microsoft/view/384486-exam-ab-100-
topic-3-question-18-discussion/

066 Question.
A company deploys agents that generate responses by using Azure OpenAI resources. The agents
are deployed to both the United States and Europe.
You need to recommend a governance solution that meets the following requirements:
Enforces the deployment of the resources to only approved Azure regions
Provides continuous compliance verification of the resources
What should you include in the recommendation for each requirement? To answer, select the
appropriate options in the answer area.
NOTE: Each correct selection is worth one point..

---

## [Página 63](AB-100%20Q%26A.pdf#page=63) · texto nativo

Answer
   Correct Answer:





   Explanation:

            1.  Azure Policy → Restrict deployments to approved regions Azure Policy can enforce
               rules such as: - “Resources may only be deployed in East US and West Europe” -
            “Deny creation of resources outside approved regions” This is the only tool
             designed for preventive governance.
            2.  Microsoft Defender for Cloud → Continuous compliance verification Defender for
            Cloud provides: - Continuous compliance assessments - Regulatory standards

---

## [Página 64](AB-100%20Q%26A.pdf#page=64) · texto nativo

mapping (ISO, SOC, GDPR, etc.) - Secure score - Alerts when resources drift out of
             compliance This satisfies the requirement for ongoing compliance monitoring.

   .Discussion: https://www.examtopics.com/discussions/microsoft/view/384063-exam-ab-
    100-topic-3-question-19-discussion/

067 Question.
A company has an AI solution that uses Azure OpenAI models.
You need to recommend a governance solution that monitors and audits changes to model
configurations and data usage. The solution must minimize administrative effort.
What should you include in the recommendation?

    A.  Azure Monitor
    B.  Azure Stream Analytics
   C. Azure API Management
   D. Azure Policy
    E.  Microsoft Purview
Answer
   Correct Answer: E

   Explanation:

   The requirement is clear: You need governance over model configuration changes and data
   usage, with minimal administrative effort. Among the options, only one service is designed
    specifically for:

       •   Monitoring data access and usage
       •   Auditing model-related assets
       •   Tracking sensitive data flows
       •   Providing governance with minimal overhead

   That service is Microsoft Purview.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384064-exam-ab-100-
topic-3-question-20-discussion/

068 Question.
A company uses Azure OpenAI models that use grounding data from Microsoft Fabric for agents.
The models are fine-tuned by using proprietary datasets.
You need to design a governance solution that meets the following requirements:
Restricts access to the grounding data to only assigned roles
Restricts model fine-tuning to only the AI engineering team
What should you include in the design? To answer, select the appropriate options in the answer

---

## [Página 65](AB-100%20Q%26A.pdf#page=65) · texto nativo

area.
NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

    1. Microsoft Purview access policies → Restrict access to grounding data Grounding data
    stored in Microsoft Fabric can be governed using:

       •  Purview access policies
       •   Data-level permissions
       •  Role-based access to sensitive datasets

   Purview is the only option that provides fine-grained, centralized data access governance.

---

## [Página 66](AB-100%20Q%26A.pdf#page=66) · texto nativo

2. RBAC in Microsoft Foundry → Restrict model fine-tuning Fine-tuning operations in Foundry
    are controlled through:

              •  Foundry workspace roles
              •   Model-level permissions
              •   Restricting fine-tuning to specific security groups (e.g., AI engineering team)

    This ensures only authorized users can initiate fine-tuning jobs.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384487-exam-ab-100-
topic-3-question-21-discussion/

069 Question.
A company has a Microsoft Copilot Studio agent that has been in production for three months.
The agent has received positive feedback from users.
You need to identify the number of questions unanswered by the agent and the number of
abandoned sessions between the users and the agent.
Which Copilot Studio insights should you use? To answer, drag the appropriate insights to the
correct requirements. Each insight may be used once, more than once, or not at all. You may need
to drag the split bar between panes or scroll to view content.
NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

    1. Generated answer rate and quality → Unanswered questions This insight shows:

       •  How often the agent generated an answer

---

## [Página 67](AB-100%20Q%26A.pdf#page=67) · texto nativo

•  How many times it failed to answer
       •   Quality and grounding issues

      It is the only insight that directly exposes unanswered or low-quality responses.

    2. Conversation outcomes → Abandoned sessions Conversation outcomes include:

       •  Completed sessions
       •  Escalated sessions
       •   Failed sessions
       •  Abandoned sessions

    This is the metric used to track when users leave before the agent completes the task.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384488-exam-ab-100-
topic-3-question-22-discussion/

070 Question.
You are evaluating a Microsoft Copilot Studio agent that supports Microsoft Dynamics 365
Customer Service representatives.
You need to recommend a testing solution that meets the following requirements:
Evaluates agent effectiveness during active sessions
Validates whether the agent delivers accurate and helpful responses
Provides measurable, actionable insights for continuous improvement
What should you recommend?

    A.  Track resolution, deflection, and accuracy by using dashboards and use scripts to ensure
       consistent responses.
    B. Perform load testing to validate how the agent scales under a high chat volume.
   C. Review historical tickets to find agents that have the shortest resolution times.
   D. Measure uptime and page load times.
Answer
   Correct Answer: A

   Explanation:

   The correct recommendation is: A. Track resolution, deflection, and accuracy by using
   dashboards and use scripts to ensure consistent responses. Resolution, deflection, and
   accuracy dashboards provide:

       •   Real-time effectiveness metrics
       •  How often the agent resolves vs. escalates
       •  How many cases are deflected
       •  Accuracy and grounding quality
       •   Patterns of failure or misunderstanding

---

## [Página 68](AB-100%20Q%26A.pdf#page=68) · texto nativo

Using scripts ensures consistent prompts and scenarios so you can measure improvements
   over time.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384489-exam-ab-100-
topic-3-question-23-discussion/

071 Question.
A company uses multiple Microsoft Copilot Studio agents across different channels.
You need to recommend a monitoring solution that provides comprehensive telemetry data and
performance insights for the agents.
What should you include in the recommendation?

    A.  Application Insights
    B.  Azure Advisor
   C. Azure DevOps
   D. Microsoft Dynamics 365 Customer Voice
Answer
   Correct Answer:

   Explanation:

   The correct recommendation is: A. Application Insights

   When a company uses multiple Copilot Studio agents across different channels, you need a
   monitoring solution that can:

       •   Collect centralized telemetry
       •  Track performance, latency, failures, and usage patterns
       •   Provide end-to-end observability
       •  Support custom events, traces, and distributed logging
       •  Scale across all agents and channels

    Application Insights is the only option that delivers this level of comprehensive monitoring.

Discussion: https://www.examtopics.com/discussions/microsoft/view/384490-exam-ab-100-
topic-3-question-24-discussion/

072 Question.
A company has an AI solution built by using Microsoft Copilot Studio and Power Platform. The
solution is used by the company's sales, marketing, and customer service teams.
You are performing a return on AI investment (ROAI) analysis to evaluate the impact of the solution.
You need to identify which measurable business drivers to include in the analysis.
Which two business drivers should you identify? Each correct answer presents part of the solution.
NOTE: Each correct selection is worth one point.

---

## [Página 69](AB-100%20Q%26A.pdf#page=69) · texto nativo

A.  the reduced average case resolution time
    B. market capitalization
   C. economic market predictability
   D. increased employee productivity
    E.  brand awareness
Answer
   Correct Answer: A,D

   Explanation:

    A. the reduced average case resolution time

    This is a classic ROAI metric because it directly measures:

       •   Faster customer service handling
       •  Reduced operational cost per case
       •  Higher customer satisfaction
       •  Improved throughput for support teams

     It’s quantifiable, trackable, and directly impacted by AI assistance.

   D. increased employee productivity

    AI copilots improve productivity by:

       •  Automating repetitive tasks
       •   Drafting responses
       •  Summarizing customer interactions
       •  Reducing manual data entry

    This leads to measurable gains such as:

       •  More cases handled per agent
       •  More leads processed
       •  More time spent on high-value tasks

Discussion: https://www.examtopics.com/discussions/microsoft/view/384093-exam-ab-100-
topic-3-question-25-discussion/

073 Question.
A company has a Microsoft Foundry agent that summarizes customer feedback and recommends
products to customers. The agent references data from multiple knowledge sources.

Users report that the agent response time is slow.

Telemetry data shows that the agent frequently reaches its token usage limit.

---

## [Página 70](AB-100%20Q%26A.pdf#page=70) · texto nativo

You need to recommend a solution to reduce token usage without degrading the quality of the
generated responses.

What should you recommend?

    A. Chunk documents during indexing.
    B. Reduce the number of knowledge sources used by the agent.
   C. Reconfigure the prompts to limit the amount of retrieved content from the knowledge
       sources.
   D. Lower the maximum token usage limit for the responses.
Answer
   Correct Answer: C

   Explanation:

    This reduces token usage by:

       •   Restricting how much grounding data is pulled into the prompt
       •  Summarizing or chunking retrieved content before passing it to the model
       •  Using more selective retrieval instructions
       •  Reducing unnecessary context while keeping quality intact

    This is the standard optimization technique for Foundry and Azure OpenAI agents that hit token
    ceilings.

      It improves latency and reduces cost without degrading answer quality.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406252-exam-ab-100-
topic-3-question-26-discussion/

074 Question.
A company has Microsoft Power Platform development, staging, and production environments.
Each environment has its own Microsoft Dataverse tables and Azure AI Search index.

You are designing an application lifecycle management (AIM) process to deploy a Microsoft Copilot
Studio agent between the environments.

The company has a Copilot Studio agent named Agent1 in development. Agent1 uses the following
grounding data sources:

    •  A Dataverse table named CustomerOrders
    •  An Azure AI Search index named customer-knowledge

---

## [Página 71](AB-100%20Q%26A.pdf#page=71) · texto nativo

You need to deploy Agent1 to production. The solution must ensure that the agent uses the
production grounding data sources, minimizes downtime, and handles credentials and endpoints
securely.

What should you include in the deployment package solution, and what should you reconfigure
after the deployment? To answer, select the appropriate options in the answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 72](AB-100%20Q%26A.pdf#page=72) · texto nativo

Explanation:

    1.  Agent1 and references to the data sources

You do not include actual data sources (Dataverse tables or Azure AI Search indexes) in the
solution package. Each environment already has its own:

       •  Dataverse table: CustomerOrders
       •  Azure AI Search index: customer-knowledge

Instead, you include:

       •  Agent1 - References to the data sources (not the data sources themselves)
    2. The Dataverse and Azure AI Search connections

Connections contain:

       •   Environment-specific endpoints
       •   Environment-specific credentials
       •   Environment-specific indexes/tables

Therefore, after deployment you must reconfigure:

       •  Dataverse connection → point to production CustomerOrders
       •  Azure AI Search connection → point to production customer-knowledge index

Discussion: https://www.examtopics.com/discussions/microsoft/view/406253-exam-ab-100-
topic-3-question-27-discussion/

075 Question.
A company has a Microsoft Copilot Studio agent that uses generative AI to assist Microsoft
Dynamics 365 Customer Service representatives.

The agent currently exhibits a low resolution rate and a high escalation rate.

You need to identify the issue.

What should you use?

    A.  the Agent dashboard of Dynamics 365 Customer Service historical analytics
    B.  the Insights tab from the Search & intelligence settings of the Microsoft 365 admin center
   C. the Copilot hub in the Power Platform admin center
   D. the Analytics tab in Copilot Studio
Answer
   Correct Answer: D

   Explanation:

---

## [Página 73](AB-100%20Q%26A.pdf#page=73) · texto nativo

The Analytics tab in Copilot Studio provides:

       •   Resolution rate
       •   Escalation rate
       •  Abandoned sessions
       •  Unanswered questions
       •  Topic performance
       •  Generated answer quality
       •  Grounding effectiveness
       •  Session outcomes

Discussion: https://www.examtopics.com/discussions/microsoft/view/406254-exam-ab-100-
topic-3-question-28-discussion/

076 Question.
A company has a Microsoft Foundry generative AI model.

You need to evaluate the model's output to measure the overall quality and coherence of
generated responses. The evaluation must use GPT-4o as a judge and return a numeric score for
each output.

Which type of metric should you use?

    A.  AI quality (NLP)
    B.  risk and safety
   C. Groundedness
   D.  AI quality (AI assisted)
Answer
   Correct Answer: D

   Explanation:

    AI quality (AI assisted) This metric:

       •  Uses an LLM (like GPT-4o) as an evaluator
       •  Scores each output numerically
       •  Measures coherence, clarity, helpfulness, and correctness
       •   Provides consistent, automated evaluation
       •   Is the recommended approach for Foundry model quality assessment

    This is exactly what the question describes.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406255-exam-ab-100-
topic-3-question-29-discussion/

---

## [Página 74](AB-100%20Q%26A.pdf#page=74) · texto nativo

077 Question.
You use Microsoft Copilot Studio analytics to analyze the performance of a deployed Copilot
Studio agent.

You need to identify which performance metrics to use to measure the following:

    •  The percentage of engaged sessions that are escalated to a live customer service
       representative
    •  The number of agent queries that cause a knowledge source error


What should you identify for each requirement? To answer, select the appropriate options in the
answer area.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:

---

## [Página 75](AB-100%20Q%26A.pdf#page=75) · texto nativo

Explanation:


    1. Escalation rate → % of engaged sessions escalated Escalation rate measures:

       •  How many engaged sessions required a human handoff
       •  The percentage of conversations that the agent could not resolve
       •  A key indicator of agent effectiveness This directly matches the first requirement.

    2. Answer quality → Knowledge source errors The Answer quality insight includes:

       •  Knowledge source errors
       •   Retrieval failures - Hallucinations
       •  Poor grounding
       •   Low-quality or incomplete answers

      It is the only metric that reports knowledge source errors.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406256-exam-ab-100-
topic-3-question-30-discussion/

078 Question.
A company plans to deploy a Microsoft Foundry agent.

You need to recommend an application lifecycle management (ALM) process to ensure that the
agent evaluates against baseline accuracy metrics before being deployed.

What should you recommend?

    A.  Configure GitHub Actions for new agent versions.
    B. Deploy each new agent version directly to production.
   C. Use Observability in Foundry Control Plane with evaluation and drift monitoring.
   D. Enable Application Insights and use Azure Monitor.
Answer
   Correct Answer: C

   Explanation:

   Observability in Foundry Control Plane gives you:

       •  Automated evaluation pipelines
       •   Baseline accuracy scoring
       •  LLM-as-a-judge evaluations
       •   Drift detection (data drift, behavior drift, quality drift)
       •   Quality gates before deployment

---

## [Página 76](AB-100%20Q%26A.pdf#page=76) · texto nativo

•  Continuous monitoring after deployment

    This is exactly what an ALM process requires for safe, high-quality AI deployment.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406257-exam-ab-100-
topic-3-question-31-discussion/

079 Question.
You need to recommend a security solution for agents in a Microsoft Power Platform environment.

The agents must use only approved connectors and services. The solution must prevent the agents
from accessing sensitive data.

What should you recommend?

    A.  Configure Azure Monitor to capture connector activity logs.
    B. Enable a Microsoft Dataverse audit.
   C. Deploy data loss prevention (DLP) policies in Power Platform.
   D. Enable customer-managed keys in Microsoft Dataverse.
Answer
   Correct Answer: C

   Explanation:

   Deploy data loss prevention (DLP) policies in Power Platform Power Platform DLP policies
    allow you to:

       •   Control which connectors agents are allowed to use
       •  Block or restrict unapproved or risky connectors
       •  Separate connectors into Business, Non-Business, and Blocked categories
       •  Prevent agents from accessing sensitive data sources
       •  Apply policies at the environment, tenant, or solution level

    This is the official and recommended way to enforce connector governance for Copilot Studio
    agents, Power Automate flows, and Power Apps.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406258-exam-ab-100-
topic-3-question-32-discussion/

080 Question.
A company has an AI business solution that uses Microsoft Copilot Studio agents.

You need to recommend prompt best practices to improve the effectiveness of agent interactions.

---

## [Página 77](AB-100%20Q%26A.pdf#page=77) · texto nativo

Which two actions should you include in the recommendation? Each correct answer presents part
of the solution.

NOTE: Each correct selection is worth one point.

    A.  Track the duration of the average user session.
    B.  Analyze the prompt length distribution.
   C. Regularly test and refine the prompts based on user input.
   D. Use clear and specific instructions in the prompts.
    E. Measure system resource usage during prompt processing.
Answer
   Correct Answer: C,D

   Explanation:

    •  C. Regularly test and refine the prompts based on user input

Clear prompts reduce ambiguity and help the agent:

    •  Stay on topic
    •  Produce more accurate responses
    •  Follow business rules consistently

This is one of the core principles of effective prompt engineering.

    •  D. Use clear and specific instructions in the prompts

Prompts must evolve based on:

    •  Real user interactions
    •   Failure cases
    •   Escalations
    •   Low-quality answers

Iterative refinement is essential for improving agent performance over time.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406259-exam-ab-100-
topic-3-question-33-discussion/

081 Question.
A company has a cloud-based AI solution that uses Azure OpenAI models.

You need to design a monitoring solution that meets the following requirements:

    •  Monitors performance metrics and operational health for the models
    •  Monitors AI apps and agents for compliance

---

## [Página 78](AB-100%20Q%26A.pdf#page=78) · texto nativo

•  Uses Azure-native capabilities
    •  Minimizes development effort


What should you use for each requirement? To answer, drag the appropriate options to the correct
requirements. Each option may be used once, more than once, or not at all. You may need to drag
the split bar between panes or scroll to view content.

NOTE: Each correct selection is worth one point.





Answer
   Correct Answer:





   Explanation:

1. Microsoft Purview → Compliance

Monitoring Purview provides:

       •  Data access governance
       •   Sensitive data classification
       •  Lineage tracking
       •   Policy enforcement

---

## [Página 79](AB-100%20Q%26A.pdf#page=79) · texto nativo

•  Compliance insights for AI apps and agents

It is the only Azure-native service designed specifically for compliance monitoring.

2. Azure Monitor → Performance & operational health

Azure Monitor provides:

       •  Latency metrics
       •  Throughput
       •  Token usage
       •   Errors and exceptions
       •  Dependency performance
       •  Health dashboards

It is the standard Azure-native solution for operational monitoring of Azure OpenAI and AI
applications.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406260-exam-ab-100-
topic-3-question-34-discussion/

082 Question.
A company has Microsoft Copilot Studio agents.

The company plans to deploy custom connectors across development, test and production
environments.

You need to design an application lifecycle management (ALM) process to ensure consistency and
prevent direct editing in production.

Which two actions should you include in the design? Each correct answer presents part of the
solution.

NOTE: Each correct selection is worth one point.

    A. Deploy managed solutions to production.
    B. Deploy unmanaged solutions to production.
   C. Manually rebuild the agents in each environment.
   D. Move the agents between the environments by using data export and import.
    E.  Include agents and connectors in a solution.
Answer
   Correct Answer: A,E

   Explanation:

---

## [Página 80](AB-100%20Q%26A.pdf#page=80) · texto nativo

A. Deploy managed solutions to production Managed solutions:

       •  Prevent editing in production (a key requirement)
       •  Lock down components so only dev/test can modify them
       •  Ensure controlled, versioned deployments
       •  Are the Microsoft-recommended practice for production environments

    E. Include agents and connectors in a solution This is essential because:

       •   Solutions are the ALM unit in Power Platform
       •  Custom connectors must be packaged inside solutions for proper versioning
       •   Copilot Studio agents are solution components and must be moved this way
       •  Ensures consistent deployment across environments

Discussion: https://www.examtopics.com/discussions/microsoft/view/406261-exam-ab-100-
topic-3-question-35-discussion/

083 Question.
A company uses multiple Microsoft Copilot Studio agents across different channels.

You need to recommend a monitoring solution that provides comprehensive telemetry data and
performance insights for the agents.

What should you include in the recommendation?

    A.  Application Insights
    B.  Microsoft Dynamics 365 Customer Voice
   C. Log Analytics
   D. Microsoft Purview
Answer
   Correct Answer: A

   Explanation:

   Application Insights gives:

       •  End-to-end telemetry
       •   Latency, token usage, failures, exceptions
       •  Dependency tracking (Dataverse, connectors, APIs)
       •  Custom events for agent interactions
       •  Dashboards and alerts
       •  Works across all channels (web, Dynamics, custom apps)

    This is the recommended monitoring solution for Copilot Studio agents at scale.

---

## [Página 81](AB-100%20Q%26A.pdf#page=81) · texto nativo

Discussion: https://www.examtopics.com/discussions/microsoft/view/406262-exam-ab-100-
topic-3-question-36-discussion/

084 Question.
A company has an AI solution named Solution1 that is deployed to the production environment.
Solution1 uses an Azure OpenAI model to generate marketing emails for existing customers.

During an internal review, you identify that Solution1 creates different emails depending on the
customers’ traits.

You need to recommend a strategy to mitigate the bias. The strategy must adhere to Microsoft
responsible AI principles.

What should you recommend?

    A.  Modify Solution1 to randomly generate emails for different traits.
    B.  Modify the system instructions of Solution1.
   C. Retrain the model by using a larger dataset.
   D. Modify the contents of the training dataset.
Answer
   Correct Answer: D

   Explanation:

   Bias in model outputs typically originates from:

       •  Biased or unbalanced training data
       •   Over-representation of certain traits
       •   Patterns in the dataset that the model learns and amplifies

    Responsible AI guidance from Microsoft emphasizes:

       •  Reviewing and correcting training data
       •  Removing or balancing sensitive attributes
       •  Ensuring datasets do not encode harmful or discriminatory patterns

    This is the most direct and effective way to mitigate bias.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406263-exam-ab-100-
topic-3-question-37-discussion/

085 Question.
A company has a canvas app named App1 in a Microsoft Power Platform environment named Env1.

---

## [Página 82](AB-100%20Q%26A.pdf#page=82) · texto nativo

Env1 uses a customer-managed key for data encryption. App1 connects to multiple data sources
to retrieve and update customer and order information.

You need to recommend a solution to add Microsoft Copilot components to App1. The solution
must NOT modify the current security or encryption configurations of Env1.

What should you include in the recommendation?

    A.  Modify the data sources of App1 to make them compatible with Copilot.
    B.  Duplicate App1 and republish the app in Env1.
   C. Enable Copilot features for Env1.
   D. Move App1 to a new environment that uses Microsoft-managed keys.
Answer
   Correct Answer: C

   Explanation:

    Copilot features in Power Apps (Copilot control, Copilot answers, Copilot suggestions) are
    environment-level capabilities. Enabling them:

       •  Does NOT modify encryption settings (CMK remains untouched)
       •  Does NOT require moving the app
       •  Does NOT require changing data sources
       •  Allows Copilot components to be added directly to App1

    Microsoft explicitly supports Copilot features in environments using customer-managed keys.

Discussion: https://www.examtopics.com/discussions/microsoft/view/406264-exam-ab-100-
topic-3-question-38-discussion/

---

## [Página 83](AB-100%20Q%26A.pdf#page=83) · texto nativo

[No se detectó texto legible en esta página]
