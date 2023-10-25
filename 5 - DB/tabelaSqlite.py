import sqlite3

# CRIA CONEXAO
connection = sqlite3.connect('base.db')

# CRIA O CURSOR PARA TRABALHO
cursor = connection.cursor()

# COMANDO SQL
cursor.execute("""
               CREATE TABLE filmes(
                   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   year INTEGER NOT NULL,
                   score REAL NOT NULL
               );
               """)

print('Tabela criada com sucesso!')

# FECHA CONEXAO

connection.close()