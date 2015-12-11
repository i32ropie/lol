# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  ping.py importado.{/cyan}'))

@bot.message_handler(commands=['ping'])
def command_COMANDO(m):
    cid = m.chat.id
    uid = m.chat.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.reply_to( m, "pong")
