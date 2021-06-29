lista = [[], []]

for i in range(7):
    n = int(input(f'Digite o {i+1}° valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    elif n % 2 == 1:
        lista[1].append(n)

print("-=" * 20)
print(lista)

lista[0].sort()
lista[1].sort()

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')