#!/usr/bin/env python3

"""Script de aprendizado para 
escrever logs

"""

__version__ = "0.0.1"
__author__ = "Juliano"
__license__ = "Unlicense"

import logging

logging.debug("Mensagem para Dev")
logging.info("Mensagem geral para usuários")
logging.warning("Mensagem de aviso que não causa erro")
logging.error("Erro que afeta uma unica execução")
logging.critical("Erro geral, afeta todo o sistema")

print("-"*30)

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("Deu erro %s", str(e))