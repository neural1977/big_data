'''
Created on 20/02/2020
Modified on 20/01/2020

@author: Francesco Pugliese
'''

#import tensorflow as tf
#import keras as tf
import pandas as pd
import numpy as np
import sklearn as sc
import matplotlib as mb
import pdb
#import timeit
from timeit import default_timer


start = default_timer()

print("Hello world!")

lista = [123, "spam", 1.23, "eggs"]
lista1 = lista + ["Francesco"]
print(lista, lista[0], lista[0:2])
print(lista1)
print(lista * 2)
lista[2] = "Giovanni"
print(lista)
for epoch in range(10):
    print("Epoch: ", epoch)
print("Total time : ", default_timer() - start)
print(lista.index("spam"))
pdb.set_trace()

