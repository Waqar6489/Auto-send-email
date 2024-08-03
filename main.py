import smtplib
# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'mzaqa1559@gmail.com'
password = 'Your password'  # Replace with the app password
subject = "Love Python"
body = "Python is a programming language, easy to use, higher programming language"
message = f"Subject: {subject}\n\n{body}"
recipients = ['waqarali6489@gmail.com', 'tahashaid8@gmail.com']

try:
    # Establish a connection to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()  # Can be omitted
        server.starttls()
        server.ehlo()  # Reconfirm connection
        server.login(sender_email, password)
        server.sendmail(sender_email, recipients, message)
        print("Mail sent successfully")
except Exception as e:
    print(f"Failed to send email: {e}")


