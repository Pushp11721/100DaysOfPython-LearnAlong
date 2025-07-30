from prettytable import PrettyTable

table=PrettyTable()

# table.field_names=["Student","Roll No","School","CGPA"]

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="l"
print(table)