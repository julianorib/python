#!/usr/bin/env python3

"""Script de aprendizado

Como usar:

python3 hello.py
./hello.py
"""

__version__ = "0.0.1"
__author__ = "Juliano"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG","en_US")[:5]
msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Olá Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)
