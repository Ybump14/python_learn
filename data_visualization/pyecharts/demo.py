from pyecharts import options as opts
from pyecharts.charts import Bar

x = ['小米', '三星', '华为', '苹果', '魅族', 'VIVO', 'OPPO']
y1 = [46, 95, 134, 127, 101, 140, 75]
y2 = [80, 116, 36, 71, 142, 28, 29]

c = (
    Bar()
        .add_xaxis(x)
        .add_yaxis("商家AAA", y1)
        .add_yaxis("商家BBB", y2)
        .set_global_opts(title_opts=opts.TitleOpts(title="Pyecharts—柱状图", subtitle=""))
).render()

