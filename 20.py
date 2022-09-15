import random

print("Olá humano 🖖\nVou sortear um número no intervalo que informar")

while True:
    try:
        input_ini = int(input("Digite o valor inicial do intervalo :\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
while True:
    try:
        input_fim = int(input("Digite o valor final do intervalo :\n✏  "))
        if input_fim < input_ini:
            raise ValueError("O valor final deve ser maior que o inicial")
        break
    except ValueError as e:
        print("\n🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")

print(f"O número sorteado foi {random.randint(input_ini, input_fim)}")