'''2.2 字符串开头或结尾匹配
问题:
你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme等等。

解决方案:
检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法。
如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传给 startswith() 或者 endswith() 方法
这个方法中必须要输入一个元组作为参数.
如果你恰巧有一个 list 或者 set 类型的选择项，
要确保传递参数前先调用 tuple() 将其转换为元组类型。'''

import os
from urllib.request import urlopen

filename = 'spam.txt'
url = 'http://www.python.org'
filename.endswith('.txt')  # True
filename.startswith('spam')  # True
url.startswith('http://www.python.org')  # True
url.endswith('.org')  # True
filenames = os.listdir(
    '../chapter01')  # ['demo1.1.py', 'demo1.2.py', 'demo1.3.py', 'demo1.4.py', 'demo3.12.py', 'demo6.1.py', 'test_demo.py']
print([name for name in filenames if
       name.startswith(('demo1.', 'test'))])  # ['demo1.1.py', 'demo1.2.py', 'demo1.3.py', 'demo1.4.py', 'test_demo.py']


def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name, encoding='utf-8') as f:
            return f.read()


url = 'http://www.python.org'
urls = 'E:\python_learn/python-cookbook/chapter02/demo2.2.py'
read_data(url)  # return 'http://www.python.org' content
read_data(urls)  # return 'demo2.2.py' content
