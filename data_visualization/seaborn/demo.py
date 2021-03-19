import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

x1 = ['小米', '三星', '华为', '苹果', '魅族', 'VIVO', 'OPPO', '小米', '三星', '华为', '苹果', '魅族', 'VIVO', 'OPPO']
y3 = [46, 95, 134, 127, 101, 140, 75, 80, 116, 36, 71, 142, 28, 29]
index1 = ['商家A', '商家A', '商家A', '商家A', '商家A', '商家A', '商家A']
index2 = ['商家B', '商家B', '商家B', '商家B', '商家B', '商家B', '商家B']
index1.extend(index2)
df = pd.DataFrame({'品牌': x1, '数据': y3, 'index': index1})

sns.barplot(x='品牌', y='数据', data=df, hue='index')
plt.xticks(rotation=90)
plt.show()
