print("Olá humano 🖖\n")

matriculas = [10,20,30,40,50,60,70,80,90,100]
print(f"Matrículas: {matriculas}\n---------------------------------")
print("Digite o número de três matrículas e direi se estão presentes na lista de alunos:\n")
numeros = []
while len(numeros) < 3:
    try:
        input_value = int(input(f"{len(numeros) + 1}º número:\n✏  "))
        numeros.append(input_value)
    except ValueError as e:
        print("🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
for num in numeros:
    if num in matriculas:
        print(f"O número {num} está presente na lista de matrículas!")
    else:
        print(f"O número {num} não está presente na lista de matrículas!")