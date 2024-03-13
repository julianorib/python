#!/usr/bin/env python

"""Trabalhando com templates e strings"""

__version__ = "1.0"
__author__ = "Juliano"

email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Clique agora em %(link)s

Apenas %(qtde)02d disponiveis!

Preço promocional %(preco).2f
"""

clientes = ["Maria","João","Juliano"]

for cliente in clientes:
    print(email_tmpl % {"nome": cliente ,"produto": "Notebook","link":"www.notebook.com","qtde": 3, "preco":5000})