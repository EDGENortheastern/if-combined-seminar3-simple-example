import tkinter as tk # for creating the GUI
import csv # to write to csv from main
from quiz_data import load_questions # for loading the questions
from quiz_utils import clean_name # cleans the name
from datetime import datetime # to record a timestamp

BG = "#ffe1a5"
TEXT = "#111111"
BUTTON_TEXT = "#2d7496"

questions = load_questions()

class QuizApp(tk.Tk):
    
    """
    A class that represents the quiz application.
    """

    def __init__(self, questions):
        super().__init__()

        self.title("History Quiz")
        self.questions = questions
        self.current_question = 0
        self.score = 0
        self.configure(bg=BG)
        self.geometry("600x700")
        self.name = tk.StringVar()
        self.answer_var = tk.IntVar(value=-1)
        self.answer_vars = []

        self.name_label = tk.Label(
            self,
            text="Please enter your name in the box below👇🏿",
            bg=BG,
            fg=TEXT,
            font=("Arial", 18)
        )
        self.name_label.pack(pady=10)

        self.name_entry = tk.Entry(
            self,
            textvariable=self.name,
            font=("Arial", 18),
            fg=TEXT
        )
        self.name_entry.pack(pady=10)

        self.build_question_screen()

        self.submit_button = tk.Button(
            self,
            text="SUBMIT!",
            font=("Arial", 18),
            fg=BUTTON_TEXT,
            bg=BG,
            command=self.handle_submit
        )
        self.submit_button.pack(pady=10)

    def handle_submit(self):
        
        """Saves the student name, score and timestamp
        to a CSV file."""
        
        st_name = clean_name(self.name_entry.get())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("student_records.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([st_name, timestamp])

    def build_question_screen(self):
        
        """Builds the question section."""

        question_number = 1

        for question in self.questions:
            q_label = tk.Label(
                self,
                text=f"Question {question_number}. {question['question']}",
                font=("Arial", 18),
                wraplength=500,  # wrap the text if it's too long
                justify="center",  
                bg = BG
            )
            q_label.pack(anchor="w", padx=40, pady=(20, 5))

            answer_var = tk.IntVar(value=-1)
            self.answer_vars.append(answer_var)

            option_value = 0
            for option in question["options"]:
                rb = tk.Radiobutton(
                    self,
                    text=option,
                    variable=answer_var,
                    value=option_value,
                    font=("Arial", 14),
                    bg=BG
                )
                rb.pack(anchor="w", padx=60)
                option_value += 1

            question_number += 1

if __name__ == "__main__":
    app = QuizApp(questions)
    app.mainloop()
