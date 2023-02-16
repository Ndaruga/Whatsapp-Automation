import core
import time
import pyautogui
import webbrowser as wb


def _web(receiver: str) -> None:
    """Opens WhatsApp Web based on the Receiver"""
    if core.check_number(number=receiver):
        wb.open(f"https://web.whatsapp.com/send?phone={receiver}")
            # + "&text="
            # + quote(message)
    else:
        open("https://web.whatsapp.com/accept?code=" + receiver)
    
def find_message_box(message:str):
    for char in message:
        if char == "\n":
            pyautogui.hotkey("shift", "enter")
        else:
            pyautogui.typewrite(char)
    # pyautogui.write(message)
    

msg="Dummy texy\nuifdhufs"
# messages=["Hello", "My name is Francis. \nI\'m a software developer and an academic tutor. \nIf you feel you need help with your projects,  assignments, quizzes or classes, please don\'t hesitate to reach out.\nFeel free to check my profile and recent projects https://github.com/Ndaruga \nThank you!"]

def send_messages(messages, receiver: str, wait_time: int) -> None:
    """Parses and Sends the Message"""
    _web(receiver=receiver)
    time.sleep(8)
    find_message_box(messages)
    # time.sleep(wait_time - 7)
                
    time.sleep(2)
    pyautogui.press("enter")
        # click(WIDTH / 2, HEIGHT / 2 + 15)


    # findtextbox()
    pyautogui.press("enter")

send_messages(msg, "+254784116116", 20)