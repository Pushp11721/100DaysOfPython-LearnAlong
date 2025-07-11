#import random library to use random functions
import random
#Importing module that we have created
import my_module

#randint(a,b) --> this functions return you random integer between a and b including a & b also.[a<=x<=b}
a=random.randint(1,100)
print(a)
print(my_module.fav_num)

#random.random() --> this function returns random float number b/w 0 to 1
rand_float=random.random()
print(rand_float)

#to generate bigger random float numbers we can add both randint() and random() functions
print(a+round(rand_float,2))#Using round() function to round it to 2 decimal points

#Or we can use another technique
random_float=random.random()*10
print(random_float)

