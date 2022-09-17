print("Olá humano 🖖\n")

print("Digite os ńumeros das matrículas:\n")
matriculas_array = []
while len(matriculas_array) < 10:
    try:
        input_value = input(f"{len(matriculas_array) + 1}º matrícula:\n✏  ")
        matriculas_array.append(input_value)
    except ValueError as e:
        print("🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
print(f"As matrículas digitadas são:\n--------------------------")
matriculas_set = set(matriculas_array)
for m in sorted(matriculas_set):
    print(f"{m}")