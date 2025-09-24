#TODO 1 : Dictionary Comprehension
#new_dict = {new_key:new_value for item in list}
#Challenge : Create a dictionary with random scores for students by using names list
import random
names = ["Alex","Beth","Carolina","Dave","Eleanor","Freddie"]
students_scores = {name:random.randint(1,100) for name in names}
print(students_scores)

#new_dict = {new_key:new_value for (key,value) in dict.items()}


#TODO 2 : Conditional Dictionary Comprehension
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}
#Challenge : Create dictionary of students who passed the exam by using previous student_scores dictionary
passed_students = {name:score for (name,score) in students_scores.items() if score>33}
print(passed_students)