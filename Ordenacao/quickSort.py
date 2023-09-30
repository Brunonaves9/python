"""
O Quick Sort é um algoritmo de ordenação muito eficiente que utiliza a abordagem "dividir para conquistar". 
Ele é amplamente utilizado em aplicações do mundo real devido ao seu desempenho rápido e eficaz. 
O Quick Sort funciona selecionando um elemento da lista, chamado de "pivô", e particionando a lista em 
duas sub-listas: uma contendo elementos menores que o pivô e outra contendo elementos maiores que o pivô. 
Em seguida, ele classifica recursivamente essas sub-listas até que toda a lista esteja ordenada.

Aqui estão os passos básicos para entender o funcionamento do Quick Sort:

1 - Selecionar um elemento da lista como pivô. A escolha do pivô pode ser feita de várias maneiras, 
mas uma abordagem comum é selecionar o elemento do meio.

2 - Reorganizar os elementos na lista de forma que todos os elementos menores que o pivô fiquem 
à esquerda e todos os elementos maiores fiquem à direita. Isso é feito usando dois índices, 
um que percorre a lista da esquerda para a direita e outro da direita para a esquerda. 
Quando esses índices se encontram ou cruzam, o particionamento está concluído.

3 - Aplicar recursivamente o Quick Sort às sub-listas à esquerda e à direita do pivô, ou seja, 
repetir os passos 1 e 2 para cada sub-lista.

4 - Quando a recursão termina, a lista estará completamente ordenada.

O ponto-chave para o desempenho eficiente do Quick Sort é o particionamento, que divide a lista original 
em duas sub-listas menores. Isso permite que o algoritmo trabalhe em partes menores da lista, 
reduzindo assim o tempo de ordenação.

O Quick Sort tem uma complexidade de tempo médio de O(n log n), tornando-o uma escolha excelente para ordenar 
grandes conjuntos de dados. No entanto, a escolha do pivô pode afetar o desempenho do algoritmo. 
Se o pivô for escolhido de forma que a lista seja dividida em partes desiguais, 
o desempenho pode degradar para O(n^2) em casos extremos. Para evitar isso, 
é comum escolher o pivô de forma aleatória ou usar algoritmos de seleção de pivô mais sofisticados, 
como o pivô de mediana de três.

O Quick Sort é amplamente utilizado em linguagens de programação e bibliotecas devido ao seu desempenho 
sólido e é frequentemente o algoritmo de escolha para ordenação rápida.
"""

def particao(lista, inicio, fim):
    pivo = lista[inicio]
    baixo = inicio + 1
    alto = fim

    while True:
        while baixo <= alto and lista[alto] >= pivo:
            alto = alto - 1

        while baixo <= alto and lista[baixo] <= pivo:
            baixo = baixo + 1

        if baixo <= alto:
            lista[baixo], lista[alto] = lista[alto], lista[baixo]
        else:
            break

    lista[inicio], lista[alto] = lista[alto], lista[inicio]

    return alto

def quickSort(lista, inicio, fim):
  
  if inicio >= fim:
    return

  p = particao(lista, inicio, fim)
  quickSort(lista, inicio, (p - 1))
  quickSort(lista, (p + 1), fim)


array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

quickSort(array, 0, len(array) - 1)
print(array)    