# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:33:02 2020

@author: francesco
"""

def check_even_odd(num):

    if num % 2 == 0 :
        print("Il numero è pari")
    else:
        print("Il numero è dispari")
        
    if num % 3 == 0 :
        print("Il numero è multiplo di 3")
    else:
        print("ma non è multiplo di 3")
    
def evens(x, check=False, check2=True):
    ''' Verifica se un numero è pari'''
    l_evens = []
    while x:
        x -= 1
        if not x % 2 == 0:
            continue      # PRINT ODDS
        
        l_evens += [x]
        
    return l_evens

def evens_fast(x):

    return [i for i in range(x) if i%2 == 0]

def square(n):
    return n**2