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