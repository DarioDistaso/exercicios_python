lista = list()
lista_grande = list()
maior = 0
menor = 0

while True:
    nome = (str(input("Nome: ")))
    lista.append(nome)
    peso = float(input("Peso: "))
    lista.append(peso)

    lista_grande.append(lista[:])

    if len(lista_grande) == 1:
        maior = lista[1]
        menor = lista[1]

    for i in range(0, len(lista_grande)):
        if lista_grande[i][1] > maior:
            maior = lista_grande[i][1]

        if lista_grande[i][1] < menor:
            menor = lista_grande[i][1]
                
    lista.clear()
    resp = str(input("Quer continuar? [S/N] ")).strip()[0]

    if resp in 'Nn':
            break

print("-=" * 30)
print(f'Ao todo você cadastrou {len(lista_grande)} pessoas.')
print(f'O maior peso foi de {maior} Kg da pessoa:', end = ' ')

for z in range(len(lista_grande)):
    if lista_grande[z][1] == maior:
        print(f'{lista_grande[z][0]}', end = ' ')

print(f'\nO menor peso foi de {menor} Kg da pessoa: ', end = " ")
for z in range(len(lista_grande)):
    if lista_grande[z][1] == menor:
         print(f'{lista_grande[z][0]}', end = ' ')