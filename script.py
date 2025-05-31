import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 


def send_mail(Workflow_name, repo_name,Workflow_id):
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv("RECEIVER_EMAIL")

    ##Email Message
    subject = f"Workflow {Workflow_name} failed for the repo {repo_name}"
    body = f"Hi, \nthe workflow {Workflow_name} failed for the repo {repo_name}. please check the logs for more details. \nMoreDetails: \nRun_ID:{Workflow_id}"

    msg = MIMEMultipart()
    msg['From'] = send_mail
    msg['To']   = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))


    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email,receiver_email, text)
        server.quit()

        print("Email sent Successfully.")
    except Exception as e:
        print(f'Error: {e}')

send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))

    
