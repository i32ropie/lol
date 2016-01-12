# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  region.py importado.{/cyan}'))

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.add('EUW', 'EUNE', 'BR', 'NA', 'LAS', 'LAN', 'KR', 'TR', 'RU', 'OCE')


@bot.message_handler(commands=['set_region'])
def command_set_region(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid) and is_beta(uid):
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['region_1'][
                    lang(cid)], reply_markup=markup)
            userStep[cid] = 'region'
        else:
            bot.send_message(cid, responses['private'][lang(cid)])
    else:
        bot.send_message(cid, responses['not_user'])
