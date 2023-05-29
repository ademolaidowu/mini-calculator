from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("Invalid Equation")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    root = Tk()
    root.title("Mini Calculator")
    root.iconbitmap("Calculator.ani")
    root.configure(bg="lightblue")


    equation = StringVar()
    #ENTRY
    e1 = Entry(root, textvariable=equation, font=("Aerial", 20), fg='black')
    e1.grid(columnspan=4, ipady=10)

    #BUTTONS
    b1 = Button(root, text=" 1 ", height=3, width=6, command=lambda: press(1))
    b1.grid(column=0, row=1)

    b2 = Button(root, text=" 2 ", height=3, width=6, command=lambda: press(2))
    b2.grid(column=1, row=1)

    b3 = Button(root, text=" 3 ", height=3, width=6, command=lambda: press(3))
    b3.grid(column=2, row=1)

    b4 = Button(root, text=" 4 ", height=3, width=6, command=lambda: press(4))
    b4.grid(column=0, row=2)

    b5 = Button(root, text=" 5 ", height=3, width=6, command=lambda: press(5))
    b5.grid(column=1, row=2)

    b6 = Button(root, text=" 6 ", height=3, width=6, command=lambda: press(6))
    b6.grid(column=2, row=2)

    b7 = Button(root, text=" 7 ", height=3, width=6, command=lambda: press(7))
    b7.grid(column=0, row=3)

    b8 = Button(root, text=" 8 ", height=3, width=6, command=lambda: press(8))
    b8.grid(column=1, row=3)

    b9 = Button(root, text=" 9 ", height=3, width=6, command=lambda: press(9))
    b9.grid(column=2, row=3)

    b10 = Button(root, text=" 0 ", height=3, width=6, command=lambda: press(0))
    b10.grid(column=1, row=4)

    b11 = Button(root, text=" C ", height=3, width=6, command=clear)
    b11.grid(column=0, row=4)

    b12 = Button(root, text=" = ", height=3, width=6, command=equalpress)
    b12.grid(column=2, row=4)

    b13 = Button(root, text=" + ", height=3, width=6, command=lambda: press('+'))
    b13.grid(column=3, row=1)

    b14 = Button(root, text=" - ", height=3, width=6, command=lambda: press('-'))
    b14.grid(column=3, row=2)

    b15 = Button(root, text=" * ", height=3, width=6, command=lambda: press('*'))
    b15.grid(column=3, row=3)

    b16 = Button(root, text=" / ", height=3, width=6, command=lambda: press('/'))
    b16.grid(column=3, row=4)


    root.mainloop()