import math

print("Olá humano 🖖\n")

while True:
    try:
        input_raio = float(input("Digite o raio da circuferência que direi o seu perímetro:\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

print(f"O perímetro da circuferência é {2 * math.pi * input_raio}")