import math


print("Olá humano 🖖\n")

while True:
    try:
        input_xa = float(input("Digite a coordenada x para o ponto A:\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
while True:
    try:
        input_ya = float(input("Digite a coordenada y para o ponto A:\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
while True:
    try:
        input_xb = float(input("Digite a coordenada x para o ponto B:\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
while True:
    try:
        input_yb = float(input("Digite a coordenada y para o ponto B:\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
def distancia(xa, ya, xb, yb):
    return math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

print(f'A distância entre os pontos A e B é {distancia(input_xa, input_ya, input_xb, input_yb)}')