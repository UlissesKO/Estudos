frutas = {'banana', 'maçã', 'laranja'} #set

num = set(range(5))
num2 = set(range(2, 8))
num3 = num2 - num
num4 = num | num2

#set ignora itens duplicados e pode ser qlqr tipo de dado

frutas.add('pera')
frutas.remove('maçã')
frutas.pop()

print(frutas)
print(len(frutas))
print(num3)
print(num4)
print(num.issubset(num2))
print(num.symmetric_difference(num2))
