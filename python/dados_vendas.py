import pandas as pd
import win32com.client as win32

#importa a planilha original em excel
tabela = pd.read_excel("vendas.xlsx")
#mostra todas as colunas originais da planilha
pd.set_option('display.max_columns', None)

#armazena, na tabela faturamento, a soma do valor final agrupado por loja
#a tabela faturamento filtra somente 2 colunas da tabela original
faturamento = tabela[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

print(faturamento)

#armazena, na tabela quantidade, o total de produtos vendidos por loja
#a tabela quantidade filtra somente 2 colunas da tabela original
quantidade = tabela[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

print(quantidade)

#armazena, na tabela ticket_medio, o valor do ticket medio por produto vendido em cada loja
#ticket_medio['Ticket Medio'] = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0:'Ticket Medio'})
print(ticket_medio)

#envio automatico do email para conta outlook especificada
outlook =  win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'dariodistaso@hotmail.com' #destinatario
mail.Subject = 'relatorio de vendas' #assunto email
#corpo email
mail.HTMLBody = f'''
<p>Bom dia,</p>
<p>Segue o relatório de vendas por cada loja:</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final':'R${:,.2f}'.format})}

<p>Quantidade vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos produtos em cada loja:</p>
{ticket_medio.to_html(formatters={'Ticket Medio':'R${:,.2f}'.format})}

<p>Att.</p>

<p>Dario Distaso</p>
'''

mail.Send()
print('email enviado com sucesso!')