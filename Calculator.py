import tkinter as tk

def on_click(button_value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(button_value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the window
root = tk.Tk()
root.title("Simple Calculator")

#  background color(light black)
root.configure(bg="#333333")  # Set the hexadecimal color code for light black

# Entry tool for displaying input and results
entry = tk.Entry(root, width=20, font=('arial', 20), justify='right', bg="#666666", fg="white")
entry.grid(row=0, column=0, columnspan=5)

button_layout = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place the buttons 
for (text, row, column) in button_layout:
    if text == 'C':
        button = tk.Button(root, text=text, command=clear_entry, width=9, height=4, bg="#666666", fg="white")
    elif text == '=':
        button = tk.Button(root, text=text, command=calculate, width=9, height=4, bg="#666666", fg="white")
    else:
        button = tk.Button(root, text=text, command=lambda t=text: on_click(t), width=9, height=4, bg="#666666", fg="white")

    button.grid(row=row, column=column)

# Run the main loop
root.mainloop()
