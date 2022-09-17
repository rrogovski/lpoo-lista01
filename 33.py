print("Olá humano 🖖\n")

alfabeto = [chr for chr in "abcdefghijklmnopqrstuvwxyz"]
codes = []

while True:
    try:
        input_value = input("Digite o código da frase com números de 1 a 26 separados por '-':\n✏  ")
        input_split = input_value.split('-')
        for code in input_split:
            if int(code) < 1 or int(code) > 26:
                raise ValueError("Código inválido.")
            else:
                codes.append(int(code))
        break
    except ValueError as e:
        print("🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
print(f"A frase decodificada é:\n----------------------")
print(''.join(alfabeto[code - 1] for code in codes))
print(f"As opções de codificação são:\n--------------------------------")
for (i, letra) in enumerate(alfabeto):
    print(f"{i+1} - {letra}")