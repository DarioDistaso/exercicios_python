tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input("\nDigite um numero entre 0 e 20: "))

while True:
    
    if 0 <= n <= 20:
        print("\nVoce digitou o numero", tupla[n])
        cont = str(input("Voce quer continuar? [S/N] ")).upper().strip()[0]
        if cont in 'N':
            print('Voce encerrou o programa!')
            break
        else:
            n = int(input("\nDigite um numero entre 0 e 20: "))

    else:
        print('Tente novamente.', end = '')
        n = int(input(" Digite um numero entre 0 e 20: "))
        

    
        


