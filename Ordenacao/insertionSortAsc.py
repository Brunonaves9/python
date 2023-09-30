"""
O Insertion Sort é um algoritmo de ordenação simples e eficaz que opera de forma semelhante à 
forma como muitas pessoas ordenam cartas de baralho em suas mãos. Ele funciona percorrendo a lista 
de elementos a serem ordenados e, a cada passo, inserindo o elemento atual na posição correta dentro 
da parte já ordenada da lista. O algoritmo começa com uma lista desordenada e, à medida que avança,
expande a região ordenada até que toda a lista esteja ordenada.

Aqui estão os passos básicos para entender o funcionamento do Insertion Sort:

1 - Comece com um único elemento na parte ordenada da lista. Isso pode ser o primeiro elemento da lista não ordenada.

2 - Pegue o próximo elemento da lista não ordenada e insira-o na posição correta na parte ordenada da lista. 
Isso envolve comparar o elemento com os elementos na parte ordenada e deslocar os elementos maiores (se houver algum) 
para a direita para abrir espaço para o novo elemento.

3 - Repita o passo 2 até que todos os elementos da lista não ordenada tenham sido inseridos na parte ordenada.

4 - Após a conclusão do processo, a lista estará completamente ordenada.

O Insertion Sort é um algoritmo in-place, o que significa que ele ordena os elementos diretamente no 
espaço de memória da lista original, sem a necessidade de memória adicional. Além disso, é estável, 
o que significa que ele não altera a ordem relativa de elementos iguais.

Apesar de sua simplicidade, o Insertion Sort não é tão eficiente quanto alguns outros algoritmos de ordenação, 
especialmente para grandes conjuntos de dados. Sua complexidade de tempo médio é de O(n^2), 
onde "n" é o número de elementos na lista, o que o torna menos adequado para listas muito grandes. 
No entanto, é eficiente para listas pequenas ou quase ordenadas, onde o número de elementos fora de ordem é limitado.

O Insertion Sort é frequentemente usado como parte de algoritmos de ordenação mais sofisticados, 
como o algoritmo "Timsort" usado no Python, que combina o Insertion Sort com o Merge Sort para obter 
desempenho eficiente em uma variedade de casos.
"""

def insertionSortAsc(A):
    
    for i in range(1, len(A)):
        key = A[i]
        j = i -1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key

    return A 

A = [31, 41, 59, 62, 42, 58]

print(insertionSortAsc(A))