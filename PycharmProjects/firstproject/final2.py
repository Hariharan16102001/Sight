import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "anupamahari1610@gmail.com"
sender_password = "rlqy mmdp cfic jdci"
receiver_email = "misowmya32@gmail.com"

def new_email():
    subject = "Dummy Mail"
    body = "Hi, I am Hari."
    signature = "Thanks & Regards\nHariharan M\nTrainee"

    message = MIMEText(f"{body}\n\n{signature}")

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(message)

    # Attach the GIF as a file attachment
    gif_path = r"C:\Users\SightSpectrum\Desktop\hello\gifsight.gif"
    with open(gif_path, "rb") as gif_file:
        gif_attachment = MIMEBase("application", "octet-stream")
        gif_attachment.set_payload(gif_file.read())
        encoders.encode_base64(gif_attachment)
        gif_attachment.add_header("Content-Disposition", 'attachment; filename="gifsight.gif"')
        msg.attach(gif_attachment)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Email not sent. Error: {str(e)}")

while True:
    new_email()
    time.sleep(1800)
