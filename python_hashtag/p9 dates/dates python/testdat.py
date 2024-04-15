from datetime import datetime
agora = datetime.now()

print(f'Agora são {agora}')
print(f'data: {agora.strftime("%d/%m")}')
print(f'data: {agora.date()}')
print(f'horas: {agora.time()}')
print(f'data: {agora.day}/{agora.month}')

#pode apenas importar o date(caso precise apenas da data).  time caso precise do horario