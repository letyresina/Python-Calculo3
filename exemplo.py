lista = [100, 150, 1000, 200, 300]
carros = ["up", "fusca", "celta", "ka", "corsinha"]

# Quando a > 0
maior = lista[0] # primeiro indíce! (100)
indiceMaior = 0

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        indiceMaior = i
print(f"No fim o carro mais caro é {carros[indiceMaior]} e custa {lista[indiceMaior]}")

'''
    A lógica para encontrar o maior/menor ponto, eu pressuponho que o maior/menor é o primeiro
    indíce e a partir daí, checar se realmente é, passando por toda a lista.
'''