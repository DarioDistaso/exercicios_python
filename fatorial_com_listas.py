num = int(input("digite um numero: "))

lista = []

for x in range(num,0,-1):
    lista.append(x)

res = lista[0] * lista[1]

i = 2
while i < num:
    mult = res * lista[i]
    res = mult
    i += 1

def resultado():
    for i in range(len(lista)):
        print(lista[i], "x ", end = "")

print("O fatorial de", num, "! é = ", end = "")
resultado()
print(" = ", mult)





