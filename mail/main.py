import os
from transformers import pipeline
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import logging
from dotenv import load_dotenv
import time

# Load environment variables from a .env file
load_dotenv()

# Configure logging
logging.basicConfig(filename='email_log.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def read_report_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def load_summarization_model():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer

def condense_report(content):
    summarizer = load_summarization_model()
    summary = summarizer(content, max_length=150, min_length=40, do_sample=False)
    return summary[0]['summary_text']

def send_email_report(subject, body, to_emails, attachments=None, retries=3):
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
    
    # Attach the body with the msg instance (HTML and plain text)
    msg.attach(MIMEText(body, 'html'))
    
    # Attach any files if provided
    if attachments:
        for attachment_path in attachments:
            try:
                filename = os.path.basename(attachment_path)
                with open(attachment_path, 'rb') as attachment_file:
                    attachment = MIMEApplication(attachment_file.read(), _subtype="octet-stream")
                attachment.add_header('Content-Disposition', 'attachment', filename=filename)
                msg.attach(attachment)
            except Exception as e:
                logging.error(f"Failed to attach file {attachment_path}: {e}")

    # Connect to the server and send the email with retries
    for attempt in range(retries):
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(from_email, from_password)
            server.sendmail(from_email, to_emails, msg.as_string())
            server.close()
            logging.info("Email sent successfully")
            print("Email sent successfully")
            break
        except Exception as e:
            logging.error(f"Failed to send email on attempt {attempt + 1}: {e}")
            print(f"Failed to send email on attempt {attempt + 1}: {e}")
            if attempt < retries - 1:
                time.sleep(5)  # Wait before retrying
    else:
        logging.error("Failed to send email after multiple attempts")
        print("Failed to send email after multiple attempts")

if __name__ == "__main__":
    # Example usage
    subject = "Daily Report"
    raw_content = read_report_content("report.txt")
    condensed_content = condense_report(raw_content)
    
    body = f"""
    <html>
    <body>
        <h1>Daily Report</h1>
        <p>{condensed_content}</p>
    </body>
    </html>
    """
    to_emails = ["recipient1@example.com", "recipient2@example.com"]
    attachments = ["path/to/your/report1.pdf", "path/to/your/report2.xlsx"]  # List of attachment paths

    send_email_report(subject, body, to_emails, attachments)
