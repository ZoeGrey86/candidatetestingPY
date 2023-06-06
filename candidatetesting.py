
candidate_name = ""

questions = ["Who was the first American woman in space? ", "True or False: 5 kilometer == 5000 meters? ",
             "(5 + 3)/2 * 10 = ? ", "Given the list [8, 'Orbit', 'Trajectory', 45], what entry is at index 2? ",
             "What is the minimum crew size for the ISS? "]

correct_answers = ["Sally Ride", "True", "40", "Trajectory", "3"]

candidate_answers = ["ans0", "ans1", "ans2", "ans3", "ans4"]

grade = [0]

candidate_status = [""]

import sys,time

def sprint(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)


def ask_for_name():
    global candidate_name
    sprint("Please enter your name: ")
    candidate_name = input("")
    return candidate_name


def ask_questions():
    for num in range(5):
        sprint(questions[num])
        candidate_answers[num] = input("")
        if candidate_answers[num].lower() == correct_answers[num].lower():
            sprint("correct")
        else:
            sprint('incorrect')
    return candidate_answers


def grade_quiz(candidate_answers):
    score = 0

    for num in range(5):
        if candidate_answers[num].lower() == correct_answers[num].lower():
            score = score + 1
    grade[0] = score*20
    sprint("\n" + str(score) + " out of 5 correct.")

    return score


def evaluate_status(score):
    candidate_status[0] = "Failed"
    if score >= 80:
        candidate_status[0] = "Passed"
    return candidate_status



def run_program():
    ask_for_name()

    sprint("\nHello " + candidate_name + "!")

    ask_questions()

    grade_quiz(candidate_answers)

    evaluate_status(grade[0])

    sprint("\n>>>>>Overall Grade: " + str(grade[0]) + "% <<<<<")
    sprint("candidate_status: " + candidate_status[0])
    if candidate_status[0] == "Passed":
        sprint("Congrats " + candidate_name + " !")
    else:
        sprint("Better luck next time " + candidate_name)
