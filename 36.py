print("Olá humano 🖖\n")

print("Digite dez números:\n")
numeros = []
while len(numeros) < 10:
    try:
        input_value = float(input(f"{len(numeros) + 1}º número:\n✏  "))
        numeros.append(input_value)
    except ValueError as e:
        print("🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
print(f"Os números digitados e sua multiplicação por 5 são:\n--------------------------")
for i in numeros:
    print(f"{i} x 5 = {i * 5}")