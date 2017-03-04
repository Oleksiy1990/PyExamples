import smtplib
import sys

#this email library parses messages 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


gmail_user = 'oleksiy1990geeky@gmail.com'  
gmail_password = '03011990*'

to = 'oleksiy1990@gmail.com'




msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = to
msg['Subject'] = 'Automatic email subject'

msg_text = MIMEText("Here's some text in the automatic e-mail")
#msg.attach(MIMEText(open("test.txt").read()))
msg.attach(msg_text)

#filetoadd = "test.txt"
#f = open(filetoadd)
#attachment = MIMEText(f.read())
#f.close()
#attachment.add_header('Content-Disposition', 'attachment', filename=filetoadd)           
#msg.attach(attachment)

filename = "sidewaysMOT.jpg"
attachment = open(filename, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)


try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, msg.as_string())
    server.close()
except:  
    print('Something went wrong...')
