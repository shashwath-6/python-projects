import tkinter as tk
import sqlite3


def create_db():
    conn = sqlite3.connect("calculator.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS calculations (id INTEGER PRIMARY KEY AUTOINCREMENT, expression TEXT, result TEXT)")
    conn.commit()
    conn.close()


def insert_calculation(expression, result):
    conn = sqlite3.connect("calculator.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO calculations (expression, result) VALUES (?, ?)", (expression, result))
    conn.commit()
    conn.close()


def on_click(button, button_text):
    for row in buttons:
        for b_text in row:
            button_references[b_text].config(bg="SystemButtonFace")
    button.config(bg="lightblue")

    if button_text == "=":
        try:
            expression = entry.get()
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            insert_calculation(expression, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

    root.after(500, lambda: button.config(bg="SystemButtonFace"))


create_db()

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=25, font=("Arial", 14), borderwidth=5, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

button_references = {}

for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button_references[button_text] = tk.Button(root, text=button_text, width=5, height=2, font=("Arial", 14))
        button_references[button_text].config(command=lambda b=button_references[button_text], text=button_text: on_click(b, text))
        button_references[button_text].grid(row=i + 1, column=j, padx=5, pady=5)


root.mainloop()
