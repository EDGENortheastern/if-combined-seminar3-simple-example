import csv # for writing the results to a CSV file
from datetime import datetime # for getting the current date and time


def calculate_score(questions, answer_vars):
    
    """
    Calculates the quiz score based on selected answers.
    Not pure, it depends on external state (the answers).
    """
    
    score = 0

    for i in range(len(questions)):
        correct_index = questions[i]["correct"]
        if answer_vars[i][correct_index].get() == 1:
            score += 1

    return score


def write_result_to_csv(name, score, total, filename="results.csv"):
    
    """
    Appends quiz results to a CSV file.
    Not pure, it write to CSV.
    """
    
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            name,
            score,
            total
        ])
