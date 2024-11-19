from pynput.keyboard import Key, Controller
import  time

keyboard = Controller()

msg=input('Met un message avec une valeur derrière')

if msg == "z":
    msg = msg.replace('z ','')
    msg = float(msg)
    if 0.1 <= msg <= 10.0:
        keyboard.press("z")
        time.sleep(msg)
        keyboard.release("z")
    else :
        keyboard.press("z")
        time.sleep(1)
        keyboard.release("z")