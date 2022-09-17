print("Olá humano 🖖\n")

print("Digite cinco números:\n")
numeros = []
while len(numeros) < 5:
    try:
        input_value = float(input(f"{len(numeros) + 1}º número:\n✏  "))
        numeros.append(input_value)
    except ValueError as e:
        print("🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
print(f"Os números digitados foram:\n{', '.join([str(i) for i in numeros])}\n--------------------------")
print(f"A soma dele é: {sum(numeros)}")