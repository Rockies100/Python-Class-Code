#This program is called 'Guess my Number'. A random number between 1 and 100 will be generated. The user must guess the number
#to win. The game continues until the number is guessed correctly.
#Gavin Van Horn
#February 26th, 2025
from random import randint

def num_game():
    play_game = input("Would you like to play 'Guess my Number'? (Y/N): ").strip().upper()
    if play_game == 'Y':
        correct_num = randint(1,100)

        user_guess = int(input("Guess a number between 1 and 100: "))

        guess_count = 1

        while user_guess != correct_num:
            print(f"Guesses = {guess_count}")
            print("Sorry, that is incorrect. ")
            user_guess = int(input("Guess again: "))
            print()

            guess_count += 1

        print(f"{correct_num} is correct! Congratulations!! You have won 'Guess my Number'. Thank you for playing!" )
    elif play_game == 'N':
        print('Maybe next time...')
    else:
        print("Invalid input. Try again")
        return num_game()
num_game()