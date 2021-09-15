from alld.FALSEorUNCOMPLETED.chains import markov_chain
from alld.generaldirectory.other import *


def get_text_ch(id):
    vava = vk.messages.getById(message_ids=id)['items']
    text = ''
    if 'reply_message' in vava[0]:
        text = vava[0]['reply_message']['text']
    elif 'fwd_messages' in vava[0]:
        if len(vava[0]['fwd_messages']) > 1:
            for element in vava[0]['fwd_messages']:
                if 'text' in element:
                    text = text + '\n' + element['text']
            text = text[2:]
        else:
            text = vava[0]['fwd_messages'][0]['text']


def mark_ch(max, c):
    if max > 1500:
        max = 1499
    mc = markov_chain.MarkovChain()
    mc.parse_and_add(c)
    return mc.generate_sentence(max)

def general(to, max, id):
    try:
        send(to, mark_ch(max, get_text_ch(id)))
    except:
        pass



def gauss_gun(sms, too):
    try:
        sms_list = sms.splitlines()
        m_a = []
        m1 = []
        del sms_list[0]
        for i in range(len(sms_list) - 1):
            m_p = sms_list[i].split()
            for j in range(len(m_p)):
                m1.append(int(m_p[j]))
            m_a.append(m1)
            m1 = []
        m_b = [int(x) for x in sms_list[len(sms_list) - 1].split()]
        ggg = Gauss(m_a, m_b)
        ggg.close()
        send_doc(too, 'gotovo', 'gusse', 'gauss.txvt')
    except:
        send(too, 'error')


def FancyPrint(A, B, selected):
    strok = '('
    strok1 = ''
    strok2 = ''
    for row in range(len(B)):
        strok1 += '('
        for col in range(len(A[row])):
            strok1 += "\t{1:10.2f}{0}".format(" " if (selected is None or selected != (row, col)) else "*", A[row][col])
        strok1 += "\t) * (\tX{0}) = (\t{1:10.2f})".format(row + 1, B[row]) + '\n'
    return strok1+strok2


def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]


def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider


def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight



def Gauss(A, B):
    senstr = ''
    column = 0
    f_g = open('gauss.txt', 'w+')
    while (column < len(B)):

        senstr += "Обрабатываем {0}-й столбец:".format(column + 1) + '\n'
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                current_row = r
        if current_row is None:
            senstr = "решений нет"
            f_g.write(senstr)
            return f_g
        senstr += FancyPrint(A, B, (current_row, column))

        if current_row != column:
            senstr += "Переставляем строку с найденным элементом повыше:" + '\n'
            SwapRows(A, B, current_row, column)
            senstr += FancyPrint(A, B, (column, column))

        senstr += "Доводим до единички:" + '\n'
        DivideRow(A, B, column, A[column][column])
        senstr += FancyPrint(A, B, (column, column))

        senstr += "Обнуляем строки ниже:" + '\n'
        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])
        senstr += FancyPrint(A, B, (column, column))

        column += 1

    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))

    senstr += "Ответ:" + '\n'
    senstr += "\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in enumerate(X))

    f_g.write(senstr)

    return f_g

