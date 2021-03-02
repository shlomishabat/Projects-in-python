import urllib.request
import requests
from bs4 import BeautifulSoup
import time
def comper(list1,s):
    splet1 = list1.split('/')
    if list1[0] == '.':
        list1 = flink + list1[5:]
        splet1 = list1.split('/')
    for l in splet1 :
        if l == 'DigitalWhisper' + str(x)+'.pdf' and  str(l) !='DigitalWhisper12.pdf' and  str(l) !='DigitalWhisper37.pdf':
            print (list1)
            urllib.request.urlretrieve(list1, r'D:\\לימודים\\סייבר -אלתא\\scraping\\files\\ss' + str(splet1[-2]) + str(splet1[-1]))
    #if splet1[1]=='f':
     #  if list1[0]=='h':
      #     req1=requests.get(list1)
       #    urllib.request.urlretrieve(list1, r'D:\\לימודים\\סייבר -אלתא\\scraping\\files\\' +str(splet1[-2]) +str(splet1[-1] ))
       #elif list1[0]=='.':
        #   req= requests.get(flink +list1[5:])
         #  urllib.request.urlretrieve(flink +list1[5:], r'D:\\לימודים\\סייבר -אלתא\\scraping\\files\\' +str(splet1[-2]) +str(splet1[-1]))




flink='https://www.digitalwhisper.co.il'


for x in range (1,127):
    url = 'https://www.digitalwhisper.co.il/issue'+str(x)
    source = urllib.request.urlopen(url)
    data = BeautifulSoup(source,'html.parser')
    atags = data.find_all('a')
    for link in atags:
        list_a=str(link.get('href'))
        comper(list_a,x)
