import sqlite3

# criando e conectando ao banco

connection = sqlite3.connect("base.db")


# verificando se existe alterações

print(connection.total_changes)
