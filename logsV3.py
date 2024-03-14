#!/usr/bin/env python3

"""Script de aprendizado para 
escrever logs em tela

"""

__version__ = "0.0.1"
__author__ = "Juliano"
__license__ = "Unlicense"

import os
import logging
from logging import handlers

# Busca a informação de legal em Variável de Ambiente
# export LOG_LEVEL=debug
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# Configuração do Log
log = logging.Logger("app-logs", log_level)

fh = handlers.RotatingFileHandler(
    "logsv3.log", 
    maxBytes=10**6, 
    backupCount=7
)
fh.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
fh.setFormatter(fmt)
log.addHandler(fh)

# Exibição do Log
log.debug("Mensagem para Dev")
log.info("Mensagem geral para usuários")
log.warning("Mensagem de aviso que não causa erro")
log.error("Erro que afeta uma unica execução")
log.critical("Erro geral, afeta todo o sistema")
