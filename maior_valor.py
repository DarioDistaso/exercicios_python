'''Crie uma funcao determinar_o maior_numero que receba dois numeros (inteiros ou
reais) e retorne o maior valor de ambos os numeros'''

'''def determinar_o_maior_numero(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else: 
        return "os numeros sao iguais"

a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))

print("Resultado: ", determinar_o_maior_numero(a,b))'''


num = int(input("Digite um numero para ver a sua tabuada: "))
for i in range(11):
    tab = num * i
    print("-----------")
    print(f'{num} x {i} = {tab}')
