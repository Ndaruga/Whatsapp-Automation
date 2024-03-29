import os
import pathlib
import time
from webbrowser import open
from pyautogui import hotkey, press, size, write
from platform import system

# WIDTH, HEIGHT = size()

def check_number(number: str) -> bool:
    """Checks the Number to see if contains the Country Code"""

    return "+" in number or "_" in number

def _web(receiver: str) -> None:
    """Opens WhatsApp Web based on the Receiver"""
    if check_number(number=receiver):
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
    write(message)
    time.sleep(1)
    press("enter")

# img_dir = os.path.join(os.path.dirname(__file__), "images")
img_dir = "./images/"

messages1=["Hello", "My name is Francis. I'm a software developer and an academic tutor. If you feel you need help with your projects, please don't hesitate to reach out. Feel free to check my profile and recent projects https://github.com/Ndarugaa "]
messages2=["Hit me up for such tasks at affordable rates"]

def send_image(path: str) -> None:
    time.sleep(1)
    # click(WIDTH / 2, HEIGHT / 2 + 15)
    copy_image(path=path)
    if system().lower() == "darwin":

        hotkey("command", "v")
    else:
        hotkey("ctrl", "v")
    press("enter")

def image_send():
    for imgs in os.listdir(img_dir):
        send_image(os.path.join(img_dir, imgs))
        time.sleep(0.5)
        press("enter")
        

def send_messages(receiver: str) -> None:
    """Parses and Sends the Message"""
    _web(receiver=receiver)
    time.sleep(15)
    for i in messages1:
        time.sleep(1)
        find_message_box(i)
    # image_send()
    # time.sleep(2)
    # for i in messages2:
    #     find_message_box(i)
    #     time.sleep(1)



