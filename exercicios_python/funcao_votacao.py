def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    print(f'Sua idade é {idade} anos:')

    if idade < 16:
        return '\033[1;31mVoto Negado\033[m'
    elif idade >= 16 and idade < 18 or idade > 65:
        return 'Voto Opcional'
    else:
        return '\033[1;32mVoto Obrigatório\033[m'

nasc = int(input("Digite se ano de nascimento: "))
print(voto(nasc))

    