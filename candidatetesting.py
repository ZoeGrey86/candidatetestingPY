
candidate_name = [""]

questions = ["Who was the first American woman in space? ", "True or False: 5 kilometer == 5000 meters? ",
             "(5 + 3)/2 * 10 = ? ", "Given the list [8, 'Orbit', 'Trajectory', 45], what entry is at index 2? ",
             "What is the minimum crew size for the ISS? "]

correct_answers = ["Sally Ride", "True", "40", "Trajectory", "3"]

candidate_answers = ["ans0", "ans1", "ans2", "ans3", "ans4"]

grade = [0]

candidate_status = [""]


def ask_for_name():
    name = input("Please enter your name: ")
    candidate_name[0] = name
    print("\nHello " + name + "!")
    return name


def ask_questions():
    for num in range(5):
        candidate_answers[num] = input(questions[num])
        if candidate_answers[num] == correct_answers[num]:
            print("correct")
        else:
            print('incorrect')
    return candidate_answers


def grade_quiz(candidate_answers):
    score = 0

    for num in range(5):
        if candidate_answers[num] == correct_answers[num]:
            score = score + 20
    grade[0] = score

    return score


def evaluate_status(score):
    candidate_status[0] = "Failed"
    if score >= 80:
        candidate_status[0] = "Passed"
    return candidate_status


def run_program():
    ask_for_name()

    ask_questions()

    grade_quiz(candidate_answers)

    evaluate_status(grade[0])

    print(candidate_name[0])
    print("Overall Grade: " + str(grade[0]) + "%")
    print("candidate_status: " + candidate_status[0])
