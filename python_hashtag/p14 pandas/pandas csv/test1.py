import pandas as pd
vendas_df = pd.read_csv(r"Contoso - Vendas - 2017.csv", sep=';')
#print(vendas_df[['Numero da Venda', 'Data da Venda', 'Data do Envio']])

#print(vendas_df['Data do Envio'][0])

vendas_df.info()
lista_clientes = vendas_df['ID Cliente']



#encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'


import pandas as pd

vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', encoding='latin-1', sep=';')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', encoding='latin-1', sep=';')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', encoding='latin-1', sep=';')

#usaremos o display para ver todos os dataframes
print(vendas_df)
print(produtos_df)
print(lojas_df)
print(clientes_df)


clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

print(clientes_df)
print(produtos_df)
print(lojas_df)


vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')

print(vendas_df)



vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do CLiente'})
print(vendas_df)

vendas_df = vendas_df.rename(columns={'E-mail': 'E-mail do CLiente'})
print(vendas_df)


frequencia_clientes = vendas_df['E-mail do CLiente'].value_counts()
print(frequencia_clientes)

frequencia_clientes[:200].plot(figsize=(15, 5), yticks=range(0, 100, 5))