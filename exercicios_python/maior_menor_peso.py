maior = 0
menor = 0

for i in range(1,6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso 
        elif peso < menor:
            menor = peso
        else:
            continue

print(f'O maior peso lido foi {maior} kg')
print(f'O menor peso lido foi {menor} kg')



