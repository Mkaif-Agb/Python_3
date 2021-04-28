from tkinter import *

root = Tk()
theLabel = Label(root,text = "Testing with text")
theLabel.pack()
root.mainloop()

root1 = Tk()
top = Frame(root1)
top.pack()
bottom = Frame(root1)
bottom.pack(side=BOTTOM)

button1 = Button(top,text="Button 1", fg="red")
button2 = Button(top,text="Button 2", fg="green")
button3 = Button(top,text="Button 3", fg="blue")
button4 = Button(bottom,text="Button 4", fg="violet")
button5 = Button(bottom,text="Button 5", fg="orange")
button6 = Button(bottom,text="Button 6", fg="purple")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = RIGHT)
button5.pack(side = LEFT)
button6.pack(side = RIGHT)

root1.mainloop()

root2 = Tk()

one = Label(root2, text = "ONE", fg= "black",bg="red")
one.pack()
two = Label(root2,text="TWO", fg ="Yellow",bg="Blue")
two.pack(fill=X)
three = Label(root2, text="THREE",fg="Orange",bg="Green")
three.pack(side = LEFT,fill = Y)

root2.mainloop()


root3 = Tk()

name = Label(root3,text="Name")
password = Label(root3, text="Password")
entry_1 = Entry(root3)
entry_2 = Entry(root3)
name.grid(row =0, sticky= E )
password.grid(row=1, sticky = W)

#for grid parameters used are N,W,E,S where they are North,ETC whereas North is Up, East is Right, West is left

entry_1.grid(row =0, column = 1)
entry_2.grid(row = 1, column =1)

c3 = Checkbutton(root3,text="Keep Me Logged In" )
c3.grid(columnspan = 2)

root3.mainloop()


root4 = Tk()

def printName():
    print("My Name is Kaif")

button1 = Button(root4,text= "Click Me",command=printName) # no parenthesis on the function
button1.pack()

root4.mainloop()


# left click for other functions,Rightclick,

root5 = Tk()

def leftClick(event):
    print("LEFT")

def middle(event):
    print("MIDDLE")

def rightClick(event):
    print("RIGHT")

frame = Frame(root5,width = 300 , height = 250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middle)
frame.bind("<Button-3>", rightClick)

frame.pack()
root5.mainloop()