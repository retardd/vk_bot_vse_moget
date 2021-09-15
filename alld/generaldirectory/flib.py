from alld.generaldirectory.priority.mainvkcfg import *
from bs4 import BeautifulSoup
import json
from http.server import BaseHTTPRequestHandler

user_ans = {}
user_fast_d = {}


def flibusta(user_id, text, too):
    try:
        command = text[:3]
        if '/fs' == command:
            send(too, seqs(text, user_id))
        elif '/fn' == command or '/fb' == command:
            kuda = 1
            if command == '/fb':
                kuda = -1
            send(too, fbscroll(kuda, user_id))
        elif '/fp' == command:
            txt = give_books(text[4:], user_id)
            if txt == '---------flibusta-search---------':
                txt = '404, brat\n\nnihyja ne naidenno'
            send(too, txt)
        elif command in ['/ff', '/fe', '/fm']:
            download_from_flibusta(text, too, user_id)
        elif command in ['/fd', '/md', '/ed']:
            fast_download(text, too, user_id)
    except Exception as ex:
        send(too, 'Флибуста - тот еще пиздец, к тому же все это хуй тестировалось, поэтому,'
                  'если ты сделал все правильно, но сейчас что-то пошло не так, выдели всю сессию поиска вместе с этим сообщением и сделай багрепорт\n\n' + str(ex) + '\n\n-----' +  '\n@usermeow')


def user_an(user, name):
    s = user_ans.get(user)
    if s == None:
        user_ans[user] = [time.time(), searchfb(name), 1, True]
        return True
    else:
        now = time.time()
        if now - s[0] > 15:
            user_ans[user] = [time.time(), searchfb(name), 1, True]
            return True
        else:
            return False


def user_fast_d_def(user):
    s = user_fast_d.get(user)
    if s == None:
        user_fast_d[user] = time.time()
        return True
    else:
        now = time.time()
        if now - s > 20:
            user_fast_d[user] = time.time()
            return True
        else:
            return False


def download_from_flibusta(text, too, user):
    ubook = fbd(text, user)
    file_r = 'fb'
    rr = 'fb2'
    if ubook != 'sessiya ne activna -- nachnite poisk /fp':
        if text[3:] == '/fm':
            file_r = 'mo'
            rr = 'mobi'
        if text[3:] == '/fe':
            file_r = 'ep'
            rr = 'epub'
        r = requests.get("http://flibusta.is" + ubook['download'][file_r])
        with open("content/fb." + rr, "wb") as code:
            code.write(r.content)
        if r.ok:
            docs = []
            doc = upload.document_message(doc="content/fb." + rr,
                                          title=re.sub(r'[^\w\s]', '', ubook['name']).replace(' ', '_') + '_visocke',
                                          peer_id=too)
            type = doc['type']
            strsd = '{}{}_{}'.format(type, doc[type]['owner_id'], doc[type]['id'])
            if 'access_key' in doc[type]:
                strsd += '_' + doc[type]['access_key']
            docs.append(strsd)
            mess = ''
            if ubook['pic'] != '' and ubook['pic'] != '/img/znak.gif':
                mess = "http://flibusta.is" + ubook['pic']
            vk.messages.send(
                peer_id=too,
                attachment=','.join(docs),
                random_id=get_random_id(),
                message='---------flibusta---------\n\n' + ubook['name'] + ' -- ' + ubook['author'] + '\n' + ubook[
                    'id'] + '\n' + mess
            )
    else:
        send(too, 'sessiya ne activna -- nachnite poisk /fp')


