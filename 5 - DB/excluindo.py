import sqlite3

# CRIA CONEXAO
connection = sqlite3.connect('base.db')

# CRIA O CURSOR PARA TRABALHO
cursor = connection.cursor()

id = int(input("Entre com a id do filme\n"))

# COMANDO SQL
cursor.execute("""
               DELETE FROM filmes WHERE id = ?;
               """, (id,))


# GRAVO AS QUERYS
connection.commit()

print('Dados excluidos com sucesso!')

# FECHA CONEXAO

connection.close()