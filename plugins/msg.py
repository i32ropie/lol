# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  msg.py importado.{/cyan}'))

@bot.message_handler(commands=['msg'])
def command_msg(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_message( cid, responses['msg'][0]['success'], reply_markup=types.ForceReply() )
        userStep[cid] = 'msg_1'
