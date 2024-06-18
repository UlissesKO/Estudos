#escrever arquivo de texto ou modifica-lo


numeros = [200, 34, 521, 345, 312, 659]

#w apenas escrever (substitui o que já foi escrito)
#r apenas ler 
#r+ ler e escrever
#a acrescentar algo (sem substituir)


with open("txt.txt", "w") as arquivo:
    for n in numeros:
        arquivo.write(str(n) + ",")

with open("txt.txt", "r") as arquivo:
    for n in arquivo:
        print(n)