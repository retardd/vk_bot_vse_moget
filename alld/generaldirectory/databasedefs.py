from alld.generaldirectory.priority.mainvkcfg import *

def connect():
    try:
        DATABASE_URL = "postgres://mkvturrykbcvjx:1361c442dc89646c7327e5290c814986be0d38b7389d65e45b865ee011be966e@ec2-3-229-210-93.compute-1.amazonaws.com:5432/d95q82opf7m4mb"
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
    except:
        print('nea')
    return cur, conn


#MUZIKA
def music_un(dialog):
    number = random.randint(1, 3750)
    id = linecache.getline('content/spsk.txt', number)
    attachments = []
    audio = {'owner_id': admin, 'media_id': int(id)}
    attachments.append(
        'audio{}_{}'.format(audio['owner_id'], audio['media_id'])
    )
    vk.messages.send(
        peer_id=dialog,
        attachment=','.join(attachments),
        random_id=get_random_id(),
        message=''
    )


#ZAKLADKI
def tabl(kon):
    cur, conn = connect()
    cur.execute('CREATE TABLE Z%s (id INT PRIMARY KEY, name TEXT, mesid INT, author INT)', [kon])
    conn.commit()
    conn.close()


def new(dialog, konf, name, mesid, author):
    id = posl(konf)
    try:
        cur, conn = connect()
        cur.execute('INSERT INTO Z%s (id, name, mesid, author) VALUES(%s, %s, %s, %s)',
                    (konf, id, name, mesid, author))
        conn.commit()
        conn.close()
        send(dialog, random.choice(sozd))
    except psycopg2.errors.UndefinedTable:
        send(dialog, random.choice(tabli))
        tabl(konf)
        new(konf, name, mesid, author)
        send(dialog, random.choice(sozd))


def vern(dialog, kon, id):
    cur, conn = connect()
    cur.execute('SELECT * from Z%s where id = %s', [kon, id])
    rows = cur.fetchall()
    try:
        send_reply(dialog, rows[0][1], rows[0][2])
    except:
        send(dialog, random.choice(vse))
    conn.commit()
    conn.close()


def posl(kon):
    try:
        cur, conn = connect()
        cur.execute('SELECT id from Z%s', [kon])
        row = cur.fetchone()
        row2 = 1
        while row:
            row2 = int(row[0]) + 1
            row = cur.fetchone()
        conn.commit()
        conn.close()
        return row2
    except psycopg2.errors.UndefinedTable:
        row2 = 1
        return row2


def vernall(dialog, kon, q):
    send(dialog, 'secundochku')
    sis = 'the conference markers:' + '\n' + '\n'
    cur, conn = connect()
    cur.execute('SELECT * from Z%s', [kon])
    rows = cur.fetchall()
    for row in rows:
        sis += str(row[0]) + ': ' + str(row[1]) + '\n' + 'author: ' + nickname_f(row[3]) + '\n'
    if sis == 'the conference markers:' + '\n' + '\n' + ': ' + '\n' + 'author: ' + '\n':
        sis = 'null'
    conn.commit()
    conn.close()
    return q.put(sis)


def sendall(to_zak, chat_id, q1):
    tt2 = Thread(target=vernall, args=[to_zak, chat_id, q1])
    tt2.start()
    result = q1.get()
    send(to_zak, result)


def delete(dialog, konfa, id, author):
    try:
        cur, conn = connect()
        cur.execute('SELECT author FROM Z%s WHERE id = %s', [konfa, id])
        rows = cur.fetchall()
        if author == rows[0][0]:
            cur.execute('DELETE FROM Z%s WHERE id = %s', [konfa, id])
            send(dialog, random.choice(ydalil))
        else:
            send(dialog, random.choice(author2))
        conn.commit()
        conn.close()
    except:
        send(dialog, random.choice(vse))


# STATISTIKA
def set_stat(id):
    cur, conn = connect()
    cur.execute('SELECT info from statistic where id = %s', [id])
    rows = cur.fetchall()
    new = int(rows[0][0]) + 1
    cur.execute('UPDATE statistic set info = %s where id = %s', [new, id])
    conn.commit()
    conn.close()


def see_stat(kuda):
    cur, conn = connect()
    cur.execute('SELECT * from statistic')
    rows = cur.fetchall()
    if rows[0][0] == 1:
        send(kuda, 'created citgens: ' + str(rows[0][1]) + '\n' + 'sent messages: ' + str(rows[1][1])+ '\n' + 'counting from 30.05')
    else:
        send(kuda, 'created citgens: ' + str(rows[1][1]) + '\n' + 'sent messages: ' + str(rows[0][1]) + '\n' + 'counting from 30.05')
    conn.commit()
    conn.close()
