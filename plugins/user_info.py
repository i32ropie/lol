# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  user_info.py importado.{/cyan}'))


@bot.message_handler(commands=['user_info'])
def command_user_info(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_message(cid, user_info(cid), parse_mode="Markdown")
    else:
        bot.send_message(cid, responses['not_user'])
