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