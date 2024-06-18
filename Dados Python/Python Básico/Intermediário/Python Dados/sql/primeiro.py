import sqlite3 as sql

Banco = sql.connect(r"C:\Users\uliss\OneDrive\Documentos\Coisas Geral\Estudos\Python Dados\sql/primeiro.sql")
Cursor = Banco.cursor()

# Cursor.execute(
#   "CREATE TABLE Nova_Tabela (Data text, Nome text, Idade int)"
# )

# Banco.commit()



Cursor.execute(" INSERT INTO Nova_Tabela VALUES ( '1/01/2032', 'Vitoria', 13 )")
Cursor.execute(" INSERT INTO Nova_Tabela VALUES ( '1/02/2032', 'Ana', 54 )")
Banco.commit()


