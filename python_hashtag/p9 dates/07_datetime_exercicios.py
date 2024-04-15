from datetime import datetime, timedelta

data_atual = datetime.now()
data_ultima_compra = datetime(2024, 1, 1)
data_desconto = data_atual - data_ultima_compra
print(data_desconto)
if data_desconto.days >= 30:
    print(f'Desconto liberado, pois se passaram {data_desconto.days} desde a ultima compra')
else:
    print(f'Desconto negado, se passaram {data_desconto.days}')



