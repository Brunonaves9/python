"""
O Merge Sort é um algoritmo de ordenação eficiente e estável que utiliza a abordagem de "dividir e conquistar" 
para classificar uma lista de elementos. Ele divide a lista em pequenas partes, 
classifica essas partes separadamente e, em seguida, mescla (ou combina) as partes ordenadas para produzir 
a lista final ordenada. O Merge Sort é conhecido por sua eficiência, com uma complexidade de tempo 
garantida de O(n log n) para todos os casos.

Aqui estão os passos básicos para entender o funcionamento do Merge Sort:

1 - Divida a lista não ordenada em duas partes iguais (ou quase iguais) no ponto médio. Isso é feito 
recursivamente até que cada parte contenha apenas um elemento, considerado ordenado por definição.

2 - Ordene cada parte separadamente, também de forma recursiva. Isso é feito dividindo novamente cada 
parte até que sejam pequenas o suficiente para serem consideradas ordenadas.

3 - Combine (ou mesclando) as partes ordenadas para formar uma única lista ordenada. 
Esse processo envolve a comparação dos elementos nas partes ordenadas e a inclusão do menor elemento 
na lista final ordenada. Esse processo de mesclagem é repetido até que todas as partes sejam combinadas 
em uma única lista ordenada.

4 - Após a conclusão do processo de mesclagem, você terá a lista original completamente ordenada.

O Merge Sort é eficiente e estável, o que significa que ele mantém a ordem relativa de elementos com chaves iguais. 
Além disso, ele é adequado para ordenar grandes conjuntos de dados, pois mantém uma complexidade 
de tempo de O(n log n) independentemente do estado de ordenação dos elementos.

No entanto, o Merge Sort consome mais espaço em memória do que alguns outros algoritmos de ordenação, 
pois requer o armazenamento temporário das partes ordenadas durante o processo de mesclagem. 
Esse espaço adicional é geralmente uma desvantagem quando se lida com listas muito grandes. Por essa razão, 
o Merge Sort é frequentemente usado quando a estabilidade e a eficiência são prioridades, 
mas a limitação de espaço não é crítica.
"""

def mergeSort(lista):

  if len(lista) > 1:
    met = len(lista) // 2
    esqMet = lista[:met]
    dirMet = lista[met:]

    # Recursividade para as metades
    mergeSort(esqMet)
    mergeSort(dirMet)

    i = 0
    j = 0
    k = 0

    while i < len(esqMet) and j < len(dirMet):
      if esqMet[i] < dirMet[j]:        
        lista[k] = esqMet[i]
        i = i + 1
      else:
        lista[k] = dirMet[j]
        j = j + 1
      k = k + 1
    
    while i < len(esqMet):
      lista[k] = esqMet[i]
      i = i + 1
      k = k + 1
    
    while j < len(dirMet):
      lista[k] = dirMet[j]
      j = j + 1
      k = k + 1
    return lista

A = [31, 41, 59, 62, 42, 58]

print(mergeSort(A))   