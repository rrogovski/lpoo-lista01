print("Olá humano 🖖\n")

while True:
    try:
        input_nome = input("Qual o seu nome?\n✏  ")
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
while True:
    try:
        input_idade = int(input("Qual a sua idade?\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
while True:
    try:
        input_altura = float(input("Qual a sua altura?\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
while True:
    try:
        input_peso = float(input("Qual o seu peso?\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
print(f"Olá {input_nome}, você tem {input_idade} anos, sua altura é {input_altura}, seu peso é {input_peso} e seu IMC é {input_peso / (input_altura * input_altura)}")