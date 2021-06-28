from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


#busca no chrome a cotacao do dolar
navegador = webdriver.Chrome()

navegador.get("https://www.google.com/")

navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")

navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

#busca no chrome a cotacao do euro
navegador = webdriver.Chrome()

navegador.get("https://www.google.com/")

navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

navegador.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro)


#busca no chrome a cotacao do ouro
navegador = webdriver.Chrome()

navegador.get("https://www.melhorcambio.com/")
navegador.find_element_by_xpath('//*[@id="commodity-hoje"]/tbody/tr[2]/td[2]/a/img').click()

aba_original = navegador.window_handles[0]
aba_nova = navegador.window_handles[1]

#vai para a nova aba do navegador
navegador.switch_to.window(aba_nova)
cotacao_ouro = navegador.find_element_by_id('comercial').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(",", ".")

print(cotacao_ouro)
navegador.quit()

produtos_df = pd.read_excel(r"C:\Users\USUARIO\Desktop\SENAI\exercicios_python\python\produtos.xlsx")

#mostra a tabela original dos preços dos produtos
print(produtos_df)
print('')


produtos_df.loc[produtos_df['Moeda'] == "Dólar", "Cotação"] = float(cotacao_dolar)
produtos_df.loc[produtos_df['Moeda'] == "Euro", "Cotação"] = float(cotacao_euro)
produtos_df.loc[produtos_df['Moeda'] == "Ouro", "Cotação"] = float(cotacao_ouro)

#calcula os preços atualizados com a cotação de hoje
produtos_df['Preço Base Reais'] = produtos_df['Preço Base Original'] * produtos_df['Cotação']
produtos_df['Preço Final'] = produtos_df['Preço Base Reais'] * produtos_df['Margem']

#mostra a tabela com as cotações e os preços atualizados
print(produtos_df)