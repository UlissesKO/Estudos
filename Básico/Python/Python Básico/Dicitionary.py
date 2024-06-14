meses = {
    'jan' : 'janeiro',
    'fev' : 'fevereiro',
    'mar' : 'março',
    'apr' : 'abril',
    'may' : 'maio',
    'jun' : 'junho',
    'jul' : 'julho',
    'aug' : 'agosto',
    'sep' : 'setembro',
}

print(meses.get('may','jan'))#o segundo parametro e caso o primeiro seja invalido, o segundo sera escrito
#diferença entre colchetes e .get é q o colchete vai quebrar se o valor for invalido
print(meses['may'])

#da pra usar tanto strings, como tuples como key de um dictionary
