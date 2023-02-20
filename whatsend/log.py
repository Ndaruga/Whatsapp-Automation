# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 20:20:54 2023

@author: User
"""

import os
import time
import whatsend.core as core


def log_message(_time: time.struct_time, receiver: str) -> None:
    """Logs the Message Information after it is Sent"""

    if not os.path.exists("Success_log.txt"):
        file = open("Success_log.txt", "w+")
        file.close()


    with open("Success_log.txt", "a", encoding="utf-8") as file:
        if core.check_number(receiver):
            file.write(
                f"Date: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nTime: {_time.tm_hour}:{_time.tm_min}\n"
                f"Phone Number: {receiver}"
            )
        else:
            file.write(
                f"Date: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nTime: {_time.tm_hour}:{_time.tm_min}\n"
                f"Group ID: {receiver}"
            )
        file.write("\n--------------------\n")
        file.close()


def log_image(_time: time.struct_time, path: str, receiver: str, caption: str) -> None:
    """Logs the Image Information after it is Sent"""

    if not os.path.exists("Success_log.txt"):
        file = open("Success_log.txt", "w+")
        file.close()


    with open("Success_log.txt", "a", encoding="utf-8") as file:
        if core.check_number(number=receiver):
            file.write(
                f"Date: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nTime: {_time.tm_hour}:{_time.tm_min}\n"
                f"Phone Number: {receiver}\nImage: {path}"
            )

        else:
            file.write(
                f"Date: {_time.tm_mday}/{_time.tm_mon}/{_time.tm_year}\nTime: {_time.tm_hour}:{_time.tm_min}\n"
                f"Group ID: {receiver}\nImage: {path}"
            )
        file.write("\n--------------------\n")
        file.close()