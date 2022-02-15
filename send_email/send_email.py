import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(email_to, subject ,message):
    #create email
    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = subject
    multipart_message["From"] = os.environ.get('LOGIN')
    multipart_message["To"] = email_to
    multipart_message.attach(MIMEText(message, "html"))
    
    #connexion open
    server_mail = smtplib.SMTP(os.environ.get('SERVER_SMTP'), os.environ.get('SERVER_PORT'))
    server_mail.starttls()
    # login 
    server_mail.login(os.environ.get('LOGIN'), os.environ.get('pwd'))
    # send mail
    server_mail.sendmail(os.environ.get('LOGIN'), email_to, multipart_message.as_string())
    
    # close connexion
    server_mail.quit()
    


message_email = """
<h1>Hello</h1>

    <p>That works</p>

<h2>Great, See ya</h2>

"""

load_dotenv()
send_email(email_to=os.environ.get('MAIL_TO'), subject="Message From Python", message=message_email)