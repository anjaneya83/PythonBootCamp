# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hello")
    print("Dattebayo")
    print("Namaste")
def greet_with_name(name):
    print(f"Hello {name}")

def greet_with(name,location):
    print(f"Hello {name}!! How is the weather in {location}")


greet()
greet_with_name("sachin")
greet_with("Sachin","Copenhagen")  # Positional Argument
greet_with(location="Copenhagen",name="Sachin") # Keyword Argument