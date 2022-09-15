print("Olá humano 🖖\n")

while True:
    try:
        input_valor = int(input("Digite um número inteiro e direi se é ímpar:\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

print(f"O número {input_valor} {'é ímpar' if input_valor % 2 else 'não é ímpar'}")