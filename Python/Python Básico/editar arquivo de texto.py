#with open('editar arquivo de texto, texto', 'r') as arquivo:  #read para informaçao unica
#    email = arquivo.read()

#with open('editar arquivo de texto, texto', 'r') as arquivo:  #readlines separa cada linha em lista
#    mensagem = arquivo.readlines()

num = 0 + 1

with open('../editar arquivo de texto, texto', 'r') as arquivo:
    texto = arquivo.readlines()
    print(texto)
    texto[0] = 'não tem1'
    linha1 = texto[0]
    texto[num] = 'não tem2'
    linha1 = texto[num]
    num = num + 1
    texto[num] = 'não tem3'
    linha1 = texto[num]
    num = num + 1
    texto[num] = 'não tem4'
    linha1 = texto[num]
    with open('editar arquivo de texto, texto', 'w') as arquivo:
        for valor in texto:
            arquivo.write(str(valor) + '\n')