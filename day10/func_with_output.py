#Functions with Outputs

def format_name(f_name,l_name):
    if f_name =="" or l_name == "":
        return f"Empty first name or last name is not allowed"
    #Convert the input parameters to camel case (first letter upper case , rest lower case of each word in the string)
    fname = f_name.title()
    lname = l_name.title()
    
    return f"The formatted name is {fname} {lname}"
    #return fname, lname


first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")

formatted_string=format_name(f_name=first_name,l_name=last_name)
print(formatted_string)
#fname,lname=format_name(f_name=first_name,l_name=last_name)
#print(f"The formatted name is {fname} {lname}")

