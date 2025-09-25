import tkinter

#Argument with default value
def my_function(a=1,b=2,c=3):
    print(a)
    print(b)
    print(c)

my_function()

my_function(a=2,b=34,c=294)#we can change it's default values
my_function(a=3)#we can change a single attribute also
#basically it's upto us that we want to use default values or not

