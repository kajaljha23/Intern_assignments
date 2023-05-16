import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pydantic import BaseModel


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str


def sending_email(body, email: Email):
    sender_email = os.environ.get("sender_email1")
    sender_password = os.environ.get("sender_password1s")
    receiver_email = email.rec_email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "total price of inventory things"

    message.attach(MIMEText(str(body), "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        return {"message": "Email sent successfully"}
    except Exception as e:

        return {"message": str(e)}
