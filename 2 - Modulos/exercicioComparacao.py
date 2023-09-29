import random

def comparar():
    numeroSorteado = random.randint(1, 10)
    numeroEscolhido = int(input("Digite o número de 1 à 10\n"))
    
    print ("###### Adivinhe um número 1.0 ######\n")
    
    if numeroEscolhido == numeroSorteado:
        print(f"Parabéns, você acertou o numero {numeroSorteado}")
        # estado = True
    else:
        print(f"Desculpe, mas você errou, o número era {numeroSorteado}\n")


estado = False

while not estado:
    print("Selecione uma  opção")
    print("0. Reiniciar Sistema")
    print("1. Jogar")
    print("2. Sair")
    
    resposta = int(input("> "))
    
    if resposta == 1:
        comparar()
    elif resposta == 2:
        print ("###### Obrigado ######\n")
        estado = True
    elif resposta == 0:
        print('Reiniciando sistema...')
    else:
        print('Opção incorreta!')

        
  
    