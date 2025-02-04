#This program is titled 'Dealing Cards'. Using the random package, 
# it will randomly select a number of cards based on the users input.
#Gavin Van Horn
#February 3rd, 2025
import random as ran
card_deck = ["A", "2", "3", "4", "5", "6",
             "7", "8", "9", "10", "J", "Q", "K"]

card_suit = ["c", "d", "h", "s"]

cards_in_hand = int(input("Enter the number of cards per hand: "))

print(f"Possible card values are {card_deck}\n")

print("Card suits are represented as follows: " 
f"Clubs = {card_suit[0]}, " 
f"Diamonds = {card_suit[1]}, " 
f"Hearts = {card_suit[2]}, "
f"Spades = {card_suit[3]} \n")

count = 1
print("Drawing cards now!\n")
for cards in range(cards_in_hand):
    selected_card = ran.choice(card_deck) + ran.choice(card_suit)
    print(f"Card {count} is {selected_card}. \n") 
    count += 1
print("Good luck!")