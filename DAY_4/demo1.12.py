'''1.12 序列中出现次数最多的元素
问题:
怎样找出一个序列中出现次数最多的元素呢？

解决方案:
collections.Counter 类就是专门为这类问题而设计的'''

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts = Counter(words)
morewords_counts = Counter(morewords)

print(word_counts)
word_counts.update(morewords)
print(word_counts)

print(word_counts + morewords_counts)
print(word_counts - morewords_counts)
print(morewords_counts - word_counts)
