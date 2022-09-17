print("Olá humano 🖖\n")

notas_n1 = []
notas_n2 = []
medias = []
while len(notas_n1) < 3 and len(notas_n2) < 3:
    try:
        input_value = float(input(f"Nota do {len(notas_n1) + 1}º aluno da primeira prova:\n✏  "))
        notas_n1.append(input_value)
    except ValueError as e:
        print("🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
    try:
        input_value = float(input(f"Nota do {len(notas_n2) + 1}º aluno da segunda prova:\n✏  "))
        notas_n2.append(input_value)
    except ValueError as e:
        print("🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
medias = [(n1 + n2) / 2 for n1, n2 in zip(notas_n1, notas_n2)]

for i in range(0, len(notas_n1)):
    print(f"Aluno {i + 1} - Média: {medias[i]}\n")
    
    if medias[i] >= 6:
        print("Aprovado!\n--------------------------")
    else:
        print("Reprovado!\n--------------------------")