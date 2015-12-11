# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  info.py importado.{/cyan}'))

@bot.message_handler( func=lambda message: message.text=="INFO")
@bot.message_handler(commands=['info'])
def command_info(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_message( cid, responses['info'][lang(cid)])
    else:
        bot.send_message( cid, responses['not_user'])
