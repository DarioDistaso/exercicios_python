#Crie uma funcao que permita o calculo da seguinte somatoria: −1 + 2 − 3 + 4 − 5 + 6 + · · · + n
soma = 0
def somatoria(m,n):
    soma_i = 0
    soma_p = 0
    for x in range(m,n+1):
        if x % 2 != 0:
            soma_i = soma_i + x
        else:
            soma_p = soma_p + x
    return soma_i*-1 + soma_p

inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
print("O resultado da somatoria eh: ", somatoria(inicio, fim))
