# Situação de Aprendizagem 3 - Programação de Aplicativos
from tkinter import *

def calcular_troco():

    if float(compra.get()) > float(pagamento.get()): # caso o cliente pagar um valor menor da compra
        saida1["text"] = "Valor errado!"
        
    else: # caso o cliente pagar um valor maior ou igual ao da compra
        troco = float(pagamento.get()) - float(compra.get())
        saida1["text"] = "R$ " + str(f'{troco:.2f}')

        for valor in [50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]:
            
            quantidade = troco // valor # divisão inteira que fornece a quantidade de notas e moedas
            troco = round((troco - (quantidade * valor)), 2) # valor que sobra a cada loop

            if quantidade > 0:

                if valor <= 1: # se o valor for igual ou menor que 1 real teremos moedas e não notas
                    moeda = "moeda"
                    valor = f'{valor:.2f}'.replace(".",",")
                    if quantidade > 1:
                        moeda = "moedas"
                    lista.insert(END, f'{int(quantidade)} {moeda}: R$ {valor}')
                
                else: # neste caso teremos apenas notas como troco
                    nota = "nota"
                    valor = f'{valor:.2f}'.replace(".",",")
                    if quantidade > 1:
                        nota = "notas"
                    lista.insert(END, f'{int(quantidade)} {nota}: R$ {valor}')
                

janela = Tk() 
janela.title("Calculadora de troco") 
janela.geometry("230x450+200+200") # largura e altura + posicionamento na tela (x,y) 
janela.iconbitmap("C:\\Users\\USUARIO\\Desktop\\SENAI\\python\\interface_python\\treetog.ico")


# widgets

texto_1 = Label(janela, text = "Valor da compra:", font=("Arial",14), foreground="black", anchor=W)
compra = Entry(janela, font=("Arial",14), bd=2, justify="right")
texto_2 = Label(janela, text = "Valor pago:", font=("Arial",14), foreground="black", anchor=W)
pagamento = Entry(janela, font=("Arial",14), bd=2, justify="right")
botao1 = Button(janela, text = "Calcula Troco", command=calcular_troco)
texto_3 = Label(janela, text = "Troco:", font=("Arial",14), foreground="blue")
saida1 = Label(janela, text = "", font=("Arial",14), fg="red")
saida2 = Label(janela, text= "", font=("Arial",14))
saida3 = Label(janela, text= "", font=("Arial",14))
lista = Listbox(janela, font=("Arial,14"), bd=5, relief=SOLID, bg="yellow")


# layouts

texto_1.grid()
compra.grid()
texto_2.grid()
pagamento.grid()
botao1.grid(row=4)
texto_2.grid()
texto_3.grid(row=5)
saida1.grid()
saida2.grid()
saida3.grid()
lista.grid()

janela.mainloop()


