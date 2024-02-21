# Protocolos e Tipos Primários
Todas as informações que usaremos durante a programação são representadas na memória do computador através de um tipo de dado, você também vai ouvir os termos classe ou categoria para se referir a mesma coisa.

Lá no comecinho do treinamento nós falamos brevemente que o computador só entende sequencias de 0 e 1, os binários, portanto quando fazemos uma atribuição como numero = 65 o Python precisa preparar o espaço de memória necessário para armazenar o binário 1000001 e junto deste valor armazenar a referencia aos métodos e operações suportadas pelo número.

Você pode abrir um terminal Python agora ai e verificar:

```
python3 -c "print(bin(65))"
'0b1000001'
```
Acontece que caso nosso valor seja um texto como em letra = "B" o valor "B" vai precisar ser armazenado também como uma sequência binária, e você pode verificar no seu terminal Python.
```
python -c "print(chr(66))"
B
```
e
```
python3 -c "print(bin(66))"
0b1000010
```
No caso do texto o Python precisa armazenar a sequência binária 1000010 e também junto deste valor armazenar a referência para a tabela de caracteres onde na posição 66 teremos a letra B.

Em Python podemos representar esta analogia com:
```
# Colocamos um valor no fichário usando a Atribuição
# aproveitamos para colocar uma etiqueta escrita o identificador "letra"
>>> letra = "B"

# Python teve que achar uma pasta vazia para armazenar nosso valor
# a função id() nos diz qual é número dessa posição
>>> id(letra)
139862029254896

# Python precisou colocar o valor "100010" dentro de um envelope
# neste envelope contém também instruções de como usar este valor para obter
# a letra "B".
# a função type() nos diz qual tipo de envelope foi usado
>>> type(letra)
str
```

## Porque usamos tipos de dados?
Para não precisar manipular os dados manualmente, por exemplo, não precisamos nos preocupar com o fato de que cada letra de um texto é armazenada como um número binário, usamos os tipos de dados definidos pelas classes para utilizar abstrações que nos entreguem diretamente a letra "B" que queremos.

Também não precisamos nos preocupar com a posição da memória, para nós tanto faz se o Python armazenou na primeira ou na última pasta da memória, o importante em nossa camada de abstração é sabermos qual é a etiqueta colada lá, e quando precisamos do valor usamos a etiqueta para encontrar, portanto se quisermos obter o "B" usamos a referência "letra".
```
>>> print(letra)
B
```
Existem vários tipos de dados para representar uma infinidade de valores e podemos também criar os nossos próprios tipos de dados.

Eles estão divididos em 2 categorias, os primários e os compostos, vamos começar explorando os primários e depois que entendermos todo os seu funcionamento passaremos para os tipos compostos.

### Primários
Os tipos primários também chamados de tipos "escalares" (scalar types) são utilizados para armazenar uma única unidade de informação como por exemplo um número ou um texto como vimos anteriormente.

### Inteiros
O tipo usado para armazenar os números inteiros em Python é representado pela classe int, em Python nós não precisamos declarar qual o tipo de dado a ser usado pois o Python faz a inferência de tipos dinâmicamente, o interpretador primeiro verifica como o valor se parece e então decide por conta própria qual a classe a ser utilizada, exemplos de uso de int
```
# a idade de uma pessoa
idade = 25

# o código de um produto
codigo_produto = 4587

# quantidade de itens
quantidade = 3
```

Em qualquer um dos casos acima o Python irá armazenar como int e você pode usar a função type para verificar.
```
>>> type(idade)
int
```
Você até pode se desejar, forçar o tipo de dado explicitamente, mas isso é considerado redundante.
```
idade = int(25)  # isso funciona, mas é redundante
```
idade é um identificador que faz referência ao valor 25 e nós podemos fazer uma variedade de operações com este valor, essas operações fazem parte do que chamamos Protocolo do objeto, e quem define os protocolos que o objeto implementa é a classe int.

Você pode em seu terminal verificar todos os protocolos que o int implementa e se você está começando agora com Python pode ser que isso ainda não faça muito sentido, não se preocupe, nosso objetivo aqui no treinamento é deixar esses conceitos cada vez mais naturais para você.

