from alld.generaldirectory.priority.overall import *

vk_session = vk_api.VkApi(
    token='')

vk = vk_session.get_api()
upload = VkUpload(vk_session)
session = requests.Session()

longpoll = VkLongPoll(vk_session)




def send_image_b(kuda, msgs, foto):
    photo = upload.photo_messages(photos=foto)[0]
    attachments = ['photo{}_{}'.format(photo['owner_id'], photo['id'])]
    vk.messages.send(
        peer_id=kuda,
        attachment=','.join(attachments),
        random_id=get_random_id(),
        message=msgs
    )
    return '{}_{}_{}'.format(photo['owner_id'], photo['id'], photo['access_key'])



def nickname_f(id_avt):
    try:
        try:
            gets = vk.users.get(user_ids=id_avt, lang=0)[0]
            return '{} {}'.format(gets['first_name'], gets['last_name'])
        except:
            gets = vk.groups.getById(group_id=id_avt, lang=0)[0]
            return gets['name']
    except:
        return 'username'


def shuffle(dialog, msgs):
    global hi
    if hi < len(msgs):
        vk.messages.send(
            peer_id=dialog,
            random_id=get_random_id(),
            message=msgs[hi],
        )
        hi += 1
    else:
        hi = 0
        vk.messages.send(
            peer_id=dialog,
            random_id=get_random_id(),
            message=msgs[hi],
        )
        hi += 1


def shuffle_reply(dialog, msgs):
    vk.messages.send(
        peer_id=dialog,
        random_id=get_random_id(),
        message=random.choice(msgs),
    )


def send(dialog, msgs):
    vk.messages.send(
        peer_id=dialog,
        random_id=get_random_id(),
        message=msgs,
    )


def send_forward(dialog, msgs, fwrd):
    vk.messages.send(
        peer_id=dialog,
        random_id=get_random_id(),
        message=msgs,
        forward_messages=fwrd,
    )


def send_reply(dialog, msgs, kuda):
    vk.messages.send(
        peer_id=dialog,
        random_id=get_random_id(),
        message=msgs,
        reply_to=kuda
    )


def text_image(dialog, msgs, foto):
    attachments = []
    image_url = foto
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append(
        'photo{}_{}'.format(photo['owner_id'], photo['id'])
    )
    vk.messages.send(
        peer_id=dialog,
        attachment=','.join(attachments),
        random_id=get_random_id(),
        message=msgs
    )


def send_image(dialog, url, msgs):
    attachments = []
    image_url = url
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append(
        'photo{}_{}'.format(photo['owner_id'], photo['id'])
    )
    vk.messages.send(
        peer_id=dialog,
        attachment=','.join(attachments),
        random_id=get_random_id(),
        message=msgs
    )


def send_doc(dialog, msgs, title, doc):
    attachments = []
    docs = upload.document_message(doc=doc, title=title, peer_id=dialog)['doc']
    attachments.append(
        'doc{}_{}'.format(docs['owner_id'], docs['id'])
    )
    vk.messages.send(
        peer_id=dialog,
        attachment=','.join(attachments),
        random_id=get_random_id(),
        message=msgs
    )


def send_v(dialog, url, msgs):
    attachments = []
    attachments.append(
        'video{}_{}_{}'.format(url['owner_id'], url['video_id'], url['access_key'])
    )
    vk.messages.send(
        peer_id=dialog,
        attachment=','.join(attachments),
        random_id=get_random_id(),
        message=msgs
    )

