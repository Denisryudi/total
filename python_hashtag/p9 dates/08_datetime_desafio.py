#Um usuário fornece sua data de nascimento no formato "dd/mm/aaaa".
#Crie um script Python que calcula a idade do usuário.

from datetime import datetime

data_atual = datetime.now()

data_nascimento = input('Digite sua idade: ''dd/mm/aaaa')


data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
print(data_nascimento)

idade= data_atual.year - data_nascimento.year


mes_atual = data_atual.month - data_nascimento.month
dia_atual = data_atual.day - data_nascimento.day

mes_nascimento = data_nascimento.month
dia_nascimento = data_nascimento.day

if mes_nascimento > mes_atual:
    idade -= 1
elif mes_nascimento == mes_atual and dia_nascimento > dia_atual:
    idade -= 1


print(idade)