Verificando quais comportamentos estão no protocolo de um tipo de dado.
```
>>> dir(int)
# atributos especiais da classse int
['__abs__',
 '__add__',
 '__and__',
 '__bool__',
 '__ceil__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__divmod__',
 '__doc__',
 '__eq__',
 '__float__',
 '__floor__',
 '__floordiv__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getnewargs__',
 '__gt__',
 '__hash__',
 '__index__',
 '__init__',
 '__init_subclass__',
 '__int__',
 '__invert__',
 '__le__',
 '__lshift__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__new__',
 '__or__',
 '__pos__',
 '__pow__',
 '__radd__',
 '__rand__',
 '__rdivmod__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rfloordiv__',
 '__rlshift__',
 '__rmod__',
 '__rmul__',
 '__ror__',
 '__round__',
 '__rpow__',
 '__rrshift__',
 '__rshift__',
 '__rsub__',
 '__rtruediv__',
 '__rxor__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__truediv__',
 '__trunc__',
 '__xor__',
 
 # daqui para baixo estão atributos públicos que podemos usar diretamente
 'as_integer_ratio',
 'bit_count',
 'bit_length',
 'conjugate',
 'denominator',
 'from_bytes',
 'imag',
 'numerator',
 'real',
 'to_bytes']
 ```
A lista acima exibe os nomes de todos os atributos dos objetos armazenados com a classe int, tudo o que começa com __ e termina com __ nós chamamos de métodos dunder e eles são atributos especiais do modelo de dados do Python, nós não precisamos usar esses atributos diretamente em nosso código (apesar de algumas vezes eles úteis), nós iremos utilizar abstrações que por baixo dos panos irão fazer a chamada para esses métodos.

Neste momento nós não vamos falar de todos eles pois são muitos e a idéia é que aos poucos você vá entendendo conforme utiliza, mas vamos explorar um exemplo simples e que provavelmente usaremos sempre.

### Float
Floats são parecidos com inteiros mas além de armazenar a parte inteira do número eles também podem armazenar o ponto flutuante, a fração, e são usados para armazenar resultados que não podem ser armazenados em inteiros, por exemplo.
```
>>> valor = 5 / 2  # cindo dividido por 2
>>> print(valor)
2.5
```
A presença de um . em um número faz com que o Python entenda que queremos armazena-lo em um objeto da classe float e assim como os inteiros ela possui todos os métodos especiais dunder para os protocolos que implementa e também métodos que são particulares apenas dos números floats.

Exemplos de uso de um float
```
# Resultados de divisão
valor = 5 / 2

# Coordenadas geográficas
latitude = -37.80467681 
longitude = 144.9659498

# Saldo de pontuação (em jogos por exempo)
pontos = 355.8
```

*NOTA Para trabalhar com dados monetários (dinheiro) damos preferência a um tipo especializado chamado Decimal ao invés de float mas não se preocupe que abordaremos isso em breve.*

### Booleanos
O tipo booleano é representado pela classe bool e ele pode armazenar apenas 2 estados Verdadeiro e Falso, em teoria poderiamos aplicar aqui a lógica binária e em nosso programa dizer que 0 é falso enquanto 1 é verdadeiro, e de fato é isso que Python faz por debaixo dos panos, porém para ficar com uma sintaxe mais bonita termos o tipo bool e suas variações True e False.

Quando utilizamos esse tipo? sempre que precisamos de flags, variavéis que podem estar em um desses dois estados, veja alguns exemplos:
```
# Tornar um usuário administrador
is_admin = True

# Verificar se o usuário quer continuar uma operação
continuar = False

# Definir se um produto está ativo em uma loja
active = True
```
Apesar de ser bastante simples, o tipo bool é muito útil e ele por sí só forma um protocolo chamado Boolean, com objetos booleanos podemos criar expressões condicionais, como as que criamos em nosso script hello.py
```
if current_language == "pt_BR":
    msg = "Hello, World!"
```

A parte current_language == "pt_BR" retorna um valor do tipo bool e sempre que usamos o statement if a expressão em seguida precisa obrigatoriamente retornar um objeto que tenha o protocolo Boolean assim como esse.

