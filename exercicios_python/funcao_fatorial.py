def fatorial(n, show = True):
    """
    param n: o numero que se quer calcular o fatorial
    param show: mostra o calculo inteiro (padrao = True)
    """
    c = n
    for c in range(n-1,0,-1):
        if show ==  True:
            print(f'{c+1} x ', end = ' ')
            if c == 1:
                print(f'{c} =', end = ' ')
        n *= c
        
    return n

num = int(input("Digite um número para cálculo do fatorial: "))
print(fatorial(num))
help(fatorial)