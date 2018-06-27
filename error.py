# -*- coding: utf-8 -*-

import urllib
import urllib.request

url = 'http://www.k1221fqwd23c.com.cn/kfccda/index.aspx'

try:
    response = urllib.request.urlopen(url=url)
except Exception as e:
    print(e)

print(response.read().decode('utf-8'))
