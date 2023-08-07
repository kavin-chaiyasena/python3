import numpy as np

def calculate_scores(answer_sheets, correct_answers, scores):
    return np.dot(np.array(answer_sheets) == correct_answers, scores)

def main():
    answer_sheets = []
    while True:
        answer_sheet = input("Enter the student's answer sheet (type '0' to finish): ")
        if answer_sheet == '0':
            break
        answer_sheets.append(np.array(answer_sheet.split()))

    correct_answers = np.array(input("Enter the list of correct answers: ").split())
    scores = np.array(list(map(int, input("Enter the scores for each problem: ").split())))

    student_scores = calculate_scores(answer_sheets, correct_answers, scores)

    print("List of student scores:")
    for i, score in enumerate(student_scores):
        print(f"Student {i + 1}: {score}")

if __name__ == "__main__":
    main()