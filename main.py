import streamlit as st
import requests
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

# ENV VARS
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
LinkdIn = "https://www.linkedin.com/in/vaishnav-agarwal-9498542b0/"
Name_Sender = "Vaishnav Agarwal"
def generate_message(name, interest, region):
    prompt = (
        f"Write a short, personalized outreach message to {name}, who is interested in {interest} and lives in {region}. "
        f"Tell them you're Vaishnav Agarwal and invite them to connect on LinkedIn here: https://www.linkedin.com/in/vaishnav-agarwal-9498542b0/. "
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

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return f"⚠️ Error from OpenRouter: {result.get('error', 'Unknown error')}"


def send_email(to_email, message):
    msg = MIMEText(message)
    msg["Subject"] = "Personalized Message from Outreach Assistant"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())

st.title("AI Outreach Assistant ")
name = st.text_input("Name")
interest = st.text_input("Interest")
region = st.text_input("Region")
email = st.text_input("Recipient Email")
if st.button("Generate & Send Email"):
    if name and interest and region and email:
        with st.spinner("Generating message..."):
            message = generate_message(name, interest, region)
            send_email(email, message)
            st.success(f"Email sent to {email} ")
    else:
        st.error("Please fill in all fields.")
