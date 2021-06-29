lista = list()
media = "MEDIA"
name = "NOME"

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    perg = str(input("Quer continuar? [S/N] ")).strip()[0]
    lista.append([nome, nota1, nota2])
    
    if perg in "Nn":
        break

print("-=" * 30)
print('No.',  f'{name:^10}', f'{media:^10}')
print("-" * 30)

for i in range(len(lista)):
    média = (lista[i][1] + lista[i][2]) / 2
    print(i, f'{lista[i][0]:^15}', f'{média:^3}')
print("-" * 30)

while True:
    i = int(input("Mostrar as notas de qual aluno? (999 interrompe): "))
    
    if i == 999:
        print("Volte sempre!")
        break
    
    while i >= len(lista):
        print("Opção inválida!")
        i = int(input("Mostrar as notas de qual aluno? (999 interrompe): "))
    print(f'As notas de {lista[i][0]} são {lista[i][1]}, {lista[i][2]}')
    print("-" * 30)
    

    