import os
import core
import pathlib
import time
from webbrowser import open
from pyautogui import click, hotkey, press, size, typewrite, write
from platform import system

WIDTH, HEIGHT = size()

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
    write(message)
    time.sleep(.75)
    press("enter")
    time.sleep(1.25)

# img_dir = os.path.join(os.path.dirname(__file__), "images")
img_dir = "./images/"


# messages1=["Hello", "My name is Francis. \nI\'m a software developer and an academic tutor. \nIf you feel you need help with your projects,  assignments, quizzes or classes, please don\'t hesitate to reach out.\nFeel free to check my profile and recent projects https://github.com/Ndarugaa \nThank you!"]
messages1=["Hello", "My name is Francis. I'm a skilled tutor who can complete your work to your satisfaction. If you need extra help, either for lessons, assignments, projects, quizzes or brushing up before finals, I'm here to help. Available 24/7, I'm not limited to niche, I cover a wide range of topics across many disciplines."]
messages2=["Above are grades for students I have helped","Hit me up for such grades at affordable rates"]

def send_image(path: str) -> None:
    time.sleep(1)
    click(WIDTH / 2, HEIGHT / 2 + 15)
    time.sleep(1)
    copy_image(path=path)
    if system().lower() == "darwin":
        hotkey("command", "v")
    else:
        hotkey("ctrl", "v")
    press("enter")

def image_send():
    for imgs in os.listdir(img_dir):
        send_image(os.path.join(img_dir, imgs))

def send_messages(receiver: str) -> None:
    """Parses and Sends the Message"""
    _web(receiver=receiver)
    time.sleep(15)
    for i in messages1:
        find_message_box(i)
    image_send()
    time.sleep(2)
    for i in messages2:
        find_message_box(i)

    

send_messages("+254784116116")


