#Normal Dictionary
capitals={
    "France":"Paris",
    "Germany":"Berlin",
}
#Nesting a list in a dictionary
travel_plan={
    "France":["Parice","nice","Dijon"],
    "Germany":["Berlin","Black Forest"],
}

#nesting dictionary in a dictioanry
travel_log={
    "France":{"cities_visited":["Parice","nice","Dijon"],"total_visits":12},
    "Germany":{"cities_visited":["Berlin","Black Forest"],"total_visits":5},
}
# The items in this dictionaries are accessed by keys: France and Germany and then within that by the keys: cities_visited
# and total_visits. The values of list are accessed via the indexes

#nesting dictioanry within a list
travel_itenary=[
    {
        "country":"France",
        "cities_visited":["Parice","nice","Dijon"],
        "total_visits":12
    },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Black Forest"],
        "total_visits":5
    },
]
