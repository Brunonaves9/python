global N
# Tamanho da Matriz
N = 8
qtd = 0

# Verifica se duas Rainhas são ameaçadas
# tabuleiro, r (Linha), c (coluna)
def isSeguro(tabuleiro, r, c):
 
    # Verifica a coluna
    for i in range(r):
        if tabuleiro[i][c] == 'R':
            return False
 
    # Verifica Diagonal
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if tabuleiro[i][j] == 'R':
            return False
        i = i - 1
        j = j - 1
 
    # Verifica Diagonal
    (i, j) = (r, c)
    while i >= 0 and j < len(tabuleiro):
        if tabuleiro[i][j] == 'R':
            return False
        i = i - 1
        j = j + 1
 
    return True
 
 
def imprimirSolucao(tabuleiro):
    for r in tabuleiro:
        print(str(r).replace(',', '').replace('\'', ''))        
    print()
 
 
def nRainhas(tabuleiro, r):
    global qtd
    # Se estiver tudo OK imprime a solução
    if r == len(tabuleiro):
        qtd = int(qtd) + 1
        valor = qtd
        print('Quantidade: ' + str(valor))
        imprimirSolucao(tabuleiro)        
        return
 
    # Coloca a Rainha em seu local
    for i in range(len(tabuleiro)):
 
        # Chama o método para verificar se as Rainhas são ameaçadas
        if isSeguro(tabuleiro, r, i):
            # Insere a Rainha
            tabuleiro[r][i] = 'R'
 
            nRainhas(tabuleiro, r + 1)
 
            # Backtrack e remove a Rainha da casa
            tabuleiro[r][i] = '–'
 
 

 

# Cria a Matriz Vazia, preenchendo com "-"
tabuleiro = [['–' for x in range(N)] for y in range(N)]
 
nRainhas(tabuleiro, 0)

