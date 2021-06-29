#Crie uma funcao que permita mostrar uma sequencia de numeros ımpares de 1 ate n.

def num_impares(n):
    i = 1
    while i <= n:
        if i %2 != 0:
            print(i)
        i += 1
num = int(input("\nDigite um numero para aparecer a sequencia dos impares: "))
num_impares(num)