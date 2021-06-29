'''Dizemos que um numero natural é triangular se ele é produto de tres numero naturais
consecutivos. Por exemplo: 120 é triangular, pois 4*5*6 = 120. 2730 é triangular,
pois 13*14*15 = 2730. Dado um inteiro não negativo n, crie uma funcao para
verificar se n é triangular. Deve-se devolver True se o numero for triangular, caso
contrario False.'''
#com loop while:
'''def triangular(n):
    i = 1
    while i <= n:
        mult = i * (i + 1) * (i + 2)
        if mult == n:
            return True
        i += 1
    else:
        return False

numero = int(input('Digite um numero: '))
print(triangular(numero))'''

#com loop for:
def triangular(n):
    for i in range(1, n+1):
        mult = i * (i + 1) * (i + 2)
        if mult == n:
            return True
    else:
        return False

numero = int(input('Digite um numero: '))
print(triangular(numero))


