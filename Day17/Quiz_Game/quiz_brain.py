from data import question_data
class QuizBrain:
    # where attributes are stored for question number, the questions, and the score
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
    # returns true while the question number hasn't caught up the the number of questions
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
            

    # finds the correct question to use from the list with the question number as an index
    # increases the question number from list index to actual number
    # asks the question and expects true or false
    # checks to see if the input was correct
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You've got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")