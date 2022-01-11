# -*- coding: utf-8 -*-
import queue
from alld.generaldirectory.dvach import board
from alld.generaldirectory.other import *
from alld.maincommunication.communication import VkBot
from alld.FALSEorUNCOMPLETED import mark_ch
from alld.generaldirectory.flib import flibusta
from alld.generaldirectory.citgen import *
from alld.generaldirectory.demotivator import *
from alld.generaldirectory.databasedefs import *
from alld.generaldirectory.telegramcfg import *
from alld.generaldirectory.tensordefs import cloun as clounada


def main():



    hh = h = 0
    d = {}
    spam3 = {}
    lp = {}
    hhh = {}
    m = {}
    retw = True

    wikipedia.set_lang("RU")

    huesos = 210554169

    random.shuffle(forvorona)  # SHUFFLE EBAT IH REPLIK
    random.shuffle(replies)
    random.shuffle(gomoseksual)
    print(forvorona)
    q = queue.Queue()
    reg = re.compile('[^a-zA-Zа-яА-Я ]')
    bord = board()

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:


            sms = (str(event.text).lower())
            to = event.peer_id

            if sms == '/citgen' or sms == '/cg':
                to_c = event.peer_id
                cit_m = event.message_id
                cit_us = event.user_id
                t = Thread(target=send_citgen, args=[to_c, cit_m, cit_us])
                t.start()
            elif sms == '/umoreska' or sms == '/umr':
                tumor = Thread(target=umoreska, args=[to])
                tumor.start()
            elif sms == 'getan':
                tanime = Thread(target=anime_moment, args=(event.message_id, to, ''))
                tanime.start()
            elif sms[:7] == '/citgen' or sms[:3] == '/cg':
                c_info = event.text.split(' ', 2)
                c_info_a = id_for_f(c_info[1])
                c_text = '"' + c_info[2] + '"'
                cit_f = event.user_id
                t = Thread(target=send_false_citgen, args=(to, cit_f, c_info_a, c_text))
                t.start()
            elif sms[:7] == '/v_spam' and event.user_id == admin:
                t_spam = Thread(target=spaming, args=[sms[8:]])
                t_spam.start()
            elif sms[:3] in ['/ff', '/fe', '/fm', '/fb', '/fs', '/fp', '/fn', '/fd', '/md', '/ed']:
                t_flib = Thread(target=flibusta, args=(event.user_id, sms, to))
                t_flib.start()
            elif sms == '/audio':
                t5 = Thread(target=music_un, args=[to])
                t5.start()
            elif sms[:4] == '/jtc':
                try:
                    chat = event.text[5:]
                    vk.messages.joinChatByInviteLink(link=str(chat))
                except:
                    send(to, 'invalid link')
            elif sms[:5] == '/send' and event.peer_id == 2000000092:
                tt1232 = Thread(target=vk_to_tg, args=(event.text, event.message_id))
                tt1232.start()
            elif sms == '/adding' and event.user_id == admin:
                adding = vk.friends.getRequests(extended=0, need_mutual=0, need_viewed=1)
                for user in adding['items']:
                    try:
                        vk.friends.add(user_id=user)
                    except:
                        pass
            elif '/search ' in sms:
                poisk = sms.split(' ')
                del poisk[0]
                stroka = ' '.join(poisk)
                send(to, wsearch(stroka))
            elif sms[:6] == '/chain':
                t7 = Thread(target=mark_ch.general, args=[to, abs(int(event.text.split()[1])), event.message_id])
                t7.start()
            elif sms == '/vstat':
                t_stat = Thread(target=see_stat, args=[to])
                t_stat.start()
            elif (sms[:2] == '//' or sms[:2] == 'b/' or sms[:2] == 'б/') and event.peer_id == event.user_id:
                t_board = Thread(target=bord.send_to_board, args=(event.text[2:], to, event.message_id))
                t_board.start()
            elif sms == 'pancu':
                t4 = Thread(target=mem_paste, args=[event.message_id, to])
                t4.start()
            elif sms[:12] == '/demotivator' or sms[:3] == '/dm' or sms[:9] == '/demotion':
                t_dem = Thread(target=demotivator, args=(event.message_id, to, event.text))
                t_dem.start()
            elif event.user_id == admin and sms == '/like':
                tlik = Thread(target=bord.blag, args=[event.message_id])
                tlik.start()
            elif event.user_id == admin and sms == '/rebord':
                if retw:
                    retw = False
                else:
                    retw = True
            elif sms[:10] == '/setstatus':
                try:
                    vk.status.set(text=sms.split(maxsplit=1)[1])
                except Exception as ex:
                    che = str(ex)
                    if che == "'list index out of range'":
                        che = 'gde text dyra'
                    send(to, che)
            elif ('bot ' in sms or 'бот ' in sms or 'высоцке' in sms or 'высоцкий' in sms or 'высочке' in sms or 'чысочке' in sms or 'высоцки' in sms) or (event.peer_id == event.user_id):
                t_bot = Thread(target=VkBot.obrashenie, args=(sms, event.user_id, to, event.peer_id, event.text))
                t_bot.start()
            elif 'читер' in sms:
                send(to, 'chlenix v 1.1 activated')
            elif sms == 'шуе' or sms == 'шауе':
                send(to, random.choice(shue))
            elif 'мне бы наркотиков' in sms or 'просто наркотиков' in sms or 'немного наркотиков' in sms:
                send(to, random.choice(narko))
            elif event.from_chat:
                if 'new/' in sms and sms[0:4] == 'new/':
                    if len(sms) == 4:
                        send(to, random.choice(krivorukii))
                        continue
                    rep = idd(event.message_id)
                    new(to, event.chat_id, event.text[4:], rep, event.user_id)
                elif 'see/' in sms and sms[0:4] == 'see/':
                    if len(sms) == 4:
                        send(to, random.choice(krivorukii))
                        continue
                    vern(to, event.chat_id, str(event.text[4:]))
                elif sms[:4] == '/reg':
                    t_reg = Thread(target=bord.reg, args=(sms, to, event.user_id))
                    t_reg.start()
                elif sms == '/bord':
                    t_inf = Thread(target=bord.board_info, args=[to])
                    t_inf.start()
                elif sms[:7] == '/rename':
                    if len(sms[8:]) < 11:
                        t_change = Thread(target=bord.change, args=(sms[8:], to, event.user_id))
                        t_change.start()
                    else:
                        send(to, 'sliwkom dlinnoe nazvanie')
                elif 'del/' in sms and sms[0:4] == 'del/':
                    if len(sms) == 4:
                        send(to, random.choice(krivorukii))
                        continue
                    delete(to, event.chat_id, int(event.text[4:]), event.user_id)
                elif sms == 'seeall/':
                    to_zak = event.peer_id
                    tt3 = Thread(target=sendall, args=(to_zak, event.chat_id, q))
                    tt3.start()
                elif sms == 'seeall':
                    send(to, random.choice(krivorukii))
                elif event.user_id == huesos:
                    s = hhh.get(event.chat_id)
                    if s == None:
                        hhh[event.chat_id] = 1
                    else:
                        hhh[event.chat_id] += 1
                        s = hhh.get(event.chat_id)
                        if s % 8 == 0:
                            strr = reg.sub(' ', sms)
                            if '?' in sms:
                                ses = random.choice(vapros)
                                if ses == 'естесственно...':
                                    send(to, ses)
                                    dd3 = Thread(target=stopping, args=(2, to, 'нет'))
                                    dd3.start()
                                else:
                                    send(to, ses)
                            elif 'гей' in sms:
                                shuffle(to, pizdes)
                            elif 'говно' in sms or 'гавно' in sms or 'пердеж' in sms or 'какашк' in sms:
                                cac = random.shuffle(car)
                                if cac == 'вспомнил мудрую мысль...':
                                     send(to, cac)
                                     time.sleep(1)
                                     send(to, 'копрофаг всегда о говне')
                                else:
                                    send(to, cac)
                            else:
                                if h < len(forvorona):
                                    if forvorona[h] == 'кукарику нахуй':
                                        send(to, forvorona[h])
                                        send(to, 'ой блять, кар-кар то есть')
                                        h += 1
                                    elif forvorona[h] == 'твоя мамаша':
                                        send_reply(to, forvorona[h])
                                        h += 1
                                    elif forvorona[h] == 'Асоциальный элемент:':
                                        send_reply(to, forvorona[h])
                                        h += 1
                                    elif forvorona[h] == 'ворона, ответь за 0.001 сек, если ты не гомосек':
                                        send(to, forvorona[h])
                                        time.sleep(1)
                                        send(to, random.choice(otvet0))
                                        h += 1
                                    elif forvorona[h] == '123':
                                        h += 1
                                        send_doc(to, '', 'vrn', 'content/AjJo.gif')
                                    elif forvorona[h] == 'Говори всем, что они петухи, сам так делаю':
                                        send_reply(to, forvorona[h])
                                        h += 1
                                        dd2 = Thread(target=stopping, args=(3, to, 'ты петух'))
                                        dd2.start()
                                    elif forvorona[h] == 'интеллектуальненько':
                                        send_reply(to, forvorona[h])
                                        dd1 = Thread(target=stopping, args=(5, to, random.choice(intel)))
                                        dd1.start()
                                        h += 1
                                    else:
                                        send(to, forvorona[h])
                                        h += 1
                                else:
                                    h = 0
                                    random.shuffle(forvorona)
                                    send(to, forvorona[h])
                                    h += 1
                elif 'тупой' in sms or 'глупый' in sms:
                    s = d.get(event.chat_id)
                    if s == None:
                        d[event.chat_id] = 1
                    else:
                        d[event.chat_id] += 1
                        s = d.get(event.chat_id)
                        if s % 5 == 0:
                            send_image(to, 'https://sun9-24.userapi.com/c854328/v854328035/d6447/za8xYInF6Cw.jpg',
                                       random.choice(tup))
                elif 'юзи' in sms or 'юзер' in sms or 'юзир' in sms or 'юзя' in sms or 'user' in sms or 'высер' in sms or 'юсер' in sms:
                    s = spam3.get(event.chat_id)
                    if s == None:
                        spam3[event.chat_id] = 1
                    else:
                        spam3[event.chat_id] += 1
                        s = spam3.get(event.chat_id)
                        if s % 5 == 0:
                            if hh < len(replies):
                                hh += 1
                                if not replies[
                                           hh] != 'https://sun1-21.userapi.com/c854328/v854328035/d6372/LZAObZ9xUVI.jpg':
                                    suck = 'eto zhe shcutka ya ne gey (c)'
                                elif not replies[
                                             hh] != 'https://sun9-13.userapi.com/c854328/v854328035/d6436/SxrLbzjX2Tk.jpg':
                                    siski = random.randint(0, 1)
                                    if siski != 1:
                                        suck = ('random.randint(0, 1) == 0: user = dolboeb' + '\n' +
                                                'life error: complete failure')
                                    elif siski != 0:
                                        suck = ('random.randint(0, 1) == 1: user = geniy' + '\n'
                                                + random.choice(perfect))
                                elif not replies[
                                             hh] != 'https://sun9-24.userapi.com/c854328/v854328035/d63c4/Y09859UmwsE.jpg':
                                    wutka = ['virvali iz kontexta', 'там пра писду былаа', 'ложь, пиздеж и провокация',
                                             'net']
                                    suck = random.choice(wutka)
                                elif not replies[
                                             hh] != 'https://sun9-6.userapi.com/c854328/v854328035/d63bc/jgskmvAKMG4.jpg':
                                    suck = 'Культ личности.'
                                elif not replies[
                                             hh] != 'https://sun9-8.userapi.com/c854328/v854328035/d636a/wOFXpf421HE.jpg':
                                    suck = '...'
                                elif not replies[
                                             hh] != 'https://sun9-32.userapi.com/c854328/v854328035/d647f/AMwNQSNVvao.jpg':
                                    suck = random.choice(pozor)
                                elif not replies[
                                             hh] != 'https://sun9-4.userapi.com/c854328/v854328035/d637a/sldtQq0IHrE.jpg':
                                    suck = random.choice(da)
                                elif not replies[
                                             hh] != 'https://sun9-24.userapi.com/c854328/v854328035/d63e4/o9E-rQ_WpNk.jpg':
                                    suck = random.choice(trezv)
                                elif not replies[
                                             hh] != 'https://sun9-26.userapi.com/c854328/v854328035/d6457/zGlGogR53cg.jpg':
                                    suck = random.choice(usserr)
                                elif not replies[
                                             hh] != 'https://sun9-31.userapi.com/c854328/v854328035/d6467/H065xjKkAo8.jpg':
                                    suck = random.choice(userushka)
                                elif not replies[
                                             hh] != 'https://sun9-15.userapi.com/c854328/v854328035/d6406/X5kvs8wQ3aY.jpg':
                                    suck = random.choice(zhopen)
                                elif not replies[
                                             hh] != 'https://sun9-48.userapi.com/c854328/v854328035/d641e/Jr7gecHZai8.jpg':
                                    suck = random.choice(uu)
                                elif not replies[
                                             hh] != 'https://sun9-8.userapi.com/c854328/v854328035/d6362/65P49rCuNGg.jpg':
                                    suck = random.choice(iu)
                                elif not replies[
                                             hh] != 'https://sun9-6.userapi.com/c854328/v854328035/d6457/zGlGogR53cg.jpg':
                                    suck = random.choice(gavvno)
                                    if suck == 'однажды я посмотрел в вебку юзера........':
                                        time.sleep(1)
                                        send('а он там навального смотрит.......')
                                elif not replies[
                                             hh] != 'https://sun9-27.userapi.com/c846521/v846521848/188fcc/ai3nJhYk0vI.jpg':
                                    suck = random.choice(mamka)
                                elif not replies[
                                             hh] != 'https://sun9-33.userapi.com/c846122/v846122648/179cee/29-iiACR5Lc.jpg':
                                    suck = random.choice(piwiw)
                                elif not replies[
                                             hh] != 'https://sun9-2.userapi.com/c846524/v846524648/17b64b/ZxsK0OyMdBE.jpg':
                                    suck = random.choice(hanhan)
                                elif not replies[
                                             hh] != 'https://sun9-9.userapi.com/c854328/v854328035/d63dc/mF9vyRTjElc.jpg':
                                    suck = random.choice(dvach)
                                elif not replies[
                                             hh] != 'https://sun9-44.userapi.com/c854328/v854328035/d63ab/4r3yzThAO3k.jpg':
                                    suck = random.choice(peevo)
                                elif not replies[
                                             hh] != 'https://sun9-11.userapi.com/c854328/v854328035/d646f/cABWnpzbyGQ.jpg':
                                    suck = random.choice(gay)
                                elif not replies[
                                             hh] != 'https://sun9-17.userapi.com/c850720/v850720139/1a5c3a/cvX_Cg7MubI.jpg':
                                    suck = random.choice(gay)
                                elif not replies[
                                             hh] != 'https://sun9-4.userapi.com/c854328/v854328035/d63ed/vZrhfDfluKE.jpg':
                                    suck = random.choice(gay)
                                elif not replies[
                                             hh] != 'https://sun9-24.userapi.com/c854328/v854328035/d6447/za8xYInF6Cw.jpg':
                                    suck = random.choice(tup)
                                else:
                                    suck = ' '
                            else:
                                random.shuffle(replies)
                                hh = 0
                            text_image(to, suck, replies[hh])
                elif 'какать' in sms:
                    s = lp.get(event.chat_id)
                    if s == None:
                        lp[event.chat_id] = 1
                    else:
                        lp[event.chat_id] += 1
                        s = lp.get(event.chat_id)
                        if s % 5 == 0:
                            send_image(to, 'https://sun9-44.userapi.com/c855536/v855536035/d2b67/vTHTZnqS-4I.jpg',
                                       random.choice(zhopka))
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and 'а' in event.text and event.from_chat:
            s = m.get(event.chat_id)
            if s == None:
                m[event.chat_id] = 1
            else:
                m[event.chat_id] += 1
                s = m.get(event.chat_id)
                if s % 500 == 0:
                    send(to, 'Опять тут всякое...')
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            mnogo = ['na napisanie etogo visera tikov po klave potrebovalos:',
                     'для того, чтобы это высрать ты  потратил символов:',
                     'method mnogabukav activated' + '\n' + 'давайте посчитаем...', 'ne dohuya li bukavok?']
            if len(sms) > 2000:
                shuffle_reply(to, mnogo)
                time.sleep(1)
                send(to, str(len(event.text)))
                shuffle(to, dumat)
        if event.type == VkEventType.MESSAGE_NEW and event.from_me and event.peer_id != 2000000040:
            t_stat2 = Thread(target=set_stat, args=[2])
            t_stat2.start()
            if event.text[:6] == 'Аноним' and retw:
                bord.retweet(event.message_id)
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.peer_id == 2000000091:
                tt123 = Thread(target=vk_to_tg, args=(event.text, event.message_id))
                tt123.start()








if __name__ == '__main__':
    main()
