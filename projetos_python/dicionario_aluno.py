alunos = dict()

alunos['Nome'] = str(input("Nome: "))
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
print("-=" * 20)

if alunos['Média'] >= 7 :
    alunos['Situação'] = "Aprovado"
elif alunos['Média'] >= 5 and alunos['Média'] < 7:
    alunos['Situação'] = "Recuperação"
else:
    alunos['Situação'] = "Reprovado"

for k,v in alunos.items():
    print(f'{k} é igual a {v}')