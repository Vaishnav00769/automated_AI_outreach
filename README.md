# AI Outreach Assistant

This project is a simple and effective AI-powered tool for sending personalized outreach messages via email. It uses Streamlit for the user interface, OpenRouter's LLM API to generate custom messages, and Gmail SMTP for email delivery.

## Objective

This project was developed as part of an AI Agent Developer Assignment. The goal is to assist a small team in generating and sending customized messages based on a recipient’s name, interest, region, and email.

## Live App

You can access the deployed application here:  
https://vaishnav-agarwal-ai-outreach.streamlit.app/

## GitHub Repository

Source code is available at:  
https://github.com/Vaishnav00769/automated_AI_outreach/tree/main

## How It Works

### User Inputs

- Name: Recipient's name
- Interest: Area of interest (e.g., AI, Robotics)
- Region: Recipient’s location
- Email: Email address of the recipient

### Workflow

1. The user accesses the Streamlit web app.
2. Inputs including name, interest, region, and email are submitted through the form.
3. A prompt is generated using these inputs, along with my name and LinkedIn profile.
4. The prompt is sent to the OpenRouter API (Mixtral model) for message generation.
5. The message is emailed to the recipient using Gmail’s SMTP service.
6. A success message is displayed on the interface.

## Tools and Technologies Used

- **Streamlit**: For the web frontend
- **Python**: Backend logic
- **OpenRouter API**: For generating AI-based messages
- **SMTP (Gmail)**: For sending emails
- **dotenv / secrets.toml**: For securely handling credentials

## Sample Prompt

```
Write a short, personalized outreach message to Raj, who is interested in AI and robotics and lives in Bangalore. 
Tell them you're Vaishnav Agarwal and invite them to connect on LinkedIn here: https://www.linkedin.com/in/vaishnav-agarwal-9498542b0/. 
Keep it under 40 words and make it sound friendly and real. Don't fake any info. Mention exploring collaboration in the future.
```

### Example Output

```
Hi Raj! Great to connect with someone interested in AI and robotics. Let’s collaborate in the future. 
Connect with me on LinkedIn: https://www.linkedin.com/in/vaishnav-agarwal-9498542b0/
```

## Running the App Locally

1. Clone the repository

```bash
git clone https://github.com/Vaishnav00769/automated_AI_outreach.git
cd automated_AI_outreach
```

2. Set up environment variables

For Streamlit Cloud, use `.streamlit/secrets.toml`, or use a `.env` file locally with:

```toml
apiKey = "your_openrouter_api_key"
email = "your_email@gmail.com"
password = "your_email_password_or_app_password"
```

3. Run the Streamlit application

```bash
streamlit run outreach_app.py
```

## Optional Extension

You can use automation tools such as n8n to enhance the workflow by:

- Importing leads from Google Sheets
- Automatically generating and sending emails
- Logging responses into a database or spreadsheet

This makes the tool scalable for larger outreach campaigns.

## Author

Vaishnav Agarwal  
Email: agarwalvaishnav007@gmail.com  
LinkedIn: https://www.linkedin.com/in/vaishnav-agarwal-9498542b0/