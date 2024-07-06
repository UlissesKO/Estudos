familia = ['eu', 'blublu', 'bleble','fds', 'boboca']

#print(familia[1]) - retorna o indice 1
#print(familia[-3]) - retorna o indice de traz pra frente
#print(familia[2:]) - retorna a partir do 2
#print(familia[1:3]) - retorna do 1 ao 2 (exclui o 3)

print(familia)
familia[3] = 'eu' #alterou o valor do indice 3
print(familia)
familia[::-1] #vai inverter a lista
print(familia)

#familia.extend(['blibli', 'gluglu']) #juntou com outra lista(pode se usar com uma lista em variavel)
#print(familia)

#familia.append('gugu') #adicionou gugu
#print(familia)

#familia.insert(3,"glitter") #adiciona glitter como indice 3 e passa o antigo pra frente
#print(familia)

#familia.pop() #remove o ultimo indice
#print(familia)

#familia.remove('blublu') #remove blublu
#print(familia)

#familia.clear() #limpa a lista
#print(familia)

#print(familia.index('bleble')) - mostra o indice da palavra
#print(familia.count('eu')) - conta qnts valores iguais tem na lista
#lista2 = [16, 12, 65, 49, 48]
#print(lista2)
#lista2.sort()#ordena a lista(para numeros é em ordem crescente
#print(lista2)
#familia.sort()#ordena a lista(para string é em ordem alfabetica
#print(familia)
#lista2.reverse() #inverte a lista
#print(lista2)
#lista2.sort()
#lista2.reverse()
#print(lista2)

#familia2 = familia.copy() #copia a lista
#familia.remove('fds')
#print(familia2)
#print(familia)

coordenadas = (-59, -54) #é um tuple, ent nao da pra alterar esta variavel
print(coordenadas)

numbers = range(10)
squares = []
for number in numbers:
    square = number **2
    squares.append(square)

print(squares)

square2 = [number**2 for number in numbers]

print(square2)

sum([i for i in range(10) if i%2 == 1])
