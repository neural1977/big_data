# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:07:28 2020

@author: francesco
"""

def check_cond(cond): 
    if (cond):
        print("Vero")
    else:
        print("Falso")
        
def calculate_occurencies(stringa_input):
    d_temp = {}

    for char in stringa_input.lower():
        occ = d_temp.get(char, 0)
        if occ == 0: 
            d_temp.update({char : 1})
        else: 
            d_temp[char] += 1
            
    return d_temp

