import csv

cursos = []

with open('linguagens.csv', 'r', encoding='utf-8') as arquivo:
    leitura = csv.DictReader(arquivo)
    for linha in leitura:
        cursos.append({"linguagem":linha["linguagem"], "aplicacao":linha["aplicacao"]})
        
print(cursos)