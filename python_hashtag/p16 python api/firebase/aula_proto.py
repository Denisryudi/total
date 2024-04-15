import requests
import json
from dotenv import load_dotenv
import os
from io import StringIO
import pandas as pd
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa a variável de ambiente CHAVE_API
link = os.getenv('CHAVE_FIREBASE')

#criar uma venda(post)
# dados= {'cliente': 'lele', 'preco': 150, 'produto': 'teclado'}
# requisicao = requests.post(f'{link}/Vendas/.json', data=json.dumps(dados))
# print(requisicao)
# print(requisicao.text)

# Editar a venda (PATCH)
# dados = {'cliente': 'lira'}
# requisicao = requests.patch(f'{link}/Vendas/ID1/.json', data=json.dumps(dados))
# print(requisicao)
# print(requisicao.text)

#venda especifica

requisicao = requests.get(f'{link}/Vendas/.json')
print(requisicao)
dic_requisicao = requisicao.json()
id_lira = None

for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if 'lira' in cliente:
        print(id_venda)
        id_lira = id_venda

print(id_lira)

#del

requisicao = requests.delete(f'{link}/Vendas/-NsGkLbna-TTiPznKhAn/.json')

print(requisicao)
print(requisicao.text)