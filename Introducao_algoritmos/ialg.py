"""
INTRUDOÇÃO AOS ALGORÍTMOS
- Operadores
- Variáveis
- Condicional
- Loops
"""

# OPERADORES
"""
------------------------------------------------------------------------------------------------------------
1 - Operadores Aritméticos:
(+) - Adição
(-) - Subtração
(*) - Multiplicação
(/) - Divisão (geralmente retorna um número de ponto flutuante)
(//) - Divisão inteira (retorna o quociente inteiro)
(%) - Módulo (retorna o resto da divisão)
(**) - Exponenciação (por exemplo, 2 ** 3 é igual a 8)

------------------------------------------------------------------------------------------------------------
2 - Operadores de Comparação (Relacionais):
(==) - Igual a
(!=) - Diferente de
(<) - Menor que
(>) - Maior que
(<=) - Menor ou igual a
(>=) - Maior ou igual a

------------------------------------------------------------------------------------------------------------
3 - Operadores Lógicos:
(and) - Retorna True se ambas as condições forem verdadeiras
(or) - Retorna True se pelo menos uma das condições for verdadeira
(not) - Inverte o valor de uma condição

------------------------------------------------------------------------------------------------------------
4 - Operadores de Atribuição:

(=) - Atribuição simples
(+=) - Atribuição com adição (por exemplo, x += 1 é equivalente a x = x + 1)
(-=) - Atribuição com subtração
(*=) - Atribuição com multiplicação
(/=) - Atribuição com divisão
(//=) - Atribuição com divisão inteira
(%=) - Atribuição com módulo
(**=) - Atribuição com exponenciação

------------------------------------------------------------------------------------------------------------
5 - Operadores de Identidade:
(is) - Retorna True se dois objetos forem o mesmo objeto na memória
(is not) - Retorna True se dois objetos não forem o mesmo objeto na memória

------------------------------------------------------------------------------------------------------------
6 - Operadores de Associação (Membership):

(in) - Retorna True se um valor estiver presente em uma sequência (por exemplo, em uma lista ou string)
(not in) - Retorna True se um valor não estiver presente em uma sequência

------------------------------------------------------------------------------------------------------------
7 - Operadores Bit a Bit (Bitwise):
(&) - E bit a bit
(|) - OU bit a bit
(^) - OU exclusivo bit a bit
(~) - Negação bit a bit
(<<) - Deslocamento à esquerda
(>>) - Deslocamento à direita

------------------------------------------------------------------------------------------------------------
"""
 
# VARIAVEIS
"""
Em Python, as variáveis são usadas para armazenar dados, como números, texto, listas, 
objetos e muito mais. As variáveis são essenciais para a programação, pois permitem que você 
mantenha e manipule valores durante a execução do programa.
"""
### Declaração
"""
Para criar uma variável em Python, você simplesmente atribui um valor a um nome de variável. 
Não é necessário declarar explicitamente o tipo da variável; Python faz a inferência de tipo 
automaticamente.
"""
numeroA = 1
numeroB = 2
resultado = numeroA + numeroB

### Convenções de Nomes de Variáveis
"""
- Os nomes de variáveis em Python devem começar com uma letra ou um sublinhado (_).
- Eles podem conter letras, números e sublinhados.
- Python é sensível a maiúsculas e minúsculas, portanto, "idade" e "Idade" são tratados como nomes de variáveis diferentes.
"""

### Tipos de Dados de Variáveis
"""
Python suporta vários tipos de variáveis, incluindo inteiros, números de ponto flutuante, 
strings, listas, tuplas, dicionários, conjuntos, entre outros. O tipo de variável é determinado 
pelo valor atribuído a ela.
"""
numero = 42           # Inteiro
salario = 1500.50     # Ponto flutuante
nome = "João"         # String
numeros = [1,2,3,4,5] # Lista
boleano = True        # Boleano True (Verdadeiro) False (Falso)

### Constantes
"""
Embora Python não tenha constantes estritas, é uma convenção usar letras maiúsculas para nomes 
de variáveis que não devem ser alterados durante a execução do programa para indicar 
que são constantes.
"""
PI = 3.14159

# CONDICIONAIS
"""
Em Python, você pode usar estruturas condicionais para tomar decisões com base em condições. 
As estruturas condicionais permitem que o programa execute blocos de código diferentes, 
dependendo se uma condição é verdadeira ou falsa. As estruturas condicionais mais comuns em Python 
são as instruções if, elif e else. 
"""

### IF
idade = 18
if idade >= 18:
    print("Você é maior de idade.")

### IF e ELSE
idade = 15
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

### elif
nota = 75
if nota >= 90:
    print("Aprovado com nota A")
elif nota >= 80:
    print("Aprovado com nota B")
elif nota >= 70:
    print("Aprovado com nota C")
else:
    print("Reprovado")


# LOOPS
"""
Em Python, você pode usar loops para repetir a execução de um bloco de código várias vezes. 
Existem dois tipos principais de loops em Python: o loop for e o loop while. 
"""
### FOR
frutas = ["maçã", "banana", "laranjas"]

"""
for <elemnto que irá receber> in <elemento fornecedor>
"""
for fruta in frutas:
    print(fruta)

"""
O FOR pode ser utlizado para percorrer um tamanho específicado
"""
for i in range(1, 6): # Números de 1 ate 6
    print(i)

"""
Percorrendo o array, lendo seu tamanho e imprimindo a lista de acordo com a
sua posição.
"""
frutas = ["maçã", "banana", "laranjas"]
for i in range(len(frutas)):
    print(frutas[i])

### WHILE
"""
O loop while é usado quando você não sabe quantas vezes o código precisa ser repetido 
antecipadamente e a repetição é baseada em uma condição. Ele continuará a executar 
o bloco de código enquanto a condição especificada for verdadeira.
"""
contador = 1
while contador <= 5:
    print(contador)
    contador += 1


