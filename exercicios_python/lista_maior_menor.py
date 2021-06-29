lista = []
maior = 0
menor = 0

i = 0
while i < 5:
    valor = int(input(f"Digite um valor para posicao {i}: "))
    if i == 0:
        maior = valor
        menor = valor

    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
        
    lista.append(valor)
    i += 1


print("=-" * 30)
print(f"Você digitou os valores {lista}")

print(f'O maior valor digitado foi {maior} nas posicoes: ', end = ' ')
for j, num in enumerate(lista):
    if num == maior:
        print(f'{j}...', end = ' ')

print(f'\nO menor valor digitado foi {menor} nas posicoes: ', end = ' ')        
for x, val in enumerate(lista):
    if val == menor:
        print(f'{x}...', end = ' ')
