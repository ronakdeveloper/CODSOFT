from tkinter import *

question = 0
start = []
end = []
button = None
score = 0

dic = {
    "questions": [
        "Which of the following data types is mutable in Python?",
        "Which Python keyword is used to define a function?",
        "which data type is used to store a sequence of characters?",
        "What data type is used to represent a binary choice?"
    ],
    "choices": [
        ["Strings", "Lists", "Tuples"],
        ["define", "function", "def"],
        ["str", "int", "float"],
        ["int", "bool", "float"]
    ],
    "answers": [2, 3, 1, 2]
}

length = len(dic["questions"])


def Page1():
    global question, score
    question, score = 0, 0

    for i in end:
        i.destroy()

    canvas.create_rectangle(50, 140, 850, 600, fill="green")
    canvas.create_text(450, 170, text="Introduction",
                       fill="blue", font=("Arial", 30))
    canvas.create_text(
        450, 230,
        text="Welcome to the ultimate quiz challenge where your knowledge\n will be put to the test and only the sharpest minds will prevail!",
        fill="black",
        font=("Arial", 20)
    )
    canvas.create_text(130, 300, text="Rules:",
                       fill="blue", font=("Arial", 30))
    canvas.create_text(
        300, 420,
        text="1. One question will be asked once.\n\n2. Only select one option at once.\n\n3. You can play multiple times.",
        fill="black",
        font=("Arial", 20)
    )

    global button
    button = Button(
        canvas, text='>', height=1, width=1, bg="green", fg="white", font=("Arial", 50), borderwidth=0, command=NEXT
    )
    button.place(x=780, y=470)


def NEXT():
    global button
    button.destroy()

    global question
    canvas.create_rectangle(50, 140, 850, 600, fill="green")
    question += 1
    if question > len(dic["questions"]):
        End()
        return 0
    Question(question)


def Question(question):
    canvas.create_text(
        200, 200, text=f"Question {question}/{length}:", fill="black", font=("Arial", 30))
    canvas.create_text(
        450, 250, text=dic["questions"][question- 1], fill="black", font=("Arial", 20))
    if question <= length:
        options(question)


def options(question):
    option_1 = Button(
        canvas, text=dic["choices"][question - 1][0], height=1, width=18, bg="green", fg="black",
        font=("Arial", 20), borderwidth=8, highlightbackground="grey",
        command=lambda: Update_score(question - 1, 1)
    )
    option_1.place(x=100, y=300)
    option_2 = Button(
        canvas, text=dic["choices"][question - 1][1], height=1, width=18, bg="green", fg="black",
        font=("Arial", 20), borderwidth=8, highlightbackground="grey",
        command=lambda: Update_score(question - 1, 2)
    )
    option_2.place(x=100, y=400)
    option_3 = Button(
        canvas, text=dic["choices"][question- 1][2], height=1, width=18, bg="green", fg="black",
        font=("Arial", 20), borderwidth=8, highlightbackground="grey",
        command=lambda: Update_score(question - 1, 3)
    )
    option_3.place(x=100, y=500)
    start.append(option_1)
    start.append(option_2)
    start.append(option_3)


def Update_score(x, y):
    global score
    if dic["answers"][x] == y:
        score += 1
    NEXT()


def End():
    for i in start:
        i.destroy()
    canvas.create_rectangle(50, 140, 850, 600, fill="grey")
    canvas.create_text(
        450, 220, text=f"You Scored {score} out of {length}", fill="black", font=("Arial", 40))
    canvas.create_text(450, 350, text="You want to play again?",
                       fill="black", font=("Arial", 30, UNDERLINE))
    YES = Button(
        canvas, text="YES", height=1, width=5, bg="grey", fg="black",
        font=("Arial", 20), borderwidth=0, command=Page1
    )
    YES.place(x=200, y=450)
    NO = Button(
        canvas, text="NO", height=1, width=5, bg="grey", fg="black",
        font=("Arial", 20), borderwidth=0, command=exit
    )
    NO.place(x=600, y=450)
    end.append(YES)
    end.append(NO)


win = Tk()
win.geometry("900x700")
win.title("Quiz Game")

canvas = Canvas(win, width=900, height=700, bg="black")
canvas.create_text(450, 70, text="Quiz Game", fill="white", font=("Arial", 40))
canvas.create_rectangle(650, 40, 250, 100, outline="white", width=2)

canvas.pack()

Page1()

win.mainloop()