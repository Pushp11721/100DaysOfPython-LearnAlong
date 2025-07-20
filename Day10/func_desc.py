def format_name(f_name,l_name):
    '''Take a first and last name and format it to return the title case version of the name.'''
    if f_name=="" or l_name=="":
        return "You did not provide valid inputs."
    return (f_name+" "+l_name).title()

print(format_name("Obito","Uchiha"))

def function1(text):
    '''Double The exact string'''
    return text+text
def function2(text):
    return text.title()
print(function2("hello"))
print(function2(function1("hello")))
