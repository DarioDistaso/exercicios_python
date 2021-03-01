num = int(input("Digite um numero para ver a sua tabuada: "))
for i in range(11):
    tab = num * i
    print("-----------")
    print(f'{num} x {i} = {tab}')