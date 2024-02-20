# Python

## Comandos do python
```
python3 -c "1"
python3 -c "print(1)"
```
```
python3 -c "juliano"
python3 -c "print('juliano')"
```
## Modulos / Bibliotecas
```
python3 -m site
```

Dentro de um projeto, adicionar:
```
import module
import os
```

## Terminal (interpretador)
```
python3
ipython ## Deve instalar com o pip
```

## Help
```
python3
```
```
>>> help()
>>> help(1)
>>> help(funcao)
>>> help(os)
```

## Trabalhar com Variáveis
```
variavel=Este.Texto
```

Mostra a quantidade de caracteres da variavel
```
len(variavel)
```

Quebra a variavel em 5 caracteres
```
variavel[:5]
```

Quebra a variavel por caractere especifico (.) e pega a primeira parte
```
variavel.split".")[1]
```

Definindo variável caso não exista
```
variavel = os.getenv("LANG","en_US")
```


## Ambiente Virtual
Ver Ambiente do Sistema. 
```
python3 -m site
```

Criar um novo ambiente virtual.\
Melhor prática de utilização.
```
python3 -m venv .venv
```

Ativar o novo ambiente virtual
```
source .venv/bin/activate
```

Ver qual python está ativo.
```
which python
```

**Lembrar de adicionar no .gitignore o .venv**

Gerenciador de pacotes do Python: <https://pypi.org>
```
python3 -m pip
```

Update do pip:
```
python3 -m pip install --upgrade pip
```

Instalar algum modulo, pacote, biblioteca, framework
```
python3 -m pip install pacote
```

Interpretator mais poderoso (color, autocomplete, help, etc)
```
python3 -m pip install ipython
```

```
ipython
In [1]:
```

## Formatação (Strings)

<pyformat.info>

Interpolação: \
Criar um Template com conjunto de itens a substituir por variáveis.
```
%s string
%d digito
%f float
```

Nomear os itens para facilitar.
```
%(nome)s
%(qtde)d
%(valor)f
```

Casas antes da virgula.
```
%(qtde)03d
```

Duas casas decimais.
```
%(valor).2f 
```

Exibindo e substituindo os valores.
```
var_template % ("Juliano",25,100.023)
var_template % ({"nome":"Juliano","qtde":25,"valor":100.023})
```