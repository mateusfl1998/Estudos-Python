palavra = "apple"
palavras = ["banana", "cherry", "date"]
dicionario = []

contador = 1  # Replace this with your actual value for contador

for i in palavras:
    dicionario.append([i, palavras[contador-1]])

print(dicionario)