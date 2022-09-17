print("Olá humano 🖖\n")

while True:
    try:
        input_texto = input("Digite alguma coisa e direi quantos caracteres há:\n✏  ")
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

print(f"O texto digitado tem {len(input_texto)} caracteres")