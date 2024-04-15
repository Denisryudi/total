import zoneinfo
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import locale

locale.setlocale(locale.LC_TIME, 'PT_br.utf-8')
agora =  datetime.now()
print(agora.strftime('%A, %d de %B'))

data_formatada = agora.strftime('%A, %d de %B de %Y, %H:%M:%S')
print(data_formatada)

#----formatos

# formato DD/MM/YYYY
string_data = "09/06/2023, 15:30:20"
formato = "%d/%m/%Y, %H:%M:%S"
data = datetime.strptime(string_data, formato)

print(f"Data: {data}")

# formato MM/DD/YYYY
string_data = "09/06/2023, 15:30:20"
formato = "%m/%d/%Y, %H:%M:%S"
data = datetime.strptime(string_data, formato)

print(f"Data: {data}")



#semfuso

fuso_horario = timezone.utc
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario)
print(f"Data/hora: {data_hora}")



print('com fuso')
#com fuso
fuso_horario_sao_paulo = timezone(timedelta(hours=-3))
data_hora = datetime(2023, 6, 26, 15, 30, 20, tzinfo=fuso_horario_sao_paulo)
print(f"Data/hora: {data_hora}")


print('fusos-------')

print('Horario maquina')
data_hora_atual = datetime.now()
print(f"Data/hora atual (fuso horário local): {data_hora_atual}")

print('Hora sp')
fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario_sao_paulo)
print(f"Data/hora atual em São Paulo: {data_hora_sao_paulo}")

print('hora ny convert')
fuso_horario_ny = ZoneInfo('America/New_York')
data_hora_ny = data_hora_atual.astimezone(fuso_horario_ny)
print(f"Data/hora atual em Nova York: {data_hora_ny}")
