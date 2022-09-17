print("Olá humano 🖖\n")

while True:
    try:
        input_valor_pago = float(input("Digite o valor pago:\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
while True:
    try:
        input_valor_produto = float(input("Digite o valor do produto:\n✏  "))
        if input_valor_pago < input_valor_produto:
            raise ValueError("O valor pago deve ser igual ou maior que o valor do produto.")
        break
    except ValueError as e:
        print("\n🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
print(f"Valor do troco: {input_valor_pago - input_valor_produto:.2f}")