import pandas

file = "Dados\Arquivos\salary.csv"

#Vai abrir o arquivo
data = pandas.read_csv(file)

#Mostra as primeiras linhas
print(data.head())
print("________________________________")

#Conta os valores da coluna especificada
print(data['Job Titles'].value_counts())
print("________________________________")

print(data['Department'].value_counts())



