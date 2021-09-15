import emoji
from alld.generaldirectory.priority.mainvkcfg import *
from alld.generaldirectory.priority.pictureoverall import *
from alld.generaldirectory.databasedefs import set_stat


times = {}


def rovn(txt):
    wp = txt
    if len(txt) > 35:
        gg1 = txt.splitlines()
        wp = ''
        for i in range(0, len(gg1)):
            gg = gg1[i].split()
            for l in range(0, len(gg)):
                w, h = d.textsize(gg[l], fnt)
                if w < 520:
                    w, h = d.textsize(wp + gg[l] + ' ', fnt)
                    if (w > 520):
                        wp = wp + '\n' + gg[l] + ' '
                    else:
                        wp = wp + gg[l] + ' '
                else:
                    if wp != '':
                        wp = wp + ' '
                    for c in gg[l]:
                        wp2 = wp + c
                        w, h = d.textsize(wp2, fnt)
                        if w < 520:
                            wp = wp2
                        else:
                            wp = wp + '\n' + c
                    wp = wp + ' '
            if (i != len(gg1) - 1):
                wp = wp + '\n'
    w, h = d.textsize(wp, fnt)
    if 340 - h < 130:
        x = 350 + h
        return x, wp[:len(wp)]
    else:
        x = 540
        return x, wp[:len(wp)]


def checking(user):
    s = times.get(user)
    if s == None:
        times[user] = time.time()
        return True
    else:
        s = times.get(user)
        now = time.time()
        if now - s > 60:
            times[user] = time.time()
            return True
        else:
            return False


def background(oy):
    xy = (960, oy)
    img = Image.new("RGB", xy)
    fnt2 = ImageFont.truetype('content/arial.ttf', 72)
    d = ImageDraw.Draw(img)
    d.text((30, 20), 'Цитаты великих людей:', font=fnt2)

    return img


def id_check(m_id):
    vava = vk.messages.getById(message_ids=m_id)['items']
    if 'reply_message' in vava[0]:
        return vava[0]['reply_message']['from_id']
    elif 'fwd_messages' in vava[0] and 'from_id' in vava[0]['fwd_messages'][0]:
        return vava[0]['fwd_messages'][0]['from_id']
    else:
        return 0


def nickname(id):
    ids = id_check(id)
    if ids > 0:
        gets = vk.users.get(user_ids=str(ids), lang=0)[0]
        return '{} {}'.format(gets['first_name'], gets['last_name'])
    elif ids < 0:
        gets = vk.groups.getById(group_ids=str(ids)[1:], lang=0)[0]
        return gets['name']


def texting(oy, imya, img):
    fnt = ImageFont.truetype('content/arial.ttf', 30)
    imya = '(ɔ) ' + imya
    d = ImageDraw.Draw(img)
    w, h = d.textsize(imya, fnt)
    d.text((930 - w, oy - h - 45), imya, font=fnt)

    return img


def ikonka(base, id):
    ids = id_check(id)
    if ids > 0:
        zhzh = vk.users.get(user_ids=ids, fields='photo_max')[0]
        url = zhzh['photo_max']
    elif ids < 0:
        zhzh = vk.groups.getById(group_ids=str(ids)[1:], fields='photo_200')[0]
        url = zhzh['photo_200']
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    size = (280, 280)
    image = image.resize(size)
    base.paste(image, (20, 110))

    return base


def ikonka_f(base, id_avt):
    try:
        zhzh = vk.users.get(user_ids=id_avt, fields='photo_max')[0]
        url = zhzh['photo_max']
    except:
        zhzh = vk.groups.getById(group_id=id_avt, fields='photo_200')[0]
        url = zhzh['photo_200']
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    size = (280, 280)
    image = image.resize(size)
    base.paste(image, (20, 110))

    return base


def get_text(id):
    text = '"'
    vava = vk.messages.getById(message_ids=id)['items']
    if 'reply_message' in vava[0]:
        text = '"{}"'.format(vava[0]['reply_message']['text'])
    elif 'fwd_messages' in vava[0]:
        if len(vava[0]['fwd_messages']) > 1:
            for element in vava[0]['fwd_messages']:
                if 'text' in element:
                    text = text + '\n' + element['text']
            text = '"' + text[2:] + '"'
        else:
            text = '"{}"'.format(vava[0]['fwd_messages'][0]['text'])
    text = deEmojify(text)
    y, text = rovn(str(text))

    return y, text


def get_id_for_al(id):
    vava = vk.messages.getById(message_ids=id)['items']
    if 'reply_message' in vava[0]:
        return vava[0]['reply_message']['from_id']
    elif 'fwd_messages' in vava[0]:
        if len(vava[0]['fwd_messages']) > 1:
            return vava[0]['fwd_messages'][0]['from_id']
    else:
        return 0


def citate(img, texts):
    fnt = ImageFont.truetype('content/arial.ttf', 30)
    xy = (340, 200)
    d = ImageDraw.Draw(img)
    d.text(xy, texts, font=fnt)

    return img


def deEmojify(inputString):
    ivent = ''.join(c for c in inputString if c not in emoji.UNICODE_EMOJI)
    if ivent == '':
        ivent = 123
    return ivent


def citgen_albom(foto, a_id, c_id, p_id, t):
    if t == 1:
        al_id = 272566983
    else:
        al_id = 272566909
    upload.photo(photos=urlopen(foto), album_id=al_id, caption=str(a_id) + '\n' + str(get_id_for_al(c_id)) + '\n' + str(p_id))


def send_citgen(too, ids, users):
    try:
        if users == admin:
            rez = True
        else:
            rez = checking(users)
        if rez:
            send(too, 'creating citgen...')
            x, txt = get_text(ids)
            fon = background(x)
            fon = texting(x, nickname(ids), fon)
            b = ikonka(fon, ids)
            b = citate(b, txt)
            b2 = bitis(b)
            izo = send_image_b(too, 'citgen accepted', b2)
            url1 = vk.photos.getById(photos=izo, photo_sizes=0)[0]['sizes']
            citgen_albom(url1[4]['url'], users, ids, too, 0)
            set_stat(1)
        else:
            send(too, 'citgen blocked for you' + '\n' + '--' + '\n' + 'you can use one /citgen per minute')
    except Exception as e:
        send(admin, str(e))


def send_false_citgen(too, users, c_avt, c_txt):
    try:
        if users == admin:
            rez = True
        else:
            rez = checking(users)
        if rez:
            send(too, 'creating citgen...')
            c_txt = deEmojify(c_txt)
            x, text = rovn(c_txt)
            fon = background(x)
            fon = texting(x, nickname_f(c_avt), fon)
            b = ikonka_f(fon, c_avt)
            b = citate(b, text)
            b2 = bitis(b)
            izo = send_image_b(too, 'citgen accepted', b2)
            url1 = vk.photos.getById(photos=izo, photo_sizes=0)[0]['sizes']
            citgen_albom(url1[4]['url'], users, c_avt, too, 1)
            set_stat(1)
        else:
            ban = 'citgen blocked for you' + '\n' + '--' + '\n' + 'you can use one /citgen per minute'
            send(too, ban)
    except:
        send(admin, 'error')

