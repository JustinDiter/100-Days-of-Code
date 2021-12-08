from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# list that the questions from data will be stored in
question_bank = []

# creates variables that the Question class can understand
# adds the questions to the bank
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

# assigns the quiz variable the QuizBrain class to handle the game functionality
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz !")
print(f"Your score was {quiz.score}/{quiz.question_number}")
