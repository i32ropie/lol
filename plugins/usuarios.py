# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  stats.py importado.{/cyan}'))

@bot.message_handler(commands=['stats'])
def command_usuarios(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        x = [0,0,0,0]
        y = [0,0,0,0]
        for uid in users:
            if int(uid) > 0:
                x[0] += 1
                if lang(uid) == 'es':
                    x[1] += 1
                elif lang(uid) == 'en':
                    x[2] += 1
                elif lang(uid) == 'it':
                    x[3] += 1
            else:
                y[0] += 1
                if lang(uid) == 'es':
                    y[1] += 1
                elif lang(uid) == 'en':
                    y[2] += 1
                elif lang(uid) == 'it':
                    y[3] += 1
        txt = "*Usuarios*: " + str(x[0]) + "\n *-*Español: _" + str(x[1]) + "_\n *-*Inglés: _" \
        + str(x[2]) + "_\n *-*Italiano: _" + str(x[3]) + "*Grupos*: " + str(y[0]) + \
        "\n *-*Español: _" + str(y[1]) + "_\n *-*Inglés: _" + str(y[2]) + "_\n *-*Italiano: _" + str(y[3])
        bot.send_message( cid, txt, parse_mode="Markdown")
