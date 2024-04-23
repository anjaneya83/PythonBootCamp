#Higher-Lower Game
#Compare two personalities's popularity and predict who is more popular
# If you succed then the winner personality is carried forward and is compared with a new one.
# This continues until you do a wrong prediction
# At that time your success count is given as your final score
#          'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
from art import logo, vs
#from art import vs
from game_data import data
import random

def pick_personality():
    person = random.choice(data)
    return person

def play_game(p_dict):
    print(logo)
    print(f'Compare A: {p_dict["A"]["name"]}, {p_dict["A"]["description"]}, from {p_dict["A"]["country"]},{p_dict["A"]["follower_count"]}')
    print(vs)
    print(f'Compare B: {p_dict["B"]["name"]}, {p_dict["B"]["description"]}, from {p_dict["B"]["country"]},{p_dict["B"]["follower_count"]}')
    choice=input("Who has more followers?Type 'A' or 'B': ").upper()
    return choice
    
player_dict={}
not_lost = True
final_score=0
winner=[]
player_dict["A"]= pick_personality()
while not_lost == True:
    player_dict["B"]= pick_personality()
    a_count=player_dict["A"]["follower_count"]
    b_count=player_dict["B"]["follower_count"]
    if player_dict["A"]== player_dict["B"]:
        b_count=player_dict["B"]["follower_count"]
    choice=play_game(player_dict)
    if a_count == b_count:
        winner ="B"
        looser = "A"
    elif a_count > b_count:
        winner="A"
        looser ="B"
    else:
        winner ="B"
        looser = "A"
    if choice == winner:
        final_score+=1
        print(f"You're right! Current score: {final_score}")
        tmp_dict= player_dict[winner]
        del player_dict[looser]
        player_dict["A"]= tmp_dict
        print(player_dict)
    else:
        print(f"Sorry, that's wrong. Final score:{final_score}")
        not_lost = False

