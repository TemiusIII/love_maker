import telebot

from random import choice
from time import sleep

TOKEN = 'Your Token'
bot = telebot.TeleBot(TOKEN)

HEART = '🤍'
fill_hearts = ['💗', '💙', '💚', '💜']
COLORED_HEARTS = ['💗', '💓', '💖', '💘', '❤', '💞']
NUM_CYCLES = 20
NUM_CYCLES2 = 40

maps = ['''
000
000
000''',
        '''
        00000
        01010
        00100
        01010
        00000''',
        '''
        0000000
        0010100
        0111110
        0111110
        0011100
        0001000
        0000000''',
        '''
        000000000
        001101100
        012212210
        012323210
        012333210
        001232100
        000121000
        000010000
        000000000''']


def funny_print(text, chat_id, message_id, delay=0.05):
    for i in range(1, len(text) + 1):
        if text[i - 1] == ' ' or text[i - 1] == '\n':
            continue
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text[0:i])
        sleep(delay)


def usual_print(text, chat_id, message_id, delay=0.05):
    bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text)
    sleep(delay)


def love_maker(message):
    rep = bot.send_message(message.chat.id, "От @ml_loser, с любовью!")

    sleep(3)
    for i in range(len(maps)):
        cur_heart = fill_hearts[i]
        temp_map = maps[i]
        temp_map = temp_map.replace('0', HEART)
        temp_map = temp_map.replace('1', cur_heart)
        temp_map = temp_map.replace('2', cur_heart)
        temp_map = temp_map.replace('3', cur_heart)

        usual_print(chat_id=rep.chat.id, message_id=rep.message_id, text=temp_map, delay=0.5)

    for x in range(NUM_CYCLES):
        last_map = ''
        for i in range(len(maps[-1])):
            if maps[-1][i] == '0':
                last_map += HEART
            elif maps[-1][i] in '1 2 3'.split():
                last_map += choice(COLORED_HEARTS)
            else:
                last_map += maps[-1][i]

        bot.edit_message_text(chat_id=rep.chat.id, message_id=rep.message_id, text=last_map)
        sleep(0.2)

    for x in range(NUM_CYCLES2):
        last_map = ''
        for i in range(len(maps[-1])):
            if maps[-1][i].isdigit():
                if int(maps[-1][i]) == 0:
                    last_map += HEART
                elif int(maps[-1][i]) >= 1:
                    last_map += fill_hearts[(int(maps[-1][i]) + x) % 4]
            else:
                last_map += maps[-1][i]

        bot.edit_message_text(chat_id=rep.chat.id, message_id=rep.message_id, text=last_map)
        sleep(0.2)

    for i in range(len(maps) - 1, 0, -1):
        cur_heart = fill_hearts[i]
        temp_map = maps[i]
        temp_map = temp_map.replace('0', HEART)
        temp_map = temp_map.replace('1', cur_heart)
        temp_map = temp_map.replace('2', cur_heart)
        temp_map = temp_map.replace('3', cur_heart)

        usual_print(chat_id=rep.chat.id, message_id=rep.message_id, text=temp_map, delay=0.5)

    usual_print(chat_id=rep.chat.id, message_id=rep.message_id, text='💜')
    sleep(3)
    funny_print(chat_id=rep.chat.id, message_id=rep.message_id, text=f'i love you, {message.from_user.username}',
                delay=0.05)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    print(message)
    if message.text == '/start':
        bot.send_message(chat_id=message.chat.id,
                         text=f'Привет, сделал смешного бота, отправляющего сердечки\.\n'
                              f' ||Я очень старался|| \n\(Напиши что\-нибудь\)',
                         parse_mode='MarkdownV2')
    else:
        love_maker(message)


if __name__ == '__main__':
    bot.infinity_polling()
