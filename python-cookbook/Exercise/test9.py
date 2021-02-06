import random
import string

'''
圣诞节到了，公司举行交换礼物活动，参加的员工每人准备一个礼物。
交换完成后，自己的礼物会随机给到另一个人，自己也能随机获得一个其他人准备的礼物。
不要求A拿了B的礼物.，B就一定要拿A的，只要自己不拿自己的即可。为公平起见，请你写一个随机程序来决定礼物何分配。'''

k = {'a': '苹果',
     'b': '梨子',
     'c': '香蕉',
     'd': '菠萝',
     'e': '哈密瓜',
     'f': '草莓',
     'g': '车厘子',
     }  # 假设员工已准备好礼物，且员工名称和礼物名称唯一
k1 = (list(k.keys()))  # 员工重组为一个list
k3 = {}


# case1
def case1():  # 生成一个礼物重新分配后的新字典方法
    k2 = list(k.values())  # 礼物重组为一个list
    for i in range(len(k2)):  # 将礼物随机分配给员工，重组为k3
        x = random.choice(k2)
        k3[k1[i]] = x
        k2.remove(x)
    for i in k1:  # 遍历员工
        if k.get(i) == k3.get(i):  # 随机分配后遍历员工，若存在员工拿到自己原本的礼物，就重新随机，生成新的k3
            case1()
    return k3


# case2
def case2():
    k_staff_random = random.sample(list(k.keys()), len(list(k.keys())))  # 打乱员工排序
    for n in range(len(k_staff_random)):
        if n < len(k_staff_random) - 1:
            k3[k_staff_random[n]] = k.get(k_staff_random[n + 1])
        else:
            k3[k_staff_random[n]] = k.get(k_staff_random[0])
    return k3


print(k)
print(case1())
print(case2())


# python生成100个不重复的4位数随机数
def gen():
    x = []
    while len(x) < 1000:
        a = "".join([random.choice(string.digits) for i in range(4)])
        if a not in x:
            x.append(a)
    return x
