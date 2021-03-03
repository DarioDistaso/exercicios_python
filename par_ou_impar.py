from random import randint


print("=-" * 30)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-" * 30)

vitoria = 0

while True:
    j = int(input("Diga um valor: "))
    vence = str(input("Par ou Impar? [P/I] ")).strip()
    print("-" * 30)
    c = randint(0,10)
    soma = j + c

    if soma % 2 == 0:

        if vence in 'Pp':
            print(f'Voce jogou {j} e o computador {c}. Total de {soma} DEU PAR')
            print("-" * 30)
            print("\033[0;32mVoce venceu!!\033[m")
            print("Vamos jogar novamente...")
            print('=-' * 30)
            vitoria += 1

        elif vence in 'Ii':
            print(f'Voce jogou {j} e o computador {c}. Total de {soma} DEU PAR')
            print("\033[0;31mVoce perdeu!!\033[m")
            print("=-" * 30, "GAME OVER !!")
            break

        else:
            print("valor invalido: digite par ou impar! ")

    elif soma % 2 == 1:

        if vence in 'Pp':
            print(f'Voce jogou {j} e o computador {c}. Total de {soma} DEU IMPAR')
            print("\033[0;31mVoce perdeu!!\033[m")
            print("=-" * 30)
            break

        elif vence in 'Ii':
            print(f'Voce jogou {j} e o computador {c}. Total de {soma} DEU IMPAR')
            print("\033[0;32mVoce venceu!!\033[m")
            print("Vamos jogar novamente...")
            print('=-' * 30)
            vitoria += 1
        
        else:
            print("valor invalido: digite par ou impar! ")

print(f'GAME OVER! Voce venceu em {vitoria} vezes.')


