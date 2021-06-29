from random import randint
from time import sleep
numeros = list()

def sorteia(lista): # sorteia 5 numeros e insere eles na lista numeros passada como parametro
    print("Sorteando 5 números...")
    for i in range(5):
        lista.append(randint(1,10))
    for x in range(len(lista)):
        print(lista[x], end = ' ')
        sleep(0.5)
    print("\033[1;32mPRONTO!\033[m")
sorteia(numeros)

def somaPar(lista): #soma os numeros pares da lista numeros passada como parametro
    soma = 0
    for y in lista:
        if y % 2 == 0:
            soma += y
    print(f'Somando os valores pares de {lista}, temos {soma}')
somaPar(numeros)
