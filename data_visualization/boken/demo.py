import inline as inline
import matplotlib
from bokeh.transform import dodge
import pandas as pd
from bokeh.core.properties import value
import numpy as np
import matplotlib.pyplot as plt

from bokeh.io import output_notebook

output_notebook()  # 导入notebook绘图模块
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource  # 导入图表绘制、图标展示

x = ['小米', '三星', '华为', '苹果', '魅族', 'VIVO', 'OPPO']
y1 = [46, 95, 134, 127, 101, 140, 75]
y2 = [80, 116, 36, 71, 142, 28, 29]

x_ = x
df = pd.DataFrame({'商家A': y1, '商家B': y2},
                  index=x_)
_x = ['商家A', '商家B']  # 系列名
data = {'index': x_}
for i in _x:
    data[i] = df[i].tolist()  # 生成数据，数据格式为dict
source = ColumnDataSource(data=data)  # 将数据转化为ColumnDataSource对象

p = figure(x_range=x_, y_range=(0, 150), plot_height=350, title="boken-柱状图",
           tools="crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select")

p.vbar(x=dodge('index', -0.1, range=p.x_range), top='商家A', width=0.2, source=source, color="#718dbf",
       legend=value("商家A"))
p.vbar(x=dodge('index', 0.1, range=p.x_range), top='商家B', width=0.2, source=source, color="#e84d60",
       legend=value("商家B"))  # dodge(field_name, value, range=None) → 转换成一个可分组的对象，value为元素的位置（配合width设置）
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"  # 其他参数设置
show(p)
