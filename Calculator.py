import tkinter as tk

def add():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result.set(num1 + num2)

def subtract():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result.set(num1 - num2)

def multiply():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result.set(num1 * num2)

def divide():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 != 0:
        result.set(num1 / num2)
    else:
        result.set("Error: Division by zero")

root = tk.Tk()
root.title("Basic Calculator")

entry_num1 = tk.Entry(root)
entry_num1.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

add_button = tk.Button(root, text="Add", command=add)
add_button.pack()

subtract_button = tk.Button(root, text="Subtract", command=subtract)
subtract_button.pack()

multiply_button = tk.Button(root, text="Multiply", command=multiply)
multiply_button.pack()

divide_button = tk.Button(root, text="Divide", command=divide)
divide_button.pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()