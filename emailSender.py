

from email.message import EmailMessage
import ssl
import smtplib

email_sender = ''  # Here insert your email
email_password = ''  # Here insert your app password
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
