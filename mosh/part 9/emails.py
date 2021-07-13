from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl

message = MIMEMultipart()

message['from'] = 'Saif Newaz'

message['to'] = 'thesaiff@gmail.com'

message['subject'] = 'Testing python'

message.attach(MIMEText('Body'))

context = ssl.create_default_context()

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login('amaazingclips@gmail.com', 'balsal12')
    smtp.send(message)
    print('Sent...')
