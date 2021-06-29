palavras = ("Java", "Python", "html", "VScode", "Ruby", "Aprender", "Programar", "Estudar", "Trabalhar", "Praticar", "Mercado", "Programador", "futuro")

for p in palavras:
    print(f'\nNa palavra {p} temos ', end = '')
    for l in p:
        if l in 'aeiou':
            print(f'{l} ', end = "")
                