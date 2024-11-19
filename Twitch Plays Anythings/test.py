import tkinter as tk
from PIL import ImageTk, Image
root = tk.Tk()
root.geometry("720x500")
root.title("Display Images using Grid Function")
image1 = Image.open(r"logo-twitch.png")
image1 = image1.resize((150, 150))
image1 = ImageTk.PhotoImage(image1)

image2 = Image.open(r"twitch-plays-anything.png")
image2 = image2.resize((1000, 150))
image2 = ImageTk.PhotoImage(image2)

label1 = tk.Label(image=image1)
label2 = tk.Label(image=image2)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1,)
root.mainloop()