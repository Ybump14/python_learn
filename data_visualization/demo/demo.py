import plotly
import plotly.offline as py
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)

x = ['小米', '三星', '华为', '苹果', '魅族', 'VIVO', 'OPPO']
y1 = [46, 95, 134, 127, 101, 140, 75]
y2 = [80, 116, 36, 71, 142, 28, 29]

trace0 = go.Bar(
    x=x,
    y=y1,
    name='商家A',
)
trace1 = go.Bar(
    x=x,
    y=y2,
    name='商家B',
)
data = [trace0, trace1]
layout = go.Layout(
    title={
        'text': "Plotly-柱状图",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)
