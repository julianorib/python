#!/usr/bin/env python3

"""Script de aprendizado com argumentos
Calculadora

Como usar:

python3 calc.py sum 5 5
./calc.py sum 5 5
"""

__version__ = "0.0.1"
__author__ = "Juliano"
__license__ = "Unlicense"

# essa classe permite trabalhar com arquivos
import os
# importando o modulo de datetime
from datetime import datetime

# essa classe permite usar os argumentos digitados.
import sys
# o argumento 0 é o próprio script. portanto, capturar a partir do 1.
arguments = sys.argv[1:]

# se os argumentos não forem preenchidos, deverá solicitar através de imput.
if not arguments:
    operation = input("operação: ")
    n1 = input("primeiro número: ")
    n2 = input("segundo número: ")

# coloca em uma lista os itens digitados
    arguments = [operation, n1, n2]

# calcula o tamanho da lista, que tem que ser 3.
elif len(arguments) != 3:
    print("Argumentos inválidos")
    print("Ex: python3 calc.py sum 5 5")

# finaliza o programa com erro, pois não foi informado os argumentos corretamente.
    sys.exit(1)

# desempacotamento da variavel arguments
operation, *nums = arguments

# validar operações disponíveis
operacoes = ("sum","sub","mul","div")
if operation not in operacoes:
    print("operação inválida")
    print("opções disponíveis: ", operacoes)

# finaliza o programa com erro, pois não foi informado os argumentos corretamente.
    sys.exit(1)

# desempacotamento da variavel nums
n1, n2 = nums

# converter em inteiro
n1 = int(n1)
n2 = int(n2)

# fazer as operações
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

# definindo pasta e arquivo de log
path = os.curdir
filepath = os.path.join(path, "calc.log")

# definindo datetime do log
timelog = datetime.now().isoformat()

# Salvando a operação no log
with open(filepath, "a") as file:
    file.write(f"{timelog} {operation}, {n1}, {n2} = {result} \n")

print(f"O resultado é: {result}")