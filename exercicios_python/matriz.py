lista = [[],[],[]]
pares = 0
cont = 0
maior = 0
menor = 0

for i in range(3):
    for x in range(3):
        n = int(input(f'Digite um valor para {[i,x]}: '))
        lista[i].append(n)
        if n % 2 == 0:
            pares += n
print("-=" * 20)

for z in range(3):
    for y in range(3):
        print(f'[{lista[z][y]:^5}]', end = ' ')
    print()
print("-=" * 20)

for y in range(3):
    cont += lista[y][2]
    if len(lista[1]) == 1:
        maior = lista[1]
    else:
        if lista[1][y] > maior:
            maior = lista[1][y]
        
print(f'A soma dos numeros pares é {pares}')
print(f'A soma dos valores da terceira coluna é {cont}')    
print(f'O maior valor da segunda linha é {maior}.')