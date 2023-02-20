# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:20:25 2023

@author: Francis
"""


import pandas as pd
import re
import os
import whatsend._core as _core
import whatsend.core as core
import whatsend.cleaner as cleaner

Clients=pd.read_table(os.path.join("Numbers", "clients.txt"), header=0)

Clients=Clients.values.tolist()



PhoneNumbers=[]
for i in Clients:
    string = re.sub('[\W\_]','',str(i))
    no = '+'+str(string)
    PhoneNumbers.append(no)

import time
import webbrowser as web
from datetime import datetime
from re import fullmatch
import whatsend.log as log, whatsend.exceptions as exceptions, whatsend.core as core
import pyautogui as pg


pg.FAILSAFE = False

_core.check_connection()

def open_web() -> bool:
    """Opens WhatsApp Web"""

    try:
        web.open("https://web.whatsapp.com")
    except web.Error:
        return False
    else:
        return True



def sendwhatmsg(
        phone_no: str,
        time_hour: int,
        time_min: int,
        wait_time: int = 2,
        tab_close: bool = True,
        close_time: int = 15,
) -> None:
    """Send a WhatsApp Message at a Certain Time"""
    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    phone_no = phone_no.replace(" ", "")
    if not fullmatch(r'^\+?[0-9]{2,4}\s?[0-9]{9,15}', phone_no):
        raise exceptions.InvalidPhoneNumber("Invalid Phone Number.")

    if time_hour not in range(25) or time_min not in range(60):
        raise Warning("Invalid Time Format!")

    current_time = time.localtime()
    left_time = datetime.strptime(
        f"{time_hour}:{time_min}:0", "%H:%M:%S"
    ) - datetime.strptime(
        f"{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}",
        "%H:%M:%S",
    )

    if left_time.seconds < wait_time:
        raise exceptions.CallTimeException(
            "Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!"
        )

    sleep_time = left_time.seconds - wait_time
    print(
        f"In {sleep_time} Seconds WhatsApp will open and Message will be Delivered to {phone_no}!"
    )
    
    core.send_messages(receiver=phone_no)
    log.log_message(_time=current_time, receiver=phone_no)

    if tab_close:
        _core.close_tab(wait_time=2)


def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if str(string_to_search) in line:
                return True
    return False


No = ["+254113927737", "+254784116116",  "+254113927737",  "+254799844628"]

for i in No:
    if check_if_string_in_file('Success_log.txt', i) == True:
#         print(f'{i} already Exists in Database')
        pass
    elif check_if_string_in_file('Numbers/Employers.txt', i) == True:
#         print(f'{i} is an employer')
        pass
    else:            
        tim=datetime.now()
        sendwhatmsg(i, time_hour=tim.hour, time_min=tim.minute+1)
        # try:
        #     sendwhatmsg(i, time_hour=tim.hour, time_min=tim.minute+1)
        # except:
        #     print(f'Failed to send message to {i}')


