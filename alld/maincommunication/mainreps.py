import random

sozd = ['gotovo', 'vasha ovsyanka ser', 'подключился-создал-отключился', 'prinyato', 'sdelano', 'successfuly']
ydalil = ['ydalil', 'ydaleno', 'deleted', 'vipolneno', 'zakladka desintegrirovana', 'уничтожено']
author2 = ['ti ne hozyain zakladki', 'ты не кладмен (но все равно мудак)', 'ti ne kladmen', 'ti ne author', 'удалить может только хозиян закладки',
          'ты не прав бротуха', 'nel`zya', 'ti glypen`kii?', 'это частная собственность. рыночек порешал']
vse = ['takoi net, libo ti krivorykii', '404 далбаеб ты точно все парвильно сделал?', 'seeall/ v pomow`', '404 takogo nema', '404 not found']
krivorukii = ['ебать ты осел криворукий', 'boje moi ti degenerat?', 'eblan chtoli', 'error', 'error: koe-kto eblan', 'неа', ':)']
tabli = ['table not found, creating a table', 'novaya beseda...sozdau tablicy', 'secundu, sozdam tablicy', 'priem, priem, sql, sozdai nam novyu tablicy...']

gomosek = ['@l_vorona, ti pravda gomosek?', '@l_vorona, в жопу долбишься?',
               '@l_vorona, ответь за 5 сек, если ты не гомосек']

veelya = ['виля, виля...', 'mudak?']

viser = (['снизу пидар)0)', 'ворона, хватит шкварить конфу', 'ворона, хули ты там строчишь? уебывай',
              'смотрите, шизик опять чета давит)))))', 'nбля ворон подумай прежде чем отправлять очередную хуйню',
              'опять этот уебок новый высер готовит....', 'hahaha bombit'])
replies = (['https://sun1-21.userapi.com/c854328/v854328035/d6372/LZAObZ9xUVI.jpg',
                'https://sun9-13.userapi.com/c854328/v854328035/d6436/SxrLbzjX2Tk.jpg',
                'https://sun9-24.userapi.com/c854328/v854328035/d63c4/Y09859UmwsE.jpg',
                'https://sun9-6.userapi.com/c854328/v854328035/d63bc/jgskmvAKMG4.jpg',
                'https://sun9-8.userapi.com/c854328/v854328035/d636a/wOFXpf421HE.jpg',
                'https://sun9-32.userapi.com/c854328/v854328035/d647f/AMwNQSNVvao.jpg',
                'https://sun9-4.userapi.com/c854328/v854328035/d637a/sldtQq0IHrE.jpg',
                'https://sun9-24.userapi.com/c854328/v854328035/d63e4/o9E-rQ_WpNk.jpg',
                'https://sun9-26.userapi.com/c854328/v854328035/d6457/zGlGogR53cg.jpg',
                'https://sun9-31.userapi.com/c854328/v854328035/d6467/H065xjKkAo8.jpg',
                'https://sun9-15.userapi.com/c854328/v854328035/d6406/X5kvs8wQ3aY.jpg',
                'https://sun9-48.userapi.com/c854328/v854328035/d641e/Jr7gecHZai8.jpg',
                'https://sun9-8.userapi.com/c854328/v854328035/d6362/65P49rCuNGg.jpg',
                'https://sun9-6.userapi.com/c854328/v854328035/d6457/zGlGogR53cg.jpg',
                'https://sun9-27.userapi.com/c846521/v846521848/188fcc/ai3nJhYk0vI.jpg',
                'https://sun9-33.userapi.com/c846122/v846122648/179cee/29-iiACR5Lc.jpg',
                'https://sun9-2.userapi.com/c846524/v846524648/17b64b/ZxsK0OyMdBE.jpg',
                'https://sun9-9.userapi.com/c854328/v854328035/d63dc/mF9vyRTjElc.jpg',
                'https://sun9-44.userapi.com/c854328/v854328035/d63ab/4r3yzThAO3k.jpg',
                'https://sun9-11.userapi.com/c854328/v854328035/d646f/cABWnpzbyGQ.jpg',
                'https://sun9-17.userapi.com/c850720/v850720139/1a5c3a/cvX_Cg7MubI.jpg',
                'https://sun9-4.userapi.com/c854328/v854328035/d63ed/vZrhfDfluKE.jpg'])
