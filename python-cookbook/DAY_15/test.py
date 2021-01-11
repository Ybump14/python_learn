d = {'one': 1, 'two': 2}

d.update({'three': 3, 'four': 4})  # 传一个字典
print(d)

d.update(five=5, six=6)  # 传关键字
print(d)

d.update([('seven', 7), ('eight', 8)])  # 传一个包含一个或多个元组的列表
print(d)

d.update((['nice', 9], ['ten', 10]))  # 传一个包含一个或多个列表的元组
print(d)

d.update(zip(['eleven', 'twelve'], [11, 12]))  # 传一个zip()函数
print(d)

d.update(one=111, two=222)  # 使用以上任意方法修改存在的键对应的值
print(d)
