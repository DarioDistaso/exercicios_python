num = int(input("digite um numero: "))
cont = 0

for x in range (1, num+1):
    print(x, end = " ")
    if num % x == 0:
        cont += 1
        #x = (\033[32mx\033[m)

if cont == 2:
    print(f'o numero {num} foi divisível {cont} vezes e por isso ele \033[32mÉ UM NUMERO PRIMO\033[m')
else:
    print(f'o numero {num} foi divisível {cont} vezes e por isso ele \033[31mNAO É PRIMO\033[m')

    


        
    
   