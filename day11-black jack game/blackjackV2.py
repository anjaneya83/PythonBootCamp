# Black jack game code
# Step-1 Shuffle two cards for you and the dealer(computer)
# Step-2 Check the sum for each player, if anyone has a score of 21 with two intial cards, then its a blackjack. end the game and declare the winner
# Step-3 If not blackjack, show the two cards for the player but only first card for the dealer. Display sum of the cards for the player
# Step-4 ask the player if he want to continue play or quit here
# step-5 If he quits here , check for dealer's score, if it is less than 17, shuffle cards for dealer untill it exceeds 17.
# step-6 If he continues, shuffle one more card. disaply all his cards and sum. Go to step 4
# Step-7 check the scores, if player score exceeds 21, he loses and vice versa. if both scores are equal, its a tie, else who has the max score wins
#Step-8 Ask player if he wants to play another game or not.
#The first player to score 21 wins. if your score exceeds 21 you loose immediately..
#if before reaching 21, you decide to stop, then dealer score is to be checked.
#dealer has to pick a card untill the score reaches 17 or above.This is not true for the player.
# player can decide to quit even beofe 17
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

def check_who_wins(pscore,dscore):
    if pscore > 21:
        print("YOu went over the limit. You loose")
    elif dscore >21:
        print("Opponent went over 21. You Win :) ")
    elif pscore == dscore:
        print("It's a tie")
    elif pscore > dscore:
        print("You win")
    else:
        print("You loose")

def deal_cards():
    cards_list =[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card =random.choice(cards_list)
    return card
def check_for_ace(pcard,dcard):
    
    if sum(pcard) > 21:
        if 11 in pcard:
            pcard.remove(11)
            pcard.append(1)
    if sum(dcard) > 21:
        if 11 in comp_card_list:
            dcard.remove(11)
            dcard.append(1)

def play_game():
    
    player_card_list=[]
    comp_card_list=[]
    player_score=0
    comp_score=0
    player_ace_count=0
    comp_ace_count=0
    print(logo)
    for _ in range(2):
        player_card_list.append(deal_cards())
        comp_card_list.append(deal_cards())
    player_score =sum(player_card_list)
    comp_score= sum(comp_card_list)
    if player_score == 21:
        print("We have a BlackJack!!! WoW, You WIN !!!!")
        print(f"		Your cards:{player_card_list}")
    elif comp_score == 21:
        print("We have a BlackJack!!! The Dealer Wins this time")
        print(f"		Your cards:{comp_card_list}")
        print(f"		Your cards:{player_card_list}")
    else:
        print(f"		Your cards:{player_card_list}, current score: {player_score}")
        print(f"		Computer's first card: {comp_card_list[0]}")
        continue_play=True
        while continue_play == True:
            play_option = input("Type 'y' to get another card, type 'n' to pass: ")
            if play_option == "y":
                player_card_list.append(deal_cards())
                player_score=sum(player_card_list)
                print(f"		Your cards:{player_card_list}, current score: {player_score}")
                print(f"		Computer's first card: {comp_card_list[0]}")
            else:
                check_for_ace(player_card_list,comp_card_list)
                comp_score=sum(comp_card_list)
                player_score=sum(player_card_list)
                while comp_score < 17:
                    comp_card_list.append(deal_cards())
                    comp_score = sum(comp_card_list)      
                print(f"		Your final hand: {player_card_list}, final score: {player_score}")
                print(f"		Computer's final hand: {comp_card_list}, final score: {comp_score}")
                check_who_wins(player_score,comp_score)
                continue_play = False

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()