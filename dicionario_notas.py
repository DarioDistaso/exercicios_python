def notas(*args, sit = False):
    """
    a funcao analisa as notas do aluno
    e mostra o total de notas
    a maior e a menor nota
    e a media total
    param n: aceita quantas notas quiser
    param sit: parametro opcional
    indicando se deve ou nao mostrar a 
    situacao

    """
    maior = menor = tot = soma = media = 0

    for i in range(len(args)):
        tot += 1
        soma += args[i]
        if i == 0:
            maior = args[0]
            menor = args[0]
        else:
            if args[i] > maior:
                maior = args[i]
            if args[i] < menor:
                menor = args[i]
    media = soma / len(args)
    dicionario = dict()
    dicionario['total'] = tot
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = media

    if sit == True:

        if media < 5:
            dicionario['situacao'] = 'REPROVADO'
        elif media >= 5 and media < 7:
            dicionario['situacao'] = 'RECUPERAÇÃO'
        else:
            dicionario['situacao'] = 'APROVADO'

    return dicionario
resp = notas(5.5, 3.5, 3.0, 4.5, 6.6, sit=True)
print("\n",resp) 
help(notas)