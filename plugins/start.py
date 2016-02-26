# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  start.py importado.{/cyan}'))

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add(
    'ESPAÑOL',
    'ENGLISH',
    'ITALIANO',
    'POLSKI',
    'DEUTSCH',
    'FRANÇAIS',
    'PORTUGUÊS',
    'РУССКИЙ',
    # 'ไทย',
    # 'ΕΛΛΗΝΙΚΆ',
    'PERSIAN')


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if not is_user(cid):
        try:
            botan.track(
                botan_token,
                cid,
                to_json(m),
                "/start"
            )
        except:
            pass
        bot.send_chat_action(cid, 'typing')
        bot.send_message(
            cid,
            responses['start_1'] %
            m.from_user.first_name,
            reply_markup=markup)
        userStep[cid] = 'start'
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['start_already_user'][lang(cid)])
