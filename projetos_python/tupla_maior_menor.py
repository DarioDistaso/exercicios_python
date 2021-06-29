from numpy import random

n = random.randint(1, 10, size = 5)
tupla = (n)

print(tupla)

menor = 0
maior = 0

for i in tupla:
    if i == tupla[0]:
        menor = i 
        maior = i 
    if i < menor:
        menor = i 
    if i > maior:
        maior = i 
print(f'O menor valor é {menor} e o maior valor é {maior}')

