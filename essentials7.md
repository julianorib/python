# Tipos compostos
Com os tipos primários temos a limitação de representar apenas uma única informação em cada objeto, porém existem casos em que desejamos compor um objeto único que contém mais de uma informação e para isso usamos os tipos compostos.

## Tuplas
As tuplas são o tipo composto mais simples de todos e bastante comum de serem usadam em Python, da mesma forma que anteriormente vimos que a string "ABC" é uma sequência de carecteres, com as tuplas conseguimos fazer uma sequência de valores que podem ser de qualquer tipo.

Exemplo de um sistema que armazena coordenadas sem o uso de tuplas:
```
coord_x = 140
coord_y = 200
coord_z = 9
```
Coordenadas desta forma são muito úteis em softwares de desenho gráfico ou mapas, ali temos a reta x e a reta y de um plano cartesiano, e ainda estamos adicionando a coordenada z que é a profundidade, usada em sistemas 3d.

Cada uma das coordenadas se refere a um ponto nessa reta e para definir um único ponto nós usamos 3 variáveis e isso fica muito dificil de manter caso nosso sistema tenha muitas dessas coordenadas, e ai que entram as tuplas.
```
coord = 140, 200, 9

# ou

coord = (140, 200, 9)
```
Em Python sempre que um ou mais objetos forem encadeados com , isso será interpretado como um objeto do tipo tupla e a tupla pode opcionalmente ter paranteses, nos já usamos tupla lembra? quando falamos de interpolação de textos.
```
"Olá %s você é o %03d da fila" % (nome, senha)
```
No exemplo acima de interpolação os parenteses são obrigatórios mas no caso das nossas coordenas o jeito mais comum de declarar é mesmo usando a sintaxe sem os parenteses e usar os parenteses comente quando for necessário para desambiguar
```
coord = 140, 200, 9
```
Portanto com este tipo de objeto não temos mais as variaveis x e y e z, agora temos uma única coord e para acessar os objetos que estão dentro da tupla usamos o protocolo de subscrição, os objetos que possuem um método chamado __getitem__ permitem que a gente acesse seus elementos usando [ ] e nós também já fizemos isso lá no primeiro script quando fatiamos a variável de ambiente. (current_language = os.getenv("LANG")[:5])

Então digamos que precisamos em nosso jogo posicionar um objeto na tela naquela exata coordenada como fazemos?
```
coord = 140, 200, 9

mover_x_para_coordenada(coord[0])
mover_y_para_coordenada(coord[1])
mover_z_para_coordenada(coord[2])
```
Repare que podemos acessar coord[0] e assim por diante usando [numero] e este número se refere a posição do valor que queremos dentro da tupla.

Nestes casos, assumimos que seu software na hora de criar a variavel coord se encarrega de colocar cada coisa em seu devido lugar :)

Existe uma infinidade de usos práticos para as tuplas, nós ainda falaremos muito delas durante o treinamento e faremos os principais usos como em retorno de funções e leitura de banco de dados.

### Desempacotamento
A caracteristica mais interessante das tuplas se chama unpacking ou desempacotamento em português. (algumas linguagens chamam isso de spread, espalhamento, explode)

O desempacotamento permite fazer a operação contrária da atribuição olha que interessante.
```
# Empacotamento (atribuição)
coord = 140, 200, 9

# Desempacotamento (atribuição multipla)
x, y, z = coord
```
No desempacotamento o Python automaticamente vai pegar cada um dos elementos da tupla e usar para definir as variaveis que separarmos por ,.

*Aliás, está ai uma dica que ainda não falamos, é possível atribuir mais de uma variável ao mesmo tempo em Python a = b = c = d = None faz com que todas sejam referencias para None*

### Imutabilidade
Outra caracteristica importante e que talvez seja decisiva na hora de escolher usar tuplas é o fato de que elas são imutáveis, uma vez criada a tupla, não é possivel alterar, não dá para mudar os valores ou adicionar novos. (este tópico contém algumas excessões que veremos na nossa aula sobre escopos)

### Algumas coisas que podemos fazer com as tuplas
```
# Atribuir sem parenteses
coord = 140, 200, 9

# atribuir com parenteses
coord = (140, 200, 9)

# desempacotar
x, y, z = coord

# ignorar elementos (será atribuito apenas o x)
x, *_ = coord

# pegar apenas o primeiro e o último elemento
x, *_, y = coord

# Verificar o tamanho
len(coord)
3

# Acessar via subscrição pelo indice
coord[0]
140

# fatiar
coord[1:]
(200, 9)
```


