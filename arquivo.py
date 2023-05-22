def achaMaior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            indiceMaior = i
    return indiceMaior

def achaMenor(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indiceMenor = i
    return indiceMenor

precos = [100, 150, 1000, 200, 300]
carros = ["up", "fusca", "celta", "ka", "corsinha"]

localMaior = achaMaior(precos)

print(f"No fim o carro mais caro é {carros[localMaior]} e custa {precos[localMaior]}")

x = -10
listaX = []
listaY = []
listaF = []

while x < 10:
    f = x**2 - 5*x +6
    listaF.append(f)
    listaX.append(x)
    x += 0.1

localMenor = achaMenor(listaF)
print(f"O yx = {listaF[localMenor]} e o xv é {listaX[localMenor]}")

