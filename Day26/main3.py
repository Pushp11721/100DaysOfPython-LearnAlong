#TODO : How to iterate over a Pandas DataFrame

#How Dictionary Comprehension works - It loops through dictionary
student_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}

# for (key,value) in student_dict.items():
#     print(key)
#     print(value)

import pandas
student_data_frame=pandas.DataFrame(student_dict)

#Loop through a data frame
# for (key,value) in student_data_frame.items():
#     print(value)
for (index,row) in student_data_frame.iterrows():
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row)

#new_dict = {new_key:new_value for (index,row) in df.iterrows()}