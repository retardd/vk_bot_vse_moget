from alld.generaldirectory.priority.mainvkcfg import *
from alld.generaldirectory.priority.pictureoverall import *
from mtcnn import MTCNN
import cv2

def face_detect():
    img = cv2.cvtColor(cv2.imread("content/ivan.jpg"), cv2.COLOR_BGR2RGB)
    detector = MTCNN()
    return detector.detect_faces(img)


def get_pic(mid):
    picture = vk.messages.getById(message_ids=mid)['items']
    pict = {}
    if len(picture[0]['attachments']) == 0:
        if 'reply_message' in picture[0]:
            pict = picture[0]['reply_message']['attachments'][0]['photo']['sizes']
        elif len(picture[0]['fwd_messages']) != 0:
            for fwd in picture[0]['fwd_messages']:
                if len(fwd['attachments']) != 0:
                    if 'photo' in fwd['attachments'][0]:
                        pict = fwd['attachments'][0]['photo']['sizes']
    else:
        pict = picture[0]['attachments'][0]['photo']['sizes']
    if pict != {}:
        pic = 0
        for photoType in pict:
            if photoType.get('type') == 'x':  # <=604x604
                pic = photoType.get('url')
            if photoType.get('type') == 'y':  # >605x605
                pic = photoType.get('url')
            if photoType.get('type') == 'z':  # <=1280x720
                pic = photoType.get('url')
            if photoType.get('type') == 'w':  # >1280x720
                pic = photoType.get('url')
        return pic
    else:
        return 0




def cloun(too, mid, uid):
    try:
        url = get_pic(mid)
        if url != 0:
            img_data = requests.get(url).content
            with open('content/ivan.jpg', 'wb') as handler:
                handler.write(img_data)
        else:
            vava = vk.messages.getById(message_ids=mid)['items']
            url = uid
            if 'reply_message' in vava[0]:
                url = vava[0]['reply_message']['from_id']
            elif len(vava[0]['fwd_messages']) > 0 and 'from_id' in vava[0]['fwd_messages'][0]:
                url = vava[0]['fwd_messages'][0]['from_id']
            if url > 0:
                try:
                    zhzh = vk.users.get(user_ids=url, fields='photo_max')[0]
                    url = zhzh['photo_max']
                    img_data = requests.get(url).content
                    with open('content/ivan.jpg', 'wb') as handler:
                        handler.write(img_data)
                except:
                    url = 0
            else:
                url = 0
        if url != 0:
            coor = face_detect()
            nosik = Image.open('content/nosik.png').convert("RGBA")
            size = (coor[0]['box'][2] // 4, coor[0]['box'][2] // 4)
            nosik = nosik.resize(size)
            image = Image.open('content/ivan.jpg').convert("RGBA")
            image.paste(nosik, (coor[0]['keypoints']['nose'][0] - size[0] // 2, coor[0]['keypoints']['nose'][1] - size[0] // 2),
                nosik)
            b2 = bitis(image)
            send_image_b(too, 'sam cloun', b2)
        else:
            send(too, 'ne vizhy kartinki')
    except:
        pass