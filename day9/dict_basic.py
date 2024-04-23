# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again."
# }
# #print(programming_dictionary["Bug"])
# 
# #Adding new item to dictionary
# programming_dictionary["int"]="A data type in C & python that represents an integer value"
# #print(programming_dictionary)

#create an empty dictionary
empty_dict={}

#wipe an existing dictionary
programming_dictionary={}
#print(programming_dictionary)
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

#editing an existing dictionary
programming_dictionary["Bug"] = "A moth in the computer"
programming_dictionary["A"] = "Player A is here"
programming_dictionary["B"] = "Player B"
print(programming_dictionary)
print("********************************\n\n")
looser="A"
winner="B"
del programming_dictionary[looser]
tmp_dict =programming_dictionary[winner]
del programming_dictionary[winner]
programming_dictionary["A"]=tmp_dict

print(programming_dictionary)

#Loop through a dictionary

for thing in programming_dictionary:
    print(thing)                             #it prints out the key present in the dictionary

for key in programming_dictionary:
    print(programming_dictionary[key])  #that is how you retrieve each value in the for loop



