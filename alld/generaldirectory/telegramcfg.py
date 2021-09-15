import telebot
from alld.generaldirectory.priority.overall import *
from alld.generaldirectory.priority.mainvkcfg import *
import os

bot = telebot.TeleBot("1971532251:AAF8hFaLjYmF4MiPC7k94yS7woezTS8sDA8")

def get_from_vk(id, sms):
    docs = vk.messages.getById(message_ids=id)
    pic = []
    logic = True
    doc = []
    text = sms
    if len(docs['items'][0]['attachments']) > 0:
        for docс in docs['items'][0]['attachments']:
            if docс['type'] == 'photo':
                for photoType in docс[docс['type']]['sizes']:
                    if photoType.get('type') == 'x':  # <=604x604
                        pic.append(photoType.get('url'))
                        logic = False
                    if photoType.get('type') == 'y':  # >605x605
                        if logic:
                            pic.append(photoType.get('url'))
                            logic = False
                        else:
                            pic[len(pic)-1] = photoType.get('url')
                    if photoType.get('type') == 'z':  # <=1280x720
                        if logic:
                            pic.append(photoType.get('url'))
                            logic = False
                        else:
                            pic[len(pic) - 1] = photoType.get('url')
                    if photoType.get('type') == 'w':  # >1280x720
                        if logic:
                            pic.append(photoType.get('url'))
                            logic = False
                        else:
                            pic[len(pic) - 1] = photoType.get('url')  # <=2560x1440
            elif docс['type'] == 'doc':
                doc.append([docс[docс['type']]['url'], docс[docс['type']]['title']])
    if len(docs['items'][0]['fwd_messages']) >0:
        for fwd in docs['items'][0]['fwd_messages']:
            text += '\n' + '\n' + fwd['text']
            if len(fwd['attachments']) > 0:
                for docс in fwd['attachments']:
                    if docс['type'] == 'photo':
                        for photoType in docс[docс['type']]['sizes']:
                            if photoType.get('type') == 'x':  # <=604x604
                                if logic:
                                    pic.append(photoType.get('url'))
                                    logic = False
                                else:
                                    pic[len(pic) - 1] = photoType.get('url')
                            if photoType.get('type') == 'y':  # >605x605
                                if logic:
                                    pic.append(photoType.get('url'))
                                    logic = False
                                else:
                                    pic[len(pic) - 1] = photoType.get('url')
                            if photoType.get('type') == 'z':  # <=1280x720
                                if logic:
                                    pic.append(photoType.get('url'))
                                    logic = False
                                else:
                                    pic[len(pic) - 1] = photoType.get('url')
                            if photoType.get('type') == 'w':  # >1280x720
                                if logic:
                                    pic.append(photoType.get('url'))
                                else:
                                    pic[len(pic) - 1] = photoType.get('url')  # <=2560x1440
                    elif docс['type'] == 'doc':
                        doc.append([docс[docс['type']]['url'], docс[docс['type']]['title']])
    return text, pic, doc



def transferMessagesToTelegram(txt, pics, docs):
    if len(pics) == 0 and len(docs) == 0:
        bot.send_message(chat_id=-523101023, text=txt)
    if len(pics) !=0:
        if len(txt) < 1000:
            for pic in pics:
                bot.send_photo(chat_id=-523101023, photo=pic, caption=txt)
                txt = ''
        else:
            bot.send_message(chat_id=-523101023, text=txt)
            for pic in pics:
                bot.send_photo(chat_id=-523101023, photo=pic)
    if len(docs) !=0:
        if len(txt) < 1000:
            for doc in docs:
                r = requests.get(doc[0])
                with open("content/" + doc[1], "wb") as code:
                    code.write(r.content)
                bot.send_document(chat_id=-523101023, data=open("content/" + doc[1], 'rb'), caption=txt)
                os.remove("content/" + doc[1])
                txt = ''
        else:
            bot.send_message(chat_id="@usermeow", text=txt)
            for doc in docs:
                r = requests.get(doc[0])
                with open("content/" + doc[1], "wb") as code:
                    code.write(r.content)
                bot.send_document(chat_id=-523101023, data=open("content/" + doc[1], 'rb'))
                os.remove("content/" + doc[1])

@bot.message_handler(content_types=['text'])
def start_message(message):
    bot.send_message(373717705, str(message.chat.id))

def vk_to_tg(sms, id):
    try:
        text, pic, doc = get_from_vk(id, sms)
        transferMessagesToTelegram(text, pic, doc)
    except:
        send(admin, 'owibkaaaa')