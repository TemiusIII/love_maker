import telebot

from random import choice
from time import sleep

TOKEN = 'YOUR TOKEN'
bot = telebot.TeleBot(TOKEN)

HEART = 'π€'
fill_hearts = ['π', 'π', 'π', 'π']
COLORED_HEARTS = ['π', 'π', 'π', 'π', 'β€', 'π']
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
    rep = bot.send_message(message.chat.id, "ΠΡ @ml_loser, Ρ Π»ΡΠ±ΠΎΠ²ΡΡ!")

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

    usual_print(chat_id=rep.chat.id, message_id=rep.message_id, text='π')
    sleep(3)

    if message.from_user.username == 'l1lcutie':
        funny_print(chat_id=rep.chat.id, message_id=rep.message_id, text=f'Π― ΠΎΡΠ΅Π½Ρ ΡΠ°Π΄, ΡΡΠΎ ΠΌΡ ΠΎΠ±ΡΠ°Π΅ΠΌΡΡ Ρ ΡΠΎΠ±ΠΎΠΉ. ΠΠ°Π΄Π΅ΡΡΡ, ΡΡΠΎ Ρ ΡΠ΅Π±Ρ Π²ΡΠ΅ Π±ΡΠ΄Π΅Ρ ΡΠΎΡΠΎΡΠΎ. Π’Ρ Π½Π΅ Π±ΡΠ΄Π΅ΡΡ Π·Π°Π³ΠΎΠ½ΡΡΡΡΡ ΠΏΠΎ ΡΡΠΉΠ½Π΅ ΠΈ Π±ΡΠ΄Π΅ΡΡ ΡΠ°Π΄ΠΎΠ²Π°ΡΡΡΡ ΠΆΠΈΠ·Π½ΠΈ. Π₯ΠΎΡΡ Π²Π΅ΡΠΈΡΡ, ΡΡΠΎ ΠΌΡ Π±ΡΠ΄Π΅ΠΌ Π΄ΡΡΠΆΠΈΡΡ ΠΈ ΠΎΠ±ΡΠ°ΡΡΡΡ ΠΎΡΠ΅Π½Ρ ΠΎΡΠ΅Π½Ρ ΠΎΡΠ΅Π½Ρ Π΄ΠΎΠ»Π³ΠΎ. πππ',
                    delay=0.05)
    else:
        funny_print(chat_id=rep.chat.id, message_id=rep.message_id, text=f'i love you, {message.from_user.username}', delay=0.05)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # ΠΠ°Π·Π²Π°Π½ΠΈΠ΅ ΡΡΠ½ΠΊΡΠΈΠΈ Π½Π΅ ΠΈΠ³ΡΠ°Π΅Ρ Π½ΠΈΠΊΠ°ΠΊΠΎΠΉ ΡΠΎΠ»ΠΈ
    print(message)
    if message.text == '/start':
        bot.send_message(chat_id=message.chat.id,
                         text=f'ΠΡΠΈΠ²Π΅Ρ, ΡΠ΄Π΅Π»Π°Π» ΡΠΌΠ΅Π½ΡΠ½ΠΎΠ³ΠΎ Π±ΠΎΡΠ°, ΠΎΡΠΏΡΠ°Π²Π»ΡΡΡΠ΅Π³ΠΎ ΡΠ΅ΡΠ΄Π΅ΡΠΊΠΈ\.\n ||Π― ΠΎΡΠ΅Π½Ρ ΡΡΠ°ΡΠ°Π»ΡΡ|| \n\(ΠΠ°ΠΏΠΈΡΠΈ ΡΡΠΎ\-Π½ΠΈΠ±ΡΠ΄Ρ\)', parse_mode='MarkdownV2')
    else:
        if message.from_user.username == 'l1lcutie':
            bot.send_message(chat_id=message.chat.id, text=f'Π­ΡΠΎ Π΄Π»Ρ ΡΠ΅Π±Ρ, ΠΠ΅Π½Π΅ΡΠΊΠ°. Π’Ρ Π»ΡΡΡΠ΅ Π²ΡΠ΅Ρ!!!')
        else:
            love_maker(message)


if __name__ == '__main__':
    bot.infinity_polling()
