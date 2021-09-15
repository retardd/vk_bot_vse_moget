from PIL import Image, ImageDraw, ImageFont, ImageColor
from io import BytesIO


fnt = ImageFont.truetype('content/arial.ttf', 30)
img = Image.open('content/fon.jpg')
d = ImageDraw.Draw(img)

def bitis(img):
    imgByteArr = BytesIO()
    img.save(imgByteArr, format='PNG')
    imgByteArr.seek(0)

    return imgByteArr