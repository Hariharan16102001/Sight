import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END) 
        entry.insert(tk.END, "Error")


def clear_display():
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]
row = 1
col = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=8, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif button == 'C':
        tk.Button(root, text=button, width=8, command=clear_display).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=8, command=lambda value=button: on_button_click(value)).grid(row=row,
                                                                                                        column=col,
                                                                                                        padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
