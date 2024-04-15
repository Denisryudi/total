import pyautogui
import time

#pyautogui.click ->clicar com o mouse
#pyautogui.write ->escrever um texto
#pyautogui.press ->apertar uma tecla
#pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 1

pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=971, y=380)
pyautogui.write("meu login")

pyautogui.click(x=970, y=451)
pyautogui.write("minha senha")
time.sleep(3)

pyautogui.click(x=957, y=520)
time.sleep(3)
#configurar pra baixar o banco de dados

pyautogui.click(x=499, y=360, button="right")
pyautogui.click(x=683, y=770)
time.sleep(3)
pyautogui.press("enter")




#calculas indicadores
import pandas
#importar base de dados
tabela = pandas.read_csv(r"Compras.csv", sep=";")
display(tabela)
#r = python ler no formato cru. pandas as pd = apelido para a biblioteca. - pd.read

#calculo dos indicadores
#total_gasto
total_gasto = tabela["ValorFinal"].sum()
#quantidade
quantidade = tabela["Quantidade"].sum()
#preço médio
preco_medio = total_gasto / quantidade

print(total_gasto)
print(quantidade)
print(preco_medio)


import pyperclip

#enviar email para chefe

#entrar no email
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")
time.sleep(3)
#clicar em escrever
pyautogui.click(x=96, y=198)

#preencher o email
time.sleep(1)
pyautogui.write("e-mail")
time.sleep(1)
pyautogui.press("tab") #seleciona email
time.sleep(2)

pyautogui.press("tab") #passar para o campo do assunto
time.sleep(1)
pyautogui.write("relatorio de Compras")

pyautogui.press("tab") #passar para o corpo do email

texto = """
Prezados
Segue o relatório de compras
Total Gasto: tanto
Quantidade: tanto
Preço médio: tanto
Qualquer duvida é só falar
Att., Denis
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
#enviar
