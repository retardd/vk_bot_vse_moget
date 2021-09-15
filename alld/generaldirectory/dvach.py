from alld.generaldirectory.priority.mainvkcfg import *
import html
from alld.generaldirectory.databasedefs import connect

spam = {}

def ident():
    cur, conn = connect()
    cur.execute('SELECT id, name from boards')
    rows = cur.fetchone()
    global list_of_confs
    list_of_confs = {}
    while rows:
        list_of_confs[rows[1]] = rows[0]
        rows = cur.fetchone()
    conn.commit()
    conn.close()

#Обновление локальной бд в памяти программы сразу после запсука/перезагрузкки
ident()

class board(object):

    def board_info(self, too):
        try:
            if board.antispam(self, too, 6):
                cur, conn = connect()
                cur.execute('SELECT name, reg_author from boards WHERE id = %s', [too - 2000000000])
                self.rows = cur.fetchone()
                conn.commit()
                conn.close()
                send(too, 'Board info:' + '\n' + 'uniquely id: ' + str(too - 2000000000) + '\n' + 'name: ' + self.rows[0]  + '\n' + 'registrator id: ' + str(self.rows[1]))
        except:
            pass


    def retweet(self, mesid):
        try:
            send_forward(2000000040, '', mesid)
        except:
            pass


    def blag(self, mes_id):
            post = vk.messages.getById(message_ids=mes_id)
            post = vk.messages.getByConversationMessageId(peer_id=2000000040, conversation_message_ids=post['items'][0]['reply_message']['conversation_message_id'])['items'][0]['fwd_messages'][0]
            self.origf = None
            self.att = []
            if len(post['attachments']) > 0:
                for doc in post['attachments']:
                    type = doc['type']
                    self.str = '{}{}_{}'.format(type, doc[type]['owner_id'], doc[type]['id'])
                    if 'access_key' in doc[type]:
                        self.str += '_' + doc[type]['access_key']
                    self.att.append(self.str)
            vk.messages.edit(peer_id=post['peer_id'], message=post['text'] + '\n' + '\n' + 'Юзер благославил этот пост.', message_id=post['id'], attachment=','.join(self.att))


    def change(self, new_name, too, user):
        try:
            if board.antispam(self, too, 10):
                self.cur, self.conn = connect()
                users = vk.messages.getConversationMembers(peer_id=too)
                self.logic = False
                self.id = too - 2000000000
                for dict_ in users['items']:
                    if "is_admin" in dict_ and dict_["member_id"] == user:
                        self.logic = True
                        break
                if self.logic == False:
                    self.cur.execute('SELECT reg_author from boards WHERE id = %s', [self.id])
                    man = self.cur.fetchone()[0]
                    if man == user:
                        self.logic = True
                if self.logic:
                    self.cur.execute('UPDATE boards SET name = %s WHERE id = %s', [new_name, self.id])
                    send(too, 'nazvanie razdela izmeneno na ' + new_name)
                else:
                    send(too, 'izmenyat` nazvanie razdela mozhet tolko admin ili registrator')
                self.conn.commit()
                self.conn.close()
                ident()
        except:
            send(too, 'error')


    def creat_names(self):
        self.cur, self.conn = connect()
        self.cur.execute('CREATE TABLE boards (id INT PRIMARY KEY, name TEXT, reg_author INT, quant INT)')
        self.conn.commit()
        self.conn.close()


    def reg(self, sms, too, user):
        try:
            if board.antispam(self, too, 6):
                self.name = sms.split()[1]
                self.s = True
                for boards in list_of_confs:
                    if list_of_confs[boards] == too-2000000000:
                        self.s = False
                        break
                if self.s:
                    self.id = too-2000000000
                    if len(self.name) > 10:
                        send(too, 'sliwkom dlinnoe nazvanie')
                    else:
                        cur, conn = connect()
                        cur.execute('INSERT INTO boards (id, name, reg_author, quant) VALUES(%s, %s, %s, %s)',
                                    (self.id, self.name, user, 0))
                        conn.commit()
                        conn.close()
                        send(too, 'razdel //' + self.name + ' ; registrator: ' + nickname_f(user).lower() + '.' + '\n' + '-------' + '\n' + 'ynikal`ny id: ' + str(self.id))
                        ident()
                else:
                    send(too, 'send /bord')
        except:
            send(admin, 'error: board_reg')


    def quantity(self, too):
            self.id = too - 2000000000
            self.cur, self.conn = connect()
            self.cur.execute('SELECT quant from boards WHERE id = %s', [self.id])
            row = self.cur.fetchone()
            new = row[0] + 1
            self.cur.execute('UPDATE boards set quant = %s where id = %s', [new, self.id])
            self.cur.execute('SELECT info from statistic where id = 2')
            row = self.cur.fetchall()
            self.conn.commit()
            self.conn.close()
            return  new, row[0][0]


    def board_send(dialog, msgs, att, rep):
        if rep == 0:
            vk.messages.send(
                peer_id=dialog,
                attachment=','.join(att),
                random_id=get_random_id(),
                message=msgs,
            )
        else:
            vk.messages.send(
                peer_id=dialog,
                attachment=','.join(att),
                random_id=get_random_id(),
                message=msgs,
                reply_to=rep
            )


    def send_to_board(self, sms, too, mes_id):
        try:
            if board.antispam(self, too, 7):
                texts = sms.split(' ', 1)
                if len(texts) > 1:
                    self.konf, self.text = texts
                else:
                    self.konf = str(sms)
                    self.text = ''
                if self.konf.isdigit():
                    self.konf = int(self.konf) + 2000000000
                else:
                    self.konf = list_of_confs[self.konf] + 2000000000
                if board.check_boards_users(self, self.konf, too):
                    self.text = html.unescape(self.text)
                    raz, dvaz = board.quantity(self, self.konf)
                    sky = 'Аноним #' + str(raz) + ' №' + str(dvaz)
                    docs = vk.messages.getById(message_ids=mes_id)['items'][0]['attachments']
                    self.att = []
                    if len(docs) > 0:
                        for doc in docs:
                            type = doc['type']
                            self.str = '{}{}_{}'.format(type, doc[type]['owner_id'], doc[type]['id'])
                            if 'access_key' in doc[type]:
                                self.str += '_' + doc[type]['access_key']
                            self.att.append(self.str)
                        board.board_send(self.konf, '{}\n{}'.format(sky, self.text), self.att, board.otvet_board(self, mes_id))
                    elif self.text != '':
                        board.board_send(self.konf, '{}\n{}'.format(sky, self.text), self.att, board.otvet_board(self, mes_id))
                else:
                    send(too, 'У вас нет доступа к данному разделу.')
        except Exception as ex:
            if str(ex)[1 : -1] == self.konf and str(self.konf) == self.konf and self.konf.isdigit() == False:
                send(too, 'ti s nazvaniem obosralsa')
            else:
                send(too, 'error')


    def otvet_board(self, id):
        self.vava = vk.messages.getById(message_ids=id)['items']
        if ('fwd_messages' in self.vava[0]) and (len(self.vava[0]['fwd_messages'])) > 0 and ('conversation_message_id' in self.vava[0]['fwd_messages'][0]):
            return self.vava[0]['fwd_messages'][0]['id']
        else:
            return 0


    def check_boards_users(self, chat, user):
        self.chat = chat - 2000000000
        users = vk.messages.getChat(chat_id=self.chat)
        if user in users["users"]:
            return True
        else:
            return False


    def antispam(self, user, seconds):
        self.s = spam.get(user)
        if self.s == None:
            spam[user] = time.time()
            return True
        else:
            now = time.time()
            if now - self.s > seconds:
                spam[user] = time.time()
                return True
            else:
                return False
