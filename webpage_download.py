import requests
import os
import webbrowser as wb

url = 'http://dimikcomputing.com'
response = requests.get(url)

if __name__ == '__main__':
    if response.status_code == 200:
        with open('dimik.html', 'w', encoding=response.encoding) as f:
            f.write(response.text)

file_path = os.path.relpath('dimik.html')
wb.open('file://' + file_path)
