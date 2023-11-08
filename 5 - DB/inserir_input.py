import sqlite3

# CRIA CONEXAO
connection = sqlite3.connect('base.db')

# CRIA O CURSOR PARA TRABALHO
cursor = connection.cursor()

name = input("Entre com o nome do filme\n")
year = int(input("Entre com o ano do filme\n"))
score = float(input("Entre com a nota do filme\n"))

# COMANDO SQL
cursor.execute("""
               INSERT INTO filmes (name, year, score)
                VALUES (?, ?, ?);
               """, (name, year, score))


# GRAVO AS QUERYS
connection.commit()

print('Dados gravados com sucesso!')

# FECHA CONEXAO

connection.close()