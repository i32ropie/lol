# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  usuarios.py importado.{/cyan}'))

@bot.message_handler(commands=['usuarios'])
def command_usuarios(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_admin(uid):
        x = 0
        y = 0
        for uid in users:
            if int(uid) > 0:
                x += 1
            else:
                y += 1
        bot.send_message( cid, '*>*Users: _%s_\n*>*Groups: _%s_' %(x,y), parse_mode="Markdown")
