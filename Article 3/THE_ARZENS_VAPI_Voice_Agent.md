# GALVAN AI • THE ARZENS VAPI VOICE AGENT
# THE ARZENS VAPI VOICE AGENT
**From business calls to automated actions**
*A practical implementation using Vapi, webhooks, Make.com, Google Calendar and Google Sheets.*
**Client:** THE ARZENS  
**Implementation:** Galvan AI  
**Voice agent:** Vapi  
**Automation:** Make.com + Google Calendar + Google Sheets
---
## From Business Calls to Automated Actions
A phone call is useful only when the information from that call reaches the right place. For **THE ARZENS**, the voice-agent workflow connects a caller's conversation to the systems used for appointments and complaint records.
The workflow uses **Vapi** as the voice-agent layer and webhook connection, while **Make.com** handles the automation logic. The supplied workflow shows a custom webhook feeding a **Voice Intent Router**. Booking requests move to Google Calendar and Google Sheets, while complaints move to a separate Google Sheets path. Each route then returns a webhook response.
The goal is simple: allow the caller to speak naturally while the system turns the result of the conversation into a useful business action.
## The Idea
The idea was not to build a complicated system. It was to connect a normal customer conversation with the actions that normally require manual work.
The workflow follows this process:
- A caller speaks with the Vapi voice agent.
- The completed call sends its information through a webhook.
- Make.com receives the request.
- The Voice Intent Router identifies the purpose of the request.
- Consultation requests are sent to the booking route.
- Complaints are sent to the complaint route.
- Booking information is added to Google Calendar and Google Sheets.
- Complaint information is added to Google Sheets.
- A webhook response is returned after the workflow processes the request.
## How We Approached It
The system is designed as a short and understandable automation pipeline. Each part has one clear responsibility:
**Vapi Voice Agent → Webhook → Make.com → Voice Intent Router → Booking or Complaint → Calendar/Sheets → Webhook Response**
The advantage of this structure is that the voice conversation does not need to know how the business records are stored. Vapi handles the conversation, while Make.com handles the business workflow.
## System Architecture
![Simplified architecture of the supplied voice-agent workflow](https://github.com/zuhairfan99-ship-it/Galvan_Ai_Internship/blob/main/Article%203/image1.jpg?raw=true)
*Figure 1. Simplified architecture of the supplied voice-agent workflow.*
The architecture begins with the caller and ends with a structured business action.
- **Caller:** starts the conversation with the voice agent.
- **Vapi:** handles the voice interaction and provides the webhook connection.
- **Make.com:** receives the completed call information.
- **Voice Intent Router:** separates the request into the correct business route.
- **Booking route:** creates a Google Calendar event and saves the appointment in Google Sheets.
- **Complaint route:** records the complaint in Google Sheets.
- **Webhook response:** returns a response after the selected workflow has been processed.
This separation keeps the workflow easy to understand and makes it possible to extend individual parts later.
## The Vapi Voice Agent
![Vapi voice agent configuration](https://github.com/zuhairfan99-ship-it/Galvan_Ai_Internship/blob/main/Article%203/image%202.jpg?raw=true)
*Figure 2. Vapi configuration used for the THE ARZENS voice-agent implementation.*
The Vapi configuration presents the agent as an AI voice receptionist and customer-support assistant for **ARZENS**.
The configured responsibilities include:
- Answering business and service inquiries.
- Capturing potential leads.
- Scheduling appointments.
- Checking appointment status.
- Rescheduling appointments.
- Supporting general customer interactions.
The agent is designed to communicate naturally and concisely while collecting the information required for the next workflow step.
The configuration also uses company-specific knowledge files. This allows the voice agent to work with information relevant to the business rather than relying only on a generic conversation.
## Collection Layer: The Webhook
The webhook is the hand-off point between Vapi and Make.com.
After the call reaches its completed stage, Vapi sends the relevant call information to the **Make.com custom webhook**. Make.com can then use that information to continue the automation.
The supplied webhook logs show **“End Of Call Report”** requests using the **POST** method and returning **HTTP 200** responses. These responses provide an operational indication that the webhook is receiving the requests successfully.
The webhook therefore acts as the bridge between the conversation and the business automation.
## Routing Layer: Make.com
![Make.com voice-agent automation workflow](https://github.com/zuhairfan99-ship-it/Galvan_Ai_Internship/blob/main/Article%203/image%203.jpg?raw=true)
*Figure 3. Make.com workflow used to route booking and complaint requests.*
Make.com is the decision and automation layer.
The **Voice Intent Router** separates the incoming request into two main paths.
### Booking / Consultation
The booking route performs the following actions:
1. Receives the completed call information.
2. Routes the request through the booking path.
3. Creates a consultation event in Google Calendar.
4. Adds the appointment information to Google Sheets.
5. Returns a webhook response.
### Complaint
The complaint route follows a different path:
1. Receives the completed call information.
2. Routes the request through the complaint path.
3. Adds the complaint information to the designated Google Sheet.
4. Returns a webhook response.
This means that booking information and complaint information are not mixed together.
## Booking a Consultation
The booking workflow can be understood as a simple sequence.
1. The caller speaks with the Vapi voice agent.
2. The caller provides the information required for the consultation.
3. Vapi sends the completed call information to the webhook.
4. Make.com receives the webhook payload.
5. The Voice Intent Router sends the request to the booking route.
6. Google Calendar creates the consultation event.
7. Google Sheets stores the appointment as a row.
8. The workflow returns a webhook response.
The important point is that the appointment does not have to be copied manually from the call into another system. The automation connects the conversation to the calendar and record.
## Handling a Complaint
Complaints use a separate route so that they can be recorded independently from appointments.
1. The caller explains the issue to the Vapi voice agent.
2. The completed call reaches the Make.com webhook.
3. The Voice Intent Router identifies the complaint route.
4. Make.com sends the information to the complaint Google Sheet.
5. The workflow returns a webhook response.
This provides the team with a dedicated record of the complaint that can be reviewed and followed up later.
## From Raw Call to Useful Record
The important part of the automation is not any single tool. It is the hand-off between the tools.
A conversation begins as **voice data**.
The completed conversation becomes a **structured call result**.
The Voice Intent Router identifies the **purpose of the request**.
The correct Make.com route performs the **business action**.
Finally, the information becomes a **useful business record** in Google Calendar or Google Sheets.
This is the practical value of connecting the systems together: the information produced during a conversation can immediately become part of the business workflow.
## Why This Fits THE ARZENS
THE ARZENS presents itself as a cybersecurity and IT-focused company, with services including penetration testing, cybersecurity, malware analysis, digital forensics, CTF events and IT consulting.
A voice agent provides a direct way for callers to start a conversation, while the automation layer turns the outcome of that conversation into structured records.
The workflow can help by:
- Moving consultation requests into a calendar workflow.
- Keeping appointment records organized.
- Separating complaints from appointment information.
- Reducing repetitive manual data entry.
- Providing visibility through webhook responses.
- Creating a workflow that can be extended as business requirements grow.
## Business Impact
Without automation, a typical process may require a person to:
1. Answer the call.
2. Understand what the caller needs.
3. Write down the information.
4. Open another application.
5. Create an appointment or record.
6. Maintain the information for future follow-up.
With the connected workflow, these steps become part of one process.
The purpose is not to remove every human task. The purpose is to reduce repetitive hand-offs and make sure that the information reaches the system where it is needed.
## Data and Implementation Notes
The supplied workflow confirms the main architecture: Vapi, webhook connection, Make.com routing, Google Calendar, Google Sheets and webhook responses.
The screenshots do not expose every internal field mapping or the complete webhook payload. Therefore, this article does not assume field names that are not visible in the supplied material.
For a production implementation, useful records could include:
- Caller name
- Phone number
- Call type
- Preferred date and time
- Consultation details
- Complaint text
- Call ID
- Timestamp
- Processing status
These are recommended implementation fields and should not be treated as fields confirmed by the screenshots.
## Challenges
Building a workflow like this requires more than connecting applications. The main challenges include:
- Keeping the voice conversation natural while collecting the information required for automation.
- Correctly identifying whether a request is a booking or a complaint.
- Making sure the correct Make.com route is triggered.
- Keeping appointment and complaint records consistent.
- Handling failed downstream actions without losing the original call information.
- Monitoring webhook responses so integration problems can be identified quickly.
## Future Improvements
The workflow can be expanded as the number of calls and appointments increases.
Possible improvements include:
- Automatic confirmation messages after successful appointment creation.
- Notifications when a new complaint is recorded.
- Workflow statuses such as **New, In Review, Contacted and Closed**.
- Error handling and retries for failed Calendar or Sheets actions.
- A unique call ID for easier troubleshooting.
- CRM integration when spreadsheet-based records are no longer sufficient.
- Additional reporting for calls, appointments and complaints.
## Our Approach at Galvan AI
At **Galvan AI**, the workflow is approached from the business process first rather than from the tool first.
The process is straightforward:
1. Understand the existing manual process.
2. Identify the decision points.
3. Connect the services that need to communicate.
4. Automate repetitive hand-offs.
5. Store information in a structured format.
6. Keep the workflow easy to inspect and extend.
For this project, that approach resulted in a **Vapi voice agent connected to Make.com**, with **Google Calendar** and **Google Sheets** handling the business actions.
The system is intentionally simple:
**Receive → Classify → Act → Respond**
Galvan AI focuses on practical automation systems that connect the tools a team already uses and reduce repetitive manual work.
## What's Next
The next stage is to expand the workflow only where it creates a real operational benefit.
As the number of calls and appointments grows, the system can be extended with CRM integration, richer reporting, notifications, stronger error handling and more detailed workflow monitoring.
The core architecture does not need to change. New capabilities can be added around the same basic process.
## Conclusion
The **THE ARZENS Vapi Voice Agent** turns a phone conversation into an automated business workflow.
**Vapi** handles the voice interaction.
**The webhook** carries the completed call information.
**Make.com** receives and routes the request.
**Google Calendar** handles consultation scheduling.
**Google Sheets** stores appointment and complaint records.
The core idea is simple: a caller speaks, the system identifies the purpose of the conversation, and the workflow takes the next action.
That is the practical value of the automation: **less manual copying, clearer records and a workflow that can grow with the business.**
## Source and Scope
This article is based on the supplied THE ARZENS workflow screenshots and the supplied Galvan AI project article. The architecture and workflow descriptions follow those materials. Details that are not visible in the supplied screenshots are presented as recommendations rather than confirmed implementation facts.
**THE ARZENS:** https://www.thearzens.tech/
**Galvan AI:** https://galvanai.com/
### Article Images
- **Figure 1 — Simplified architecture:**  
  https://github.com/zuhairfan99-ship-it/Galvan_Ai_Internship/blob/main/Article%203/image1.jpg
- **Figure 2 — Vapi voice-agent configuration:**  
  https://github.com/zuhairfan99-ship-it/Galvan_Ai_Internship/blob/main/Article%203/image%202.jpg
- **Figure 3 — Make.com automation workflow:**  
  https://github.com/zuhairfan99-ship-it/Galvan_Ai_Internship/blob/main/Article%203/image%203.jpg
