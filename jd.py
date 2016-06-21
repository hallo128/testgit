#jd.py
# -*- coding: utf-8 -*-  
import urllib2
import string
import re
from bs4 import BeautifulSoup

url = 'http://item.jd.com/2385681.html'
myPage = urllib2.urlopen(url).read().decode('gbk')

ll=myPage.encode("gbk")       #转换为字符格式
soup = BeautifulSoup(ll)

#---------------------------商品编号
soup_id=soup.find('div','fl')
s_id=str(soup_id).decode('utf-8')
id_k=s_id.rsplit('</')[0].rsplit('>')[2]
id_v=s_id.rsplit('</')[1].rsplit('>')[2]

11111111111111