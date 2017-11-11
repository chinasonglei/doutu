# -*- coding=UTF-8 -*-
import requests
import re
import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='meizi',
)

cursor = db.cursor()

def getImagesList(page):
    res = requests.get('http://www.doutula.com/photo/list '.format(page))
    html = res.text
    reg = r'<a target=.*?<img src="(.*?)" alt="(.*?)"'
    reg = re.compile(reg, re.S)
    imagesList = re.findall(reg, html)
    for i in imagesList:
        cursor.execute("insert into meitu(imageName,imageUrl) values('{}','{}')".format(i[1],i[0]))
        db.commit()

for i in range(1,73):
    #print('爬去第{}页'.format(i))
    getImagesList(i)

db.close()
