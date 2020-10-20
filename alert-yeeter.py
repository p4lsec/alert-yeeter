#!/usr/bin/python3

from email.message import EmailMessage
from lxml import html
from urllib.request import urlopen
import configparser
import hashlib
import os
import requests
import smtplib
import sys

def get_new(url):  # Generates a SHA256 hash of the targeted XPath
    source_code = html.fromstring(requests.get(url).content)
    tree = source_code.xpath(config['Site']['path'])
    new = hashlib.sha256(tree[0].text_content().encode('utf-8')).hexdigest()
    return new

def main(cf):  # Compares the old hash in your config to the new hash
    new = get_new(url)
    if old == new:
        sys.exit()
    else:
        alert(cf)
        overwrite(cf,new)

def overwrite(cf,new):  # Replaces the old hash with the new hash
    config.set('Results', 'value', new)
    with open(cf, 'w') as cf:
        config.write(cf)

def alert(cf):  # Sends an email alert
    msg = EmailMessage()
    msg.set_content(url)
    msg['From'] = config['Email']['from']
    msg['To'] = config['Email']['to']
    msg['Subject'] = config['Email']['subject']
    fromaddr = config['Email']['from']
    toaddrs = config['Email']['to']
    server = smtplib.SMTP(config['Email']['smtp_url'], config['Email']['smtp_port'])
    server.starttls()
    server = smtplib.SMTP_SSL(config['Email']['smtp_url'], config['Email']['smtp_ssl_port'])
    server.login(config['Email']['from'], config['Email']['auth'])
    server.send_message(msg)
    server.quit()

if __name__ == "__main__": 
    for cf in os.listdir():
        if '.ini' in cf and cf != 'alert-yeeter-template.ini':
            config = configparser.ConfigParser()
            config.read(cf)
            old = config['Results']['Value']
            url = config['Site']['URL']
            config.read(cf)
            main(cf)