#TODO : *args - unlimited arguments
def add(n1, n2):
    return n1+n2
#now what if I want to add more numbers like 2,3,4,5,...
#We can create function with unlimited arguments
#chellenge - create add function with unlimited arguments
def add_1(*args):
    result=0
    for n in args:
        result+=n
    print(result)
    print(type(args))

add_1(2,3,4,5,6,7,8)

#In this, position of arguments passed plays most important role