## Listas
Listas são bastante similares as tuplas e a maioria das operações que podemos fazer com tuplas também podemos fazer com as listas, uma das grandes diferenças está na implementação de protocolos de edição dos elementos, portanto as listas são mutáveis e permitem que incluamos novos itens, permitem a remoção de itens existentes e a reordenação.

As listas são criadas usando os literais [ ] ou a chamada para a classe list

Criando uma lista vazia
```
colors = []  # forma preferida
# ou
colors = list()
```

Adicionando elementos ao final da lista
```
colors.append("green")
```

Adicionando elementos ao inicio da lista
```
colors.insert(0, "red")
```

Adicionando em uma posição especifica
```
colors.insert(2, "blue")
```

Obtendo o tamanho da lista
```
len(colors)
```

Acessando elementos via indice
```
button_color = colors[0]
```

Desempacotamento (igual as tuplas)
```
red, green, blue = colors
```

E também é possível já iniciar uma lista com valores.
```
>>> colors = ["red", "green", "blue"]
>>> colors[0]
"red"
```

Podemos somar 2 listas (criando uma nova lista como resultado)
```
>>> nova_lista = colors + ["yellow"]
>>> print(nova_lista)
["red", "green", "blue", "yellow"]
```

E podemos extender uma lista in-place
```
>>> colors.extend(["purple"])
>>> print(colors)
["red", "green", "blue", "purple"]

# Ou usando um operador de acréscimo
>>> colors += ["purple"]
>>> print(colors)
["red", "green", "blue", "purple"]
```

Remover elementos
```
colors.remove("purple")
# ou
colors.pop()
```

Contar elementos
```
>>> colors.count("green")
1=
```

Mais uma vez vos digo que existe uma infinidade de coisas interessantes para fazermos com a lista e faremos tudo em nossos exericios e projetos durante o treinamento.


## Sets
Na antiga 5 séria (atual 1 ano do ensino médio) aprendemos a teoria dos conjuntos

Python tem um tipo de objeto para representar este tipo composto, as caracteristicas de uso são bastante similares com listas e tuplas, mas é um objeto bastante particular e tem usos especificos.

Sets podem ser criados usando as sintaxes:
```
# A partir de qualquer objeto iterável
iteravel = [1, 2, 3]  # list
iteravel = 1, 2, 3  # tuple
iteravel = "Banana"  # str

# usando a classe
set(iteravel)

# usando literais com { e }
{1, 2, 3, 4}

# desempacotando tuplas, listas ou textos
{*iteravel}
```
Aplicamos a teoria dos conjuntos usando operadores
```
>>> conjunto_a = [1, 2, 3, 4, 5]
>>> conjunto_b = [4, 5, 6, 7, 8]

# | para união
>>> set(conjunto_a) | set(conjunto_b)
{1, 2, 3, 4, 5, 6, 7, 8}

# & para intersecção
>>> set(conjunto_a) & set(conjunto_b)
{4, 5}

# – para diferença
>>>  set(conjunto_a) - set(conjunto_b)
{1, 2, 3}

# para ^ diferença simétrica
>>> set(conjunto_a) ^ set(conjunto_b)
{1, 2, 3, 6, 7, 8}
```

Interessante mas você pode estar se perguntando onde usar isso?

Pensa em uma rede social como o twitter, no conjunto A estao as pessoas que você segue, no conjunto B estão as que te seguem de volta, com este objeto você consegue determinar rapidamente quem não está te seguindo de volta.

Você pode também usar set para determinar quais seguidores você e algum amigo tem em comum na mesma rede social.

### Performance

Fazer buscar em sequencias é uma operação bastante pesada, imagina que no seu twitter você tem 5000 seguidores e você deseja buscar um deles ou fazer essas operações de comparação como fizemos com os conjuntos.

Se você tiver uma lista ["joao", "bruno", "maria", ...] contendo os elementos, e quiser por exemplo buscar pelo usuario "alfredo" o python vai ter que percorrer toda a lista e comparar elemento por elemento até encontrar o alfredo, e se o alfredo estiver no final? Vai demorar muito, essa é uma operação que tem uma complexidade algoritmica O(n) pois Python vai ter que efetuar uma comparação para cada item n da lista.

Os sets implementam uma hash table! 🎉

