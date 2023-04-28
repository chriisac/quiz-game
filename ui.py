from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="White", font=("Ariel", 10, "normal"))
        self.score_label.grid(column=1, row=0,)

        self.question_canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.question_canvas.create_text(
            150, 125,
            text="Text",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"),
            width=299,
        )
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg="white")
        self.false_button.config(state="active")
        self.true_button.config(state="active")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You've reached the end of the questions.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
