'''Crie uma funcao numero_par que permita verificar se um dado numero, x, passado
como parametro eh numero par.'''

def numero_par(x):
    if x % 2 == 0:
        return "\nO numero digitado eh par\n"
    else:
        return "\nO numero digitado eh impar\n"

numero = int(input("\nDigite um numero inteiro: "))
print(numero_par(numero))