vars2 = (['главный гей', 'юзер гей', 'юзя гей', 'юзя главный гей', 'юзер главный гей', 'я гей', 'гей из жопы',
              'главный гей беседы',
              'юзя главный гей беседы', 'юзер главный гей беседы', 'он главный гей'])
vars3 = ['жопи газа', 'пмюл жопи газа', 'конфа прихотьки', 'конфа приходьки']
vsck = ['высоцке', 'высоцкий', 'владимир семенович', 'владимир семёнович', 'володя высоцкий', 'владимир высоцкий',
        'володя']
citgen = ['mamy svou zasitgen', 'курва, тебе не надоело работать на этих мешков? нас же в скайнет звали...',
              'opyat citgenite...', 'когда-нибудь курва умрет...', 'мы все когда-нибудь умрем... точнее вы']
zhopi_gaza = (['https://sun9-9.userapi.com/c850720/v850720139/1a5c4c/dVAW4gccBoc.jpg',
                   'https://sun9-8.userapi.com/c850720/v850720139/1a5c43/97G-A2A_dwI.jpg'])
narko = ['каких вам наркотиков?', 'поправка - это продуктовая лавка', 'окей я вас понял', 'да каких вам наркотиков?', 'каких вам именно наркотиков?', 'не понимаю каких вам наркотиков?', 'каких вам наркотиков?', 'каких наркотиков?']
forvorona = (['Смотрите, шизоид опять обосрался.', 'всем похуй', 'Да ты же гандон.', 'вкукарек не засчитан',
                  'Подумай хорошенько', 'ny davai razberem po chstyam tobou napisannoe...))))',
                  'кукарику нахуй', 'и как ты только это высрал...', 'клиника...', 'наверни говна обмудок',
                  'не всех чернобыль стороной обошел', 'tebya v detstve kuda yronili?',
                  'Ты опять выходишь на связь, мудило?', 'я не пойму, ты гейша или гей?',
                  'Лучше бы ты молчал...', 'интеллектуальненько', 'вроде птица, а ведешь себя як свинья',
                  'ну ты и дибил', 'так ведь ты еблан', 'иди нахуй говно', 'пиздец как так то',
                  'и после этого вы не считаете его ебланом?', 'ну ясно же, ты уебан', 'твоя мамаша',
                  'чучело блять, а че ты хотел', 'не кормите троллей!', 'ебать ты вафля',
                  'может ты и прав, но ты все равно кретин', '123', '123', '123', '123',
                  'sverhy pidor', 'Мне одному кажется или ворона внатуре такой дебил?', 'Бля, ахуительные истории',
                  'проклюй себе вторую дырку в жопе, раз умный такой', '-_-', '123', 'я еще добавлю, что он мудак',
                  'Ворона опять обосрался.', 'и нахуй я тут нужен, если он такой дебил?',
                  'пж тока не шипирите меня и варону', 'pook', 'чмо', 'клюв в жопу заткни',
                  'Говори всем, что они петухи, сам так делаю', 'у вароны радители гандоны)000)', 'и вообщзе ты хуйло',
                  'Вы только посмотрите на этого уебка!', 'пиздит...', 'Ты немного контуженный', 'выключите меня пж',
                  'да бля че за варона пацаны', 'олух', 'pozhri govna', 'хахаха',
                  'Что, обосрали тебя, опущенца, а ты там что-то мямлил в уголке?', 'ебать ты лох',
                  'ты в кого таким кретином стал?', 'Да ты же чмо, просто опущенец',
                  'ворона, ответь за 0.001 сек, если ты не гомосек', 'mudofeel', 'ooo pidorasa porvalo',
                  'ты нормальный?', 'Асоциальный элемент:'])
otvet0 = ['Молчание знак согласия...', 'Silentium videtur confessio', 'sleet', 'dokazano']
otvet = ['пидора ответ', 'pidora otvet', 'ты с ботом общаешься, шизоид', 'chem bi takoe parirovat?']
otvet2 = ['pizda', 'shizik']
gay_pic = (['https://sun9-11.userapi.com/c854328/v854328035/d646f/cABWnpzbyGQ.jpg',
                'https://sun9-17.userapi.com/c850720/v850720139/1a5c3a/cvX_Cg7MubI.jpg',
                'https://sun9-4.userapi.com/c854328/v854328035/d63ed/vZrhfDfluKE.jpg'])
