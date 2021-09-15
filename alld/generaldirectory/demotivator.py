from alld.generaldirectory.priority.mainvkcfg import *
from alld.generaldirectory.priority.pictureoverall import *



def demotivator(mid, too, sms):
    try:
        sms_rezuld = sms.splitlines()
        if len(sms_rezuld) == 2 or len(sms_rezuld) == 1:
            if len(sms_rezuld) == 1:
                sms_rezuld.append('верхний текст')
            sms_rezuld.append('нижний текст')
        picture = vk.messages.getById(message_ids=mid)['items']
        if len(picture[0]['attachments']) == 0:
            if 'reply_message' in picture[0]:
                picture = picture[0]['reply_message']['attachments'][0]['photo']['sizes']
            elif len(picture[0]['fwd_messages']) != 0:
                picture = picture[0]['fwd_messages'][0]['attachments'][0]['photo']['sizes']
        else:
            picture = picture[0]['attachments'][0]['photo']['sizes']
        origf = ''
        for pic in picture:
            if pic['type'] == 'z' or pic['type'] == 'x':
                origf = pic['url']
                break
        hg, imge = image_dem(origf)
        e, rcr, lens = rovn_dem(sms_rezuld[1].upper(), 100)
        e2, rcr2, lens2 = rovn_dem(sms_rezuld[2], 80)
        img1 = vst_dem(hg, imge, background_dem(e + 50 + e2 + 50 + hg + 50 + 80))
        t1 = texting_dem(hg, rcr, img1, lens, 0)
        t2 = texting_dem(hg, rcr2, t1, lens2, e)
        t2 = ssil(hg, t2)
        b2 = bitis(t2)
        send_image_b(too, 'demotion accepted', b2)
    except Exception as ex:
        if str(ex) == 'list index out of range':
            ex = 'dai pikchu'
        send(too, str(ex))


def background_dem(x):
    xy = (1500, x)
    img = Image.new("RGB", xy)

    return img


def rovn_dem(txt, dano):
    wp = txt
    lens = dano
    lines = []
    if len(txt) > 50:
        lens -= 20
    fnt = ImageFont.truetype('content/tmr.ttf', lens)
    if len(txt) > 25:
            wp = ''
            wp3 = ''
            gg = txt.split()
            for l in range(0, len(gg)):
                w, h = d.textsize(gg[l], fnt)
                if w < 1300:
                    w, h = d.textsize(wp + gg[l] + ' ', fnt)
                    if (w > 1300):
                        lines.append(wp[:len(wp)-1])
                        wp = gg[l] + ' '
                    else:
                        wp = wp + gg[l] + ' '
                else:
                    if wp != '':
                        wp = wp + ' '
                        wp3 = wp
                    for c in gg[l]:
                        wp2 = wp + c
                        w, h = d.textsize(wp2, fnt)
                        if w < 1200:
                            wp = wp + c
                        else:
                            if wp == wp3:
                                wp = wp[:len(wp)-1]
                            lines.append(wp)
                            wp = c
                    wp = wp + ' '
            lines.append(wp[:len(wp)-1])
    else:
        gg = txt.split()
        gig = ''
        for ggs in gg:
            gig += ggs + ' '
        lines.append(gig[:len(gig)-1])
    w, h = d.textsize('\n'.join(lines), fnt)
    return h, lines, lens


def image_dem(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    w2, h2 = image.size
    w_r = 1300/w2
    h2 = h2*w_r
    h2 = int(h2)

    return h2, image


def vst_dem(h2, image, base):
    size = (1300, h2)
    image = image.resize(size)
    base.paste(image, (100, 80))
    d = ImageDraw.Draw(base)
    d.rectangle((90, 70, 1410, 90 + h2), outline=ImageColor.getrgb("white"), width=4)
    d.rectangle((950, 90 + h2, 1240, 90 + h2), outline=ImageColor.getrgb("black"), width=4)

    return base


def texting_dem(hg2, spsk, img, lens, logic):
    fnt = ImageFont.truetype('tmr.ttf', lens)
    d = ImageDraw.Draw(img)
    h_dop = 0
    hlast = 0
    pribavka = 10
    if logic != 0:
        hlast = logic + 30
        pribavka = 8
    new_h = hg2 + 80 + 50 + hlast
    for i in range(len(spsk)):
        if spsk[i][len(spsk[i])-1:] == ' ':
            spsk[i] = spsk[i][:len(spsk[i])-1]
        w, h = d.textsize(spsk[i], fnt)
        if i == 0:
            h = 0
        new_h += h + h_dop
        d.text(((1500 - w)/2, new_h), spsk[i], font=fnt)
        h_dop = pribavka

    return img


def ssil(h2, img):
    fnt = ImageFont.truetype('content/jb.ttf', 30)
    d = ImageDraw.Draw(img)
    d.text((968, 78 + h2), 'vk.com/visocke', font=fnt)

    return img