def fazer_lanche(nome):
    print(f'lanche {nome}')

def fazer_batata(tamanho):
    print(f'batata{tamanho}')

def pegar_refri(tipo, tamanho2):
    print(f'{tipo} {tamanho2}')


def fazer_combo(nome, tamanho,tipo,tamanho2):
    fazer_lanche(nome)
    fazer_batata(tamanho)
    pegar_refri(tipo,tamanho2)

fazer_combo('ulisses', 'grande', 'coca', 'media')