#Uma empresa tem escritórios em São Paulo, Nova York e Tóquio. Crie um script Python que mostra
#a data e hora atuais nesses três fusos horários. Exiba, também, se estes escritórios estão
#abertos ou fechados (9h às 17h).

from datetime import datetime
from zoneinfo import ZoneInfo

data_atual = datetime.now()

print(data_atual.strftime('%A, %d de %B'))

fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
data_hora_sao_paulo = data_atual.astimezone(fuso_horario_sao_paulo)
print(f"Data/hora atual em São Paulo: {data_hora_sao_paulo}")

fuso_horario_nova_york = ZoneInfo('America/New_York')
data_hora_nova_york = data_atual.astimezone(fuso_horario_nova_york)
print(f"Data/hora atual em Nova York: {data_hora_nova_york}")

fuso_horario_toquio = ZoneInfo('Asia/Tokyo')
data_hora_toquio = data_atual.astimezone(fuso_horario_toquio)
print(f"Data/hora atual em Tokyo: {data_hora_toquio}")

def verificar_horario(data_hora):
    if 9 <= data_hora.hour <17:
        return 'aberto'
    else:
        return 'fechado'


print(f'Escritorio de sp esta {verificar_horario(data_hora_sao_paulo)}')
print(f'Escritorio de ny esta {verificar_horario(data_hora_nova_york)}')
print(f'Escritorio de tokyo esta {verificar_horario(data_hora_toquio)}')