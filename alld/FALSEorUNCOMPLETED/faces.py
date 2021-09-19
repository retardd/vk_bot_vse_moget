from mtcnn import MTCNN
import cv2
from PIL import Image, ImageDraw, ImageFont, ImageColor
from io import BytesIO

img = cv2.cvtColor(cv2.imread("ivan.jpg"), cv2.COLOR_BGR2RGB)
detector = MTCNN()
coor = detector.detect_faces(img)
print(coor)
nosik = Image.open('../../content/nosik.png').convert("RGBA")
size = (coor[0]['box'][2]// 4, coor[0]['box'][2]// 4)
nosik = nosik.resize(size)
image = Image.open('ivan.jpg').convert("RGBA")
image.paste(nosik, (coor[0]['keypoints']['nose'][0] - size[0]//2, coor[0]['keypoints']['nose'][1] - size[0]//2), nosik)

image.save('out.png')