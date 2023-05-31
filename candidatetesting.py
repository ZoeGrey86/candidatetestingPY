# TODO 2: modify your quiz app to ask 5 questions

# TODO 1.2a: Assign question, correct_answer, and candidate_answer
candidate_name = ""

questions = ["Who was the first American woman in space? ", "True or False: 5 kilometer == 5000 meters? ", "(5 + 3)/2 * 10 = ? ", "Given the list [8, 'Orbit', 'Trajectory', 45], what entry is at index 2? ", "What is the minimum crew size for the ISS? "]

correct_answers = ["Sally Ride","True","40","Trajectory","3"]

candidate_answers = ["ans0","ans1","ans2","ans3","ans4"]


def ask_for_name():
    # TODO 1.1: Ask for candidate's name
    candidate_name = input("Please enter your name: ")
    print("\nHello " + candidate_name + "!")

    return candidate_name

def ask_question():
    # TODO 1.2b: Ask candidate the question and assign the response as candidate_answer
    candidate_answer = input(question)

    return candidate_answer

def ask_questions():
    for num in range(5):
        candidate_answers[num] = input(questions[num])
        if candidate_answers[num] == correct_answers[num]:
            print("correct")
        else:
            print('incorrect')
    return candidate_answers


def grade_quiz(candidate_answers):

    # TODO 1.2c: Let the candidate know if they have answered the question correctly or incorrectly
    grade = 0

    for num in range(5):
        if candidate_answers[num] == correct_answers[num]:
            grade = grade+20

    results = "Overall Grade: " + str(grade) + "%"
    return print(results)


def run_program():

    # TODO 1.1b: Ask for candidate's name and greet them by their name
    ask_for_name()

    ask_questions()

    grade_quiz(candidate_answers)

