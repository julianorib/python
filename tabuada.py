#!/usr/bin/env python

"""Aprendendo Python
Exemplo de Tabuada
"""

__version__ = "0.0.1"
__author__ = "Juliano"
__license__ = "Unlicense"

# variavel lista
# lista = [1,2,3,4,5,6,7,8,9,10]
# print(lista)

# variavel lista range
# numeros = range(1,11)
# numeros = list(range(1,11))
# print(numeros)

# Tabuada
numeros = list(range(1,11))

# Template
# %s string
# %d digito
# %f float
msg = "Numero %s x %s = "

for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(msg % (numero,outro_numero), numero * outro_numero)
    print("-" *15)