from tkinter import *


root = Tk()

l1 = Label(root,text="Welcome to First Class",fg="black",bg="red")
l1.config(font=(None,25,'italic'))
l1.pack()

b1 = Button(root,text="Button1",bg="black",fg="red")
b1.pack()

b2 = Button(root,text="Button1",bg="black",fg="yellow")
b2.pack(side='left')



root.geometry('700x700')
root.resizable(0,0)
root.mainloop()