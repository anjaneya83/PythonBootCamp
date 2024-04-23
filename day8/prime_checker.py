#Prime number checker

def prime_checker(number):
    
    if number == 2 or number == 3 :
        print("It's a prime number.")
    else:
        for count in range(2,number):
            if number%count == 0:
                print("Number is not prime")
                return
        print("It's a prime number.")

def prime_checker_1(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
n = int(input("Enter a number: "))
prime_checker_1(number=n)

