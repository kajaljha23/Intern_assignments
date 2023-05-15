import smtplib
from pydantic import BaseModel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email(BaseModel):
    rec_email: str
    subject: str
    body: str


def send_email(email: Email):
    sender_email = "k.kajal1115@gmail.com"
    sender_password = "uvjrhssxhwrwrapo"
    receiver_email = email.rec_email

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email.subject

    message.attach(MIMEText(email.body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        server.send_message(message)

        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:

        return {"message": str(e)}