Veja em seu terminal:
```
# inicialize a variável
>>> current_language = "en_US"

# obtenha um bool através de comparação por igualdade
>>> current_language == "pt_BR"
False

# verifique o tipo diretamente
>>> type(current_language == "pt_BR")
bool

# Isso também funciona com números int
>>> type(1 == 1)
True
```
Se você rodar o comando dir(int) verá que na lista de métodos especiais tem um chamado __bool__ e é ele que é chamado quando fazemos operações if usando os inteiros.
```
if 500:
    print("Ok, 500 é um int que implementa __bool__")
```

Muitos objetos no Python implementam __bool__ e podem ser usados diretamente após o if mesmo que não exista uma expressão de comparação.

### NoneType
Em alguns casos precisamos inicializar uma variável porém ainda não temos o valor para armazenar nela, nesse caso usamos o objeto None
```
>>> type(None)
NoneType
```
Este é um tipo especial que serve para quando não possuimos um valor mas precisamos da variável definida pois em algum momento no decorrer do programa iremos refazer a atribuição daquela variável.
```
produto = None

if produto is None:
    produto = funcao_para_definicao_do_produto()
``` 
O objeto None é um singleton, só existe um None mesmo que você defina várias variáveis como None todas elas farão referência ao mesmo None
```
>>> a = None
>>> b = None

>>> id(a)
139862040616512

>>> id(b)
139862040616512

>>> a is b
True

a == b
True
```

### Textos
### Caracteres
Agora sim vamos falar do último dos 4 tipos primários que abordaremos que é o tipo usado para armazenar texto.

Tudo o que você aprendeu até agora sobre protocolos e métodos especiais também se aplica aos textos, mas os textos tem uma pequena particularidade, eles são formados por caracteres.
```
>>> chr(65)
A
>>> chr(66)
B
>>> chr(67)
C
```
Portanto o texto "ABC" internamente contém um conjunto de 3 caracteres em suas respectivas posições na tabela de caracteres.

Existem várias tabelas de caracteres usadas na computação mas nesse treinamento vamos ficar em apenas duas ascii e utf8.

A tabela ASCII possui 128 posições, ou seja, vai do 0 ao 127 e em cada posição armazena apenas um caracter.

Estes são os carecteres básicos da lingua inglesa e como pode perceber ela não considera acentuação ou carecteres especiais de outros idiomas como Russo ou Mandarim.

Quando a computação globalizou foi preciso mudar de tabela e adotar uma maior que pudesse comportar uma quantidade universal de caracteres e também os emojis que se tornaram parte da comunicação moderna.

A tabela unicode de 8 bits - utf8 atualmente tem 120 mil caracteres.

https://unicode-table.com/en/

Nesta tabela além da tabela ASCII padrão, apartir da posição 128 temos acentuação e sub tabelas para simbolos e emojis.

Na tabela ASCII cada caracter ocupava menos de 1 byte (7 bits) e por isso que A é 65 que na tabela é 1000001 (7 digitos).

Já na tabela unicode cada caractere pode ser formado por mais de um byte, por exemplo, uma letra com acento Ã ocupa 2 bytes 11000011 10000011 na tabela.

E alguns emojis como o 🍉 ocupam 4 bytes 11110000 10011111 10001101 10001001

Durante a programação com Python nós iremos considerar que nossos textos utilizam os caracteres disponíveis na tabela utf8 e em alguns raros casos no Python3 teremos que explicitamente fazer operações de encode e decode a partir de um texto ascii para utf-8.

```
# variável
fruit = "🍉"

# para transmitir este texto ou gravar em um arquvivo
# ou banco de dados pode ser necessário encodificar ele.
>>> fruit.encode("utf-8")
b'\xf0\x9f\x8d\x89'
```

Esse valor b'\xf0\x9f\x8d\x89' é um objeto do tipo bytes e repare que ele tem 4 elementos separados por \ cada um deles é um dos bytes que formam a 🍉

A operação contrária, por exemplo quando lermos de um arquivo ou banco de dados que não suporta utf8 será com o decode.

```
melancia_em_bytes = b'\xf0\x9f\x8d\x89'
>>>  melancia_em_bytes.decode("utf-8")
'🍉'
```

O objeto ali iniciado por b'' é uma sequencia de bytes em formato hexadecimal a titulo de curiosidade
```
f0 = 11110000
9f = 10011111
8d = 10001101
89 = 10001001
```

