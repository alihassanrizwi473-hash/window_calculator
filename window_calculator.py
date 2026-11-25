from tkinter import*

def click(event):
    global scvalue, memory_value

    text = event.widget.cget("text")
    print(text)


    if text == "=":
        try:
            if scvalue.get().isdigit():
                value = int(scvalue.get())
            else:
                value = eval(screen.get())

            scvalue.set(value)
            screen.update()

        except:
            scvalue.set("Error")
            screen.update()


    elif text == "C":
        scvalue.set("")
        screen.update()


    elif text == "CE":
        scvalue.set("")
        screen.update()


    elif text == "⌫":
        scvalue.set(scvalue.get()[:-1])
        screen.update()

    
    elif text == "%":
        try:
            value = float(scvalue.get())
            scvalue.set(value / 100)
            screen.update()
        except:
            scvalue.set("Error")

    
    elif text == "1/x":
        try:
            value = float(scvalue.get())
            scvalue.set(1 / value)
            screen.update()
        except:
            scvalue.set("Error")

    
    elif text == "x²":
        try:
            value = float(scvalue.get())
            scvalue.set(value ** 2)
            screen.update()
        except:
            scvalue.set("Error")

    
    elif text == "²√x":
        try:
            value = float(scvalue.get())
            scvalue.set(value ** 0.5)
            screen.update()
        except:
            scvalue.set("Error")

    
    elif text == "+/-":
        try:
            value = float(scvalue.get())
            scvalue.set(-value)
            screen.update()
        except:
            scvalue.set("Error")

    
    elif text == "MC":
        memory_value = 0


    elif text == "MR":
        scvalue.set(memory_value)
        screen.update()

    
    elif text == "M+":
        try:
            memory_value += float(scvalue.get())
        except:
            scvalue.set("Error")

    
    elif text == "M-":
        try:
            memory_value -= float(scvalue.get())
        except:
            scvalue.set("Error")

    
    elif text == "MS":
        try:
            memory_value = float(scvalue.get())
        except:
            scvalue.set("Error")

    
    elif text == "M∨":
        scvalue.set(memory_value)
        screen.update()

    
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()

root.geometry("380x500")
root.title("Calculator")
icon = PhotoImage(file="calculator.png")
root.iconphoto(False, icon)

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
f.pack()

memory = ["MC", "MR", "M+", "M-", "MS", "M∨"]

for text in memory:
    b = Label(f, text=text,padx=20, pady=5, font="lucida 10", bg="#f5f5f5")
    b.pack(side=LEFT, expand=True, fill=X)

numbers = [
    ["%", "CE", "C", "⌫"],
    ["1/x", "x²", "²√x", "/"],
    ["7", "8", "9","*"],
    ["4", "5", "6","-"],
    ["1", "2", "3","+"],
    ["+/-", "0", ".", "="]
]

for row in numbers:
    f = Frame(root, bg="grey")
    f.pack()

    for number in row:
        b = Button(f, text=number, width = 4, height = 1,
                   font="lucida 20 bold")
        b.pack(side=LEFT, padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()

