i = 1

while i < 10: #repete até que a condição seja atingida
    print(i)
    i += 1
print(i)

#lista = ['blu', 'glu', 'fla', 'flu']

#for item in lista: #imprime cada item em uma linha diferente(serve não só pra listas mas para string tbm)
#    print(item)

#for index in range(len(lista)): #primeiro é onde incia a contar, do meio é até onde vai contar e o terceiro e de qnt em qnt vai pular
#    print(lista[index],index)

#for index in range(5):
#    if index == 0:
#        print('nome:                                ')
#    else:
#        print(f' {index}')

matrix_numeros = [[1,2,3],[4,5,6],[7,8,9],[0]]

for linha in matrix_numeros:
    print('---------')
    for coluna in linha:
        print(coluna)