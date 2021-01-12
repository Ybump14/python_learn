'''11.1 作为客户端与HTTP服务交互
问题:
你需要通过HTTP协议以客户端的方式访问多种服务。例如，下载数据或者与基于REST的API进行交互。

解决方案:
对于简单的事情来说，通常使用 urllib.request 模块就够了。例如，发送一个简单的HTTP GET请求到远程的服务上，可以这样做'''

from urllib import request, parse
# Base URL being accessed
url = 'http://httpbin.org/get'

# Dictionary of query parameters (if any)
parms = {
    'name1': 'value1',
    'name2': 'value2'
}

# Encode the query string
# querystring =

# Make a GET request and read the response
u = request.urlopen(url + '?' + parse.urlencode(parms)).read()


