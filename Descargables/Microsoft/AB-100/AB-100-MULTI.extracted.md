# Transcripción: AB-100-MULTI.pdf

- Archivo fuente: `AB-100-MULTI.pdf`
- Páginas del archivo: 4
- Páginas incluidas: `1-4`
- Extracción: 2026-10-02T11:15+02:00
- Aviso: resultado automático; cotejar cifras e identificadores con el original.

## [Página 1](AB-100-MULTI.pdf#page=1) · texto nativo

MULTI 01
A company uses Microsoft 365 and Dynamics 365.

You need to recommend a solution to automatically summarize email threads, generate suggested
replies in Microsoft Outlook, and provide meeting preparation summaries that include relevant
customer relationship management (CRM) data.

Option 1:
Solution: You recommend Microsoft 365 Copilot for Sales.
Does this meet the goal?

    A.  Yes
    B. No


Microsoft 365 Copilot for Sales does enhance Outlook with CRM-aware insights, but the scenario
requires automatic email thread summaries, suggested replies, and meeting preparation summaries
that include Dynamics 365 CRM data. The correct solution for those capabilities is Copilot for Microsoft
365 with Sales Copilot (formerly Viva Sales). Sales Copilot is an add-on that enriches Copilot for
Microsoft 365 with CRM context — but by itself, it does not provide the full Outlook and meeting-prep
generative AI experience. So recommending only Microsoft 365 Copilot for Sales does not meet the
goal.

Option 2:
Solution: You recommend a classic Microsoft Dataverse workflow.
Does this meet the goal?

    A.  Yes
    B. No

A classic Microsoft Dataverse workflow cannot meet the goal because: - It does not generate AI-based
email summaries - It does not create suggested replies in Outlook - It does not produce meeting
preparation summaries enriched with Dynamics 365 CRM data - It is a legacy automation engine focused
on record updates, notifications, and simple logic — not generative AI The required capabilities come
from Copilot for Microsoft 365 combined with Sales Copilot, not from Dataverse workflows.
Option 3:

Solution: You recommend a Microsoft 365 Copilot agent template.
Does this meet the goal?

    A.  Yes
    B. No

Agent templates are designed for building custom task-oriented agents (e.g., workflow automation,
domain-specific copilots). They do not provide: - Automatic email thread summarization in Outlook -
Suggested replies in Outlook - Meeting preparation summaries enriched with Dynamics 365 CRM data

---

## [Página 2](AB-100-MULTI.pdf#page=2) · texto nativo

MULTI 02
A company has a Microsoft Dynamics 365 Sales environment that has Microsoft Copilot enabled.

You need to customize Copilot by tailoring how opportunity summaries are generated or how they are
presented to users.

Option 1:
Solution: You add fields to the opportunity summary.
Does this meet the goal?

    A.  Yes
    B. No

Adding fields to the opportunity entity does not customize how Copilot generates or presents
opportunity summaries. Copilot’s opportunity summaries are controlled through Copilot Studio (custom
prompts, plugins, grounding data, etc.), not by modifying Dynamics 365 fields. Adding fields only
changes the data model — it does not change Copilot’s summarization behavior.

Option 2:
Solution: You build Microsoft Power Automate flows to trigger customized Copilot summaries.
Does this meet the goal?

    A.  Yes
    B. No

Power Automate flows cannot customize how Copilot generates or presents opportunity summaries in
Dynamics 365 Sales. Flows can automate notifications, data updates, or downstream actions, but they
do not modify Copilot’s summarization logic, prompt structure, or presentation layer. To customize
Copilot summaries, you must use Copilot Studio—specifically custom prompts, plugins, or grounding
data—not Power Automate.

Option 3:
Solution: You configure AI Builder lead scoring models to influence opportunity summaries.
Does this meet the goal?

    C.  Yes
    D. No

Configuring AI Builder lead scoring models does not influence how Copilot generates or presents
opportunity summaries in Dynamics 365 Sales. Lead scoring affects qualification insights for leads, not: -
Copilot’s summarization prompts - The structure or content of opportunity summaries - How Copilot
interprets or presents opportunity data To customize Copilot summaries, you must adjust Copilot Studio
custom prompts or Copilot grounding data, not AI Builder models.

Option 4:
Solution: You add the opportunity summary widget to the Opportunity form..
Does this meet the goal?

---

## [Página 3](AB-100-MULTI.pdf#page=3) · texto nativo

A.  Yes
    B. No

Explanation
Adding the opportunity summary widget to the Opportunity form only surfaces Copilot’s existing
summary—it does not customize: - how Copilot generates the summary - what data Copilot includes -
how the summary is structured or phrased It’s a UI placement action, not a customization of Copilot
behavior. To actually tailor summaries, you must modify Copilot Studio prompts or Copilot grounding
data.

MULTI 03
You A company has a team that analyzes its customers by using a manual process.

You are designing an AI-based agent to automate and improve the process.

You need to recommend on which platform to build the agent. The solution must meet the following
requirements:

   •  Use generative AI to answer common questions.
   •   Provide analytics to review AI performance.
   •   Identify customer demographics.
   •  Minimize custom development.

Option 1:
Solution: You recommend GitHub Copilot..
Does this meet the goal?

    A.  Yes
    B. No

Correct answer: B. No Why? GitHub Copilot is a developer productivity tool. It helps write code,
generate functions, and accelerate software development.

It does not meet the requirements of this scenario.

Requirements vs. GitHub Copilot

   •  Use generative AI to answer common questions No: GitHub Copilot does not build
        conversational agents or customer-facing AI.
   •   Provide analytics to review AI performance No: GitHub Copilot has no analytics for agent
        interactions, usage, or performance.
   •   Identify customer demographics : No GitHub Copilot cannot analyze customer data or build
        business workflows.
   •  Minimize custom development: No GitHub Copilot requires more custom development, not less.

---

## [Página 4](AB-100-MULTI.pdf#page=4) · texto nativo

Option 2:
Solution: You recommend Microsoft Security Copilot.


Does this meet the goal?

    A.  Yes
    B. No

    Microsoft Security Copilot is designed for cybersecurity operations, not for building
    customer-analysis agents or business-facing AI workflows.

    •  Use generative AI to answer common questions No: Security Copilot answers security-related
       questions (incidents, threats, alerts). It is not a platform for customer-facing Q&A or business
       process automation.
    •   Provide analytics to review AI performance No. It provides security investigation analytics, not
       agent performance analytics.
    •   Identify customer demographics No Security Copilot cannot analyze customer data or
       demographics.
    •  Minimize custom development No. It is not a low-code/no-code agent-building platform.

Option 3:
Solution: You recommend Microsoft Copilot Studio.


Does this meet the goal?

    A.  Yes
    B. No


Recommending Microsoft Copilot Studio does meet the goal.

    •  Use generative AI to answer common questions: Yes — Copilot Studio builds generative AI
       agents using GPT models, orchestration, and knowledge sources.
    •   Provide analytics to review AI performance: Yes — Copilot Studio includes built-in analytics
       dashboards.
    •   Identify customer demographics: Yes — Copilot Studio can connect. This allows the agent to
        retrieve and analyze customer demographic data with minimal custom code.
    •  Minimize custom development :Yes — Copilot Studio is a low-code/no-code platform designed
        for business AI agents.
