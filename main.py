import tkinter as tk # for creating the GUI
import csv # to write to csv from main
from quiz_data import load_questions # for loading the questions
# utility functions to clean and validate names 👇
from quiz_utils import clean_name, character_check, length_check, presence_check
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

    def build_question_screen(self):
        
        """
        Builds the question section.
        """

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
    
    def handle_submit(self):
        
        """
        Saves the student name, score and timestamp
        to a CSV file.
        """
        
        st_name = clean_name(self.name_entry.get())
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.validate_name_with_messages(st_name):

            answers = []
            for var in self.answer_vars:
                answers.append(var.get())
                    
            with open("student_records.csv", mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([st_name, timestamp, answers])

            self.build_thank_you_screen(st_name)
            
            
    def build_thank_you_screen(self, name):
        
        """Shows the final confirmation screen."""

        self.clear_screen()

        tk.Label(
            self,
            text="Thank you for submitting your answers, ",
            font=("Arial", 18),
            bg = BG
        ).pack(pady=20)

        tk.Label(
            self,
            text=f"{name}, the assessor will let you know your results soon!",
            font=("Arial", 24),
            wraplength=500,
            justify="center",
            bg = BG
        ).pack(pady=10)

        tk.Button(
            self,
            font=("Arial", 18),
            fg=BUTTON_TEXT,
            bg=BG,
            text="QUIT",
            command=self.destroy
        ).pack(pady=30)
        
    def validate_name_with_messages(self, cleaned_name: str) -> bool:
        
        """
        Validates the cleaned name and shows an error message if invalid.
        Returns True if the name is valid. Not pure because depends on messagebox.
        """
        valid = True

        if not presence_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Please enter your name."
            )
            valid = False

        if valid and not length_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Name must be between 2 and 50 characters."
            )
            valid = False

        if valid and not character_check(cleaned_name):
            messagebox.showerror(
                "Invalid name",
                "Names must only contain letters, spaces, hyphens, or apostrophes."
            )
            valid = False

        return valid

    def clear_screen(self):
        
        """Removes all widgets from the window."""
        
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = QuizApp(questions)
    app.mainloop()
