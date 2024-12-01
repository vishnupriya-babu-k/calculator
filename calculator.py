from tkinter import*
root = Tk()
input = Entry(root,width=50)
input.grid(row=0,column=0,columnspan=3,padx=15,pady=15)
def click(num):
    current = input.get()
    input.delete(0,END)
    input.insert(0,str(current) + str(num))
    return
def add():
    current= input.get()
    global fnum
    fnum = int(current)
    input.delete(0,END)
    return
def clear():
    input.delete(0,END)
    return
def equal():
    current =input.get()
    snum = int(current)
    input.delete(0,END)
    input.insert(0,str(snum+fnum))
    return
but1 = Button(root,text="1",padx=50.5,pady=25,command=lambda: click(1))
but2 = Button(root,text="2",padx=50.5,pady=25,command=lambda: click(2))
but3 = Button(root,text="3",padx=50.5,pady=25,command=lambda: click(3))
but4 = Button(root,text="4",padx=50.5,pady=25,command=lambda: click(4))
but5 = Button(root,text="5",padx=50.5,pady=25,command=lambda: click(5))
but6 = Button(root,text="6",padx=50.5,pady=25,command=lambda: click(6))
but7 = Button(root,text="7",padx=50.5,pady=25,command=lambda: click(7))
but8 = Button(root,text="8",padx=50.5,pady=25,command=lambda: click(8))
but9 = Button(root,text="9",padx=50.5,pady=25,command=lambda: click(9))
but0 = Button(root,text="0",padx=50.5,pady=25,command=lambda: click(0))
butadd = Button(root,text="+",padx=108.49,pady=25,command=add)
butclear = Button(root,text="AC",padx=45,pady=25,command=clear)
butequal = Button(root,text="=",padx=108.49,pady=25,command=equal)

but7.grid(row=1,column=0)
but8.grid(row=1,column=1)
but9.grid(row=1,column=2)

but6.grid(row=2,column=0)
but5.grid(row=2,column=1)
but4.grid(row=2,column=2)

but3.grid(row=3,column=0)
but2.grid(row=3,column=1)
but1.grid(row=3,column=2)

but0.grid(row=4,column=0)
butadd.grid(row=4,column=1,columnspan=2)
butclear.grid(row=5,column=0)
butequal.grid(row=5,column=1,columnspan=2)

butequal
root.mainloop()