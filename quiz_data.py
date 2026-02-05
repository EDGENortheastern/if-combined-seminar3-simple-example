import csv

def load_questions(filepath="questions.csv"):
    """
    Reads questions from a CSV file and returns a list of question dictionaries.
    """
    questions = []

    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            question = {
                "question": row["question"],
                "options": [
                    row["option_a"],
                    row["option_b"],
                    row["option_c"],
                    row["option_d"],
                ],
                "correct": int(row["correct"]) - 1
            }
            questions.append(question)

    return questions

print(load_questions())