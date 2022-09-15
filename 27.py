from datetime import datetime


print("Olá humano 🖖\n")

while True:
    try:
        input_valor = int(input("Digite a sua idade:\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
today = datetime.today()

print(f"Você já viveu {today.year - input_valor} anos.\n")

print(f"Você já viveu {today.month - input_valor} anos")

print(f"Você já viveu {(today - datetime.date(today.year - input_valor, today.month, today.day)).days} dias")