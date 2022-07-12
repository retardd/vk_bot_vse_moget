# vk bot - Руководство пользователя

# Преамбула

Код урезанный, только основные реализации.

Захостил на хероку, присутствует ненормативная лексика (18+).

Затестить можно здесь - https://vk.com/visocke

Подключена БД Postgersql, но ничего особенного (vk_bot_vse_moget/alld/generaldirectory/databasedefs.py).

Есть API vk и telegram.

ОСНОВНЫЕ ФУНКЦИИ (далеко не все):

# Генератор цитат

/citgen or /cg — генерирование цитаты по пересланному(-ым)/отвеченному сообщению:

![image](https://user-images.githubusercontent.com/53952373/178583068-8361f410-b47c-4973-8ea9-a16735a0c3ae.png)

# Борда (такого нигде нет)

Перед использованием необходимо зарегистрировать конфу:

![image](https://user-images.githubusercontent.com/53952373/178583881-8ef110bd-699c-479f-ab78-d12f2c426425.png)

Узнать название и айди беседы: /bord

![image](https://user-images.githubusercontent.com/53952373/178583919-9625dc3e-ede4-4281-954e-74714cd0d7e0.png)

//*id* text + attachments, где вместо *id* название раздела (указываемое в /bord) или его айди.
Вложения можно любые, для ответа необходимо вместе с командой переслать сообщение из конфы, на которое необходимо овтетить.

вместо двух слешей можно б/ или b/

![image](https://user-images.githubusercontent.com/53952373/178583955-03db74d0-b072-4135-b5ef-b1f6a3306483.png)

![image](https://user-images.githubusercontent.com/53952373/178583985-88a666e0-e64c-472b-86e3-d6f94c6d6576.png)

/rename (для админов или регистратора) — сменить название

# flibusta downloader

/fp *название книги* — для поиска книг

![image](https://user-images.githubusercontent.com/53952373/178584326-18a8131f-3123-4ed7-a60d-d40b4301f918.png)

Если количество книг или серий превышает 10, то для просмотра дальнейших результатов надо листать список через команды /fn (вперед) и /fb (назад).

Раскрыть серию — /fs *номер серии, указанный в сообщении в САМОМ НАЧАЛЕ* — так же этой командой можно и свернуть обратно список серии и вернуться к странице поиска
(пока доступно скачивание только fb2 форматов)

![image](https://user-images.githubusercontent.com/53952373/178584420-b3eff122-9886-480b-ac3e-6c2d4b060f21.png)

/ff *номер книги* — чтобы скачать книгу. Номер книги также указан в самом начале строки, — перед названием и прочим, — для скачивания книги ИЗ серии необходимо писать ту же хуйню, что и написано в раскрытом спике серии — то есть со слешом, например:

![image](https://user-images.githubusercontent.com/53952373/178584474-d4227955-736a-47cb-a4ee-5be99ecbce7c.png)

Увы, флибуста сама по себе медлительная вещь и задержками при скачивании и ужасным поиском — поэтому наберитесь терпения (среднее время скачивания книги 11 секунд, а поиска от 1 до 15) и главное делайте правильный и четкий запрос

![image](https://user-images.githubusercontent.com/53952373/178584533-8c1c3b43-481a-4261-aba1-7453e0455e35.png)

# Закладки

new/name name — создать закладку с названием name name. Либо по отвеченному сообщению, если таковое имеется, либо же по сообщению с командой. Так же выдается уникальный номер.

seeall/ — узреть все закладки с номерами и авторами.

see/1 — показать закладку с номером 1.

del/1 — удалить закладку с номером 1. Только для автора закладки.