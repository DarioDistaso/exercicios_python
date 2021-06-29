lista = list()
acc = 0

while True:
    num = int(input("\033[0;32mDigite um valor:\033[m "))
    lista.append(num)
    cont = str(input("Quer continuar?[S/N] ")).upper().strip()
    acc += 1

    while cont[0] not in 'SN':
        print("Opção errada!")
        cont = str(input("Quer continuar?[S/N] ")).upper().strip()
    
    if cont[0] == 'N':
        break
    
print("-=" * 30)
print(f'Você digitou {acc} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')

if 5 not in lista:
    print("O valor 5 não foi encontrado na lista!")
else:
    print("O valor 5 faz parte da lista!")
