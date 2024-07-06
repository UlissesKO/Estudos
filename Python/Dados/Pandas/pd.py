import pandas

dados = {"Marca" : ["Chevrolet", "Ford", "Volkswagen"],
         "Ano"
         "Modelo" : ["Opala", "Maverick", "Gol"],
         "Motor" : ["I6", "V8", "AP"],
         "Cilindrada" : [4.1, 4.9, 2.2]}

#Cria a tabela do pandas
df = pandas.DataFrame(dados)

#Vai printar as 5 primeiras linhas
print(df.head(), "\n")

#Datatypes do dataframe
print(df.dtypes, "\n")

#Printa uma coluna especifica
print(df["Modelo"], "\n")
        #Coloca dois colchetes pois esta passando uma lista para o index
print(df[ ["Motor", "Cilindrada"] ], "\n")

