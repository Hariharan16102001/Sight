import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "anupamahari1610@gmail.com"
sender_password = "rlqy mmdp cfic jdci"
receiver_email = "misowmya32@gmail.com"

def new_email():
    subject = "dummy mail"
    body = "Hi I am hari."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Email not sent. Error: {str(e)}")


new_email()
