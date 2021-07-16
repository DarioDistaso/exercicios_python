from tkinter import *  

def fatorial():
    lista = []
    lista_2 = []

    for x in range(int(entrada.get()),0,-1): #criação da lista de numeros
        lista.append(x)
        
    res = lista[0] * lista[1]
    i = 2
    while i < int(entrada.get()): #parte de calculo
        mult = res * lista[i]
        res = mult
        i += 1

    for y in lista:# parte grafica das multiplicações
        if y == 1:
            lista_2.append(y)
            lista_2.append("=")
            break
        lista_2.append(y)
        lista_2.append("x")

    texto2["text"] = f'O fatorial de {entrada.get()} é'
    texto3["text"] = lista_2
    texto4["text"] = res

janela = Tk()
janela.title('Fatorial')
texto1 = Label(janela, text="Calcular o fatorial de um numero", font=("Arial",30))
texto1.pack(padx=10, pady=10)
entrada = Entry(janela, width=5,font=("Arial",24))
entrada.pack()
botao = Button(janela, text="Calcular Fatorial", font=("Arial",20), command=fatorial)
botao.pack(padx=50, pady=50)
texto2 = Label(janela, text="", font=("Arial",20))
texto2.pack()
texto3 = Label(janela, text="", font=("Arial",20))
texto3.pack()
texto4 = Label(janela, text="", font=("Arial",20))
texto4.pack()

janela.mainloop()





