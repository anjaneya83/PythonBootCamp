# Black jack game code
#The first player to score 21 wins. if your score exceeds 21 you loose immediately..
#if before reaching 21, you decide to stop, then dealer score is to be checked.
#dealer has to pick a card untill the score reaches 17 or above.This is not true for the player.
# player can decie to quit even beofe 17
# if dealer score and your socre bot are under 21, then the one with max score wins
# The ace can be counted for as 1 or 11 both
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
#An exception to ace is , if your sum goes over 21 then ace is counted as 1 and not 11. This is applicable for both players
from art import logo
import random
cards_list =[11,2,3,4,5,6,7,8,9,10,10,10,10]
continue_play = True
end_game = False
def check_who_wins(player_score,comp_score):
    if player_score > 21:
        print("YOu went over the limit. You loose")
    elif comp_score >21:
        print("Opponent went over 21. You Win :) ")
    elif player_score == comp_score:
        print("It's a tie")
    elif player_score > comp_score:
        print("You win")
    else:
        print("You loose")

while end_game == False:
    game_option = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if game_option == 'y':
        player_card_list=[]
        comp_card_list=[]
        player_score=0
        comp_score=0
        player_ace_count=0
        comp_ace_count=0
        print(logo)
        player_card_list.append(random.choice(cards_list))
        player_card_list.append(random.choice(cards_list))
        player_score =sum(player_card_list)
        comp_card_list.append(random.choice(cards_list))
        print(f"		Your cards:{player_card_list}, current score: {player_score}")
        print(f"		Computer's first card: {comp_card_list}")
        continue_play=True
        while continue_play == True:
            play_option = input("Type 'y' to get another card, type 'n' to pass: ")
            if play_option == "y":
                player_card_list.append(random.choice(cards_list))
                if player_ace_count >0:
                    player_score =sum(player_card_list) - (10*player_ace_count)
                else:
                    player_score =sum(player_card_list)
                print(f"		Your cards:{player_card_list}, current score: {player_score}")
                if player_score >21:
                    if 11 in player_card_list:
                        player_ace_count +=1
                        player_score-=10*player_ace_count
                        continue_play =True
                        print("Your ace is counted as 1 now")
                    else:
                        continue_play= False
            else:
                continue_play = False
        while comp_score < 17:
            comp_card_list.append(random.choice(cards_list))
            comp_score = sum(comp_card_list)
        if (comp_score > 21) and (11 in comp_card_list):
            comp_ace_count+=1
            comp_score-=10*comp_ace_count
            print("Dealer's ace is counted as 1 now")
        print(f"		Your final hand: {player_card_list}, final score: {player_score}")
        print(f"		Computer's final hand: {comp_card_list}, final score: {comp_score}")
        check_who_wins(player_score,comp_score)
        
    else:
        end_game = True
        

