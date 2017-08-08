import time
import sys
from PIL import Image, ImageTk
from tkinter import Tk, Canvas 

root = Tk()
root.geometry('128x128')
canvas = Canvas(root,width=128,height=128)
canvas.pack()
root.mainloop()

def create_animation(filename_base, count, sleep_time = 1):
        global canvas
        for i in  range(0,count):
                name = '%05d' % i
                name = filename_base + name + '.png'
                image = Image.open(name)
                image1 = ImageTk.PhotoImage(image)
                imagesprite = canvas.create_image(64,64,image=image1)
                time.sleep(sleep_time)
create_animation("GRUST_",154)



