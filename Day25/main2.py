import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data["temp"]))
print(type(data))

data_dict=data.to_dict()
print(data_dict)

data_temp=data["temp"].to_list()
#let's find average temperature
# average_temp=sum(data_temp)/len(data_temp)
# print(round(average_temp,2))
average_temp=data["temp"].mean()
print(average_temp)

#Find maximum temperature using pandas documentation
max_temp=data["temp"].max()
print(max_temp)

#Get data in Columns
print(data.condition)

#Get data of specific row
monday=data[data.day=="Monday"]
print(monday)
print(monday.condition)


#Challenge - bring data where temperature is highest
highest_temp=data[data.temp==data.temp.max()]
print("highest temperature")
print(highest_temp)
print("\n"*10)

#Challenge - Convert Monday's temperature to Fahrenheit
# monday_temp= ((monday.temp * 9) / 5) + 32
# print(monday_temp)
monday_temp=((monday.temp[0] * 9) / 5) + 32
print(f"Monday temperature in Fahrenheit {monday_temp}")
print("\n"*10)


#Create a dataframe from scratch
data_dict={
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}
data_scratch=pandas.DataFrame(data_dict)
print(data_scratch)
data_scratch.to_csv("scratch_data.csv")
