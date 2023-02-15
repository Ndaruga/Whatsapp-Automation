import core
import time
import pyautogui


def _web(receiver: str, message: str) -> None:
    """Opens WhatsApp Web based on the Receiver"""
    if core.check_number(number=receiver):
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
        )
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)
    



messages=["Hello", "My name is Francis. \nI\'m a software developer and an academic tutor. \nIf you feel you need help with your projects,  assignments, quizzes or classes, please don\'t hesitate to reach out.\nFeel free to check my profile and recent projects https://github.com/Ndaruga \nThank you!"]

def send_messages(messages, receiver: str, wait_time: int) -> None:
    """Parses and Sends the Message"""
    _web(receiver=receiver, message=i)
    for i in messages:
        time.sleep(wait_time - 7)
        if not core.check_number(number=receiver):
            for char in messages:
                if char == "\n":
                    pyautogui.hotkey("shift", "enter")
                else:
                    pyautogui.typewrite(char)
        time.sleep(10)
        pyautogui.press("enter")
        # click(WIDTH / 2, HEIGHT / 2 + 15)


    # findtextbox()
    pyautogui.press("enter")

send_messages(messages, "+254784116116", 20)