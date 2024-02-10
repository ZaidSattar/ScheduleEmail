import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime

# Email details
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@example.com"
password = "your_password"

# SMTP server configuration
smtp_server = "smtp.gmail.com"
port = 587  # For starttls

# Email content
subject = "Scheduled Email"
body = "This is an automated email sent by Python."

# Create a secure SMTP connection
def send_email():
    try:
        # Create email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

# Schedule the email
target_time = "18:00"  # 24-hour format, HH:MM
while True:
    current_time = datetime.now().strftime("%H:%M")
    if current_time == target_time:
        send_email()
        print(f"Email sent at {current_time}")
        break
    else:
        time.sleep(60)  # Check the time every minute
