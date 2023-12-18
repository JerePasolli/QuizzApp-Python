from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.score_value = quiz_brain.score
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"), width=280)
        self.get_next_question()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text=f"Score: {self.score_value}", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        tick_img = PhotoImage(file="images/true.png")
        cross_img = PhotoImage(file="images/false.png")
        self.tick_button = Button(highlightthickness=0, image=tick_img, command=self.true_pressed)
        self.cross_button = Button(highlightthickness=0, image=cross_img, command=self.false_pressed)
        self.tick_button.grid(row=2, column=0)
        self.cross_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score.config(text=f"Score: {self.score_value}")
            self.canvas.itemconfig(self.question_text, text=self.quiz_brain.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You have answered all the questions, congrats!")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz_brain.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

