from cgitb import text
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#D3D3D3"
SCREEN_COLOR = "#020204"
TEXT_COLOR = "#22b455"


class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Tech Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg=SCREEN_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.question_text = self.canvas.create_text(
            150,
            125, 
            text="Question Goes HERE", 
            width=250, 
            font=("Courier", 16, "bold"), 
            fill=TEXT_COLOR)

        cross_image = PhotoImage(file="./images/false.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.false_pressed)
        self.cross_button.grid(row=2,column=1)

        check_image = PhotoImage(file="./images/true.png")
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.true_pressed)
        self.check_button.grid(row=2,column=0)

        self.score_label = Label(text="Score here", fg="black", bg=THEME_COLOR , font=(("Courier", 18, "normal")))
        self.score_label.grid(row=0, column=1)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg = SCREEN_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.cross_button.config(state="disabled")
            self.check_button.config(state="disabled")
    
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        if is_right == False:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)