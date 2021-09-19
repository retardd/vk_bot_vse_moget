from cv2 import CascadeClassifier
import cv2
import requests
from io import BytesIO
from PIL import Image
from urllib.request import urlopen
import numpy as np


def face_detect(url):
    duck = []
    req = urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        duck.append(y + (10 * h) // 21)
        duck.append(x + (2 * w) // 5)
        duck.append(h//4)
    return duck

def cloun2(url):
    tochki = face_detect(url)
    nosik = Image.open('../../content/nosik.png').convert("RGBA")
    size = (tochki[2] // 4, tochki[2] // 4)
    nosik = nosik.resize(size)
    response = requests.get(url)
    image = Image.open(BytesIO(response.content)).convert("RGBA")
    image.paste(nosik, (x2, x1), nosik)

    return image




url = 'https://sun9-31.userapi.com/c855228/v855228794/19f86c/7lhAA3tXcA4.jpg'
req = urlopen(url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1)
nosik = Image.open('../../content/nosik.png').convert("RGBA")

classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = classifier.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    x1 = y+(10*h)//21
    x2 = x+(2*w)//5

size = (h//4, h//4)
nosik = nosik.resize(size)
response = requests.get(url)
image = Image.open(BytesIO(response.content)).convert("RGBA")
image.paste(nosik, (x2, x1), nosik)


image.show()