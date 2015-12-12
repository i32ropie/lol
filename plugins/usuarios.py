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
        normal_chat, group_chat, es, en, it = 0, 0, 0, 0, 0
        for uid in users:
            if int(uid) > 0:
                normal_chat += 1
            else:
                group_chat += 1
            if lang(uid) == 'es':
                es += 1
            elif lang(uid) == 'en':
                en += 1
            elif lang(uid) == 'it':
                it += 1
        bot.send_message( cid, '*>*Usuarios: _%s_\n*>*Grupos: _%s_\n*>*Español: _%s_\n*>*Inglés: _%s_\n*>*Italiano: _%s_' %(normal_chat, group_chat, es, en, it), parse_mode="Markdown")
