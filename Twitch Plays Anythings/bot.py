from pyautogui import *
from twitchio.ext import commands
import pyautogui
from pynput.keyboard import Key, Controller
import time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

keyboard = Controller()
class Bot(commands.Bot):

    def __init__(self):
        super().__init__() 
    async def event_ready(self):
        #Message pour savoir si le bot est connecté
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
    
    async def event_message(self, message):
        control=["z","q","s","d"]
        print(message.content.lower())
        # affiche message dans la console. 
        lowered_content = message.content.lower()
        for letter in lowered_content:
            if letter in control :
                print(1)
                temps = lowered_content
                temps = temps.join(x for x in control)
                temps = float(temps)
                if 1 <= (temps) <= 10:
                    keyboard.press('z')
                    time.sleep(int(temps))
                    keyboard.release('z')
                else:
                    keyboard.press('z')
                    time.sleep(1)
                    keyboard.release('z')
            if lowered_content == "q" :
                print(2)
                temps = lowered_content
                temps = temps.replace('q','')
                if 0.1 <= float(temps) <= 10.0:
                    keyboard.press('q')
                    time.sleep(int(temps))
                    keyboard.release('q')
                else:
                    keyboard.press('q')
                    time.sleep(1)
                    keyboard.release('q')
            if lowered_content == "s" :
                print(3)
                temps = lowered_content
                temps = temps.replace('s','')
                if 0.1 <= float(temps) <= 10.0:
                    keyboard.press('s')
                    time.sleep(int(temps))
                    keyboard.release('s')
                else:
                    keyboard.press('s')
                    time.sleep(1)
                    keyboard.release('s')
            if lowered_content == "d" :
                print(4)
                temps = lowered_content
                temps = temps.replace('d','')
                if 0.1 <= float(temps) <= 10.0:
                    keyboard.press('d')
                    time.sleep(int(temps))
                    keyboard.release('d')
                else:
                    keyboard.press('d')
                    time.sleep(1)
                    keyboard.release('d')
            else:
                return

window = tk.Tk()
window.title("Twitch Plays Anythings")
window.geometry("1920x1080")
window.iconbitmap("logo-twitch.png")
img = ImageTk.PhotoImage(Image.open("twitch-plays-anything.png"))
panel = Label(window, image=img)
hello= tk.Label(window, text="Bienvenue sur Twitch Plays Anythings !",
bg="#6441a5",
fg="#ffffff",
font=("Arial",36),
width= 500,
height= 100,
)
panel.pack(side="top", fill="both",expand="yes")
panel.pack()
hello.pack()
mainloop()


bot = Bot()
bot.run()
