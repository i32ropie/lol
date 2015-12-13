# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  admin.py importado.{/cyan}'))

@bot.message_handler(commands=['all'])
def command_all(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        txt = """
Comandos de administración

/all - Difundido a TODOS
/all\_es _[mensaje]_ - Difundido a chats españoles
/all\_en _[mensaje]_- Difundido a chats *NO* españoles
/ban _[id]_ - Banea un ID
/unban _[id]_ - Desbanea un ID
/mute - No responder a baneados
/unmute - Responder a baneados
"""
