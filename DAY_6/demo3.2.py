'''3.2 执行精确的浮点数运算
问题:
你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现。

解决方案:
浮点数的一个普遍问题是它们并不能精确的表示十进制数。
并且，即使是最简单的数学运算也会产生小的误差
如果你想更加精确(并能容忍一定的性能损耗)，你可以使用 decimal 模块'''

from decimal import Decimal

a = 4.2
b = 2.1
print(a + b)  # Outputs 6.300000000000001

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)  # Outputs 6.3
c = Decimal(4.2)
d = Decimal(2.1)
# 当Decimal参数不为字符串类型时，仍然可能出现精度问题
print(c + d)  # Outputs 6.300000000000000266453525910
