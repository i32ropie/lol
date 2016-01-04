# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  twitch.py importado.{/cyan}'))

@bot.message_handler(commands=['lomos'])
def command_lomos(m):
    cid = m.chat.id
    uid = m.from_user.id
    if uid in [39680922,52033876]:
        txt = 'Cuentas que usaron el comando /tw:'
        for key in twitch_users:
            txt += '\n`' + twitch_users[key] + '`'
        bot.send_message( cid, txt, parse_mode="Markdown")
