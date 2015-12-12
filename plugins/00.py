# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  00.py importado.{/cyan}'))

@bot.message_handler(commands=['cancel'])
def command_cancel(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        if next_step_handler(cid) != 0:
            userStep[cid] = 0
            bot.send_message( cid, responses['cancel_1'][lang(cid)])
        else:
            bot.send_message( cid, responses['cancel_2'][lang(cid)])
    else:
        bot.send_message( cid, responses['not_user'])
