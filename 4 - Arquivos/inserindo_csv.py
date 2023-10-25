import csv 

linguagem = input('Entre com a linguagem:\n')
fins = input('Entre com a aplicação: \n')

with open("linguagens.csv", "a", encoding="utf-8") as arquivo:
    linha = csv.writer(arquivo, lineterminator='\n')
    linha.writerow([linguagem, fins])