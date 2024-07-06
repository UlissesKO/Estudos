import numpy as np

x = np.array([1,2,3])
y = np.array([1,4,7])

print(x.mean()) #numero medio #quando tem um () no final da palavra mean(), é uma funçao ou um method
print(y.mean())
print(y.shape) #quantos elementos possui #quando nao tem (), é um atributo ou data atribute

zero_vector = np.zeros(5)
zero_matrix = np.zeros((5, 3))



x = np.array([1, 2, 3])
y = np.array([2, 4, 6])

a = np.array([[3,6,5], [5,7,9]])
b = np.array([[2,5,9], [1,3,6]])

print(a.transpose())

print(x + y)

print(y[0:2])
print(a[:,0])
print(a[:,1] + b[:,1])
print(a[0,:] + b[0,:])

X = np.array([1,2,5,6])
print(X[1:])
ind = [1,2]
print(y[y > 2])
print(x[ind])   #quando indexa uma array, se obtem uma copia da mesma, já quando se usa : pra conseguir o numero, e apenas uma amostra, entao
                #o que for modificado ali, vai modificar a array original
print(np.linspace(0, 100, 10))  #ponto de começo, final, e numero de pontos na lista
print(np.logspace(1, 2, 10)) #logaritmo do começo(10), logaritmo do final(100) e numero de pontos
print((np.logspace(np.log10(250), np.log10(500), 10)))
print(X.size)

z = np.random.random(10)
print(np.any(z>0.9))
print(np.all(z >= 0.1))

x = 20
print(not np.any([x%i == 0 for i in range(2, x)]))
