#!/usr/bin/env python3

"""Script de aprendizado para 
tratamento de erros

"""

__version__ = "0.0.1"
__author__ = "Juliano"
__license__ = "Unlicense"

import os
import sys

# EAFP - Easy to ask forgiveness than permission
# Giria - É mais facil pedir perdão do que permissão

try:
    names = open("names.txt").readlines() #FileNotFoundError
    #1 / 0 # ZeroDivisionError
    1 / 1
except FileNotFoundError:
    print("Error: File names.txt not found")
    sys.exit(1)
except ZeroDivisionError:
    print("Error: You cant divide by zero")
    sys.exit(1)

try:
    print(names[2])
except IndexError as e:
    print(f"{str(e)}")
    print("Error: Missing name in the list")
    sys.exit(1)