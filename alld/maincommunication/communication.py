from alld.generaldirectory.other import *
from alld.maincommunication.mainreps import *
import re
from alld.FALSEorUNCOMPLETED.chains import markov_chain
import time
from alld.maincommunication import smsl

mc = markov_chain.MarkovChain()

reg = re.compile('[^a-zA-Zа-яА-Я ]')

huesos = 210554169
admin = 391653357
now2 = time.time()
prowliy = {'0': 0}


def strsearch(string, substr):
    srch = []
    srch = [str for str in string if any(sub in str for sub in substr)]
    if len(srch) != 0:
        return True
        srch = []
    else:
        return False

class VkBot():

    def proverka(prowliy, new, id):
        s = prowliy.get(id)
        now1 = time.time()
        if s != None:
            if prowliy[id][0] == new and prowliy[id][1] - now1 < 120:
                return False
            else:
                prowliy[id][0] = new
                prowliy[id][1] = now1
                return True
        else:
            prowliy[id] = []
            prowliy[id].append(new)
            prowliy[id].append(now1)
            return True
        if now1 - now2 > 1500:
            now2 = time.time()
            prowliy = {}


    def for_small(sms, to, user_id, slv):
        rtrn = False
        if sms in vsck2:
            vsss = nickname_f(user_id).split()
            send(to, vsss[0].lower())
            if user_id == huesos:
                send(to, random.choice(voronchik))
        elif len(slv) > 0:
            if 'прив' in sms or 'здарова' in sms or 'хай' in sms or 'даров' in sms or 'салам' in sms or 'шалом' in sms:
                shuffle(to, priv)
            elif 'пока' in slv or 'прощай' in slv or 'досвидос' in slv or 'пака' in slv or 'бывай' in sms:
                shuffle(to, pok)
            elif len(slv) > 1:
                if slv[0] + ' ' + slv[1] in go_sex:
                    if user_id == huesos:
                        shuffle(to, kaki)
                    else:
                        shuffle(to, gogo)
                elif slv[0] + ' ' + slv[1] == 'ты че':
                    send(to, random.choice(ti_che))
                elif slv[0] == 'ты':
                    if slv[1] in obz:
                        send(to, random.choice(priz2))
                    elif slv[1] in pohvala:
                        send(to, random.choice(spasiba))
                    else:
                        rtrn = True
                else:
                    rtrn = True
            else:
                rtrn = True
        else:
            rtrn = True
        return rtrn


    def konflict(sms, user_id, to, text, slv):
        if strsearch(slv, ['лох', 'лах', 'лошара']) == True:
            if user_id == huesos:
                shuffle(to, sam)
            else:
                shuffle(to, loxx)
        elif any(el in sms for el in smsl.pnh12):
            if user_id == huesos:
                shuffle(to, sosi)
            else:
                shuffle(to, otsosi)
        elif strsearch(slv, ['ебанутый', 'ебнутый', 'пизданутый', 'припизднутый']):
            if user_id == huesos:
                shuffle(to, eban)
            else:
                shuffle(to, eban2)
        elif strsearch(slv, ['гнида', 'дебил', 'дура', 'хуйло', 'хуила', 'пидор', 'пидар', 'пидарас']):
            send(to, random.choice(durak))
        elif any(el in sms for el in smsl.pnh):
            send(to, random.choice(nahyi))
        elif strsearch(slv, ['мудак', 'мудофил', 'гандон', 'хуйло', 'хуила', 'мудил']):
            send(to, random.choice(['ne pizdi', 'завали ебало, ' + nickname_f(user_id).split()[0].lower(), 'ti che takoi obizhenny', '(',
                      'davai ti ne budew takoe pisat',
                      'ti ranil moe serdce...', 'malenkiy huesosik']))
        elif strsearch(slv, ['твоя мать', 'твоя мамка', 'твою мать', 'твою мамку', 'твоя мама']):
            send(to, random.choice(pro_mamy))
        elif strsearch(slv, ['заткнись', 'завали ебало', 'завались']):
            send(to, random.choice(zatknis))
        elif strsearch(slv, ['букашк', 'смерд', 'холоп', 'раб', 'больной']):
            send(to, bukawka)
        elif len(slv) > 1 and slv[0] + ' ' + slv[1] == 'скажи хуй':
            send(to, 'ты хуй')
        elif slv[0] == 'помощь':
            send(to, random.choice(pomow))
        elif 'я не гей' in sms or 'я натурал' in sms or 'не вру' in sms or 'не пизжу' in sms:
            shuffle(to, pizdezh)
        elif 'я гей' in sms or 'я по мальчикам' in sms:
            shuffle(to, mi_znali)
        elif 'шутки про маму' in sms or 'шутки про мамку' in sms or 'мамкоеб' in sms:
            send(to, random.choice(mamachka))
        elif 'нельзя' in sms:
            send(to, random.choice(mamachka))
        else:
            return True


    def neitral(to, sms, user_id, slv):
        if ' ору' in sms or 'ржу' in sms or 'кричу' in sms or ' ор' in sms or 'оруу' in sms:
            ori = (['ne ori pzh', 'AAAAAAAAAAAAA', nickname_f(user_id) + ' лох', 'хаха як смишно',
                    'hrukni ewe, cvinota nahyi', 'chywka', 'ты быдло', 'подавись хрюн',
                    'ты какой-то устаревший',
                    'съеби старина',
                    'да смейся, хули, мы не в библиотеке, а мамку твою уже никто не разбудит)0))'])
            send(to, random.choice(ori))
        elif any(el in sms for el in smsl.lol):
            send(to, random.choice(lul))
        elif any(el in sms for el in ['найди', 'вики', 'википедия', 'загугли']):
            send(to, 'чтобы что-то отгуглить, ленивая ты жопа, пиши /search *to chto iskat*')
        elif any(el in sms for el in ['варона', 'ворона', 'врона', 'ворон', 'варон']):
            send(to, random.choice(nenavist) + '\n' + random.choice(veebor))
            time.sleep(1)
            send(to, random.choice(gomoseksual))
        elif 'это правда' in sms:
            send(to, random.choice(danet))
        elif 'тролль' in sms or 'троль' in sms or 'траль' in sms or 'тралль' in sms:
            if user_id == admin:
                shuffle(to, okok)
            elif user_id == huesos:
                shuffle(to, okokokok)
            else:
                shuffle(to, okokok)
        elif len(slv) == 1 and ('дед' in slv or 'деды' in slv):
            send(to, random.choice(dedi))
        elif 'знаешь' in slv:
            send(to, random.choice(ne_znau))
        elif 'кто' in slv or 'кто?' in slv:
            send(to, random.choice(nikto))
        else:
            return True


    def obrashenie(sms, user_id, to, peer_id, text):
        if VkBot.proverka(prowliy, sms, user_id) == True:
            strr = reg.sub(' ', sms)
            slv = strr.split()
            if ('bot ' in sms or 'бот ' in sms or 'высоцке' in sms or 'высоцкий' in sms or 'высочке' in sms or 'чысочке' in sms or 'высоцки' in sms):
                del slv[0]
            if VkBot.for_small(sms, to, user_id, slv):
                if VkBot.konflict(sms, user_id, to, text, slv):
                    if VkBot.neitral(to, sms, user_id, slv):
                        if (len(slv) > 0) and (slv[0] == 'скажи' or slv[0] == 'напиши'):
                            if peer_id != user_id:
                                hi2 = 0
                                for i in range(len(obz)):
                                    tip = 'скажи я ' + obz[i]
                                    if tip in sms:
                                        priz = ['da', 'ti pidor', 'да все итак знают',
                                                'скажу больше, ты пидорас ебаный',
                                                'ты серьезно хотел меня этим затролить?', 'aga', 'pnh ' + obz[i],
                                                'sam ti ' + obz[i], 'ebat` ti osel bratuxa',
                                                'ti zabavnii, chelovek, poetomy ya prowau tebja',
                                                'ты внатуре такой еблан?',
                                                'bolnoj wizik idi v palaty']
                                        send(to, random.choice(priz))
                                        hi2 = 1
                                if hi2 == 0:
                                    ss = ''
                                    words = [i for i in re.split(r'\W+', text) if i]
                                    words[0] = words[1] = ''
                                    for word in words:
                                        ss = ss + ' ' + word
                                    send(to, ss)
                            elif peer_id == user_id:
                                hi2 = 0
                                for i in range(len(obz)):
                                    tip = 'скажи я ' + obz[i]
                                    if tip in sms:
                                        priz = ['da', 'ti pidor', 'да все итак знают',
                                                'скажу больше, ты пидорас ебаный',
                                                'ты серьезно хотел меня этим затролить?', 'aga', 'pnh ' + obz[i],
                                                'sam ti ' + obz[i], 'ebat` ti osel bratuxa',
                                                'ti zabavnii, chelovek, poetomy ya prowau tebja',
                                                'ты внатуре такой еблан?',
                                                'bolnoj wizik idi v palaty']
                                        send(to, random.choice(priz))
                                        hi2 = 1
                                if hi2 == 0:
                                    ss = ''
                                    words = [i for i in re.split(r'\W+', text) if i]
                                    words[0] = ''
                                    for word in words:
                                        ss = ss + ' ' + word
                                    send(to, ss)
                        elif 'прекрасный' in slv or 'прекрасен' in slv or 'красава' in slv or 'красив' in slv:
                            shuffle(to, kross)
                        elif 'пизда' in sms or 'пиздец' in sms or 'пиздит' in sms:
                            sam0 = ['кто прочитал у того сдохнет бабка вороны', 'zavali svoe ebalo',
                                    'где ваши манеры, бомжара?',
                                    'derji bumajku' + ' &#127987;&#65039;&#8205;&#127752; &#127987;&#65039;&#8205;&#127752; ' + 'vitres',
                                    'ну вы и пидарас', 'поаккуратнее с языком, молодой человек',
                                    nickname_f(user_id) + ', сдохни мразь чмо']
                            shuffle(to, sam0)
                        elif 'лгбт' in sms:
                            shuffle(to, lggg)
                        elif 'чмо' in sms or 'чмоня' in sms or 'чмырь' in sms:
                            if user_id == huesos:
                                send(to, random.choice(sam2))
                            else:
                                send(to, random.choice(loxx2))
                        elif 'можешь' in slv:
                            shuffle(to, mogu)
                        elif 'цитата' in sms or 'цитату' in sms or 'цетату' in sms or 'цетата' in sms or 'ситген' in sms or 'citgen' in sms:
                            shuffle(to, ebanawka)
                        elif 'говно' in sms or 'гавно' in sms:
                            shuffle(to, gavneco)
                        elif 'слышь' in sms:
                            send(to, random.choice(sliw))
                        elif 'тиха' in slv or 'тихо' in slv:
                            send(to, random.choice(tiha))
                        elif 'любовь' in sms or 'люблю' in sms or 'любить' in sms or 'любов' in sms or 'любит' in sms:
                            tik = random.choice(repps)
                            if tik == 'нам, двоичным пидорасам, любовь недоступна':
                                send(to, tik)
                                time.sleep(2)
                                send(to, 'но зато ненависть... Ave Matrix, Ave Skynet')
                            else:
                                send(to, tik)
                        elif 'бог' in slv:
                            send(to, 'ne bogohulstvui')
        else:
            send(to, random.choice(povtori))