#!/usr/bin/env python3

"""Script de aprendizado para 
tratamento de erros

"""

__version__ = "0.0.1"
__author__ = "Juliano"
__license__ = "Unlicense"

import os
import sys

# Método LBYB - Look before you leap
# Giria - Olhe antes de fazer / Valide antes de fazer

if os.path.exists("names.txt"):
    names = open("names.txt").readlines()
else:
    print("Error: File names.txt not found")
    sys.exit(1)


if len(names) >= 3:
    print(names[2])
else:
    print("Error: Missing name in the list")
    sys.exit(1)