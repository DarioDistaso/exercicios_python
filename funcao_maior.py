from time import sleep
maior = 0
def maior(*args):
    print("-=" * 30)
    print("Analisando os valores passados...")
    for i in args:
        if i == args[0]:
            maior = i
        else:
            if i > maior:
                maior = i
        print(i, end = " ")
        sleep(0.5)
    print(f'Foram informados {len(args)} valores ao todo.')
    if len(args) == 0:
        maior = 0
    print(f'O maior valor informado foi {maior}.')

maior(6,5,2,3,4)
maior(3,2,5,7,8,4,2,1,0)
maior(2,3)
maior(6)
maior()

