# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  love.py importado.{/cyan}'))


@bot.message_handler(commands=['love'])
def command_inline(m):
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
        txt = "@ManesHome (by @ilmanes): 15€\n@GoRhY: 11.11€ ❤️❤️\nNicolas: 10€ ❤️\nLuvo: 5€ ❤️\nVir: 5€ ❤️\nDiego: 5€ ❤️\nA-man: 5$ ❤️\n@Webrom: 3€ ❤️\nMiri (pelirosa): 2.50€ ❤️\nMaldo Manco: 1€ ❤️\n@Principebot: 1€ ❤️\nDavid (Cocho): 1€ ❤️\nAlbertisiu: 1€ ❤️\nMaciek: 0.69€ ❤️\nZimoon: 0.50€ ❤️\nFrederik: 0.30€ ❤️\nFausto: 0.11€ ❤️\nAlbert: 0.10€ ❤️\nPablo: 0.10€ ❤️\nTicho: 0.10€ ❤️\nMichael (flame): 0.03€ ❤️\n@PilaricaBot: 0.02€ ❤️\nMario (Abumatas): 0.01€ ❤️"
        bot.send_message(cid, txt)
    else:
        bot.send_message(cid, responses['not_user'])
