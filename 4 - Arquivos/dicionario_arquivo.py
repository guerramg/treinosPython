cursos = []

with open('linguagens.csv', 'r', encoding='utf-8') as arquivo:
    for linhas in arquivo:
        linguagem, aplicacao = linhas.rstrip().split(',')
        
        dicionario = {}
        dicionario['linguagem'] = linguagem
        dicionario['aplicacao'] = aplicacao
        
        cursos.append(dicionario)
        
print(cursos)