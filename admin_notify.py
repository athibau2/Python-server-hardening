#!usr/bin/python3

import smtplib
from email.mime.text import MIMEText

# connect with Google's servers
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# use username or email to log in
username = 'a.tihbs98@gmail.com'
password = 'workcrew15'

from_addr = 'a.thibs98@gmail.com'
to_addrs = ['a.thibs98@gmail.com']

# the email lib has a lot of templates
# for different message formats,
# on our case we will use MIMEText
# to send only text
message = MIMEText('An unauthorized IP address has attempted to access the admin page and has been banned.')
message['subject'] = 'Admin Jail Activity Notification'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)

# we'll connect using SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# to interact with the server, first we log in
# and then we send the message
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()