txt = "s"
cont = 0
media = 0
soma = 0

maior = 0
menor = 999999999

while txt != "N":
    num = int(input("\nDigite um numero: "))
    cont += 1
    soma += num
    if num > maior:  
        maior = num 
    elif num < menor: 
        menor = num  
    txt =  str(input("Quer continuar?: ")).upper()
media = soma / cont

print(f'Você digitou {cont} números e a média foi {media:.2f}\n')
print(f'O \033[0;32mmaior valor foi {maior}\033[m e o \033[0;32mmenor foi {menor}\033[m\n')