Que são os 4 bytes que formam o carecte 🍉 e você pode verificar isso no Python com cada um dos valores da lista:
```
>>> hex(0b11110000)
'0xf0'
```
Em Python números começados com 0b são binários e 0x são hexadecimais.

### Strings, ou cadeia de caracteres
Até aqui falamos de caracteres isolados como A, B, 🍉 mas ao programar também precisaremos juntar esses carecteres para formar palavras e frases, quando criamos uma variável do tipo texto em Python ele através da presença de aspas sejam elas simples ' ou duplas " armazena esse valor em uma classe do tipo str e este tipo de dado pode armazenar um ou mais caracteres.
```
>>> nome = "Bruno"
type(nome)
```
E como você já deve ter imaginado aqui estamos armazenando cada uma das letras B, r, u, n, o com seus respectivos bytes e sequencia posicional em um único objeto. (a plavra string significa corda, cadeia ou corrente),

A palavra "Bruno" é uma lista contendo em cada posição um caractere da tabela utf8.
```
>>> list(bytes(nome, "utf-8"))
[66, 114, 117, 110, 111]

>>> chr(66)
'B'

>>> chr(114)
'r'

>>> chr(117)
'u'

>>> chr(110)
'n'

>>> chr(111)
'o'
```

Bem, para guardar o nome "Bruno" você mais uma vez não precisa se procupar com esses detalhes todos, basta fazer nome = "Bruno" e usar este texto para efetuar as operações que você desejar, porém é muito útil saber como o objeto está implementado pois isso te permite efetuar operações como a que fizemos em nosso script hello.py
```
current_language = os.getenv("LANG", "en_US")[:5]
```

Sabendo que current_language poderia ter o valor en_US.utf8 nós usamos o protocolo Sliceable do objeto str para fatiar o texto e pegar somente os primeiros 5 caracteres.
```
>>> "en_US.utf8"[:5]
'en_US'

>>> "Bruno"[2]
'u'

>>> "Python"[0]
'P'
```
O tipo str possui a maioria das carecteristicas que já abordamos nos outros tipos de dados e uma grande quantidade de protocolos implementados, vamos ver alguns.
```
# Sliceable (pode ser fatiado)
>>> "Bruno"[1]
'r'
# que internamente invoca o método `__getitem__`
>>> "Bruno".__getitem__(1)
'r'

# Addible (pode ser adicionado a outro texto)
# Essa operação se chama "Concatenação"
>>> nome = Bruno" 
>>> sobrenome = "Rocha"
>>> nome + " " + sobrenome
'Bruno Rocha'
# que internamente invoca o método `__add__`
>>> nome.__add__(" ".__add__(sobrenome))
'Bruno Rocha'

# Multipliable (que pode ser multiplicado)
>>> "Bruno" * 5
'BrunoBrunoBrunoBrunoBruno'

# Iterable (que pode ser iterado/percorrido)
>>> for letra in "Bruno":
...     print("-->" + letra.upper())
-->B
-->R
-->U
-->N
-->O
# Internamente o statement `for` invoca o método `__iter__`
>>> iterador = "Bruno".__iter__()
>>> next(iterador)
'B'
>>> next(iterador)
'r'
```
Além disso tudo, o tipo str também oferece muitos métodos públicos, que nós podemos usar explicitamente e que são muito úteis.
```
>>> "Bruno".upper()
'BRUNO'

>>> "BRUNO".lower()
'bruno'

>>> "bruno rocha".capitalize()
'Bruno rocha'

>>> "bruno rocha".title()
'Bruno Rocha'

>>> "bruno rocha".split(" ")
['bruno', 'rocha']

>>> "bruno".startswith("b")
True

>>> "bruno".endswith("b")
False

>>> "bruno rocha".count("o")
2

>>> "bruno rocha".index("c")
8
>>> "bruno rocha"[8]
'c'
```
E também algumas coisas que podemos fazer com qualquer objeto sequencial do Python:
```
>>> len("Bruno Rocha")
11

>>> sorted("Bruno Rocha")
[' ', 'B', 'R', 'a', 'c', 'h', 'n', 'o', 'o', 'r', 'u']

>>> list(reversed("Bruno Rocha"))
['a', 'h', 'c', 'o', 'R', ' ', 'o', 'n', 'u', 'r', 'B']
```