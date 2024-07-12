import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_report(subject, body, to_emails, attachment_path=None):
    # Email configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587
    from_email = 'your_email@example.com'
    from_password = 'your_password'  # Consider using environment variables for security
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject
    
    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach any file if provided
    if attachment_path:
        filename = os.path.basename(attachment_path)
        attachment = MIMEApplication(open(attachment_path, "rb").read(), _subtype="octet-stream")
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(attachment)