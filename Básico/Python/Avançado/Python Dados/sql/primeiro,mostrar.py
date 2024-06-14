import sqlite3 as sql

Banco = sql.connect(r"C:\Users\uliss\OneDrive\Documentos\Coisas Geral\Estudos\Python\Python Dados\sql/primeiro.sql")
Cursor = Banco.cursor()



resultado = Cursor.execute("SELECT * FROM Nova_Tabela").fetchall()

for linhas in resultado:
    print(linhas)


#resultado = Cursor.execute("SELECT Data, Idade FROM Nova_Tabela").fetchall()

#for linhas in resultado:
#    print(linhas)

#resultado = Cursor.execute(
#"""
#SELECT * FROM Nova_Tabela
#Where Nome = "Ulaisses"
#"""
#).fetchall()

print(resultado)

resultado = Cursor.execute(""" Select * FROM Nova_Tabela WHERE Idade BETWEEN 14 AND 30 """ )
print("==========================================================================")

for linha in resultado:
    print(linha)

print("==========================================================================")

resultado = Cursor.execute(""" Select * FROM Nova_Tabela WHERE Nome LIKE '___' """ )

for linha in resultado:
    print(linha)