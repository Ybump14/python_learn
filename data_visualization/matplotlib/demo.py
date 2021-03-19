import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
import warnings

warnings.filterwarnings("ignore")

x = ['小米', '三星', '华为', '苹果', '魅族', 'VIVO', 'OPPO']
y1 = [46, 95, 134, 127, 101, 140, 75]
y2 = [80, 116, 36, 71, 142, 28, 29]
width = 0.35
x1 = np.arange(len(x))

fig, ax = plt.subplots()
rects1 = ax.bar(x1 - width / 2, y1, width, label='商家A')
rects2 = ax.bar(x1 + width / 2, y2, width, label='商家B')

ax.set_title('Matplotlib—柱状图')
ax.set_xticks(x1)
ax.set_xticklabels(x)
ax.legend()

plt.show()
