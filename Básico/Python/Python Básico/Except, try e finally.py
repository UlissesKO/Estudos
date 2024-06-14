try:          #troca a mensagem de erro
    numero = int(input(' '))
    print(numero)
except ZeroDivisionError:  #escolhe o tipo de erro
    print('Essa divisão não é possivel')
except ValueError:
    print('Digite outro ')
except:
    print('erro ')
finally:  #sempre é executado
    print('Sempre executa')