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