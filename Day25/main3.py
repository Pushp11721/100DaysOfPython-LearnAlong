#Challenge - Create a data with only count of Squirrels based on colour
import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250115.csv")

fur_colour=data["Primary Fur Color"].to_list()
gray=fur_colour.count("Gray")
red=fur_colour.count("Cinnamon")
black=fur_colour.count("Black")
print(f"grey={gray}\nred={red}\nblack={black}")

answer={
    "Fur Color":["grey","red","black"],
    "Count":[gray,red,black]
}
squirrel_count=pandas.DataFrame(answer)
squirrel_count.to_csv("squirrel_count.csv")