from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("500x500")

root.title("Hacktoberfest Quiz")


label = Label(root,text="Hacktoberfest Quiz ",width = 20,height=4,font=("algerian",15))
label.pack()

class Quiz:
    print('Welcome to the Hacktoberfest 2022 Quiz')
    score=0
    total_questions=4

    def __init__(self):
        # self.ask_question()
        pass

    def ask_question(self):
        answer=input('Are you ready to play the Quiz ? (yes/no) :')

        if answer.lower()=='yes':
            answer=input('Question 1: What programming language was this quiz created in? Hint: Java, C++, Python')
            if answer.lower()=='python':
                self.score += 1
                print('correct')
            else:
                print('Wrong Answer :(')
        
        
            answer=input('Question 2: Is one of the values of Hacktoberfest 2022 "EVERYONE IS WELCOME" ? ')
            if answer.lower()=='yes':
                self.score += 1
                print('correct')
            else:
                print('Wrong Answer :(')
        
            answer=input('Question 3: Does Hacktoberfest end on December 31?')
            if answer.lower()=='no':
                self.score += 1
                print('correct')
            else:
                print('Wrong Answer :(')
       
            answer=input('Question 3: Does Hacktoberfest have a discord server?')
            if answer.lower()=='yes':
                self.score += 1
                print('correct')
            else:
                print('Wrong Answer :(')
        
        print('Thankyou for Playing the Hacktoberfest quiz game, you attempted',self.score,"questions correctly!")
        mark=(self.score/self.total_questions)*100
        print('Marks obtained:',mark)
        print('BYE!')

    def get_score(self):
        return self.score

    def validate_question_one(self, question_one_value = ''):
        if question_one_value.lower()=='python':
            self.score += 1
            print('correct')
        else:
            print('Wrong Answer1')
            print('correct answer is python ')
        return True if question_one_value.lower()=='python' else False
        
    def validate_question_two(self, question_two_value):
        if question_two_value.lower()=='yes':
            self.score += 1
            print('correct')
        else:
            print('Wrong Answer2')
            print('correct answer is yes ')
        return True if question_two_value.lower()=='yes' else False

    def validate_question_three(self, question_three_value):
        if question_three_value.lower()=='no':
            self.score += 1
            print('correct')
        else:
            print('Wrong Answer2')
            print('correct answer is no')
        return True if question_three_value.lower()=='no' else False

    def validate_question_four(self, question_four_value):
        if question_four_value.lower()=='yes':
            self.score += 1
            print('correct')
        else:
            print('Wrong Answer2')
            print('correct answer is yes')
        return True if question_four_value.lower()=='yes' else False

    def evaluate(self):
        self.score = 0

        question_one_value = question_one.get()
        self.validate_question_one(question_one_value=question_one_value)

        question_two_value = question_two.get()
        self.validate_question_two(question_two_value=question_two_value)

        question_three_value = question_three.get()
        self.validate_question_three(question_three_value=question_three_value)
        
        question_four_value = question_four.get()
        self.validate_question_four(question_four_value=question_four_value)


        print('Thankyou for Playing the Hacktoberfest quiz game, you attempted',self.score,"questions correctly!")
        mark=(self.score/self.total_questions)*100
        my_label.config(text = "Your score is " + str(mark) +"%")
        print('Marks obtained:',mark)

        
        

quiz = Quiz()

w1_label = Label(root,text="Question 1: What programming language was this quiz created in? Hint: Java, C++, Python ?",font=("arial",10),width=100,height=4)
w1_label.pack()
question_one = ttk.Combobox(root,value=["Python","Java","C++"])
question_one.current(0)
question_one.pack()

w1_label = Label(root,text="",font=("arial",10),width=100,height=4)
w1_label.pack()

w2_label = Label(root,text="Question 2: Is one of the values of Hacktoberfest 2022 'EVERYONE IS WELCOME' ?",font=("arial",10),width=100,height=4)
w2_label.pack()
question_two = ttk.Combobox(root,value=["Yes","No"])
question_two.current(0)
question_two.pack()

w2_label = Label(root,text="",font=("arial",10),width=100,height=4)
w2_label.pack()


w3_label = Label(root,text="Question 3: Does Hacktoberfest end on December 31?",font=("arial",10),width=100,height=4)
w3_label.pack()
question_three = ttk.Combobox(root,value=["Yes","No"])
question_three.current(0)
question_three.pack()

w3_label = Label(root,text="",font=("arial",10),width=100,height=4)
w3_label.pack()

w4_label = Label(root,text="Question 4: Does Hacktoberfest have a discord server?",font=("arial",10),width=50,height=4)
w4_label.pack()
question_four = ttk.Combobox(root,value=["Yes","No"])
question_four.current(0)
question_four.pack()

w4_label = Label(root,text="",font=("arial",10),width=50,height=4)
w4_label.pack()


button = Button(root,text="Submit",font=("bell mt",10), command=quiz.evaluate)
button.pack()


# w6_label = Label(root,font=("arial",10),width=100,height=4, textvariable=quiz.get_score())
my_label = Label(root,
                 text = "Score:")
my_label.pack()


root.mainloop()
