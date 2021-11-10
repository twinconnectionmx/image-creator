import os
from PIL import Image, ImageFont, ImageDraw
from random import randrange
from datetime import date


sup = input("Ingresa el texto superior: ")
inf = input("Ingresa el texto inferior: ")

sup = sup.upper()
inf = inf.upper()

background = Image.open("assets/bg.png")
foreground = Image.open("assets/site.png")

basepath = 'assets/png foxpos/'
pngs = os.listdir(basepath)

pngNo = randrange(0,len(pngs))
png = Image.open("assets/png foxpos/"+pngs[pngNo])
png = png.resize((4500,3500), Image.ANTIALIAS)

draw = ImageDraw.Draw(background)
font = ImageFont.truetype("assets/Gibson Bold.ttf", 350)
draw.text((0, 500),sup,(255, 119, 0),font=font, align="center")
draw.text((0, 1000),inf,(0, 0, 0),font=font, align="center")

background.paste(png, (0, 1500), png)
background.paste(foreground, (1070, 4250), foreground)
today = date.today()
background.save(str(today)+'.png')