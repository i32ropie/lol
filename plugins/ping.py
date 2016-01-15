# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  ping.py importado.{/cyan}'))


@bot.message_handler(commands=['ping'])
def command_COMANDO(m):
    cid = m.chat.id
    uid = m.from_user.id
    botan.track(
        botan_token,
        cid,
        json.dumps(to_json(m)),
        "/ping"
    )
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_chat_action(cid, 'typing')
        bot.reply_to(m, "pong")
