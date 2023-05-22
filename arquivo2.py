def achaMenor(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indiceMenor = i
    return indiceMenor

x = 0.001
listaX = []
listaY = []
listaF = []

while x < 10:
    f = 2*x**2 + 4/x
    listaF.append(f)
    listaX.append(x)
    x += 0.1

localMenor = achaMenor(listaF)
print(f"O yx = {listaF[localMenor]} e o xv é {listaX[localMenor]}")