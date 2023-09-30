"""
O Selection Sort (ou "Ordenação por Seleção") é um algoritmo de ordenação simples, porém ineficiente para 
listas grandes, que funciona selecionando repetidamente o elemento mínimo da lista não ordenada e movendo-o 
para a posição correta na lista ordenada. Ele é um exemplo de algoritmo de ordenação por comparação, 
onde os elementos são comparados e trocados para alcançar a ordenação desejada.

Aqui estão os passos básicos para entender o funcionamento do Selection Sort:

1 - O algoritmo mantém duas partes na lista: a parte ordenada e a parte não ordenada. Inicialmente, 
a parte ordenada está vazia e a parte não ordenada contém todos os elementos da lista.

2 - Percorra a parte não ordenada da lista para encontrar o elemento com o menor valor. 
Esse elemento mínimo será movido para a parte ordenada.

3 - Troque o elemento mínimo encontrado no passo anterior com o primeiro elemento da parte não ordenada. 
Isso efetivamente move o elemento mínimo para a parte ordenada e expande a parte ordenada.

4 - Repita os passos 2 e 3 para encontrar o próximo menor elemento e coloque-o na posição apropriada na parte ordenada. 
Continue esse processo até que toda a lista esteja ordenada.

5 - Após a conclusão do algoritmo, a lista estará completamente ordenada.

O Selection Sort é ineficiente em termos de desempenho, principalmente para listas grandes, porque a cada iteração 
ele precisa procurar o mínimo na parte não ordenada, resultando em um tempo de execução de O(n^2), 
onde "n" é o número de elementos na lista. Isso o torna menos adequado para listas extensas em comparação 
com algoritmos de ordenação mais eficientes, como o Quick Sort ou o Merge Sort, que possuem complexidade 
de tempo média de O(n log n).

No entanto, o Selection Sort é simples de entender e implementar, além de ser útil em cenários 
onde a quantidade de dados é pequena ou quando a simplicidade de implementação é mais importante do que o desempenho. 
Em resumo, o Selection Sort é um exemplo didático de algoritmo de ordenação, mas raramente é a escolha preferencial 
em aplicações reais devido à sua ineficiência em listas maiores.
"""

def selectionSort(A):
    n = len(A)
    # Percorre o arranjo A.
    for i in range(n):
        # Encontra o elemento mínimo em A.
        minimo = i
        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j
        # Coloca o elemento mínimo na posição correta.
        A[i], A[minimo] = A[minimo], A[i]
    return A

A = [11, 10,5,6,3,9,1,8,2,4,7]
print(selectionSort(A))