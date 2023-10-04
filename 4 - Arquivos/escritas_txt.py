nome = input("Digite o nome à armazenar:\n")

with open("nomes.txt", "a") as arquivo:
    arquivo.write(f"{nome}\n")
