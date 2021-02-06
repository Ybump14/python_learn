'''5.1 读写文本数据
问题:
你需要读写各种不同编码的文本数据，比如ASCII，UTF-8或UTF-16编码等。

解决方案:
使用带有 rt 模式的 open() 函数读取文本文件。'''

text1 = '初始内容1'
text2 = '初始内容2'
line1 = '覆盖内容1'
line2 = '覆盖内容2'
aa = '追加内容1'
bb = '追加内容2'


def output():
    with open('somefile.txt', 'rt', encoding='utf-8', newline='') as f:
        data = f.read()
        print(data)


def first():
    # Write chunks of text chapterData
    with open('somefile.txt', 'wt', encoding='utf8') as f:
        # f.write(text1)
        # f.write(text2)

        # 将 print() 函数的输出重定向到一个文件中去，指定 file 关键字参数，如下
        # 但是有一点要注意的就是文件必须是以文本模式打开。
        # 如果文件是二进制模式的话，打印就会出错
        print(text1, file=f)
        print(text2, file=f)
    output()


def second():
    # Redirected print statement
    with open('somefile.txt', 'wt', encoding='utf8') as f:
        # f.write(line1)
        # f.write(line2)
        print(line1, file=f)
        print(line2, file=f)
    output()


def three():
    with open('somefile.txt', 'at', encoding='utf8') as f:
        # f.write(aa)
        # f.write(bb)
        print(aa, file=f)
        print(bb, file=f)
    output()


first()
second()
three()
