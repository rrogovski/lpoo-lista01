print("Olá humano 🖖\n")

print("Digite 10 números inteiros:\n")
numeros = ()
sair = False
while not(sair):
    try:
        input_value = int(input(f"{len(numeros) + 1}º número:\n✏  "))
        if len(numeros) == 9:
            if input_value == 999:
                sair = True
            else:
                raise ValueError("O último valor deve ser 999!")
        else:
            numeros = numeros + (input_value,)
    except ValueError as e:
        print("🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
print(f"As números digitadas em orderm reversa são:\n--------------------------")
for num in sorted(numeros, reverse=True):
    print(f"{num}")