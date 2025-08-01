import streamlit as st
import requests
import smtplib
from email.mime.text import MIMEText

OPENROUTER_API_KEY = st.secrets["apiKey"]
EMAIL_ADDRESS = st.secrets["email"]
EMAIL_PASSWORD = st.secrets["password"]
LINKEDIN = "https://www.linkedin.com/in/vaishnav-agarwal-9498542b0/"

def generate_message(name, interest, region):
    prompt = (
        f"Write a short, personalized outreach message to {name}, who is interested in {interest} and lives in {region}. "
        f"Tell them you're Vaishnav Agarwal and invite them to connect on LinkedIn here: {LINKEDIN}. "
        "Keep it under 40 words and make it sound friendly and real. Don't fake any info. "
        "Mention exploring collaboration in the future."
    )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        result = response.json()
        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            st.error(f" OpenRouter Error: {result.get('error', 'Unknown error')}")
            return "⚠ AI failed to generate a response. Please check your API key or prompt."
    except Exception as e:
        st.error(f" Exception occurred: {e}")
        return " Unexpected error occurred during API call."

def send_email(to_email, message):
    msg = MIMEText(message)
    msg["Subject"] = "Personalized Message from Outreach Assistant"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
    except smtplib.SMTPResponseException as e:
        st.error(f" Email send failed: {e.smtp_code} - {e.smtp_error.decode()}")
st.title("AI Outreach Assistant")

name = st.text_input("Name")
interest = st.text_input("Interest")
region = st.text_input("Region")
email = st.text_input("Recipient Email")

if st.button("Generate & Send Email"):
    if name and interest and region and email:
        with st.spinner("Generating message..."):
            message = generate_message(name, interest, region)
            st.text_area("Generated Message", message, height=100)
            send_email(email, message)
            st.success(f" Email sent to {email}")
    else:
        st.warning(" Please fill in all fields.")
