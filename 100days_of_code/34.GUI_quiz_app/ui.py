from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

class QuizInterface():
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lable = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_lable.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.quz_text = self.canvas.create_text(
            150, 125, width=280, font=FONT, fill=THEME_COLOR)

        false_img = PhotoImage(file='./images/false.png')
        self.false_button = Button(
            image=false_img, highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2, column=1)

        true_img = PhotoImage(file='./images/true.png')
        self.true_button = Button(
            image=true_img, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_brain.still_has_questions():
            self.score_lable.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.quz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quz_text, text="Out of questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz_brain.check_answer('true'))

    def false_press(self):
        self.give_feedback(self.quiz_brain.check_answer('false'))

    def give_feedback(self, trueorfalse):
        if trueorfalse:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question)