É como se eles tivessem um indice gravado neles com uma tabela invertida dizendo
```
"joao" -> "esta na posição 0"
"alfredo" -> "esta na posicao 345"
```

Portanto quando precisarmos buscar o alfredo o python olha primeiro essa tabela e já vai diretamente na informação que está em 345 como se fizessemos users[345] em uma lista e a complexidade desta operação passa a ser O(1) pois agora só tem uma comparação a ser feita.

Bom, eu estou super simplificando a idéia aqui para você, tem mais detalhes internos nessa implementação mas deu para sacar né?

Por quê isso importa? Sets são mais rápidos!

operações como if "alfredo" in usuarios: se usuarios for um set irá ser bem mais rápido do que caso usuarios seja uma lista ou tupla.

### Mutabilidade

Você pode criar um conjunto vazio e ir adicionando elementos e também pode remover elementos, eles são mutáveis
```
>>> a = set([1,2,3])
>>> a.add(4)
>>> a.remove(1)
>>> print(a)
{2, 3, 4}
```

### Deduplicação

Esta é uma das caracteristica mais interessante dos sets e talvez a sua maior utilidade, sets não permitem itens duplicados, então ao criar um set você elimina as duplicidades.
```
>>> conjunto = set()
>>> conjunto.add("Bruno")
>>> conjunto.add("Maria")
>>> conjunto.add("Bruno")
>>> conjunto.add("Maria")
>>> conjunto.add("Bruno")
>>> conjunto.add("Bruno")
>>> conjunto.add("Bruno")
>>> conjunto.add("Bruno")

# Digamos que por algum motivo (ou engano) adicionou o mesmo item mais de uma vez
# sem problemas :)

>>> print(conjunto)
{'Bruno', 'Maria'}

# E isso também functiona em tempo de atribuição
>>> {1, 2, 3, 1, 1, 1, 1, 5, 5, 5, 5}
{1, 2, 3, 5}
```

### Desvantagens dos sets?

Não respeitam a ordem de inserção, os elementos são ordenados automaticamente
Não permitem subscrição para acesso aos valores
Ou seja, você não pode fazer set[0] para acessar o primeiro elemento.
```
>>> conjunto = {4, 5, 6, 7, 8}

conjunto[0]
---------------------------------------------
TypeError   Traceback (most recent call last)
Input In [60], in <module>
----> 1 conjunto[0]

TypeError: 'set' object is not subscriptable
```

mas pode usar in ou converter o set em uma lista.
```
>>> 4 in conjunto
True


>>> list(conjunto)[0]
4
```


## Dicionários
Conhecidos também como HashMaps ou Arrays Associativos os dicionários são um misto entre o set e list e com certeza a estutura de dados mais importante da linguagem.

Curiosidade: Todos as tipos de dados do Python são implementados usando dicionários, os objetos possuem um método especial __dict__, experimente no terminal imprimir int.__dict__, até mesmo a resolução de nomes do Python é feita usando um dicionário __builtins__.__dict__ quando digitamos print o Python vai ali naquele dicionário verificar se existe uma função chamada print lá dentro.

Vamos entender para que servem os dicionários com este exemplo usando tipos primários.

```
produto_nome = "Caneta"
produto_cor1 = "azul"
produto_cor2 = "branco"
produto_preco = 3.23
produto_dimensao_altura = 12.1
produto_dimensao_largura = 0.8
produto_em_estoque = True
produto_codigo = 45678
produto_codebar = None
```

Acima estamos representando um único produto em um programa de vendas, é uma única caneta porém precisamos de 9 objetos de diferentes tipos.

E para resolver este problema que temos os tipos compostos, eles são containeres, objetos que podem agrupar mais de um tipo e mais de uma unidade de informação dentro deles.

Dicionários são criados com { } ou através da classe dict(), é bom ter cuidado para não os confundir com sets já que sets também usam { } e a diferença principal é o fato de que no set cada posição armazena apenas um valor e nos dicionários podemos colocar 2 valores em cada posição.

Um desses valores é chamado de chave key e o outro valor val e são separados por :, veja com um dicionário a mesma informação pode ser representada com:
```
produto = {
	"nome": "Caneta",
	"cor1": "azul",
	"cor2": "branco",
	"preco": 3.23,
	"dimensao_altura": 12.1,
	"dimensao_largura":  0.8,
	"em_estoque": True,
	"codigo": 45678,
	"codebar": None,
}
```

