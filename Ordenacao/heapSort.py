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