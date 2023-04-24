print("Obá! Vamos calcular sua bagagem?\n")

status = int(input("Qual é seu status?: "))
malas = int(input("Quantas malas para viagem?: "))

if status == 1 and malas == 1:
    print("Ok, tudo certo, vamos calcular as dimenssões. \n")

    comprimento = int(input("Informe o comprimento da bagagem: "))
    largura = int(input("Informe a largura da bagagem: "))
    altura = int(input("Informe a altura da bagagem: "))
    peso = float(input("Informe a altura da bagagem: "))

    if comprimento + largura + altura <= 158 and peso <= 32.0:
        print("Tudo ok com sua bagagem, boa viagem!")
    else:
        print("Infelizmente sua bagagem ultrapassa as dimessões ou peso permitido.")
else:
    print("Você terá que pagar uma taxa de serviço por excesso de bagagem!")
