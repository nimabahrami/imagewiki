import requests
import urllib
import re
import io
import textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

website=input("insert the website url here: \n")
req=requests.get(website)
pars=BeautifulSoup(req.text,'html.parser')
result=pars.find_all('p')
images=pars.find('img',attrs={'class':'thumbimage'})['src']
image_url='https:'+images
image_url_get=urllib.request.urlopen(image_url)
thumbnail_get=io.BytesIO(image_url_get.read())
thumbnail=Image.open(thumbnail_get).resize((275,600))
print(image_url)
f=''
for i in range(10):
    paragraphs=re.sub(r'<.*?>','',str(result[i]))
    f=f+paragraphs
l=len(result)
print(l)
printable=f.replace('<p>','')[0:550]+"..."
print(printable)

source_img = Image.open('thumbnail.jpeg')
draw = ImageDraw.Draw(source_img)
draw.rectangle(((0, 00), (800, 600)), fill="#222b45")
lines = textwrap.wrap(printable, width=40)
w,h=draw.textsize(lines[0].encode('utf-8'))
y_text = 40
y_text_p = 110
titles=website.split('/')[-1].replace('_',' ')
titles_wrap= textwrap.wrap(titles, width=20)
fontsize=10
font=ImageFont.truetype(font='georgia.ttf',size=22)
font_title=ImageFont.truetype(font='georgiab.ttf',size=28)

for title in titles_wrap:
    draw.text(((840-w)/2, y_text), title,font=font_title)
    y_text += 28

for line in lines:
    draw.text(((840-w)/2, y_text_p), line,font=font)
    y_text_p += 26
    
source_img.paste(thumbnail,(0,0))
img_res=source_img.save('kir.png')
