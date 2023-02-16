import os
import core
import pathlib
import time
from webbrowser import open
from pyautogui import click, hotkey, locateOnScreen, moveTo, press, size, typewrite, write
from platform import system

def _web(receiver: str) -> None:
    """Opens WhatsApp Web based on the Receiver"""
    if core.check_number(number=receiver):
        open(f"https://web.whatsapp.com/send?phone={receiver}")
            # + "&text="
            # + quote(message)
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)
    

def copy_image(path: str) -> None:
    """Copy the Image to Clipboard based on the Platform"""

    _system = system().lower()
    if _system == "linux":
        if pathlib.Path(path).suffix in (".PNG", ".png"):
            os.system(f"copyq copy image/png - < {path}")
        elif pathlib.Path(path).suffix in (".jpg", ".JPG", ".jpeg", ".JPEG"):
            os.system(f"copyq copy image/jpeg - < {path}")
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    elif _system == "windows":
        from io import BytesIO

        import win32clipboard  # pip install pywin32
        from PIL import Image

        image = Image.open(path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
    elif _system == "darwin":
        if pathlib.Path(path).suffix in (".jpg", ".jpeg", ".JPG", ".JPEG"):
            os.system(
                f"osascript -e 'set the clipboard to (read (POSIX file \"{path}\") as JPEG picture)'"
            )
        else:
            raise Exception(
                f"File Format {pathlib.Path(path).suffix} is not Supported!"
            )
    else:
        raise Exception(f"Unsupported System: {_system}")


def find_message_box(message:str):
    for char in message:
        if len(char) > 20:
            write(char)
        else:
            if char == "\n":
                hotkey("shift", "enter")
            else:
                typewrite(char)
    time.sleep(2)
    press("enter")


path= "./images"

messages = ["Hello There", "My name is Francis"]
# messages=["Hello", "My name is Francis. \nI\'m a software developer and an academic tutor. \nIf you feel you need help with your projects,  assignments, quizzes or classes, please don\'t hesitate to reach out.\nFeel free to check my profile and recent projects https://github.com/Ndaruga \nThank you!"]

def send_image(img_path: str) -> None:
    for img in os.listdir(img_path):
        copy_image(path=img)
        if system().lower() == "darwin":
            hotkey("command", "v")
        else:
            hotkey("ctrl", "v")
        time.sleep(1)
        press("enter")


def send_messages(receiver: str, wait_time: int) -> None:
    """Parses and Sends the Message"""
    _web(receiver=receiver)
    time.sleep(15)
    for i in messages:
        find_message_box(i)
    send_image(path)
    

send_messages("+254784116116", 20)