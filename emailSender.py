# import smtplib

# # Set up the SMTP server
# smtp_server = 'smtp.gmail.com'  # replace with your email provider's SMTP server
# smtp_port = 587  # replace with your email provider's SMTP port
# smtp_username = 'your_email@gmail.com'  # replace with your email address
# smtp_password = 'your_password'  # replace with your email password
# sender_email = 'your_email@gmail.com'  # replace with your email address

# # Set up the email message
# receiver_email = 'recipient_email@example.com'  # replace with the recipient email address
# subject = 'Subject line of the email'
# body = 'Body of the email'

# message = f'Subject: {subject}\n\n{body}'

# # Send the email message
# try:
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()
#     server.login(smtp_username, smtp_password)
#     server.sendmail(sender_email, receiver_email, message)
#     print('Email sent successfully!')
# except Exception as e:
#     print(f'Error sending email: {str(e)}')
# finally:
#     server.quit()


from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'alejoepico@gmail.com'
email_password = "mrrmfsqklcdmjsdf"
email_receiver = 'pmuw76d@femailtor.com'

subject = 'Please play videogames'
body = """
Steam is the best platform for purchase videogames!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