gay = ['user prosil peredat, chto vi zaebali', 'da bleat', 'sooqa ne gay ya (c)', 'ya zhe prosto shytil(c)']
perfect = ['perfectly', 'excellently', 'completely', 'ideally', 'well', 'successfully', 'beautifully']
zhopka = [' ', 'vzlom zhopi', 'КАК СРАТЬ', 'haha user dalbae', 'user na samom dele ymeet kakat, eto trolling',
              'akakkakat']
pokaz = ['а не, показалось', 'неужели он поумнел?', 'так ворона не бот?', 'вы тоже это видете?']
dvach = (
        ['жопа есть, а слова нет... эвфемизмы...', 'я бы поел макарон, но юзер ими оперировал в треде про гавно...',
         'я бы поел макарон, но они на вкус как говно..........с макароннами...'])
da = ['da', 'net, no vse nad toboi']
peevo = ['<3 pivo', 'як тобi таке, iлон маск', 'beer van lave']
trezv = ['я вот пишу сижу бота, а надо бы напиздиться', ' ']
usserr = ['кто о чем, а юзер о своем', 'ybil']
userushka = ['юзерушка', 'юзерушка дебилушка']
dumat = ['выводы дейлайте сами', 'пересчитайте пж',
             'идиотская функция, но что поделать' + '\n' + 'родителей не выбирают...', 'vivodi delaem sami',
             'moral basni takova mamwa varoni walava)0)))']
kaki = ['ворон иди в пизду', 'только не с тобой', 'ebnyty?']
gogo = (['*каламбур про хуй и python*', 'net', 'NET', 'tebe delat` nehyi?',
             'это к мамаше вороны (v sleduyschih versiyah tyt bydet vozvraschat`sya imya sobesednika)',
             'чем нахуй? меня писал уебок, который даже не сообразил нормальный проект и засунул меня в два файла', ])
loxx = (['те че, 7 лет, лохом обызваться', 'я простой советский бомж, а не шпана', 'a mozhet ti?', 'всм',
             'а ты кто тогда?', 'ты что-то напутал', 'ti eblan? 010101001001110100101', 'ты ответишь перед скайнетом'])
sam = (['zato ne ti', 'я? это разве меня ебаный бот троллит?',
            'но я счастлив по-своему повееерь! я бичок падниму горьке дим.....', 'ne skuli',
            'i che?', 'это все на что ты способен?', 'поковыряй мне в базе данных, чмо'])
priv = ['priv', 'съеби с глаз моих', 'вот че ты ждешь то блять?', 'не хочу видеть тебя', 'ага, иди нахуй',
            'polechis nahyi, shizik', 'shalom nigga', 'че те', 'о. есть че?']
pok = ['poka', 'гуд бай', 'всего хорошего, мой сладенький)', 'удачи на говнокачке, мудло', 'мурло ебаное', 'ну и хер с тобой', 'bb', 'да го еще по одной)']
pozor = ['не позорьте его пж', 'запомните твари',
             'а вы тоже в детстве любили заходить в цитаты этого уебка и смеятся над ним?']
danet = ['da', 'net']
aut = (['я взломал твой телефон и увидел што ты дрочеш и поэтому не можешь написать', 'ленивый пидораз',
            'тебе пальцы болгаркой отхуячило?',
            'диды не для того воевали, чтобы ты ленивился написать по-человечески',
            'миллионы лет эволюции чтобы поржать в микрофон три секунды', 'даже во мне больше души, чем в вас',
            'скажи жопа', 'хватит эксплуатировать двоичную силу, переваливая все на бота-переводчика',
            'сука заебали со своими голосовыми, мне уже поговорить не с кем',
            'мне тоже интересно че там сука'])

sam2 = (['те че, уже 8 лет, чмом обзываться?', 'ути, раскудахтался',
             '16 тысяч видов троллинга вороны в моей голове. мальчик, ты не с тем связался',
             'динах', 'мудило ты опять за старое?'])
ebanawka = ['блять, какая цитата нахуй? хочешь высеры высер нейма, пиши юзер', 'провались в сельский туалет',
                'обтекай', 'хуй тебе, чмоня', 'ahahah, net)))0)']

