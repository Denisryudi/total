import matplotlib.pyplot as plt

vendas = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['Jan', 'Feb', 'Mar', 'abr', 'May', 'Jun', 'Jul', 'ago', 'sep', 'oct', 'nov', 'dec']

plt.plot(meses, vendas)
plt.xlabel('meses')
plt.ylabel('vendas')
plt.axis([0, 12, 0, max(vendas)+500])
plt.show()
