from RowData.DataSet import dataset
import matplotlib.pyplot as plt
import numpy as np

x = np.array([i[0] for i in dataset])
print(x)
y = np.array([i[1] for i in dataset])
print(y)
a, b1, b2 = np.polynomial.polynomial.polyfit(x, y, deg=2)
ax1 = plt.subplot(1, 1, 1)
ax1.scatter(x, y, c='b', marker='o', alpha=1)
ax1.plot(x, a + b1 * x + b2 * (x ** 2), '_', label=r'$\hat{y} = a + b_1x + b_2x^2$')
ax1.legend()
ax1.set_title('Data')
ax1.set_xlabel('Data')
ax1.set_ylabel('Fishing Time')
plt.show()
