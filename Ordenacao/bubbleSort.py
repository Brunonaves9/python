"""
O Bubble Sort é um algoritmo de ordenação simples, porém ineficiente em termos de desempenho, 
que funciona comparando repetidamente pares de elementos adjacentes em uma lista e trocando-os se 
estiverem na ordem errada. O algoritmo continua passando pela lista até que nenhum par de elementos 
precise ser trocado, o que indica que a lista está ordenada. O nome "Bubble" (bolha) vem do fato 
de os elementos "bolharem" para suas posições corretas conforme as trocas são feitas.

Aqui está uma descrição passo a passo do algoritmo Bubble Sort:

1 - Percorra a lista de elementos a serem ordenados da esquerda para a direita.
2 - Compare o elemento atual com o próximo elemento na lista.
3 - Se o elemento atual for maior do que o próximo elemento, troque-os de lugar.
4 - Continue comparando e trocando os elementos à medida que avança pela lista, até chegar ao final.
5 - Repita os passos 1 a 4 para cada elemento na lista, percorrendo a lista várias vezes até que nenhum 
elemento precise mais ser trocado em uma passagem completa.
"""
def bubbleSort(lista):
    n = len(lista)

    for i in range(n-1, 0, -1):
      for j in range(i):
        if lista[j] > lista[j+1]:
          # Swap
          temp = lista[j]
          lista[j] = lista[j+1]
          lista[j+1] = temp
    return lista

A = [31, 41, 59, 62, 42, 58]

print(bubbleSort(A))