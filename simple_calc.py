# https://www.youtube.com/watch?v=XhCfsuMyhXo
# Basic Calculator
# 27 Dec 2021


from tkinter import *

root = Tk()
root.title("Simple Calc")


e = Entry(root, width=35,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    first = e.get()
    e.delete(0, END)
    e.insert(0, str(first) + str(number))

def button_clear():
    e.delete(0, END)

def f_add():
    first_number = e.get()
    global f_num
    global math
    math = "+"
    f_num = int(first_number)
    e.delete(0, END)

def f_sub():
    first_number = e.get()
    global f_num
    global math
    math = "-"
    f_num = int(first_number)
    e.delete(0, END)

def f_mul():
    first_number = e.get()
    global f_num
    global math
    math = "x"
    f_num = int(first_number)
    e.delete(0, END)

def f_div():
    first_number = e.get()
    global f_num
    global math
    math = "/"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "+":
        e.insert(0, f_num + int(second_number))
    elif math == "-":
        e.insert(0, f_num - int(second_number))
    elif math == "x":
        e.insert(0, f_num * int(second_number))
    elif math == "/":
        if second_number != 0 or second_number != "0":  # Fånga med en riktig try-except 
            e.insert(0, f_num / int(second_number))




# defines the buttons

button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_plus = Button(root, text="+", padx=40, pady=20, command= lambda: f_add())
button_minus = Button(root, text="-", padx=40, pady=20, command= lambda: f_sub())
button_div = Button(root, text="/", padx=40, pady=20, command= lambda: f_div())
button_x = Button(root, text="x", padx=40, pady=20, command= lambda: f_mul())

button_equal = Button(root, text="=", padx=40, pady=20, command= button_equal)
button_clear = Button(root, text="C", padx=40, pady=20, command= button_clear)

# displays the buttons on the screen

button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)
button_3.grid(row=1, column=3)

button_4.grid(row=2, column=1)
button_5.grid(row=2, column=2)
button_6.grid(row=2, column=3)

button_7.grid(row=3, column=1)
button_8.grid(row=3, column=2)
button_9.grid(row=3, column=3)

button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_equal.grid(row=4, column=3)

button_plus.grid(row=5, column=1)
button_minus.grid(row=5, column=2)
button_x.grid(row=5, column=3)
button_div.grid(row=5, column=4)

# loops the GUI

root.mainloop()
