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
        txt = "Vir: 5€ ❤️\nDavid (Cocho): 1€ ❤️\nMaclek: 0.69€ ❤️\nAlbert: 0.10€ ❤️\nPablo: 0.10€ ❤️\nTicho: 0.10€ ❤️\nMario (Abumatas): 0.01€ ❤️"
        bot.send_message(cid, txt)
    else:
        bot.send_message(cid, responses['not_user'])
