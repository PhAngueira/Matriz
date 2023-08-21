def cria_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            n = int(input("Digite o número: "))
            linha.append(n)
        matriz.append(linha)
    return matriz

def soma_numeros_matriz(matriz):
    soma = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            soma += matriz[linha][coluna]
    return soma

def imprimir(soma):
    print(f"Soma: {soma}")

def principal():
    matriz = cria_matriz(3,3)
    soma = soma_numeros_matriz(matriz)
    imprimir(soma)

#Principal
principal()