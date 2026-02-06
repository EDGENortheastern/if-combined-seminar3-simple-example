import tkinter as tk # for creating the GUI
from quiz_data import load_questions # for loading the questions

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
        self.geometry("600x500")
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
            bg=BG
        )
        self.submit_button.pack(pady=10)

    def build_question_screen(self):
        """Builds the question screen."""

        q_label = tk.Label(
            self,
            text=f"Question {self.current_question + 1}. "
            f"{self.questions[self.current_question]['question']}",
            font=("Arial", 18),
            bg=BG,
            fg=TEXT
        )
        q_label.pack(pady=10)

        for option in self.questions[self.current_question]["options"]:
            rb = tk.Radiobutton(
                self,
                text=option,
                variable=self.answer_var,
                font=("Arial", 14),
                bg=BG,
                fg=TEXT
            )
            rb.pack(anchor="w", pady=5)
            self.answer_vars.append(rb)


if __name__ == "__main__":
    app = QuizApp(questions)
    app.mainloop()
