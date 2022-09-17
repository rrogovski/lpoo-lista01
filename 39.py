print("Olá humano 🖖\n")

elementos = [1,2,3,'Mas o que temos aqui', 3.1415, ['Isso é outro vetor'], ('Aqui temos uma tupla'), 8, 9, 10]

for (index, elemento) in enumerate(elementos):
    print(f'''O elemento "{elemento}" do tipo {type(index)}, está na posição {index}''')