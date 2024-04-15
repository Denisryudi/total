from datetime import datetime, timedelta

data_atual = datetime.now()

data_futura = data_atual + timedelta(days=11)
print(data_futura)
#timedelta(hours=10) para horas

data = datetime(2023, 7, 20, 8, 30, 20, 2)
#ano-mes-dia-hora-minuto-segundos-microsegundos
print('--data2')
print(data)

print('somente data')
somente_data = datetime(2024, 1, 30)
print(somente_data)

print('iso')
data_hora_iso = datetime.fromisoformat('2024-01-30 16:12:00')
print(data_hora_iso)

print('diferenças')

data1 = datetime(2024, 1, 30)
data2 = datetime(2024, 6, 20)
diferencas = data2 - data1
print(diferencas)

if data1 > data2:
    print(f'Data 1 posterior a data 2')
else:
    print(f'Data2 posterior a data 1')




datas_ = [
    datetime(2023, 6, 28),
    datetime(2023, 5, 28),
    datetime(2023, 7, 28),
    datetime(2023, 6, 18),
]

datas_ordenadas = sorted(datas_)

print(datas_ordenadas)

for data in datas_ordenadas:
    print(data.date())
    #pode usar para time tb