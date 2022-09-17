from datetime import datetime, timedelta

print("Olá humano 🖖\n")

while True:
    try:
        input_dias = int(input("Digite quantos dias de vida você tem:\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
        
data_nascimento = datetime.today() - timedelta(days=input_dias)

print(f"Data de nascimento: {data_nascimento.strftime('%d/%m/%Y')}")
