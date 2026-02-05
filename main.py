import tkinter as tk
from quiz_data import load_questions

BG = "#ffe1a5"
TEXT = "#111111"
BUTTON_TEXT = "#2d7496"

questions = load_questions()

root = tk.Tk()
root.title("History Quiz")
root.geometry("600x800")
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

submit_button = tk.Button(
    root,
    text="SUBMIT",
    fg=BUTTON_TEXT,
    font=("Arial", 20, "bold"),
    padx=20,
    pady=8,
    relief="flat"
)
submit_button.pack(pady=40)

answer_vars = []

def show_questions():
    for q_index, question in enumerate(questions):
        q_label = tk.Label(
            root,
            text=f"Question {q_index + 1}. {question['question']}",
            bg=BG,
            fg=TEXT,
            font=("Arial", 18),
            wraplength=520,
            justify="left"
        )
        q_label.pack(anchor="w", padx=40, pady=(20, 5))

        vars_for_question = []

        for option in question["options"]:
            var = tk.IntVar()
            cb = tk.Checkbutton(
                root,
                text=option,
                variable=var,
                bg=BG,
                fg=TEXT,
                font=("Arial", 14),
                anchor="w",
                justify="left"
            )
            cb.pack(anchor="w", padx=60)
            vars_for_question.append(var)

        answer_vars.append(vars_for_question)

show_questions()

root.mainloop()
