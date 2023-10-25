nomes = []

with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
    for linhas in arquivo:
        nomes.append(linhas.rstrip())
for nomesO in sorted(nomes):
    print(nomesO)