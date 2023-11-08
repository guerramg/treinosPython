import sqlite3

# CRIA CONEXAO
connection = sqlite3.connect('base.db')

# CRIA O CURSOR PARA TRABALHO
cursor = connection.cursor()

id = int(input("Entre com a id do filme\n"))
name = input("Entre com o novo nome do filme\n")

# COMANDO SQL
cursor.execute("""
               UPDATE filmes SET name = ?
               WHERE id = ?;
               """, (name, id))


# GRAVO AS QUERYS
connection.commit()

print('Dados atualizados com sucesso!')

# FECHA CONEXAO

connection.close()