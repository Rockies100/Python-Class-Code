#This program is titled 'Coin match'. The game imports a coin class and plays a coin toss based game.
#The winner is the player with the most coins at the end.
#Gavin Van Horn
#March 18th, 2025.
from class_coin import Coin

def coin_match():
    player_1 = Coin()
    player_2 = Coin()

    play_game = input('Would you like to play the coin match game? (Y/N) :').strip()

    while play_game == 'y' or play_game == 'Y':
        player_1.toss()
        player_2.toss()

        print(f"Player 1 tossed a {player_1.get_sideup()}")
        print(f"Player 2 tossed a {player_2.get_sideup()}")

        if player_1.get_sideup() == player_2.get_sideup():
            player_1.set_amount(1)
            player_2.set_amount(-1)

            print("The coins matched! Player 1 gets a coin from Player 2!")
        else:
            player_1.set_amount(-1)
            player_2.set_amount(1)

            print("The coins did not match! Player 2 gets a coin from Player 1!")

        print(f"Player 1 has {player_1.get_amount()} coins.")
        print(f"Player 2 has {player_2.get_amount()} coins.")
        if player_1.get_amount() == 0 or player_2.get_amount() == 0 :
            break
        play_game = input('Would you like to toss again? (Y/N) :').strip()
    
    print(f"Thanks for playing. Player 1 finished with {player_1.get_amount()} coins. Player 2 finished with {player_2.get_amount()} coins.")
    if player_1.get_amount() > player_2.get_amount():
        print('Player 1 wins!!')
    elif player_2.get_amount() > player_1.get_amount():
        print('Player 2 wins!!')
    else:
        print('The players have tied!!')

coin_match()
    
