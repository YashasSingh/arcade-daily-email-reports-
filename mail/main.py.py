import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email_report(subject, body, to_emails, attachment_path=None):
    # Email configuration
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    from_email = os.getenv('FROM_EMAIL')
    from_password = os.getenv('FROM_PASSWORD')
    
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
    
    # Connect to the server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_emails, msg.as_string())
        server.close()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Example usage
    subject = "Daily Report"
    body = "This is your daily report."
    to_emails = ["recipient1@example.com", "recipient2@example.com"]
    attachment_path = "path/to/your/report.pdf"  # If no attachment, set to None

    send_email_report(subject, body, to_emails, attachment_path)
