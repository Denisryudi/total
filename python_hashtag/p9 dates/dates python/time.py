import time
#import webbrowser as wb
#wb.open('https://google.com')

print('iniciando pausa')
time.sleep(1)
print('iniciando pausa')


tempo_em_segundos = time.time()
tempo_local = time.ctime(tempo_em_segundos)
print(f"Tempo local: {tempo_local}")


tempo_em_segundos = time.time()
tempo_local = time.localtime(tempo_em_segundos)

print(f"Tempo local: {tempo_local}")

print(tempo_local.tm_year)

print(tempo_local.tm_hour)

print(tempo_local.tm_mday)


# Dia da semana (0-6, 0 é segunda-feira, 6 é domingo). Documentação: https://docs.python.org/3/library/time.html#time.struct_time
print(tempo_local.tm_wday)

print(tempo_local.tm_yday)

print(tempo_local.tm_zone)

print(time.time()) #epoch time 1º janeiro 1970
print(time.ctime(time.time()))
print(time.localtime())