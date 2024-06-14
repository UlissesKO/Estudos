import os

path = 'C:\\Users\\uliss\\OneDrive\\Documentos\\Coisas pro discord\\Imagens'

if os.path.exists(path):
    print('existe')
    if os.path.isfile(path):
        print('isto é um arquivo')
    elif os.path.isdir(path):
        print('é uma pasta')
else:
    print('não existe')

if os.path.exists('test.txt'):
    os.remove('test.txt')
else:
    print('este arquivo não existe')

