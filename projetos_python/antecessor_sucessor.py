from random import randint

print("""olá so seu computador, acabei de pensar em um número entre 0 e 10.
Será que consegue adivinhar qual foi?""")

computador = randint(1,10)
jogador = 0
palpite = 0

while jogador != computador:
    jogador = int(input("Qual o seu palpite? "))
    palpite += 1
    if jogador < computador:
        print("Mais...Tente mais uma vez.")
    elif jogador > computador:
        print("Menos...Tente mais uma vez.")
    else:
        print(f'Parabéns..você acertou em {palpite} palpites!')
    
