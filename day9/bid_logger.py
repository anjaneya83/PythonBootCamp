#Bidding program
import art

bid_log = {}


print(art.logo)
bid_run="yes"
while bid_run == "yes":
    print("Welcome to the secret auction program.")
    name=input("What is your name?: ")
    bid_value=int(input("What's your bid?: $"))
    bid_log[bid_value]=name
    choice=input("Are there any other bidders?Type 'yes' or 'no'.\n")
    bid_run = choice
max_bid=0
for key in bid_log:
    if max_bid < key:
        max_bid =key

print(f"The winner is {bid_log[max_bid]} with a bid of ${max_bid}")
    
