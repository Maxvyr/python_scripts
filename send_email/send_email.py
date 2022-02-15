import os
import smtplib
import config_file
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email_to, subject ,message):
    #create email
    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = subject
    multipart_message["From"] = config_file.LOGIN
    multipart_message["To"] = email_to
    multipart_message.attach(MIMEText(message, "html"))
    
    #connexion open
    server_mail = smtplib.SMTP(config_file.SERVER_SMTP, config_file.SERVER_PORT)
    server_mail.starttls()
    # login 
    server_mail.login(config_file.LOGIN, config_file.PWD)
    # send mail
    server_mail.sendmail(config_file.LOGIN, email_to, multipart_message.as_string())
    
    # close connexion
    server_mail.quit()
    


message_email = """
<h1>Hello</h1>

    <p>That works</p>

<h2>Great, See ya</h2>

"""

send_email(email_to=config_file.MAIL_TO, subject="Message From Python", message=message_email)