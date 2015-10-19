#!/usr/bin/env python
import dwgconfig
import mailconfig
import smtplib
import shutil
from os import remove

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_sms(body, phone, subject_prefix, gw_port, filename):
    try:
        msg = MIMEMultipart()
        msg['From'] = mailconfig.from_addr
        msg['To'] = mailconfig.to_addrs
        if phone == None:
            msg['Subject'] = subject_prefix + '   (' + gw_port + ')'
        else:
            msg['Subject'] = subject_prefix + '\t' + phone + '   (' + gw_port + ')'

        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()

        username = mailconfig.username
        password = mailconfig.password
        server = smtplib.SMTP(mailconfig.server)
        server.starttls()
        #server.set_debuglevel(1)
        server.login(username, password)
        server.sendmail(mailconfig.from_addr, mailconfig.to_addrs, text)
        server.quit()
        txt.close()
        shutil.copy(filename, mailconfig.archive)
        remove(filename)

    except Exception:
        print "Error: unable to send email"


# convert sms file to phone and sms message
def create_msg(text):
    res = text.split("\n\n")
    phone = None
    gw_port = None
    for _h in res[0].split("\n"):
        if _h.lower().startswith('number:'):
            phone = _h.split()[1]
        if _h.lower().startswith('port:'):
            gw_port = mailconfig.gw[int(_h.split()[1])]

    return res[1], phone, gw_port


# list sms files
import glob

for filename in glob.glob(dwgconfig.income_path + '*'):
    subject_prefix = "SMS"
    txt = open(filename)
    body, phone, gw_port = create_msg(txt.read())
    send_sms(body, phone, subject_prefix, gw_port, filename)


for filename in glob.glob(dwgconfig.ussd_income_path + '*'):
    subject_prefix = "USSD"
    txt = open(filename)
    body, phone, gw_port = create_msg(txt.read())
    send_sms(body, phone, subject_prefix, gw_port, filename)

