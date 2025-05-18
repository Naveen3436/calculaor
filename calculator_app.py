import tkinter as tk
from tkinter import messagebox

def button_click(value):
    current = entry_var.get()
    if value == "C":
        entry_var.set("")
    elif value == "=":
        try:
            result = str(eval(current))
            entry_var.set(result)
        except:
            messagebox.showerror("Error", "Invalid Expression")
            entry_var.set("")
    else:
        entry_var.set(current + value)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x450")
root.resizable(False, False)
root.configure(bg="#1e272e")

# Entry field to show expressions and results
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=0, bg="white", fg="black", justify="right")
entry.pack(padx=10, pady=20, ipady=15, fill="x")

# Button layout
buttons = [
    ["C", "", "", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

# Create and arrange buttons in a grid
frame = tk.Frame(root, bg="#1e272e")
frame.pack(expand=True, fill="both")

for row in range(5):
    for col in range(4):
        text = buttons[row][col]
        if text == "":
            continue
        btn = tk.Button(
            frame, text=text, font=("Arial", 18), fg="white",
            bg="#3c6382" if text in "+-*/" else "#e58e26" if text == "=" else "#222f3e" if text != "C" else "#eb2f06",
            bd=0, command=lambda val=text: button_click(val)
        )
        btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1, ipadx=10, ipady=20)

# Make the grid resize evenly
for i in range(5):
    frame.rowconfigure(i, weight=1)
for i in range(4):
    frame.columnconfigure(i, weight=1)

# Start the app
root.mainloop()
