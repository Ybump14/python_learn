'''6.3 解析简单的XML数据
问题:
你想从一个简单的XML文档中提取数据。

解决方案:
可以使用 xml.etree.ElementTree 模块从简单的XML文档中提取数据。 为了演示，假设你想解析Planet Python上的RSS源。'''
from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

# Extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()
