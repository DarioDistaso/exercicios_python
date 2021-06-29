#Crie uma funcao que permita imprimir a palavra SPAM, n vezes usando o for e depois o while.

def imprima():
    for x in range(4):
        print("SPAM", end = " ")

imprima()

def imprima2():
    i = 0
    while i < 5:
        print("SPAM")
        i += 1

imprima2()
