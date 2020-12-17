'''3.11 随机选择
问题:
你想从一个序列中随机抽取若干元素，或者想生成几个随机数。

解决方案:
random 模块有大量的函数用来产生随机数和随机选择元素。
比如，要想从一个序列中随机的抽取一个元素，可以使用 random.choice()'''

import random

values = [1, 2, 3, 4, 5, 6]

print(random.choice(values))  # 从一个序列中随机的抽取一个元素.
print(random.sample(values, 3))  # 提取出N个不同元素的样本.
random.shuffle(values)  # 想打乱序列中元素的顺序.
print(random.randint(0, 10))  # 生成随机整数.
print(random.random())  # 生成0到1范围内均匀分布的浮点数.
print(random.getrandbits(2))  # 生成N位随机位(二进制)的整数.
