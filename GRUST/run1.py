from tkinter import *
from PIL import Image, ImageTk
import time
#----------------------------------------------------------------------

class MainWindow():

    #----------------

    def __init__(self, main,filename_base, count, sleep_time = 1):

        # canvas for image
        self.canvas = Canvas(main, width=128, height=128)
        self.canvas.grid(row=0, column=0)
        self.count = count
        # images
        self.my_images = []
        for i in range(count):
                name = '%05d' % i
                name = filename_base + name + '.png'
                image = Image.open(name)
                image1 = ImageTk.PhotoImage(image)
                self.my_images.append(image1)
        self.my_image_number = 0

        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor = NW, image = self.my_images[self.my_image_number])

        # button to change image
        self.button = Button(main, text="Change", command=self.onButton)
        self.button.grid(row=1, column=0)

    #----------------

    def onButton(self):

        # next image
        for i in range(self.count):
            self.canvas.itemconfig(self.image_on_canvas, image = self.my_images[self.my_image_number])
            self.my_image_number+=1
            time.sleep(0.5)

#----------------------------------------------------------------------

root = Tk()
MainWindow(root,"GRUST_",154)
root.mainloop()
