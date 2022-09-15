print("Olá humano 🖖\n")

while True:
    try:
        input_valor = float(input("Digite um valor que direi a quantidade mínima de moedas (1 real, 50 centavos, 25 centavos, 10 centavos, 5 centavos e 1 centavo) representa esse valor:\n✏  "))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

moedas_utilizadas = {1: 0, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
        
def minimo_moedas(valor):
    moedas = list(moedas_utilizadas.keys())
    quantidade = 0
    for moeda in moedas:
        while valor >= moeda:
            moedas_utilizadas[moeda] += 1
            valor -= moeda
            quantidade += 1
    return quantidade

print(f"A quantidade mínima de moedas que representa o valor {input_valor} é {minimo_moedas(input_valor)}")

print("\nMoedas utilizadas:\n")

for moeda, quantidade in moedas_utilizadas.items():
    if quantidade > 0:
        print(f"{quantidade} moeda(s) de {moeda} {'centavo(s)' if moeda < 1 else 'real'}")