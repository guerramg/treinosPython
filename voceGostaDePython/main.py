resposta = input("Você gosta de python? (Sim/Não): ").upper()

while resposta.upper() != "SIM":
    print (f"Resposta Incorreta! {resposta}")
    resposta = input("Você gosta de python? (Sim/Não): ")
else:
    print("Resposta Correta!")
