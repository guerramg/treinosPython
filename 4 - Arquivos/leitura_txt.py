
with open('nomes.txt', 'r', encoding='utf-8') as arquivo:
    for linhas in arquivo:
        print(f"Nome: {linhas.rstrip()}")