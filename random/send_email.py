#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import argparse
import os
import smtplib
import sys
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailMessage(object):
    def __init__(self, title, to_addrs, from_addr):
        msg = MIMEMultipart('alternative')
        msg.set_charset('utf-8')
        msg['Subject'] = title
        msg['From'] = from_addr
        msg['To'] = ', '.join(to_addrs)
        self.to_addrs = to_addrs
        self.from_addr = from_addr
        self.msg = msg

    def get(self):
        return self.msg

    def as_string(self):
        return self.msg.as_string()

    def add_plain_text(self, content):
        text = MIMEText(content, 'plain', 'utf-8')
        self.msg.attach(text)

    def add_html_text(self, content):
        text = MIMEText(content, 'html', 'utf-8')
        self.msg.attach(text)

    def add_attachment(self, file_path, file_name):
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file_path).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % (os.path.basename(file_name)))
        self.msg.attach(part)


def send_email(user, passwd, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(user, passwd)
    server.sendmail(msg.from_addr, msg.to_addrs, msg.as_string())
    server.quit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', action='store')
    parser.add_argument('--title', action='store')
    parser.add_argument('--text', action='store')
    parser.add_argument('--receivers', action='store')
    parser.add_argument('--user', action='store')
    parser.add_argument('--passwd', action='store')
    args = parser.parse_args()

    receivers = args.receivers.split(',')
    files = []
    if args.files:
        files = args.files.split(',')
    msg = EmailMessage(args.title, receivers, args.user)
    text = args.text
    if args.text is None:
        text = sys.stdin.read()
    msg.add_plain_text(text)
    for f in files:
        msg.add_attachment(f, f)
    send_email(user=args.user, passwd=args.passwd, msg=msg)


if __name__ == '__main__':
    main()
