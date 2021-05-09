# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  updates.py importado.{/cyan}'))


@bot.message_handler(commands=['updates'])
def command_updates(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_message(cid, responses['updates'])
    else:
        bot.send_message(cid, responses['not_user'])
