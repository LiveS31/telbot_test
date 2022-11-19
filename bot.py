#code bot

#from typing import Any
import telebot


fca = telebot.TeleBot('5731589447:AAHxW5k2j5xHVy2jY2NAzVfHIRCgmtU_q90')

@fca.message_handler(commands= ['start', 'help'])
def start(message):

    user = f'<b>{message.from_user.first_name}</b>'
    info = '! Вставляем ключ в замок зажигания и делаем три поворота ключа "туда- обрано" до положения включения приборной панели. На третий раз оставляем в положениие и переписываем ошибки '

    fca.send_message(message.chat.id, user+ info, parse_mode= 'html')
    fca.send_message(message.chat.id, "вводить код: P0101")
    print("Пользователь:", message.from_user.first_name + ".")
    print("Сообщение пользователя:", message.text)


@fca.message_handler(content_types = ['text'])
def code(message):

    user_answer = 'НЕТ ТАКОЙ ОШИБКИ!!!'

    print("Пользователь:", message.from_user.first_name)
    print("Сообщение пользователя:", message.text)
    code = (message.text).upper()
    if code in errors:
        fca.send_message(message.chat.id, errors[(message.text).upper()])
    else:
        fca.send_message(message.chat.id,user_answer, parse_mode = 'html')
    #print ("Сообщенеие пользоватеerrors[message.text])
    fca.send_message(message.chat.id, 'введите ошибку:')
    #print (message)

fca.polling(none_stop = True)
