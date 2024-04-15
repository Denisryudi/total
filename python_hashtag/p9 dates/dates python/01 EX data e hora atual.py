#Uma empresa quer exibir a data e a hora atual em seu site no formato "Dia da semana, dia do mês de mês do ano, horas:minutos".
#Crie um script Python que mostra a data e a hora atuais neste formato.

import locale
import time
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tempo_em_struct = time.localtime()

tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S", tempo_em_struct)
print(f"Tempo formatado: {tempo_formatado}")


tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M", tempo_em_struct)

print(f"Data e hora atuais: {tempo_formatado}")