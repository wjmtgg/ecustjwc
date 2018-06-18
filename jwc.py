from PIL import Image,ImageFont,ImageDraw
import requests
from bs4 import BeautifulSoup
import re


def jwcx(xh,sf,sou):
    print('学号身份证号',xh,sf)
    s= requests.Session()
    url1='http://59.78.108.120/ecustedu/K_StudentQuery/K_PatriarchQueryLogin.aspx'
    a=s.get(url1)
    c1=a.headers['Set-Cookie']
    co=re.split(';',c1)
    b=BeautifulSoup(a.text)
    tate=b.find_all('input')[0]['value']
    tion=b.find_all('input')[4]['value']
    headers={
        'Accept':'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
        'Accept-Encoding':'gzip,deflate',
        'Accept-Language':'zh-CN',
        'Cache-Control':'max-age=0',
        'Connection':'Keep-Alive',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'59.78.108.120',
        'Cookie':co[0],
        'Referer':'http://59.78.108.120/ecustedu/K_StudentQuery/K_PatriarchQueryLogin.aspx',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
        }
data={
        '__EVENTARGUMENT':'',
        '__EVENTTARGET':'',
        '__EVENTVALIDATION':tion,
        '__VIEWSTATE':tate,
        'BtnLogin':'%E7%99%BB%E5%BD%95',
        'TxtSFZH':sf,
        'TxtStudentId':xh
        }
    c=s.post('http://59.78.108.120/ecustedu/K_StudentQuery/K_PatriarchQueryLogin.aspx',data=data,headers=headers)
    d=s.get('http://59.78.108.120/ecustedu/K_StudentQuery/K_BigScoreTableDetail.aspx?key=1')
    e=BeautifulSoup(d.text)
    max=int((len(e.find_all('td'))-11)/7)
    str=''
    str=e.find_all('td')[1].get_text()+'\n\n'
    list=[]
    list.append(str)
    for i in range(1,max+1):
        str='学期：'+e.find_all('td')[i*7+3].get_text()+'\n课程名称：'+e.find_all('td')[i*7+4].get_text()+'\n课程性质：'+e.find_all('td')[i*7+5].get_text()+'\n平台类别：'+e.find_all('td')[i*7+6].get_text()+'\n成绩>：'+e.find_all('td')[i*7+7].get_text()+'\n学分：'+e.find_all('td')[i*7+8].get_text()+'\n绩点：'+e.find_all('td')[i*7+9].get_text()+'\n\n'
        list.append(str)
    str='学号：'+xh+'\n'
    for strs in list:
        str=str+strs
    text = str
    font=ImageFont.truetype('MSYH.TTF',14)
    lines = []
    line =''
    for word in text.split():
        lines.append(word)
    line_height = font.getsize(text)[1]
    img_height = line_height*(len(lines)+1)
    im = Image.new("RGB",(444,img_height),(255,255,255))
dr = ImageDraw.Draw(im)
    z,y=5,5
    for line in lines:
        dr.text((z,y),line,font=font,fill="#000000")
        y += line_height
    im.save("666.jpg")