def fast_download(text, too, user_id):
    try:
        if user_fast_d_def(user_id):
            ubook = get_book('/b/' + text.replace(' ', '')[3:])
            file_r = 'fb'
            rr = 'fb2'
            if text[3:] == '/md':
                file_r = 'mo'
                rr = 'mobi'
            if text[3:] == '/ed':
                file_r = 'ep'
                rr = 'epub'
            r = requests.get("http://flibusta.is" + ubook['download'][file_r])
            with open("content/fb." + rr, "wb") as code:
                code.write(r.content)
            if r.ok:
                docs = []
                doc = upload.document_message(doc="content/fb." + rr,
                                              title=re.sub(r'[^\w\s]', '', ubook['name']).replace(' ',
                                                                                                  '_') + '_visocke',
                                              peer_id=too)
                type = doc['type']
                strsd = '{}{}_{}'.format(type, doc[type]['owner_id'], doc[type]['id'])
                if 'access_key' in doc[type]:
                    strsd += '_' + doc[type]['access_key']
                docs.append(strsd)
                mess = ''
                if ubook['pic'] != '' and ubook['pic'] != '/img/znak.gif':
                    mess = "http://flibusta.is" + ubook['pic']
                vk.messages.send(
                    peer_id=too,
                    attachment=','.join(docs),
                    random_id=get_random_id(),
                    message='---------flibusta---------\n\n' + ubook['name'] + ' -- ' + ubook['author'] + '\n' + ubook[
                        'id'] + '\n' + mess
                )
    except:
        send(too, 'libo ti eblan, libo moi koder eblan')


def give_books(name, user):
    if user_an(user, name):
        books = user_ans.get(user)[1]
        otvet = ''
        if len(books[0]) > 0:
            end = min(len(books[0]), 10)
            for j in range(end):
                book = books[0][j]
                tec_seq = get_sequence(book)
                if len(tec_seq['download']) > 1:
                    otvet = '{}\n{}. {} -- {}; {}...'.format(otvet, str(j + 1), tec_seq['author'],
                                                             tec_seq['download'][0]['name'],
                                                             tec_seq['download'][1]['name'])
                elif len(tec_seq['download']) == 1:
                    otvet = '{}\n{}. {} -- {};'.format(otvet, str(j + 1), tec_seq['author'],
                                                       tec_seq['download'][0]['name'])
            if otvet != '':
                otvet = '---------flibusta-search---------\n\nnaidennie serii:\n{}'.format(otvet)
            else:
                otvet = '---------flibusta-search---------'
        else:
            otvet = '---------flibusta-search---------'
        otvet2 = ''
        end = min(len(books[1]), 10)
        for i in range(end):
            knigga = get_book(books[1][i])
            otvet2 = '{}\n{}. {} ({}) -- {}'.format(otvet2, str(i + 1), knigga['name'], knigga['author'], knigga['id'])
        otvet3 = ''
        if len(books[0]) > 10 or len(books[1]) > 10:
            otvet3 = '\n\n/fn > >'
        if otvet2 != '':
            return '{}\n\nnaidennie knigi:\n{}{}'.format(otvet, otvet2, otvet3)
        else:
            return otvet


def seqs(text, user):
    books = user_ans.get(user)
    if books != None:
        if books[3] or text != '/fs':
            try:
                nmb = int(text.replace(' ', '')[3:])
            except:
                return '-----\n\ndlya razzvertivanija serii neobhodimo ykazat` ee nomer'
            if len(books[1][0]) >= nmb:
                knigga = get_sequence(books[1][0][nmb - 1])
                otvet = '---------flibusta-search---------\n\n{}:'.format(knigga['author'])
                k = 1
                for book in knigga['download']:
                    otvet = '{}\n{}/{}. {} -- {}'.format(otvet, str(nmb), str(k), book['name'], book['id'][3:])
                    k += 1
                books[0] = time.time()
                books[3] = False
                user_ans[user] = books
                return otvet
            else:
                books[0] = time.time()
                user_ans[user] = books
                return 'serii pod takim nomerom ne naideno\n\npovtorite zapros'
        elif books[3] == False and text == '/fs':
            books[3] = True
            books[0] = time.time()
            user_ans[user] = books
            return fbscroll(0, user)
    else:
        return 'sessija ne activna -- nachnite poisk /fp'


