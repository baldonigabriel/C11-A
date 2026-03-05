import numpy as np

# Exercício 1

arr1 = np.ones(8)
arr2 = np.random.randint(0, 10, 8)

print(f"Array de 1's: {arr1}")
print(f"Array aleatório (0-9): {arr2}")

arr3 = arr1 + arr2
print(f"Soma dos arrays: {arr3}")

soma_total = arr3.sum()
print(f"Soma total de todos elementos: {soma_total}")

if soma_total >= 40:
    mtz = arr3.reshape(4, 2)
    print(f"\nSoma total ({soma_total}) >= 40")
    print(f"Remodelado para matriz (4 linhas x 2 colunas):")
    print(mtz)
else:
    mtz = arr3.reshape(2, 4)
    print(f"\nSoma total ({soma_total}) < 40")
    print(f"Remodelado para matriz (2 linhas x 4 colunas):")
    print(mtz)

# Exercício 2

pares1 = np.arange(0, 52, 2)
print(f"Números pares de 0 a 51: {pares1}")

pares2 = np.arange(100, 48, -2)
print(f"Números pares de 100 até 50: {pares2}")

concatenado = np.concatenate((pares1, pares2))
print(f"Concatenado: {concatenado}")

ordenado = np.sort(concatenado)
print(f"Ordenado: {ordenado}")

# Exercício 3

mtz_minado = np.zeros([2, 2])
print(f"Matriz inicial (2x2 com zeros):\n{mtz_minado}")

posicao_bomba = np.random.randint(0, 4)
mtz_minado.flat[posicao_bomba] = 1
print(f"\nBomba adicionada na posição {posicao_bomba}")
print(f"Matriz com bomba:\n{mtz_minado}")

print("\nBem-vindo ao Mini Campo Minado!")
print("Digite as coordenadas (linha e coluna) para fazer suas jogadas")
print("Coordenadas válidas: linha 0 ou 1, coluna 0 ou 1")

jogadas = 0
encontrou_bomba = False
posicoes_clicadas = []

while jogadas < 3:
    try:
        linha = int(input(f"\nJogada {jogadas + 1} - Digite a linha (0 ou 1): "))
        coluna = int(input(f"Jogada {jogadas + 1} - Digite a coluna (0 ou 1): "))
        
        if linha < 0 or linha > 1 or coluna < 0 or coluna > 1:
            print("Coordenadas inválidas! Use 0 ou 1.")
            continue
        
        posicoes_clicadas.append((linha, coluna))
        jogadas = jogadas + 1
        
        if mtz_minado[linha][coluna] == 1:
            print(f"\nVocê encontrou a bomba na posição ({linha}, {coluna})")
            print("Game Over! :( Try Again!")
            encontrou_bomba = True
            break
        else:
            print(f"Posição ({linha}, {coluna}) segura!")
    
    except ValueError:
        print("Entrada inválida! Digite números 0 ou 1.")

if not encontrou_bomba and jogadas == 3:
    todas_posicoes = [(0, 0), (0, 1), (1, 0), (1, 1)]
    posicoes_seguras = []
    
    for pos in todas_posicoes:
        if mtz_minado[pos[0]][pos[1]] == 0:
            posicoes_seguras.append(pos)
    
    clicou_todas = True
    for pos_segura in posicoes_seguras:
        if pos_segura not in posicoes_clicadas:
            clicou_todas = False
            break
    
    if clicou_todas:
        print("\nCongratulations! You beat the game! :)")
    else:
        print("\nGame Over! Você não conseguiu identificar todos os campos seguros.")

# Exercício 4

mtz_teste = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matriz criada:\n{mtz_teste}")

linhas = mtz_teste.shape[0]
colunas = mtz_teste.shape[1]

print(f"Número de linhas: {linhas}")
print(f"Número de colunas: {colunas}")

produto = linhas * colunas
print(f"Produto (linhas x colunas): {produto}")

if produto % 2 == 0:
    print(f"Este array remodelado como vetor teria {produto} elementos (NÚMERO PAR)")
else:
    print(f"Este array remodelado como vetor teria {produto} elementos (NÚMERO ÍMPAR)")

# Exercício 5

np.random.seed(10)
mtz_analise = np.random.randint(1, 51, [4, 4])

print(f"Matriz gerada (4x4):\n{mtz_analise}")

print("\na) Médias das Linhas:")
for i in range(4):
    media_linha = mtz_analise[i].mean()
    print(f"Linha {i}: {media_linha}")

print("\na) Médias das Colunas:")
for j in range(4):
    media_coluna = mtz_analise[:, j].mean()
    print(f"Coluna {j}: {media_coluna}")

maior_media_linhas = mtz_analise.mean(axis=1).max()
maior_media_colunas = mtz_analise.mean(axis=0).max()

print(f"\nb) Maior Valor das Médias:")
print(f"Maior valor das médias das linhas: {maior_media_linhas}")
print(f"Maior valor das médias das colunas: {maior_media_colunas}")

print(f"\nc) Quantidade de Aparições:")
unicos, contagens = np.unique(mtz_analise, return_counts=True)

print("Quantidade de aparições de cada número:")
for numero, contagem in zip(unicos, contagens):
    print(f"Número {numero}: aparece {contagem} vezes")

print("\nNúmeros que aparecem 2 vezes:")
encontrou = False
for numero, contagem in zip(unicos, contagens):
    if contagem == 2:
        print(f"Número {numero}")
        encontrou = True

if not encontrou:
    print("Nenhum número aparece exatamente 2 vezes")