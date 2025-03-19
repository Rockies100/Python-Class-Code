#This file defines the coin class used in the main file coin game.
#Gavin Van Horn
#March 18th, 2025

import random as ran

class Coin:
    def __init__(self):
        self.__amount = 20
        self.__sideup = 'Heads'
    
    def toss(self):
        if ran.randint(0,1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"
    
    def get_sideup(self):
        return self.__sideup
    
    def set_amount(self, result):
        self.__amount += result

    def get_amount(self):
        return self.__amount