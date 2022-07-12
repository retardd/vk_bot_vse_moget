# -*- coding: utf-8 -*-
import queue
from alld.generaldirectory.dvach import board
from alld.generaldirectory.other import *
from alld.generaldirectory.flib import flibusta
from alld.generaldirectory.citgen import *
from alld.generaldirectory.demotivator import *
from alld.generaldirectory.databasedefs import *
from alld.generaldirectory.telegramcfg import *



def main():

    retw = True

    wikipedia.set_lang("RU")


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
            elif sms[:7] == '/citgen' or sms[:3] == '/cg':
                c_info = event.text.split(' ', 2)
                c_info_a = id_for_f(c_info[1])
                c_text = '"' + c_info[2] + '"'
                cit_f = event.user_id
                t = Thread(target=send_false_citgen, args=(to, cit_f, c_info_a, c_text))
                t.start()
            elif sms[:3] in ['/ff', '/fe', '/fm', '/fb', '/fs', '/fp', '/fn', '/fd', '/md', '/ed']:
                t_flib = Thread(target=flibusta, args=(event.user_id, sms, to))
                t_flib.start()
            elif sms[:4] == '/jtc':
                try:
                    chat = event.text[5:]
                    vk.messages.joinChatByInviteLink(link=str(chat))
                except:
                    send(to, 'invalid link')
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
            elif (sms[:2] == '//' or sms[:2] == 'b/' or sms[:2] == 'б/') and event.peer_id == event.user_id:
                t_board = Thread(target=bord.send_to_board, args=(event.text[2:], to, event.message_id))
                t_board.start()
            elif sms == 'pancu':
                t4 = Thread(target=mem_paste, args=[event.message_id, to])
                t4.start()
            elif sms[:12] == '/demotivator' or sms[:3] == '/dm' or sms[:9] == '/demotion':
                t_dem = Thread(target=demotivator, args=(event.message_id, to, event.text))
                t_dem.start()
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
