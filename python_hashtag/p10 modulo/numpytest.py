import matplotlib.pyplot as plt

import numpy as np

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)
print(meses)

plt.plot(meses, vendas)
plt.axis([0, 50, 0, max(vendas)+500])
plt.xlabel('meses')
plt.ylabel('vendas')
plt.show()


plt.plot(meses, vendas, 'ro')
plt.axis([0, 50, 0, max(vendas)+500])
plt.xlabel('meses')
plt.ylabel('vendas')
plt.show()

plt.plot(meses, vendas, 'r--')
plt.axis([0, 50, 0, max(vendas)+500])
plt.xlabel('meses')
plt.ylabel('vendas')
plt.show()

plt.plot(meses, vendas, 'bs', color='red')
plt.axis([0, 50, 0, max(vendas)+500])
plt.xlabel('meses')
plt.ylabel('vendas')
plt.show()

#https://matplotlib.org/stable/tutorials/pyplot.html


plt.scatter(meses, vendas)
plt.axis([0, 50, 0, max(vendas)+500])
plt.xlabel('meses')
plt.ylabel('vendas')
plt.show()

plt.bar(meses, vendas)
plt.axis([0, 50, 0, max(vendas)+500])
plt.xlabel('meses')
plt.ylabel('vendas')
plt.show()

plt.figure(1, figsize=(2, 3))
plt.subplot(1, 3, 1)
plt.scatter(meses, vendas)
plt.subplot(1, 3, 2)
plt.bar(meses, vendas)
plt.subplot(1, 3, 3)
plt.plot(meses, vendas, 'r--')