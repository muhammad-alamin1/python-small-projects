# Collection information from http://dimik.pub web pages
import os
import re
import sys
import requests


url = 'http://dimik.pub'
response = requests.get(url)
if response.ok is False:
    sys.exit('Could not get response from server')

page_content = response.text

regexp = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<', re.S)
result = re.findall(regexp, page_content)
# print(result)

for item in result:
    print(f'''
        Name: {item[2]}
        URL : {item[0]}
        Img : {item[1]}
    ''')