#!/usr/bin/env python

"""Aprendendo Python
Exemplo de Tabuada
"""

__version__ = "0.0.2"
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

for n1 in numeros:
    print()
    print("{:#^20}".format(f" Tabuada do {n1} "))
    for n2 in numeros:
        resultado = n1 * n2
        print("#"+"{:^18}".format(f"{n1} x {n2} = {resultado}")+"#")
    print("#" *20)
    print()