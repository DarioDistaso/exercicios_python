num = (int(input("digite o primeiro numero: ")), int(input("digite o segundo numero: ")),
int(input("digite o terceiro numero: ")), int(input("digite o quarto numero: ")))

print(f'voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'o primeiro valor 3 foi digitado na posicao {num.index(3) + 1}')
else:
    print("o valor 3 nao foi encontrado")

print(f'Os números pares foram: ', end = ' ')

for i in num:
    if i % 2 == 0:
        print(i, end = " ")
        
