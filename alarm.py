import sys
import time
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
from pygame import mixer

root = Tk()
img = PhotoImage(file='icon2.png')
root.iconphoto(False, img)
root.title("Alarm Clock")

# Set the minimum window size to prevent it from being too small when resizing
root.minsize(541, 360)

# Create a canvas with a fixed size and anchor it to the top-left corner
canvas = Canvas(root, width=541, height=360)
canvas.pack()

# Load and display the image on the canvas
photo = ImageTk.PhotoImage(Image.open("alarm_clock.jpg"))
canvas.create_image(0, 0, anchor=NW, image=photo)

# Add a text in Canvas
canvas.create_text(170, 130, text="Set Time (HH:MM:SS)", fill="black", font='Helvetica 15 bold')
canvas.create_text(280, 50, text="Python Alarm Clock", fill="black", font='Helvetica 20 bold')

# Create frames for organizing widgets
header = Frame(root)
box1 = Frame(root)
box2 = Frame(root)

# Place the frames using the 'place' method with fixed coordinates
header.place(x=0, y=0)
box1.place(x=120, y=150)
box2.place(x=120, y=200)

# Time taken user by Input
user_input = Entry(box1, font=('Arial Narrow', 20), width=8)
user_input.grid(row=0, column=2)


def alarm_fn():
    alarm_time = user_input.get()
    if alarm_time == "":
        messagebox.askretrycancel("Error Message", "Please Enter Value")
    else:
        messagebox.showinfo("Message", "Alarm has been set!!")
        while True:
            time.sleep(1)
            if alarm_time == time.strftime("%H:%M:%S"):

                playmusic()


def playmusic():
    mixer.init()
    mixer.music.load('alarm_sound.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(15)
        mixer.stop()
        sys.exit()


# Set Alarm button
start_button = Button(box2, text="Set Alarm", font=('Arial Narrow', 16, 'bold'), command=alarm_fn)
start_button.grid(row=4, column=2)

root.mainloop()
