print("Olá humano 🖖\n")

words = []
frase = ''

while True:
    try:
        input_value = input("Digite uma frase:\n✏  ")
        frase = input_value
        values_splited = input_value.split(' ')
        for word in values_splited:
            words.append(''.join(chr for chr in word if chr.isalnum()))
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")

print(f"As palavras digitadas são:\n------------------------")
for (index, word) in enumerate(words):
    print(f"{index + 1} - {word}")
    
while True:
    try:
        input_idx = int(input("Digite o índice da palavra que deseja substituir:\n✏  "))
        index = input_idx - 1
        if index < 0 or index + 1 > len(words):
            raise ValueError("Índice inválido.")
        break
    except ValueError as e:
        print("\n🚨 Valor inválido. Tente novamente!\n")
        print(f"{e}\n")
        
while True:
    try:
        input_new_word = input(f"Digite a nova palavra que irá substituir {words[index]}:\n✏  ")
        break
    except ValueError:
        print("🚨 Valor inválido. Tente novamente!\n")
        
print(f"A nova frase agora é:\n---------------------")
print(f"{frase.replace(words[index], input_new_word)}")
