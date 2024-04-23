import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=[]
for i in range(0,nr_letters):
    index= random.randint(0,len(letters)-1)
    password.append(letters[index])
print(password)
for i in  range(0,nr_symbols):
    random_char= random.choice(symbols)
    password.append(random_char)
print(password)
for i in  range(0,nr_numbers):
    random_char = random.choice(numbers)
    password.append(random_char)
print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# now we generate random non repaeating index sequence for truely random password
'''
the randomness lies at first level in picking number, symbol or string
'''
type_list =[letters,numbers,symbols]

#for each position , we first randomly pick what type of input to choose out of type list
#0 represent letters, 1 represent numbers and 2 represent symbols
random_password=[]
password_len= nr_letters+nr_symbols+nr_numbers
numbers_left=nr_numbers
symbols_left=nr_symbols
letters_left=nr_letters
letters_range=len(letters)
symbols_range=len(symbols)
numbers_range =len(numbers)

while password_len > 0:
    list_type_index =random.randint(0,2)
    if list_type_index == 0:
        #Check if all letters have been utilized or not
        if letters_left > 0:
            random_index = random.randint(0,letters_range-1)
            random_password.append(type_list[0][random_index])
            letters_left-=1
            print(random_password)
            password_len-=1
    if list_type_index == 1:
        #Check if all numbers have been utilized or not
        if numbers_left > 0:
            random_index = random.randint(0,numbers_range-1)
            random_password.append(type_list[1][random_index])
            numbers_left-=1
            print(random_password)
            password_len-=1
    if list_type_index == 2:
        #Check if all symbols have been utilized or not
        if symbols_left > 0:
            random_index = random.randint(0,symbols_range-1)
            random_password.append(type_list[2][random_index])
            symbols_left-=1
            print(random_password)
            password_len-=1
# we could also use the random.shuffle method to simply convert the ordered password created in easy method to a random password            
#convert list to string to make it usable
rand_pass = ''.join(random_password)
print(f"Random password is {rand_pass}")