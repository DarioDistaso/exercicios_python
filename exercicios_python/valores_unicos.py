lista = list()

while True:
    num = int(input("digite um valor: "))
    if num in lista:
        print("Valor duplicado! nao vou adicionar...")
        continue
    lista.append(num)
    print("Valor adicionado com sucesso...")
    perg = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    
    if perg not in 'SN':
        print("Resposta invalida!")

    if perg == 'N':
        break

print("-=" * 30)
lista.sort()
print(f'Você digitou os valores: {lista}')