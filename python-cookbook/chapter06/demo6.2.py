'''6.2 读写JSON数据
问题:
你想读写JSON(JavaScript Object Notation)编码格式的数据。

解决方案:
json 模块提供了一种很简单的方式来编码和解码JSON数据。 其中两个主要的函数是 json.dumps() 和 json.loads() ，
要比其他序列化函数库如pickle的接口少得多。 下面演示如何将一个Python数据结构转换为JSON：'''

import json

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data)
print(json_str)

# print(type(chapterData))  # <class 'dict'>
# print(type(json_str))  # <class 'str'>

with open('stocks.json', 'w') as f:
    json.dump(json_str, f)

with open('stocks.json', 'r') as f:
    f = json.load(f)
    print(f)
#     print(type(f))  # <class 'dict'>

with open('stocks.json', 'r') as f:
    f = f.read()
    print(f)
    # print(type(f))  # <class 'str'>
