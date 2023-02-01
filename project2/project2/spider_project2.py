city='cd'
page=1
url='https://'+city+'.lianjia.com/ershoufang/ty'+str(page)
#print(url)

import requests
import time
#response=requests.get(url)
response=requests.get(url, headers={'Connection':'close'})
#print(response.text)

time.sleep(0.5)

from lxml import etree
data=etree.HTML(response.text)
print(data) 


positionInfo=data.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[2]/div/a[1]')
print(type(positionInfo))
print(len(positionInfo))
for temp in positionInfo:
    print(temp.text)

time.sleep(0.5)


houseInfo=data.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[3]/div/text()')
print(type(houseInfo))
print(len(houseInfo))
for temp in houseInfo:
    print(temp)


time.sleep(0.5)


#爬取价格
priceInfo=data.xpath('//*[@id="content"]/div[1]/ul/li/div[1]/div[6]/div[1]/span/text()')
#//*[@id="content"]/div[1]/ul/li[1]/div[1]/div[6]/div[1]/span
#//*[@id="content"]/div[1]/ul/li[2]/div[1]/div[6]/div[1]/span
print(type(priceInfo))
print(len(priceInfo))
for temp in priceInfo:
    print(temp)
