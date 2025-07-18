#normal dictionary
capitals={
    "France":"Paris",
    "Germany":"Berlin"
}

#nested list in dictionary
travel_log={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Stuttgart","Berlin"]
}

#print Lille
print(travel_log["France"][1])

#nested list
nested_list=["A","B",["C","D"]]
#printout D
print(nested_list[2][1])

#nesting dictionary inside dictionary
travel_log1={
    "France":{
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12
    },
    "Germany":{
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
    }
}
#print Stuttgart
print(travel_log1["Germany"]["cities_visited"][2])
