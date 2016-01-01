# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  start.py importado.{/cyan}'))

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add('ESPAÑOL','ENGLISH','ITALIANO','POLSKI','DEUTSCH','FRANÇAIS','PORTUGUÊS','PERSIAN')

@bot.message_handler(commands=['start'], func=lambda msg: next_step_handler(0) == 0)
def command_start(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to( m, responses['banned'])
        return None
    if not is_user(cid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['start_1']%m.from_user.first_name, reply_markup=markup)
        userStep[cid] = 'start'
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['start_already_user'][lang(cid)])
