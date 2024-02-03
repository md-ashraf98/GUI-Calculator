import tkinter
from tkinter import *

root = Tk()
root.geometry("644x970")
root.title("Calculator")

# Use the default Tkinter icon
root.iconbitmap(default='info')


scvalue = StringVar()
scvalue.set(" ")
screen = Entry(root, textvar=scvalue, font="Arial")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

def click(event):
    current = scvalue.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            scvalue.set(result)
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
    else:
        scvalue.set(current + text)

f = Frame(root, bg="grey")
b = Button(f, text="9", padx=28, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=28, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=28, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="6", padx=28, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=28, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=28, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="3", padx=28, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=28, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=28, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="0", padx=31, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=31, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=31, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="/", padx=33, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=21, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=27, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="C", padx=26, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=26, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=26, pady=18, font="Arial")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()
