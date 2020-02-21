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
#import utils 
from Utilities.utils import check_cond, calculate_occurencies
from Utilities.maths import check_even_odd

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
print(lista.index("spam"))                      # find index of spam word 
#pdb.set_trace()

listaNumeri = ["uno", "due", "tre"]
listaNumeri.append("quattro")
listaNumeri.insert(2,"cinque")
del listaNumeri[3]
listaNumeri.remove("quattro")
listaNumeri.sort(reverse=True)
print(listaNumeri)
numeri_l = [82,32,33, 2 ,2]
#pdb.set_trace()
print(type(numeri_l))
numeri_l.sort(reverse = True)
print(numeri_l)

numeri_s = {82, 32, 3, 2, 2}
print(type(numeri_s))
print(numeri_s)

numeri_t = (82, 32, 33, 2, 2)
print(type(numeri_t))
print(numeri_t)

string1 = "Francesco Pugliese"
string1_l = list(string1)
print(string1_l)
string2 = "".join(string1_l)
print(string2)
string3 = "-".join((string2," ciao"))
print(string3)
string1_l[2] = "pippo"
print(string1_l)
t1 = (12, "Pippo", 3.4)
t2 = (2, "Ciccio", 2.3)
t3 = (12, "Pippo", 3.4)
cond1 = t1 == t2
cond2 = t1 == t3
print(cond1, cond2)
tupla = (1,3.4, "Prova", [2,2], {3,1,1},(3,3), {0:"Francesco",1:"Michele"})
print(tupla)
print("\n\n\t\t",tupla[3])
print(tupla[2:4], tupla+({'a':0, 'b':1}, ))
print(tupla * 2)

lista_container = []
#lista_container = list()
for i in range(100):
    lista_container.append(i)
print(lista_container)
    
#tupla_container = ()
tupla_container = tuple()
for i in range(100):
    tupla_container+=(i,)
print(tupla_container)

set_container = set()
#lista_container = list()
for i in range(100):
    set_container.add(i)
print(set_container)
print (100 in set_container)

set_numeri = {1,3,4,5,5,6,6}
print(set_numeri)
try:
    set_numeri.remove(7)
except(LookupError):
    print("Idiota!!!")
set_numeri.discard(7)
print(set_numeri)

s1 = {1,2,3}
s2 = {3,4,5}
print(s1<=s2)
print(s1|s2, s1&s2, s1-s2, s1^s2, (s1|s2)-(s1&s2))

dd = {"Nome":"Francesco", 2:43, "Tipo": "Poco serio"}


print(dd)
print(dd.items())
print(dd.keys())
print(dd.get("Eta", 0))
for k in dd.keys():
    print(dd.get(k))

stringa_input = "Noi siamo i ragazzi del Master e siamo stufi abbiamo fame"
print(calculate_occurencies(stringa_input=stringa_input))

prova = 1
check_cond(prova)
    
s_vuoto = set({0})
check_cond(s_vuoto)
    
cond1 = True
cond2 = False
    
check_cond(cond1 and cond2)
check_cond(cond1 or cond2)
check_cond(not cond1)

check_even_odd(12)
check_even_odd(13)
check_even_odd(9)

print("Total time : ", default_timer() - start)
#pdb.set_trace()
    
