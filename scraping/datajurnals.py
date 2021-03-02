import urllib.request
import requests
from bs4 import BeautifulSoup
import time
def comper(list1):
    newdata = open("data.txt","a")
    newdata.write(list1)
    newdata.write("\n")







flink='https://www.digitalwhisper.co.il'

for x in range (1,125):
    url = 'https://www.digitalwhisper.co.il/issue'+str(x)
    source = urllib.request.urlopen(url)
    data = BeautifulSoup(source,'html.parser')
    atags = data.find_all('a')
    newdata = open("data.txt", 'a')
    newdata.write(str(x)+ ''' ''' )
    newdata.close()
    for link in atags:
        list_a=str(link.get('href'))
        comper(list_a)
