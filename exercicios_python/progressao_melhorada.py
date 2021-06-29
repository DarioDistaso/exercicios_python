print("Gerador de PA")
print("-=" * 20)

n = int(input("Primeiro termo: "))
r = int(input("Razão da PA: "))
cont = 0

i = 0
while i < 10:
    print(n, "→ ", end = "")
    n += r
    i += 1
    cont += 1
print("PAUSA")

while True:
    repete = int(input("Quantos termos quer mostrar a mais? "))
    i = 0
    while i < repete:
        print(n, "→ ", end = "")
        n += r
        i += 1
        cont += 1
    if repete == 0:
        print(f'\n\033[0;31mProgressão finalizada com {cont} termos mostrados.\033[m\n')
        break
    print("PAUSA")


