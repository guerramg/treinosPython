with open('linguagens.csv', 'r', encoding='utf-8') as arquivo:
    for linhas in arquivo:
        linguagem, aplicacao = linhas.rstrip().split(',')
        print(f"{linguagem} - {aplicacao}")