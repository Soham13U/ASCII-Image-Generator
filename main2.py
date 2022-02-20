from lib2to3.pgen2 import driver
from urllib import request
from PIL import Image, ImageDraw, ImageFont
import requests
import math
import random
import json
import os
import sys
import imghdr
import urllib.parse
import urllib.request
from urllib.request import Request,urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
import re

import urllib3




chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = 0.09

oneCharWidth = 8
oneCharHeight = 15

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]



text_file = open("Output.txt", "w")

im = Image.open("gojo.jpg")

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))

    text_file.write('\n')

outputImage.save('output.png')
