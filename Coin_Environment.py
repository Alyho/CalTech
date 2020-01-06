# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 18:40:36 2019

@author: student-minecraft
"""


import numpy as np

class coin_environment:

    def __init__(self):
       self.prob_heads = [0.9, 0.5, 0.7]
        
    def flip(self, coin_number):
        random_number = np.random.randint(0,2)
        
        if random_number == 0:
            return "heads"
        else:
            return "tails"
    
coin = coin_environment()

#print ("Coin 1 = " + coin.flip(1))
#print ("Coin 2 = " + coin.flip(2))
#print ("Coin 3 = " + coin.flip(3))        
    