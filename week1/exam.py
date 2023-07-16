import numpy as np

def get_student_scores():
    student_answers = []
    while True:
        answers = input(">>> ")
        if answers == '0':
            break
        student_answers.append(list(answers.replace(" ", "")))
    student_answers = np.array(student_answers)
    correct_answers = list(input(">>> ").replace(" ", ""))
    scores = list(map(int, input(">>> ").split()))
    student_scores = []
    for answers in student_answers:
        score = 0
        for i in range(len(answers)):
            if answers[i] == correct_answers[i]:
                score += scores[i]
        student_scores.append(score)
    return student_scores

print(get_student_scores())
