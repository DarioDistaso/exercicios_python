numero = 0
soma = 0
cont = 0

while numero != 999:
    numero = int(input("\nDigite um numero [999 para parar]: "))
    if numero != 999:
        soma += numero
        cont += 1
print(f'Você digitou \033[0;32m{cont} números\033[m e a soma entre eles foi {soma}\n')