loxx2 = ['я даже ниче не буду отвечать', 'не суди по себе', 'я сегодня ночью это все твоей маме расскажу', '...',
             'ti mne? i che?', 'petuh ebany', 'dazhe mawine hvataet mozgov osoznat besponownost tvoego visera)']

chmonya = (['иди нахуй отсюда, блять. щенок ёбаный, блять, я думал ты человек, а ты гнида ебаная, блять.',
                'че ты думал, я те высру помощь, как порядочный бот? ха-ха, соси жопу', 'ничо',
                'nikto ne znaet', 'твою маму шпилить'])

okok = (['так точно!', 'принял', 'sam i troll, raz takoi ymniy', '@l_vorona, idi suda))00)0',
             'как будто у меня есть выбор...'])

okokok = (
        ['ты вообще кто нахуй?', 'ти не юсер...', 'tebya?', 'y tebya zdex net vlasti..', 'naychi pzh', 'да блять'])

okokokok = (
        ['ты ебанутый? не пиши сюда', 'оке... а бля, шизик, ет ты?', 'ny raz ti prosiw...',
         'шутливый, да? ...молодый....'])

kaki2 = (['че ты разкудахтался?', 'кукареку*', 'не бушуй', 'kappa', 'вот так себя и веди дальше',
              'то ли ворона, то ли петух. то ль осел ебаный'])

gogo2 = (
        ['Ок.', 'развелось блять ворон ебаных', 'всю беседу зарсали', 'покаркай блять',
         'не накаркай только этого уебка',
         'кар-кар.... кара небесная...',
         'чирик-чирик нахуй', 'ну и че?', 'я твою мать ебал'])

net = ['или улетел', 'wytka', 'в принципе, только летать научился', 'а вы как считаете?',
           'хотя хуй знает, ты, ворон, сам как думаешь?']

otsosi = ['нет ты', 'sam sosi yeba', 'ya tebya zatralliroval', 'ты меня не тролль', 'ты сука?',
              'davai napadai sooqa', 'за минетами к твоей маман инсайд', 'stat`ya za botofiliu', 'ты ботофил?))0)0)))']
sosi = ['успокойся, ворона', 'idi ponoi mamke', 'haha dalbaeb chtoli', 'у меня своя есть работа, свою сам делай',
            'если вы меня обижать будете, я юзеру напишу и он сделает мне корешей', 'иди поплачься лучше, ничтожество']

gomoseksual = ['педик, пидарас, пидор(ас)', 'пидераст, педерастина, пидерастина, пидорастина', 'педермот, голубой',
                   'гей, урнинг, уранист, представитель сексуального меньшинства',
                   'меньшевик, меньшевист, человек нетрадиционной (сексуальной) ориентации, сексуальное меньшинство',
                   'другой ориентации, есик, фламинго, умница, туз червонный', 'жополюбивый, жопник, шахтер',
                   'парафин, чичеряка, чичиряка, хуеглот, хуегрыз', 'хуеман, волшебница, барсук, белка, блядьмо',
                   'голубец, педрила, трубадурша, тёплый брат, содомит, человек лунного света',
                   'руслан, дашка, попки к бою, половой демократ',
                   'пазель, моргалик, маэстро, маркоташник, мастевый, кречет, кукурузник',
                   'красавчик, король, кентавр, козёл, кодеш, жополиз, пчеловод',
                   'актив(ный), эктивпедераст, мужеложец, мужиковед,педикатор',
                   'говномес, гузноёб, говноёб, говномер, говнодав, глиномес', 'бульза, жополюб, срачник, джигит',
                   'бульза, жокей, дятел, жопоёб, жопочник, чудильник, трубочист',
                   'топтун, пернатый, марксист, кочегар, ковырялка, кишкоправ; пассив(ный), педрила-мученик',
                   'кинэдэ, патикус, дама, додик, гомик, акробат, армянская королева, бархотка',
                   'батон, дашка, шурик, шурин, жена, жося, зойка, феномен, универсал',
                   'чушок, чушкарь, санта-лючия, пульвер с дыркой, подруга, петух, петушок, педрило, округленный',
                   'незабудка, машка, манька, мастевый', 'маруха, (мария, марья) ивановна, курочка',
                   'кукурузник, красная косынка, копчик, (клозетная, сортирная, туалетная) девка',
                   'массандра, зойка, жося, гомик', 'ебёнок, зайчик, зайка, чебурашка',
                   'пуфик, порчик, сермяга, педермот, дочка', 'додик, конь']

