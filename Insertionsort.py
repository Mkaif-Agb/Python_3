def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [99,77,55,22,44,11,-1]
insertionSort(arr)
for i in range(len(arr)):
    print ("%d" %arr[i])

from tkinter import *
from tkinter import messagebox

root = Tk()
def click():
    print("Hello There")
f = Frame(root,width=700,height=500)
f.propagate(0)
f.pack()
text = Text(f,width=10,height=20)
text.grid()
text.pack()
b = Button(text='Click Me',command=click())
b.pack()
messagebox.showinfo("Window","All is worknig Fine")
messagebox.showerror("Window","ERROR")
label = Label(text='Okay')
label.pack()

root.mainloop()



root1 = Tk()
root1.title("Easy AF")
msg=''
def reveal():
    content = en.get()
    if content =='Python':
        print("Hello There")
    else:
        print("What")


f = Frame(root1,width=800,height=500)
f.propagate(0)
f.pack()
lb1 = Label(f,text='Only Authorised Person Allowed')
lb1.grid(row =0, column =0)
lb2 = Label(f,text="Enter Password")
lb2.grid(row =1, column =0)
en = Entry(f,width=25,fg='red',bg='blue')
te = Text(f)
en.pack()
b = Button(f,text = "Okay", command = reveal)
b.pack()
messagebox.showinfo("HEY")
root1.mainloop()