Agora temos um único objeto produto do tipo dict e isso torna nosso programa muito melhor organizado, facilita operações e deixa a complexidade menor também pois os dicionários assim como os sets também implementam a Hash Table, ou seja, as operação de acesso são O(1) super rápidas.

Assim como as listas os dicionários podem receber subscrições a partir de uma chave, ou seja, usamos [] e dentro passamos a key que queremos acessar.

```
>>> produto["nome"]
'Caneta'
>> produto["codigo"]
45678
```

Além disso podemos diminuir a redundancia colocando objetos compostos dentro do dicinário, ao invés de 2 chaves para representar cor podemos criar uma lista de cores e ao invés de 2 chaves para dimensoes podemos ter um subdicionário.
```
produto = {
	"nome": "Caneta",
	"cores": ["azul", "branco"],
	"preco": 3.23,
	"dimensao" {
        "altura": 12.1,
	    "largura":  0.8,
    },
	"em_estoque: True,
	"codigo": 45678,
	"codebar": None,
}
```

As chaves de um dicionário podem ser de qualquer tipo de dados que seja compatível com hash table, exemplo:
```
d = {
    10: "Bruno",
    True: 45,
    False: None,
    None: True,
    (4,5,6): "uma tupla", 
}

>>> d[(4, 5, 6)]
'uma tupla'

```
Mas não podemos usar tipos unhashable.

```
d = {[1, 2, 3]: "uma lista"}
...
TypeError: unhashable type: 'list'
```

Já os valores podem ser de qualquer tipo sem restrições!

### Sintaxe
Podemos iniciar um dicionário vazio e depois ir adicionando elementos dentro dele.
```
cliente = {}
# ou
cliente = dict()
```

### CRUD
E usar as operações de CRUD (Create, Read, Update, Delete)

Criar - Adicionar chave+valor
```
cliente["nome"] = "Bruno"
```
Ler valor a partir de uma chave
```
>>> cliente["nome"]
'Bruno'
```
Update - Alterar valor a partir de uma chave

```
cliente["nome"] = "Bruno Rocha"
```

Delete - Remover um valor e sua chave.
```
del cliente["nome"]
```
*A keyword del remove uma variável que foi atribuida e pode ser usada com chaves de dicionários.*

### Buscas
O dicionário implementa Hash Table, ele também é conhecido como hash map e portanto as buscas em dicionário quando feitas por chave tem acesso constante O(1).

```
"nome" in cliente
True
```

in invoca o protocolo Lookupable através do método __contains__ e efetua a busca imediata sem necessidade de iterar todo o dicionário para encontrar uma chave, e assim como os sets as chaves não podem se repetir.

### Métodos de Lookup
Obter uma lista de chaves
```
cliente = {"nome": "Bruno", "cidade": "Viana"}

cliente.keys()
dict_keys(["nome", "cidade"])
```

Obter uma lista de valores
```
cliente.values()
dict_keys(["Bruno", "Viana"])
```

Obter uma lista de tuplas contendo chave e valor
```
cliente.items()
dict_items([("nome", "Bruno"), ("cidade", "Viana")])
```

Iterando com for
```
# apenas chaves
for key in cliente:
    print(key)

nome
cidade


# Buscando os valores com subscrição
for key in cliente:
    print(key, "-->", cliente[key])

nome-->Bruno
cidade-->Viana


# Com desenpacotamento de tuplas
for key, value in cliente.items():
    print(key, "-->", value)

nome-->Bruno
cidade-->Viana
```

### Combinando 2 dicionários
```
# informacao original
cliente = {"nome": "Bruno", "cidade": "Viana"}

# informacao adicional
extra = {"pais": "Portugal"}

# Informação final
final = {**cliente, **extra}
print(final)
{"nome": "Bruno", "cidade": "Viana", "pais": "Portugal"}
```

Ou fazendo update in place.
```
# informacao original
cliente = {"nome": "Bruno", "cidade": "Viana"}

# informacao adicional
extra = {"pais": "Portugal"}

# Cliente atualizado
cliente.update(extra)
print(cliente)
{"nome": "Bruno", "cidade": "Viana", "pais": "Portugal"}
```

### Erros
Caso uma chave não exista no dicionário o Python estoura um erro chamado KeyError
```
print(cliente["telefone"])
...
KeyError 'telefone'
```

Para evitar o erro podemos usar o método get que busca a chave e caso não exista retorna um valor padrão que inicialmente é None
```
print(cliente.get("telefone"))
'None'

print(cliente.get("telefone", "191"))
'191'
```
