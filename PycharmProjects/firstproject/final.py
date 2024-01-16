import smtplib
import time
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

sender_email = "anupamahari1610@gmail.com"
sender_password = "rlqy mmdp cfic jdci"
receiver_email = "vsampathkumar376@gmail.com"

def new_email():
    subject = "Dummy Mail"
    body = "Hi, I am Hari."
    signature = "Thanks & Regards\nHariharan M\nTrainee"

    message = MIMEText(f"{body}\n\n{signature}")

    with open(r"C:\Users\SightSpectrum\Desktop\hello\gifsight.gif", "rb") as image_file:
        image = MIMEImage(image_file.read(), name="my_image.gif")


    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(message)
    msg.attach(image)

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

