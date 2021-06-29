print("Área do terreno")

def area(larg,comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a} m²')
    
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))

area(l,c)
