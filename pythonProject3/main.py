from RowData.DataSet import dataset
import numpy as np
x = [i[0] for i in dataset]
y = [i[1] for i in dataset]

a, b1, b2 = np.polynomial.polynomial.polyfit(x, y, deg=2)
e = f'y = {round(a, 3)}{"+" if b1>0 else ""}{round(b1, 3)}x{"+" if b2>0 else ""}{round(b2, 3)}x^2'
print(e)
