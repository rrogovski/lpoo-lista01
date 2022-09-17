print("Olá humano 🖖\n")

while True:
    try:
        input_texto = input("Digite um texto em maiscúlo e vou deixá-lo em minúsculo:\n✏  ")
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

print(f"O texto digitado em minúsculo é: {input_texto.lower()}")

while True:
    try:
        input_texto = input("Digite um texto em minúsculo e vou deixá-lo em maiscúlo:\n✏  ")
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

print(f"O texto digitado em maiscúlo é: {input_texto.upper()}")