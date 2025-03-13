import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


# use python script to login into your email account and use smt protocol to send email

server = smtplib.SMTP('smtp.gmail.com', 25)

# start server
server.ehlo()

# login into account
# going to implement a way to encrypt and decrypt password
# decrpytion will likely be done outside the repo
# server.login('houtan.ghaebi@gmail.com', 'password')

with open('password.txt', 'r') as f:
    password = f.read()

server.login('email.com', password)

# creating the mail message

msg = MIMEMultipart()
msg['From'] = 'Houtan Ghaebi'
msg['To'] = 'testmail.com"
msg['Subject'] = 'Just a test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain')) # attach as plain text

# attach an image
filename = 'image.jpg'
attachment = open(filename, 'rb') # reading binary

p = MIMEBase('application', 'octet-stream') # stream we are going to use to process image data
p.set_payload(attachment.read()) # read the image data
encoders.encode_base64(p) # encode the data
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('email.com', 'testmail.com', text)

