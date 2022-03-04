from tkinter import ttk
from tkinter import *
import threading
from tkinter import PhotoImage
from PIL import ImageTk, Image  
import HarryGUI as hg

def starttask():
    t1 = threading.Thread(target = hg.Task_Gui)
    t1.start()
root = Tk()
root.title("Harry-At Your Assistance")
root.geometry("780x750")
root.configure(background='black')
l1 = Label (root, text="Hey! Glad you are back", font=("Arial Bold", 20))
l1.grid(row=0, column=4, padx=10, pady=10)


b1 = ttk.Button(root, text="Start",command = starttask)
b1.grid(row = 2, column = 0, padx=50, pady=100)
b2 = ttk.Button(root, text="Quit",command = root.destroy)
b2.grid(row = 2, column =5, padx=50, pady=100)

image1 = Image.open("C:\\Users\\HP\\OneDrive\\Desktop\\GUI\\Iron_Template_1.gif")
image2=image1.resize((400,400), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image2)

l2 = Label(image=test,state='normal',borderwidth=0)
l2.image = test
l2.grid(row=1, column=4, padx=10, pady=20)

root.mainloop()