from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.label1 = Label(text="Score: 0")
        self.label1.config(bg=THEME_COLOR, fg="white", padx=20, pady=20, font=(10))
        self.label1.grid(row=0,column=1)

        self.canvas = Canvas(bg="white", height=250, width=300)
        self.text = self.canvas.create_text(150,125, width=280, text="Hi",fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2)


        self.button1_img = PhotoImage(file="images/true.png")
        self.button1 = Button(image= self.button1_img, highlightthickness=0, command=self.check_button)
        self.button1.grid(row=2, column=0, pady=20)
        self.button2_img = PhotoImage(file="images/false.png")
        self.button2 = Button(image=self.button2_img, highlightthickness=0, command=self.cross_button)
        self.button2.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label1.config(text=f"Score: {self.quiz.score}")
            new_q = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=new_q)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def check_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def cross_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


