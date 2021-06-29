# Lista ordenada sem usar laços de repetição

lista = list()

num = int(input("\nDigite um valor: "))    # posição 0 na lista
lista.append(num)
print("adicionado ao final da lista...")

num = int(input("Digite um valor: "))   # posição 1 na lista
if num < lista[0]:
    lista.insert(0, num)
    print(f"adicionado à posição {lista.index(num)} da lista")
elif num > lista[0]:
    lista.insert(1, num)
    print(f"adicionado ao final da lista")

num = int(input("Digite um valor: "))    # posição 2 na lista
if num < lista[0]:
    lista.insert(0, num)
    print(f"adicionado à posição {lista.index(num)} da lista")
elif lista[0] < num < lista[1]:
    lista.insert(1, num)
    print(f"adicionado à posição {lista.index(num)} da lista")
elif num > lista[1]:
    lista.insert(2, num)
    print(f"adicionado ao final da lista")

num = int(input("Digite um valor: "))   # posição 3 na lista
if num < lista[0]:
    lista.insert(0, num)
    print(f"adicionado à posição {lista.index(num)} da lista")
elif lista[0] < num < lista[1]:
    lista.insert(1, num)
    print(f"adicionado à posição {lista.index(num)} da lista")
elif lista[1] < num < lista[2]:
    lista.insert(2, num)
    print(f"adicionado à posição {lista.index(num)} da lista")
elif num > lista[2]:
    lista.insert(3, num)
    print(f"adicionado ao final da lista")

num = int(input("Digite um valor: "))   # posição 4 na lista
if num < lista[0]:
    lista.insert(0, num)
    print(f"adicionado à posição {lista.index(num)} da lista")
elif lista[0] < num < lista[1]:
    lista.insert(1, num)
    print(f"adicionado à posição {lista.index(num)} da lista")
elif lista[1] < num < lista[2]:
    lista.insert(2, num)
    print(f"adicionado à posição {lista.index(num)} da lista")
elif  lista [2] < num < lista[3]:
    lista.insert(3, num)
    print(f"adicionado à posição {lista.index(num)} da lista")
elif num > lista[3]:
    lista.insert(4, num)
    print(f"adicionado ao final da lista")

print("-=" * 30)
print(f'Os valores digitados em ordem foram {lista}')

