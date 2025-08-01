from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    question_text=i["text"]
    question_answer=i["answer"]
    #create new question using Question class
    new_question=Question(question_text,question_answer)
    #Append new_question object into question_bank list
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
