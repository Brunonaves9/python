"""
Em Python, funções são blocos de código que realizam uma tarefa específica e podem ser reutilizados 
em diferentes partes de um programa. As funções permitem que você divida seu código em partes 
menores e mais gerenciáveis, tornando-o mais legível e modular. Aqui estão os conceitos fundamentais 
relacionados a funções em Python:

Definindo uma Função:
Para definir uma função em Python, você usa a palavra-chave "def", seguida pelo nome da função e 
parênteses que podem conter parâmetros (argumentos) necessários para a função.
"""
# Recebe dois parâmetros e realiza a soma e imprime o resultado
def soma(a, b):
    print(a + b)

a = 5
b = 4

soma(a, b)

# Recebe dois parâmetros e realiza a multiplicação, mas retornando o valor.
def multiplica(a,b):
    return a * b

print(multiplica(a,b))

"""
Funções são uma parte essencial da programação, permitindo que você escreva código modular e reutilizável.
"""