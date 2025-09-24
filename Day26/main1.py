#TODO 1 : List Comprehension
#List Comprehension
#new_list = [new_item for item in list]

numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)

#Now let's do this using list comprehension
new_comprehensive_list=[i+1 for i in numbers]
print(new_comprehensive_list)

#Not only lists, we can play with strings too
name="Pushp"
new_name_list=[letter for letter in name]
print(new_name_list)

#Now let us play with range
range_num=[num*2 for num in range(1,5)]
print(range_num)


#TODO 2 : Conditional List Comprehension
#new_list = [new_item for item in list if test]

names = ["Alex","Beth","Carolina","Dave","Eleanor","Freddie"]
short_names=[name for name in names if len(name)<5]
print(short_names)
uppercase_name=[name.upper() for name in names]
print(uppercase_name)

