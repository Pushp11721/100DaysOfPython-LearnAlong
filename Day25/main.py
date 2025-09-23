# with open("weather_data.csv") as file:
#     data=file.readlines()
#     print(data)



# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp":
#             if int(row[1]) not in temperatures:
#                 temperatures.append(int(row[1]))
#
#     print(temperatures)



import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["temp"])
