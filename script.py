import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 



def send_mail(workflow_name, repo_name, workflow_id):
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv("RECEIVER_EMAIL")

    
    if not all([sender_email, sender_password, receiver_email]):
        print("Missing email credentials or recipient address.")
        return

    ##Email Message
    subject = f"Workflow {workflow_name} failed for the repo {repo_name}"
    body = (
        f"Hi,\n\n"
        f"The workflow '{workflow_name}' failed for the repo '{repo_name}'. Please check the logs for more details.\n"
        f"More Details:\nRun ID: {workflow_id}"
    )


    msg = MIMEMultipart()
    msg['From'] = sender_email
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

    
