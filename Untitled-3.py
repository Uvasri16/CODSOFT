
import tkinter as tk

def button_click(item):
    global expression
    expression += str(item)
    entry_text.set(expression)

def clear():
    global expression
    expression = ""
    entry_text.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        entry_text.set(result)
        expression = ""
    except:
        entry_text.set("Error")
        expression = ""

def set_background_color(color):
    root.configure(bg=color)

root = tk.Tk()
root.title("Simple Calculator")


default_bg_color = "#ffffff"  # white
root.configure(bg=default_bg_color)


entry_text = tk.StringVar()
expression = ""

entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), bd=10, insertwidth=4, width=15, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=("Helvetica", 16), padx=30, pady=10, command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=("Helvetica", 16), padx=30, pady=10, command=clear)
    else:
        btn = tk.Button(root, text=text, font=("Helvetica", 16), padx=30, pady=10, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)


color_button = tk.Button(root, text="Set Background Color", font=("Helvetica", 12), padx=10, pady=5,
                         command=lambda: set_background_color("#f0f0f0"))  # light gray
color_button.grid(row=5, columnspan=4, padx=10, pady=10)

root.mainloop()
