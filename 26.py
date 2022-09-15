print("Olá humano 🖖\n")

while True:
    try:
        input_value = input("Digite uma lista de números inteiros separados por ',' e no final direi qual deles é o menor:\n✏  ")
        values_splited = input_value.split(',')
        values_int = [int(num) for num in values_splited]
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

print(f"O menor número da lista é {min(values_int)}")