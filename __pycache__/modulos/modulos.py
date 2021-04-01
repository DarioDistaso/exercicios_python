
def metade(p=0):
    metade = (p / 2)
    return f'{metade:.2f}'.replace('.',',')


def dobro(p=0):
    dobro = (p * 2)
    return f'{dobro:.2f}'.replace('.',',')


def aumenta(p=0, taxa=0):
    porcent = (p + (p * taxa) / 100)
    return f'{porcent:.2f}'.replace('.',',')
    

def diminui(p=0, taxa=0):
    porcent = (p - (p * taxa) / 100)
    return f'{porcent:.2f}'.replace('.',',')

def moeda (p=0, m = 'R$'):
    return f'{m}{p:.2f}'.replace('.',',')