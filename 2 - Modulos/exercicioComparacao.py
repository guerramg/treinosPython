import random

print ("###### Adivinhe um número ######\n")

def comparar():
    numeroSorteado = random.randint(1, 10)
    numeroEscolhido = int(input("Digite o número de 1 à 10\n"))
    
    if numeroEscolhido == numeroSorteado:
        print(f"Parabéns, você acertou o numero {numeroSorteado}")
        # estado = True
    else:
        print(f"Desculpe, mas você errou, o número era {numeroSorteado}\n")


estado = False

while not estado:
    print("Selecione uma  opção\n")
    print(">")  
    print
  
    