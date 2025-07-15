student_score=[180,124,165,173,189,169,146]
#sum() --> return total of numbers in list
print(sum(student_score))

#Other way of doing this using for loop
sum1=0
for score in student_score:
    sum1+=score
print(sum1)

#max() --> this functions returns the MAX value in the list
print(max(student_score))

#replicate max() using for loop
b=0
for score in student_score:
    if score>b:
        b=score
print(b)