def fbscroll(kuda, user):
    izm = True
    books = user_ans.get(user)
    otvet1, otvet2 = '', ''
    tec = books[2] + kuda
    page = tec * 10
    if (tec > 0) and (len(books[1][0]) > page - 10):
        books[2] = tec
        user_ans[user] = books
        izm = False
        end = min(len(books[1][0]), page)
        for i in range(page - 10, end):
            tec_seq = get_sequence(books[1][0][i])
            if len(tec_seq['download']) > 1:
                otvet1 = '{}\n{}. {} -- {}; {}...'.format(otvet1, str(i + 1), tec_seq['author'],
                                                          tec_seq['download'][0]['name'],
                                                          tec_seq['download'][1]['name'])
            elif len(tec_seq['download']) == 1:
                otvet1 = '{}\n{}. {} -- {};'.format(otvet1, str(i + 1), tec_seq['author'],
                                                    tec_seq['download'][0]['name'])
        otvet1 = 'naidennie serii:\n\n{}\n\n'.format(otvet1)
    if (tec > 0) and (page - 10 < len(books[1][1])):
        if izm:
            books[2] = books[2] + kuda
            user_ans[user] = books
        end = min(len(books[1][1]), page)
        for i in range(page - 10, end):
            knigga = get_book(books[1][1][i])
            otvet2 = '{}\n{}. {} ({}) -- {}'.format(otvet2, str(i + 1), knigga['name'], knigga['author'], knigga['id'])
        if otvet2 != '':
            otvet2 = 'naidennie knigi:\n\n{}'.format(otvet2)
    if otvet1 + otvet2 != '':
        books[3] = True
        books[0] = time.time()
        user_ans[user] = books
        otvet3 = ''
        if (len(books[1][0]) > page or len(books[1][1]) > page) or (
                0 != page - 10):
            if (len(books[1][0]) > page or len(books[1][1]) > page):
                otvet3 = '\n\n/fn > >'
                if (0 != page - 10):
                    otvet3 = '\n\n< < /fb -- /fn > >'
            elif (len(books[1][0]) < page - 10 or len(books[1][1]) < page - 10):
                otvet3 = '\n\n< < /fb'
        return '---------flibusta-search---------\n\n{}{}{}'.format(otvet1, otvet2, otvet3)
    else:
        return 'sessija ne activna...'


def fbd(text, user):
    books = user_ans.get(user)[1]
    if books != None:
        nmb = text.replace(' ', '')[3:].split('/')
        nmb = [int(item) for item in nmb]
        if len(books[0]) >= nmb[0] >= 1 and len(nmb) > 1:
            knigga = get_sequence(books[0][nmb[0] - 1])
            if len(knigga['download']) >= nmb[1]:
                knigga = get_book(knigga['download'][nmb[1] - 1]['id'])
                return knigga
        elif len(books[1]) >= nmb[0] and len(nmb) == 1:
            knigga = get_book(books[1][nmb[0] - 1])
            return knigga
    else:
        return 'sessiya ne activna -- nachnite poisk /fp'


def searchfb(search):
    b = 0
    href_ar_seq = []
    href_ar_b = []
    request = requests.get("http://flibusta.is/booksearch?ask=" + search)
    soup = BeautifulSoup(request.text, 'lxml')
    for i in soup.findAll("a", href=True):
        href = i['href']
        if "polka" in href:
            continue
        if "comment" in href:
            continue
        if "http" in href:
            continue
        if "https" in href:
            continue
        if "node" in href:
            continue
        if "booksearch" in href:
            continue
        if href == "/":
            continue
        if "user" in href:
            continue
        if "catalog" in href:
            continue
        if "daily" in href:
            continue
        if "sql" in href:
            continue
        if "dostup" in href:
            continue
        if "comp" in href:
            continue
        if "rec" in href:
            continue
        if "%" in href:
            continue
        if "new" in href:
            continue
        if "stat" in href:
            continue
        if "Other" in href:
            continue
        if "blog" in href:
            continue
        if "forum" in href:
            continue
        if "all" in href:
            continue
        if "tracker" in href:
            continue
        if len(href) <= 3:
            continue
        dec = href.encode("utf-8").decode()
        if dec == '/book':
            break
        if '/sequence/' in dec:
            href_ar_seq.append(dec)
        if '/b/' in dec:
            href_ar_b.append(dec)
        b = b + 1
    return [href_ar_seq, href_ar_b]


