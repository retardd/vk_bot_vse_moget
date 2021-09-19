# -*- coding: utf-8 -*-
from alld.generaldirectory.priority.mainvkcfg import *
from alld.generaldirectory.priority.pictureoverall import *


# не активно
def transliteration(text):
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ja'.split('|')
    trantab = {k:v for k,v in zip(cyrillic,latin)}
    newtext = ''
    for ch in text:
        casefunc =  str.capitalize if ch.isupper() else str.lower
        newtext += casefunc(trantab.get(ch.lower(),ch))
    return newtext


def umoreska(too):
    wol = vk.wall.get(owner_id=-92876084, offset=random.randint(0, 25000))
    vk.messages.send(
        peer_id=too,
        attachment="wall-92876084_" + str(wol['items'][0]['id']),
        random_id=get_random_id(),
        message=random.choice(['vash anek, ser', 'смейся сука', 'priyatnogo appetita', 'ВАШ АНЕКДОТ ДОСТАВЛЕН. ПОДТВЕРДИТЕ ПОЛУЧЕНИЕ ПОСЫЛКИ АХАХАХ-ОМ'])
    )


def anime_moment(mid, too, msgs):
    try:
        kvk = vk.messages.getById(message_ids=mid)
        origf = kvk['items'][0]['attachments'][0]['photo']['sizes']
        for origfs in origf:
            if origfs['type'] == 'z':
                origf = origfs['url']
                break
        tracemoe = TraceMoe()
        responses = tracemoe.search(origf, True, 1)
        video = tracemoe.getVideo(responses, mute=0)
        tracemoe.writeFile("content/file.mp4", video)
        yrl = upload.video(video_file='content/file.mp4', name='file.mp4', is_private=1)
        yrl['access_key'] = yrl.pop('video_hash')
        send_v(too, yrl, msgs)
    except Exception as ex:
        send(too, str(ex))


# не активно
def captcha_handler(captcha):
    key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)


def spaming(msgss):
    try:
        peers = vk.messages.getConversations(count=100, filter='all', extended=0)
        peers_t = []
        for itemz in peers['items']:
            if itemz['conversation']['peer']['type'] == 'chat' and itemz['conversation']['can_write']['allowed'] == True:
                peers_t.append(itemz['conversation']['peer']['id'])
        for id in peers_t:
            send(id, msgss)
            time.sleep(2)
        send(admin, str(len(peers_t)) + 'chats giving spam')
    except vk_api.exceptions.Captcha:
        send(admin, 'capcha')
    except Exception as err:
        send(admin, str(err))


def id_for_f(ident):
    list_ident = ident.split('/')

    return list_ident[len(list_ident) - 1]


def idd(msgs):
    vava = vk.messages.getById(message_ids=msgs)['items']
    if 'reply_message' in vava[0]:
        return vava[0]['reply_message']['id']
    else:
        return msgs


def wsearch(item):
    try:
        res = 'Вот что я нашёл: \n' + wikipedia.summary(item)
    except:
        res = 'тут какая-то ашыпка, гугли конкретнее, мудак'
    return res


def stopping(n, kuda, msgs2):
    time.sleep(n)
    send(kuda, msgs2)


def mem_paste(m_ids, too):
    bc = Image.open('content/mem1.jpg')
    kvk = vk.messages.getById(message_ids=m_ids)
    len_ = len(kvk['items'][0]['attachments'][0]['photo']['sizes'])
    orig = kvk['items'][0]['attachments'][0]['photo']['sizes'][len_ - 1]['url']
    response = requests.get(orig)
    image = Image.open(BytesIO(response.content))
    image = image.resize((350, 202))
    bc.paste(image, (891, 225))
    bc = bitis(bc)
    send_image_b(too, 'vash mem, ser', bc)
    bc.close()


def softmax(x):
    proba = np.exp(-x)
    return proba / sum(proba)


class NeighborSampler(BaseEstimator):
    def __init__(self, k=5, temperature=1.0):
        self.k = k
        self.temperature = temperature

    def fit(self, X, y):
        self.tree_ = BallTree(X)
        self.y_ = np.array(y)

    def predict(self, X, random_state=None):
        distances, indices = self.tree_.query(X, return_distance=True, k=self.k)
        result = []
        for distance, index in zip(distances, indices):
            result.append(np.random.choice(index, p=softmax(distance * self.temperature)))
        return self.y_[result]
