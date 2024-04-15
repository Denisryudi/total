#passo 1: importar base de dados
import pandas as pd

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")

#deletar coluna inútil. axis = eixo. 0 -> linha e 1 -> coluna
tabela = tabela.drop("Unnamed: 8", axis=1)

#passo 2 visualizar base de dados
    #entender as informações disponíveisp
    #procurar as cagadas da base de dados
display(tabela)

#passo 3: tratamento de Dados
    #valores no formato errado
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
    #valores vazios
tabela = tabela.dropna() #joga as linhas com valor vazio fora
print(tabela.info()) #verificar quantidade e características(string, int)

#passo 4: analise inicial = entender como estão as notas dos clientes
display(tabela.describe())

#passo 5: análise Completa = troçar o perfil ideal de clientes = entender 

#palpites: cliente que vem por promoção é pior
import plotly.express as px 

#cria o gráfico. obs: utilizando o plotly primeiro cria o gráfico dp exibe. nbins = numero de divisões
for coluna in tabela.columns: #for imprime todos
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    

#exibe o gráfico
    grafico.show()


#como cada característica do cliente impacta na nota
#perfil ideal de cliente
#clientes acima de 10 anos
#àreas de tabalho: Entretenimento e artista (evitar construção)
#Tem entre 10 e 15 anos de experiência
#Famílias de até 7 pessoas

#média 52 de nota, mas 75% tem nota ate 77 
#obs: final
# O salário não parece fazer muita diferença. Clientes de promoção parecem ter uma leve nota menor, mas não tanto