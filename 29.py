print("Olá humano 🖖\n")

while True:
    try:
        input_a = int(input("Digite o valor do lado a do de um triângulo:\n✏  "))
        if input_a < 1:
            raise ValueError("O valor deve ser positivo.")
        break
    except ValueError as e:
        print("\n🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
while True:
    try:
        input_b = int(input("Digite o valor do lado b do de um triângulo:\n✏  "))
        if input_b < 1:
            raise ValueError("O valor deve ser positivo.")
        break
    except ValueError as e:
        print("\n🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
while True:
    try:
        input_c = int(input("Digite o valor do lado c do de um triângulo:\n✏  "))
        if input_c < 1:
            raise ValueError("O valor deve ser positivo.")
        if input_c > input_a + input_b:
            raise ValueError("O valor de c deve ser menor ou igual a soma dos valores de a e b.")
        break
    except ValueError as e:
        print("\n🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
lados = set([input_a, input_b, input_c])

print(f"Os lados do triângulo são: {input_a}, {input_b} e {input_c}\n")

if len(lados) == 1:
    print("Triângulo equilátero")
elif len(lados) == 2:
    print("Triângulo isósceles")
else:
    print("Triângulo escaleno")