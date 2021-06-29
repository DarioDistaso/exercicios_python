#Crie uma funcao que permita imprimir os primeiros n numeros naturais.

def numeros_naturais(n):
    for x in range(1, n+1):
        print("---")
        print(x)

numeros_naturais(10)


def numeros_naturais2(n):
    i = 0
    while i <= n:
        print(i, end = " ")
        i += 1

numeros_naturais2(100)


