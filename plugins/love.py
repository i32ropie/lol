# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  love.py importado.{/cyan}'))


@bot.message_handler(commands=['love'])
def command_COMANDO(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('love')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        txt = "Vir: 5€ <3\nAlbert: 0.10€ <3\nMario: 0.01€ <3"
        bot.send_message(cid, txt)
    else:
        bot.send_message(cid, responses['not_user'])
