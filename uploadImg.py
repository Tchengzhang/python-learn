import requests
from bs4 import BeautifulSoup

url = "http://www.27270.com/ent/meinvtupian/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

html = requests.get(url, headers=headers)
msg = BeautifulSoup(html.text, "html.parser")
pic_url = msg.find_all('img')
for i in range(len(pic_url)):
    html2 = requests.get(pic_url[i]['src'], headers=headers)
    f = open(R'e://image/%stest.jpg' % i, 'wb')
    f.write(html2.content)
    f.close()
    print('all %s in ' % i)
