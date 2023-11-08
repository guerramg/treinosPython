import sqlite3

# CRIA CONEXAO
connection = sqlite3.connect('base.db')

# CRIA O CURSOR PARA TRABALHO
cursor = connection.cursor()


# COMANDO SQL
data = cursor.execute("""
               SELECT name, year, score FROM filmes ORDER BY score DESC
               """)



# print (data.fetchall()) #array de tuplas

for linhas in data:
    print (linhas) #LISTANDO TUPLAS


# FECHA CONEXAO

connection.close()