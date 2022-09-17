# n = int(input('Digite a dimensão n da matriz: '))
# m = int(input('Digite a dimensão m da matriz: '))

# matriz = []

# for i in range(n):
#     linha = []
#     for j in range(m):
#         linha.append(int(input(f'Digite o elemento ({i}, {j}): ')))
#     matriz.append(linha)
    
# print(f"A matriz é: {matriz}")



    
    
# n = int(input('Digite a dimensão n da matriz: '))
# m = int(input('Digite a dimensão m da matriz: '))

# matriz = []

# for i in range(n):
#     linha = []
#     for j in range(m):
#         linha.append(0)
#     matriz.append(linha)
    
# print(f"Matriz {n}x{m} preenchida com zeros: {matriz}")

# n = int(input('Digite a dimensão n da matriz: '))
# m = int(input('Digite a dimensão m da matriz: '))

# matriz = []

# for i in range(n):
#     matriz.append([0]*m)

# for i in range(n):
#     print(matriz[i])




# matriz = []
# n = 3
# m = 3
# total_pares = 0

# for i in range(n):
#     linha = []
#     for j in range(m):
#         valor = int(input(f'Digite o elemento ({i}, {j}): '))
#         linha.append(valor)
#         # if (valor % 2 == 0):
#         #     total_pares += 1
#     matriz.append(linha)
    
# print(f"A matriz é: {matriz}")

# for i in range(n):
#     for j in range(m):
#         if (matriz[i][j] % 2 == 0):
#             total_pares += 1

# print(f"Total de pares: {total_pares}")





# m = []

# for i in range(10):
#     linha = []
#     linha.append(input('Digite o nome da pessoa ' + str(i) + ': '))
#     linha.append(int(input('Digite a idade da pessoa ' + linha[0] + ': ')))
    
# menor = m[0][1]
# pos = 0

# for i in range(10):
#     if m[i][1] < menor:
#         menor = m[i][1]
#         pos = i

# for i in range(10):
#     print(m[i][0] + ' tem ' + str(m[i][1]) + ' anos')
    
# print('A pessoa mais nova é ' + m[pos][0] + ' com ' + str(m[pos][1]) + ' anos')


def func_01(lista):
    lista.append('func 01')
    
def func_02(lista):
    lista.append('func 02')
    
lista = ['Tem só isso']

func_01(lista)

print(lista)

func_02(lista)

print(lista)