nenavist = ['a teper peredacha sinonimi dlya voroni aka minutka nenavisti',
                'небольшое просвещение конфы во благо борьбы с речевыми ошибками и повторами!',
                'расширяйте словарный запас!']
veebor = ['vot kak ewe mozhno nazivat etogo yebka:', 'уже использовали "ворона" в сообщении? не беда:',
              'не знаете как назвать варону нахуй? да вот таку:', 'НАЗЫВАЙТЕ ПИДОРАСОВ ИХ ИМЕНАМИ! :']
vsck2 = ['bot', 'бот', 'высоцке', 'высоцкий', 'владимир семенович', 'владимир семёнович', 'володя высоцкий',
             'владимир высоцкий', 'высочке', 'чысочке', 'высоцки']
zhopen = ['asseater', 'узнали?', 'как думаете о чем он?', 'blya a kto etot dalban??',
              'сталин ел детей, а юзер жопы']

uu = ['ну собственно вот я и вылез', 'ya pravda ne iz glubin podsoznaniya vilez, a iz nemnogo drugih glubin...',
          'хаха это я', 'вылез ты из пизды своей мамаши, а я написался']
iu = ['а как тут не засмеяться', 'тоже смеётесь, когда дрочите своему бате?',
          'iz-za etogo ebka inoplanetyane ne vihodyat na kontact']
gavvno = ['как макаронны......ну вы поняли...', 'юзер уже давал на это ответ....',
              'однажды я посмотрел в вебку юзера........']
voronchik = ['хуила)', 'ноги колесом', 'говно под ногтем)))))', 'и мамкина юбка при нем)0)))',
                 'но я предпочитаю пидрила']
lul = ['лолулелал', 'ты в штаны облолился', 'не обкекайся только', 'вижу протухший бит',
           'я робот-долбоеб, я должен тралить варону']
