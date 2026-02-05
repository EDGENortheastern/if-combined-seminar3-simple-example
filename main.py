import tkinter as tk
from quiz_data import load_questions

BG = "#ffe1a5"
TEXT = "#111111"
BUTTON_TEXT = "#2d7496"

root = tk.Tk()
root.title("History Quiz")
root.geometry("600x400")
root.configure(bg=BG)

instruction = tk.Label(
    root,
    text="Please enter your name in the box below 👇🏿",
    bg=BG,
    fg=TEXT,
    font=("Arial", 20)
)
instruction.pack(pady=(40, 15))

name_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=20
)
name_entry.pack(pady=(0, 40))

next_button = tk.Button(
    root,
    text="NEXT",
    fg=BUTTON_TEXT,
    font=("Arial", 20, "bold"),
    padx=20,
    pady=8,
    relief="flat"
)
next_button.pack(pady=40)

root.mainloop()