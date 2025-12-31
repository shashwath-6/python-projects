import pyjokes
import random
import sqlite3
import tkinter as tk
from tkinter import scrolledtext


def setup_database():
    conn = sqlite3.connect("jokes.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS jokes (id INTEGER PRIMARY KEY, joke TEXT)")
    conn.commit()
    conn.close()


def save_joke_to_db(joke):
    conn = sqlite3.connect("jokes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jokes (joke) VALUES (?)", (joke,))
    conn.commit()
    conn.close()


def get_unique_joke():
    conn = sqlite3.connect("jokes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT joke FROM jokes")
    used_jokes = {row[0] for row in cursor.fetchall()}
    conn.close()

    available_jokes = set(pyjokes.get_jokes()) - used_jokes
    if not available_jokes:
        return "No more unique jokes available!"

    joke = random.choice(list(available_jokes))
    save_joke_to_db(joke)
    return joke


def show_joke():
    joke = get_unique_joke()
    joke_display.config(state=tk.NORMAL)
    joke_display.delete("1.0", tk.END)
    joke_display.insert(tk.END, joke)
    joke_display.config(state=tk.DISABLED)


def main():
    setup_database()
    global joke_display

    root = tk.Tk()
    root.title("Random Joke Generator")
    root.geometry("500x300")

    joke_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10, state=tk.DISABLED)
    joke_display.pack(pady=10)

    joke_button = tk.Button(root, text="Get Joke", command=show_joke)
    joke_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
