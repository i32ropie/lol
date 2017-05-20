# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  leave_channel.py importado.{/cyan}'))

@bot.channel_post_handler(func=lambda m: True)
def leave_channel(m):
    cid = m.chat.id
    username = m.chat.username
    bot.leave_chat(cid)
    bot.send_message(52033876, "Bot eliminado de un canal\n\nID: {}\nAlias: @{}".format(cid, username))