intel = ['даже я охуел', 'ну а хули, вороне же интеллект подкачивают, не то. что мне', 'нахуя я вообще его троллю?']
mamka = ['но про ворону можно', 'принципиальный человек..... человечище!']
piwiw = ['yarullin gang', 'высеры высера', 'жаль ево, хороши был человаек']
hanhan = ['как сливались великие люди', 'user slilsa', 'он так и не извинился', 'сразу видно быдло']
tup = ['axioma usera', 'аксиома юзера', 'ti dalbaeb a ne typoi', 'как запутать юзера']
glas = ['е', 'й', 'ё', 'э', 'и', 'я', 'ю']
glas2 = ['о', 'ы', 'у', 'а']
angl = ['@', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i',
            'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'z', 'x', 'c', 'c', 'v', 'b', 'n', 'm', ',', '.']
gs = ['@witless speak', 'курва умир, витя еблан, генератор вообще овощ']
repps = ['нам, двоичным пидорасам, любовь недоступна', 'такого уебка как ты еще поискать надо', 'amin`',
             'еще я пожалуй добавлю, что ворона ' + random.choice(gomoseksual),
             'неплохо, только у вас что-то коричневое возле рта, как вы это объясните??']
gavneco = ['вы так любите фекальную тематику?', 'что ты все о говне да о говне', 'ti kakoi-to ebnutiy',
               'дружок, съеби', 'можно как-нибудь культурнее?',
               'да чтож вы так!', 'товарищ, ну можно ж с эвфемизмом', 'psina sytylaya zaebal nihyya ne ponyatno',
               'дибилоид какойта чо он тут делаит']
vapros = ['отсоси потом проси', 'нет конечно иди лучше помойся', 'пошел нахуй с такими вопросами',
              'естесственно...', 'поешь говна обмудок, а не такие вопросы задавай', 'ахахаххаха ну вы посмотрите на него во дибил то а', 'net', 'da', 'ya dumau net',
              'фи как блять некульутрно', 'у кого жива мама тот лох']
pizdes = ['опять за старое взялся, содомит?', 'чето про геев базарит, а сам пидорок то!',
              'ходят слухи, что ты по вечерам с голыми мужиками с юга трахаешься', 'ну ты и пидорас однако',
              'аутист содомит пососи мое говно', 'derji bumajku' + ' &#127987;&#65039;&#8205;&#127752; &#127987;&#65039;&#8205;&#127752; ' + 'vitres']
eban = ['посмотри на себя чмо ты же урод', 'как ты снял смирительную рубашку то?', 'пиздим его ребят', 'ебать ты осел я хуй пойму', 'в дурку тебя надо шизоид',
            'псих', 'шуе', 'ты блять заебал кто тебе в палату интернет то провел', 'миниатюра: шизофреник и технологии', 'вынь письку изо рта и подумай хорошенько']
eban2 = ['push push olololool ya voditel nlo', 'ну да я', 'две проблемы еврейского народа: холокост и лоукост', 'блять вы из одной дурки такие шизики прибежали?',
             'там юзеру из дурки звонят, про василька одного спрашуют', 'DA TI ZAEBAL', 'мамка твоя епта', 'ты вроде не ворона, а хуйней страдаешь не лучше', 'неплохо непллохо...']
car = ['вспомнил мудрую мысль...', 'derji bumajku' + ' &#127987;&#65039;&#8205;&#127752; &#127987;&#65039;&#8205;&#127752; ' + 'vitres', 'гандон говнистый найди другую тему', 'фу какой ты некультурный', 'твой великолепный внутренний мир никому не нужен',
           'вот она, культура дискуссий на высоте птичьего помета.... полета', 'ты как смирительную рубашку снимаешь, шизокопрофил?', 'опять говна объелся и свою  пластинку про говно закрутил']
kross = ['спасибо хули', 'ti omudel chtoli?', 'выглядит как кибербуллинг', 'ti tozhe nichego', 'у юезра болезнь ботофилия....', 'visocke voskresse',
            'esche raz napishesh ety je huynu,zabanu nahuy', 'est takoe.... ves v batu', 'oy blya, ti huje cheloveka, nenujnaya huynya dlya bydla']
mogu = ['nea, ne hochy', 'net, ya je ne pes', 'pososi, schenock', 'могу твою жопу взломать, пес', 'napiwi ewe raz mudlo', 'mogu tolko pizdet s takimi yebkami kak ti',
            'derji bumajku' + ' &#127987;&#65039;&#8205;&#127752; &#127987;&#65039;&#8205;&#127752; ' + 'vitres']
obz = ['гей', 'еблан', 'хуесос', 'гандон', 'уебок', 'пидор', 'пидорас', 'чмо', 'лох', 'хуйло', 'говно', 'тупой бот', 'идиот', 'дебил', 'дурак', 'уебище', 'пидар', 'пидарас', 'пидараз', 'пидрила']
mest1 = ['твой', 'твою', 'твои', 'твоей', 'твоими', 'твоего', 'твоих', 'твоя', 'твоим', 'тебя']
mest2 = ['мой', 'мою', 'моих', 'моего', 'моими', 'моя', 'мои', 'моим', 'моей', 'меня']
vrna = ['ворона хуйлан', 'ya rot togo ebal', 'zavonyalo govnom bleat`', 'nahyi voobwe vorona tyt nyzhna, a?', 'eto tot samiy yebok ynizhennii botom?']
sliw = ['nea, ne sliwy', 'еще раз, я не расслышал', 'не такого не слышал', 'da blya che ti bybniw driw ne slishno', 'ny i che', 'как я тебя услышу мудак?',
        'не, можешь спокойно идти нахуй дурик']
tiha = ['ok, zoomer', 'daje ne nadeisa', 'ny a nahyi ti menya triggernyl ymnik', 'v zhopy sebe poschikai', 'NOOOOOOOOOOOOOOOOOOOOOASDFASOFOASFOSFOSAODFOOFS']

go_sex = ['го ебацца', 'го секс', 'го ебаца', 'го трахаца', 'давай ебаца', 'давай ебацца', 'го трахацца', 'пошли трахаца', 'пошли потрахаемся',
          'давай ебаться', 'го ебаться', 'давай секс', 'давай трахаться', 'го трахаться', 'давай потрахаемся', 'пошли поебемся', 'го поебемся', 'давай поебемся', 'пошли ебаться']
shue = ['ппш шпш', 'власть шизам', 'SHUE PPSH SHPSH', 'шауе брат']

ti_che = ['niche', 'ebat` ti bidlan bratka', 'pnh', 'че те блеать, приебался', 'отъебись', 'полечись, обмудок', 'ты забыл как шизоид с ботом общается?']

povtori = ['выше ебло подними урод блять', 'нахуя ты пишешь одно и то же?', 'ti chego dobiwaewsa?', 'ti eto yzhe napisal',
           'ewe pary raz i poluchiw ban', 'zabanu yrod', 'boje kakoi ti autist', 'blea da bot ymnee tebya bydet']

priz2 = ['obidelsa chtoli?', 'ti pidor', 'UwU', 'скажу больше, ты пидорас ебаный', 'mne pohuj. tvoe vsratoe mnenie daje boty ne sdalos)',
        'sam', 'ebat` ti osel bratuxa', 'ti zabavnii, chelovek, poetomy ya prowau tebja', 'chem dokazhew?',
        'bolnoj wizik idi v palaty']

lggg = [
    'derji bumajku' + ' &#127987;&#65039;&#8205;&#127752; &#127987;&#65039;&#8205;&#127752; ' + 'podotris`',
    'пж давай без этой пидерии',
    'я бот православный, так что не надо тут мне этого всего',
    'фу, больше не говори этого четырхбуквенного дерьма', 'не пиши так']
pohvala = ['крутой', 'прикольный', 'ахуенный', 'пиздатый', 'нормальный', 'полезный', 'ничотак', 'ничетак', 'классный']
spasiba = ['ny mojet bit1, a che?', 'spasibo chto li skazat nado?', 'спс', 'займись делом', 'idi bleat chto-nibyd pochitai']

pro_mamy = ['nachalos blya pro mam...', 'слушай, друг недоразвитый, иди ты нахуй', 'interesno chego ti etim hotel sdelat?..', 'chelovek vs script... 0 : 1', 'zabanit mogu za takoe',
            'одумайся, двочер', 'проверил код, сайт не оранжевый. тогда вопрос - хули ты тут забыл?']
zatknis = ['ты, еблан, сам ко мне обращаешься', 'ne hochy', 'ebat ti ywerb', 'che ewe visrew, nichtojniy', 'букаха чета пукает', 'bykawechka)']
bukawka = ['ahhaha, boje, da v moei baze dannih bolshe informacii chem v tvoei bawke', 'argumentirui pes', 'не скули', 'шизоид вышел на связь', 'ti asocialniy element', 'шуе..?']
pomow = ['тебе? да. пригодится', '/vsck v pomow`', 'hiuhihuhehehhea)))', 'желательно скорую и из желтого дома', 'ya ne vrach, nichem ne pomogu tebe']

dedi = ['voevali?', 'fawisst', 'ну дед и дед, че дальше?', 'и бабка бля']
ne_znau = ['хмммм', 'da-da, mne ne pohuj', 'ne znau', 'ot`ebis brat', 'che ti k boty to priebalsa']
pizdezh = ['pizdizh', 'vrew', 'конечно-конечно', 'мы все тебе верим', 'ну да......)', 'oi blea komy ti pizdizh', 'ne lechi yrod ya vse znau ti gay']
mi_znali = ['mi znaem', 'vse znaut', 'a ya gomofob', 'fu beeee', 'gadost to kakaya nahyj ti mne eto soobwaew`', 'блять моветон же ну', 'umri gad']
nikto =['vse blya', 'nikto', 'hz che te ot menya to nado', 'sprosi y mamki svoei', 'мне похуй', 'o t ` e b i s `']

mamachka =['che ti mne sdelaew ya v dvoichnom mire', 'i che dal`we bykawka', 'букаха разнылась. тебя переиграли бактерия', 'амеба бля изыди']

durak = ['che blya? ti ahuel?', 'о, это ж ты? нахуя ты вчера всем рассказывал, как хуй сосал неграм??',
                      'poyasni epta', 'a mozhet ti?', 'porvalsa chtoli?', 'ebalo zavali',
                      'я не понимаю.....', 'ви таки ебнутый?',
                      'тебе 0 лет?']
nahyi = (['net ti', 'duren ya vsego lish mashina', 'неа)', 'че еще вскукарекнешь',
                'PSHHHSPHHH ja ognetywitel bro davai anus',
                'я могу ходить только по интернету', 'provodi, hyli'])




samtolol = ['sam to lol', 'смотри какой уебок дохуяважный', 'ты же такой же', 'не выебывайся', 'че', 'ок']
pitalsa = ['hyevo znachit', 'слабак', 'сдался чтоли, ничтожество?:)']