import sqlite3

# CRIA CONEXAO
connection = sqlite3.connect('base.db')

# CRIA O CURSOR PARA TRABALHO
cursor = connection.cursor()

# COMANDO SQL
cursor.execute("""
               INSERT INTO filmes (name, year, score)
                VALUES ('Super Mario','2023','9.5');
               """)

cursor.execute("""
               INSERT INTO filmes(
                   name,
                   year,
                   score
                   )
                VALUES(
                    'Avatar 2',
                    '2023',
                    '8.0'
                   );
               """)

# GRAVO AS QUERYS
connection.commit()

print('Dados gravados com sucesso!')

# FECHA CONEXAO

connection.close()