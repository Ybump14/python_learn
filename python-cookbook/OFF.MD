2.print(int('111', 2)) 的结果是？
```python
print(int('111', 2))  # 将111转化为整数111，再以2进制计算输出，结果为7
```

3.在python当中如何获取命令行参数？
```python
import sys
def get():
    print('参数个数', len(sys.argv), '个参数')
    print('参数列表', str(sys.argv))
    print('脚本名', sys.argv)
    for i in range(1, len(sys.argv)):
        print('参数 %s 为: %s' % (i, sys.argv[i]))
```

4.根据salary由大到小进行排序
```python
from operator import itemgetter
test = [{'name': 'tom', 'salary': 20000}, {'name': 'jack', 'salary': 15000}, {'name': 'liming', 'salary': 10000}]
row = sorted(test, key=itemgetter('salary'))
print(row)  # [{'name': 'liming', 'salary': 10000}, {'name': 'jack', 'salary': 15000}, {'name': 'tom', 'salary': 20000}]
```

5.python中id、is、=、== 分别是比较什么的？
- id是内存地址
- is 是比较两边的内存地址是否相等
- =是赋值
- ==是比较的两边的数值是否相等
```python
name = 'Tom_`122.;sssssssssssssssssssssssss'
print(id(name))  #
name2 = 'Tom_`122.;sssssssssssssssssssssssss'
print(id(name2))  # id是内存地址
tg1 = 333
print(id(tg1))
tg2 = 333
print(id(tg2))
print(tg1 is tg2)
print(name is name2)
print(name == name2)
```

6.什么是小数据池
> Python自动将-5~256的整数进行了缓存，
> 当你将这些整数赋值给变量时，并不会重新创建对象，而是使用已经创建好的缓存对象。

> python会将一定规则的字符串在字符串驻留池中创建一份，
> 当你将这些字符串赋值给变量时，并不会重新创建对象， 而是使用在字符串驻留池中创建好的对象。

> 其实，无论是缓存还是字符串驻留池，都是python做的一个优化，就是将-5~256的整数，和一定规则的字符串，放在一个‘池’（容器，或者字典）中，
> 无论程序中那些变量指向这些范围内的整数或者字符串，那么他直接在这个‘池’中引用，言外之意，就是内存中只创建一个。

> 优点：
- 能够提高一些字符串，整数处理在时间和空间上的性能；
- 需要值相同的字符串，整数的时候，直接从‘池’里拿来用，
- 避免频繁地创建和销毁，提升效率，节约内存。

> 缺点：
- 在‘池’中创建或插入字符串、整数时，会花费更多的时间。'''

7.truncate的作用?

- truncate的作用是清空表或者说是截断表，只能作用于表'''

9.pass、continue、break、exit分别是什么作用
- pass 作用：可用pass占位
```python
def function(**kwags):
    pass
```
- break  作用：结束当前循环
```python
for a in range(10):
    if a == 5:
        break
    print(a)
# 只打印0到4
```
- continue 作用：跳过当前循环轮次，去执行下一轮循环。
```python
for a in range(10):
    if a == 5:
        continue
    print(a)
#从0到9，只跳过5
```

10.python当中的赋值、浅拷贝、深拷贝有什么区别
- 赋值：只是将变量指向了原对象，其实就是对象的引用（别名）；
- 浅拷贝(copy)：copy 模块的 copy 方法，只拷贝父对象，不会拷贝对象的内部的子对象；
- 深拷贝(deepcopy)：copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。
> 复制可变对象时:
- 赋值并没有生成新的对象，只是将变量指向了原对象，
- 而浅拷贝和深拷贝都生成了新的对象，但是浅拷贝没有复制对象的子对象
```python
import copy
testlist = [3,4]
cc = copy.copy(testlist)
dd = copy.deepcopy(testlist)
id(cc)
147365080
id(dd)
143244904
id(testlist)
147351272
```
> 复制不可变对象时
- 区别是浅拷贝也没有生成新的对象，而是和赋值一样，直接指向了原对象。
```python
import copy
a = (1,2)
b=copy.copy(a)
c=copy.deepcopy(a)
id(a)
147347536
id(b)
147347536
id(c)
147347536
```

12.python中的可变数据类型有哪些？为什么叫做可变数据类型？
> 不可变:整型/字符串元组
- 不可变数据类型:当该数据类型的对应变量的值发生了改变，那么它对应的内存地址也会发生改变，对于这种数据类型，就称不可变数据类型。
> 可变:列表/集合/字典	
- 可变数据类型:当该数据类型的对应变量的值发生了改变，那么它对应的内存地址不发生改变，对于这种数据类型，就称可变数据类型。

17.字符串的拼接可以使用+和join完成，两者有什么区别？
> 使用 + 
- 首先需要知道的是，在python中字符串属于不可变对象。
- 当用操作符+连接字符串的时候，由于字符串是不可变对象，其工作原理实际上是这样的：如果要连接如下字符串：S1+S2+S3+.......+SN，执行一次+操作便会在内存中申请一块新的内存空间，并将上一次操作的结果和本次操作的右操作数复制到新申请的内存空间，即当执行S1+S2的时候会申请一块内存，并将S1、S2复制到该内存中，依次类推，这样就要进行N-1次内存空间的申请了，非常影响效率。
> 使用 join
- 当使用join时，会一开始就计算出所需要的总的内存空间，也就是说只需要进行一次内存空间的申请，相比 使用 + ，效率提升巨大。
