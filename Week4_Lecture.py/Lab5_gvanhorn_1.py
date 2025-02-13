#Title: 'Rolling Dice'. This program randomly rolls a set of die and prints a specified statement based on outcome of the roll.
#The dice are rolling one at a time, therefore to get a matching output, it has to match exactly.
#Gavin Van Horn
#February 12th, 2025
import random as ran

dice_value = [1, 2, 3, 4, 5, 6]

play_game = input("Would you like to roll the dice? (yes/no): ").strip().lower()
while play_game == 'yes':
    first_roll = ran.choice(dice_value)
    second_roll = ran.choice(dice_value)
    roll_total = first_roll + second_roll

    if roll_total in (2,3,5,9,12):
        roll_outcome=roll_total
    else:
        roll_outcome = f'{first_roll},{second_roll}'

    if roll_total == 2:
        print(roll_outcome)
        print('Snake Eyes')
    elif roll_total == 3:
        print(roll_outcome)
        print('Ace Caught a Deuce')
    elif first_roll == 2 and second_roll == 2:
        print(roll_outcome)
        print('Little Joe from Kokomo')
    elif roll_total == 5:
        print(roll_outcome)
        print('Little Phoebe')
    elif first_roll == 3 and second_roll == 3:
        print(roll_outcome)
        print('Jimmy Hicks from the Sticks')
    elif (first_roll == 6 and second_roll == 1):
        print(roll_outcome)
        print('Six Ace')
    elif roll_total == 9:
        print(roll_outcome)
        print('Nina from Pasadena')
    elif first_roll == 5 and second_roll == 5:
        print(roll_outcome)
        print('Puppy Paws')
    elif (first_roll == 6 and second_roll == 5):
        print(roll_outcome)
        print('Six Five no Jive')
    elif roll_total == 12:
        print(roll_outcome)
        print('Boxcars')
    else:
        print(roll_outcome)
        print('No win...')
    play_game = input("Would you like to roll the dice? (yes/no): ").strip().lower()
print('Thanks for rolling.')