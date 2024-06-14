nome = input("nome: ")
idade = int(input(f'qual a sua idade {nome}? '))

nascimento = 2022 - idade

print(nome.capitalize())
print(f'seu nome é {nome}, e sua idade é: {idade}')
print(f'{nome} você nasceu em {nascimento}')