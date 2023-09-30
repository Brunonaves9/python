"""
Construção do Heap Máximo (Max Heap):

- O primeiro passo do Heapsort é construir uma estrutura de heap máxima a partir do conjunto de dados não ordenado.
- Um heap máximo é uma árvore binária especial em que o valor de cada nó é maior ou igual aos valores de seus filhos.
- A construção do heap máximo envolve transformar o conjunto de dados em uma estrutura de heap, 
garantindo que o maior valor esteja na raiz da árvore.
- Esse processo é realizado começando pelo último nó não folha e percorrendo todos os nós até a raiz.

Ordenação do Heap:

- Após construir o heap máximo, o maior elemento (na raiz) é trocado com o último elemento da lista 
(o elemento não ordenado).
- O último elemento é agora considerado como parte do conjunto ordenado, e o heap máximo é restaurado 
para os elementos restantes na lista não ordenada.
- Esse processo de troca e reconstrução do heap máximo é repetido até que todos os elementos estejam 
no conjunto ordenado.

Resultado:

- Uma vez que todos os elementos tenham sido trocados e o heap máximo tenha sido reconstruído para cada iteração, 
a lista estará completamente ordenada.

O Heapsort é um algoritmo de ordenação in-place, o que significa que ele ordena os elementos no próprio 
espaço de memória do conjunto de dados, sem a necessidade de alocação de memória adicional. Isso faz com que 
o Heapsort seja eficiente em termos de espaço.

Embora o Heapsort seja eficiente e tenha um desempenho consistente, ele não é tão amplamente usado quanto 
alguns outros algoritmos de ordenação, como o Quick Sort ou o Merge Sort, devido à sua implementação um pouco 
mais complexa. No entanto, ele é uma escolha sólida quando você precisa de um algoritmo de ordenação com 
bom desempenho e não deseja a complexidade adicional de algoritmos como o Merge Sort, que requerem espaço 
de memória adicional para trabalhar.
"""

def heapFy(lista, n, i):
  # Maior
  maior = i
  # Direta
  l = 2 * i + 1
  # Esquerda  
  r = 2 * i + 2

  if l < n and lista[i] < lista[l]:
    maior = l

  if r < n and lista[maior] < lista[r]:
    maior = r

  if maior != i:
    # Swap
    (lista[i], lista[maior]) = (lista[maior], lista[i])

    # Recursividade
    heapFy(lista, n, maior)


# Função Heap Sort
def heapSort(lista):
  n = len(lista)

  for i in range(n // 2 - 1, -1, -1):
    heapFy(lista, n, i)

  for i in range(n - 1, 0, -1):
    # Swap
    (lista[i], lista[0]) = (lista[0], lista[i])
    heapFy(lista, i, 0)


arr = [12, 11, 13, 5, 6, 7, ]
list = []
heapSort(arr)

n = len(arr)

print('Sorted array is')
for i in range(n):
    list.append(arr[i])

print(list)