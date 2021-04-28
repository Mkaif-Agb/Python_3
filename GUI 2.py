from tkinter import *


class Method:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printbutton = Button(frame, text = "Print Message",command = self.printmessage)
        self.printbutton.pack(side = LEFT)

        self.quit = Button(frame,text="QUIT",command = frame.quit)
        self.quit.pack(side = LEFT)

    def printmessage(self):
        print("This Actually Worked")


root = Tk()
b = Method(root)
root.mainloop()

#---------- Drop Down Menu --------#

def doNothing():
    print("I Wont")

def doSomething():
    print("Okay i will")

def insert():
    print("Insert")

def printy():
    print("Print")


root1=Tk()

menu = Menu(root1)
root1.config(menu = menu)

submenu = Menu(menu)
menu.add_cascade(label = 'File', menu = submenu)
submenu.add_command(label = "New Project...",command = doNothing)
submenu.add_separator()
submenu.add_command(label = "Close Project...",command = doSomething)
submenu.add_separator()
submenu.add_cascade(label = "Exit")

editmenu = Menu(menu)
menu.add_cascade(label ="Edit", menu = editmenu)
editmenu.add_command(label = "Redo", command = doNothing)

#--------ToolBar----------#

toolbar = Frame(root1,bg = "blue")
insert_button = Button(toolbar,text = "Insert", command = insert)
insert_button.pack(side = LEFT, padx=2, pady =3)
print_button = Button(toolbar,text = "Print", command = printy)
print_button.pack(side = LEFT, padx = 2 , pady = 3)
toolbar.pack(side = TOP, fill = X)

#-------Statusbar---------#
status = Label(root1,text = "Preparing to do Nothing",bd=1,relief = SUNKEN,anchor = W)
status.pack(side = BOTTOM,fill = X)

root1.mainloop()