# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:53:52 2024

@author: tkhan
"""

# Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat 4 slices of pizza. The local pizza shop sells pizzas of only 6 slices. What is the minimum number of pizzas needed? - Use Floor division

total_slices = 4*4
number_of_pizzas = (total_slices+5)//6
slices_left = number_of_pizzas*6 - total_slices
print('Number of pizzas required is',number_of_pizzas,'there will be',slices_left,'remaining slices.')
