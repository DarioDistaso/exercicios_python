from time import sleep

def contador(inicio,fim,passo):
    print("-=" * 20)
    if fim < 0 or passo < 0:
        fim -= 1
        print(f'Contagem de {inicio} até {fim+1} de {abs(passo)} em {abs(passo)}')
        for i in range(inicio,fim,passo):
            print(i, end = ' ')
            sleep(0.5)
    else:
        print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
        for i in range(inicio,fim+1,passo):
            print(i, end = ' ')
            sleep(0.5)
    
    print("FIM!")

contador(1,10,1)
contador(10,0,-2)
print("Agora é sua vez de personalizar a contagem!")
i = int(input("Inicio: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i,f,p)