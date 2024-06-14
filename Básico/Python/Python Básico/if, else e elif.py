sede = True
fome = True

#if sede or fome: #se um dos dois forem verdadeiros
#    print('cozinha')
#else:
#    print('fica')

#if sede and fome: #se os dois forem verdadeiros
#    print('bebo e como')
#else:
#    print('nao como')

if sede and fome:
    print('bebo e como')
elif sede and not (fome):
    print('bebo')
elif not(sede) and fome:
    print('como')
else:
    print('ficar')

num1 = 5
num2 = 32

#if num1 == num2: #para saber se é igual
#    print('num igual num2')
#elif num1 < num2:
#    print('menor')
#elif num1 > num2:
#    print('maior')
#elif num1 != num2: #saber se é diferente
#    print('diferente')

#if num1 <= num2: #saber se é menor ou igual
#    print('menor ou igual')

#or = ou
#and = e
#not() = negaçao