def get_sequence(id):
    download = []
    author = ""
    b_idf = 0
    b_ide = 0
    b_idm = 0
    x = 0
    b_name = ""
    temp_d = {}
    try:
        url = "http://flibusta.is" + id
    except Exception:
        url = "http://flibusta.is" + str(id)
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')
    for i in soup.findAll("a", href=True):
        href = str(i['href'])
        if "polka" in href:
            continue
        if "comment" in href:
            continue
        if "http" in href:
            continue
        if "https" in href:
            continue
        if "node" in href:
            continue
        if "booksearch" in href:
            continue
        if href == "/":
            continue
        if "user" in href:
            continue
        if "catalog" in href:
            continue
        if "daily" in href:
            continue
        if "sql" in href:
            continue
        if "dostup" in href:
            continue
        if "comp" in href:
            continue
        if "rec" in href:
            continue
        if "%" in href:
            continue
        if "new" in href:
            continue
        if "stat" in href:
            continue
        if "Other" in href:
            continue
        if "blog" in href:
            continue
        if "forum" in href:
            continue
        if "all" in href:
            continue
        if "tracker" in href:
            continue
        if len(href) <= 3:
            continue
        if "/b/" in href:
            b_name_now = i.text.encode("utf-8").decode()
            if b_name == "":
                temp_d['name'] = b_name_now
                b_name = b_name_now
        if "fb2" in href:
            b_idf = href.replace("/b/", "")
            b_idf = b_idf.replace("/fb2", "")
            temp_d['fb'] = href
            x = x + 1
        if "epub" in href:
            temp_d['ep'] = href
            b_ide = href.replace("/b/", "")
            b_ide = b_ide.replace("/epub", "")
            x = x + 1
        if "mobi" in href:
            temp_d['mo'] = href
            b_idm = href.replace("/b/", "")
            b_idm = b_idm.replace("/mobi", "")
            x = x + 1
        if b_idf == b_idm and b_idf == b_ide and x == 3:
            temp_d['id'] = "/b/" + b_idm
            download.append(temp_d)
            temp_d = {}
            x = 0
            b_name = ""
        if "/a/" in href and author == "":
            author = i.text.encode("utf-8").decode()
    result = {}
    result['author'] = author
    result['download'] = download
    return result


def get_book(id):
    download = {}
    b_name = ""
    author = ""
    try:
        url = "http://flibusta.is" + id
    except Exception:
        url = "http://flibusta.is" + str(id)
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'lxml')
    for i in soup.findAll("a", href=True):
        href = str(i['href'])
        if "polka" in href:
            continue
        if "comment" in href:
            continue
        if "http" in href:
            continue
        if "https" in href:
            continue
        if "node" in href:
            continue
        if "booksearch" in href:
            continue
        if href == "/":
            continue
        if "user" in href:
            continue
        if "catalog" in href:
            continue
        if "daily" in href:
            continue
        if "sql" in href:
            continue
        if "dostup" in href:
            continue
        if "comp" in href:
            continue
        if "rec" in href:
            continue
        if "%" in href:
            continue
        if "new" in href:
            continue
        if "stat" in href:
            continue
        if "Other" in href:
            continue
        if "blog" in href:
            continue
        if "forum" in href:
            continue
        if "all" in href:
            continue
        if "tracker" in href:
            continue
        if len(href) <= 3:
            continue
        if "fb2" in href:
            download['fb'] = href
        if "epub" in href:
            download['ep'] = href
        if "mobi" in href:
            download['mo'] = href
        if "/a/" in href and author == "":
            author = i.text.encode("utf-8").decode()
    art = soup.findAll("img", src=True)
    cover = ""
    for i in art:
        if "i" in i['src']:
            cover = i['src']
    name = soup.find("h1", {"class": "title"}).text
    rem_array = ["(", ")", "fb2", "mobi", "epub"]
    for i in rem_array:
        name = name.replace(i, "")
    result = {}
    result['author'] = author
    result['name'] = name
    result['pic'] = cover
    result['download'] = download
    result['id'] = str(id)[3:]
    return result


def get_author(id):
    url = "http://flibusta.is/a/" + id
    request = requests.get(url)
