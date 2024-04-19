#!/usr/bin/env python3

"""Script de aprendizado

Como usar:

python3 hello.py
./hello.py
"""

__version__ = "0.0.2"
__author__ = "Juliano"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG","en_US")[:5]

#dicionario
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá mundo",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])
