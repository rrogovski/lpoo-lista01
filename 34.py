print("Olá humano 🖖\n")

numeros = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]

while True:
    try:
        input_value = input("Digite digite um número inteiro:\n✏  ")
        for i in input_value:
            num = int(i)
            if num < 0:
                raise ValueError("Número inválido.")
            numeros.append(num)
        break
    except ValueError as e:
        print("🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
print(f"Os algarismos do número digitado são: {', '.join([numeros[int(i)] for i in str(input_value)])}")