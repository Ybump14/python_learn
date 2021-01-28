'''2.4 字符串匹配和搜索
问题:
你想匹配或者搜索特定模式的文本

解决方案:
如果你想匹配的是字面字符串，那么你通常只需要调用基本字符串方法就行，
比如 str.find() , str.endswith() , str.startswith() 或者类似的方法：'''
import re

text = 'yeah, but no, but yeah, but no, but yeah'

print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.endswith('yeah'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
