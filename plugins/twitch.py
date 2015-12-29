# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  twitch.py importado.{/cyan}'))

@bot.message_handler(commands=['tw'])
def command_twitch(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        if cid > 0:
            bot.send_message( cid, responses['twitch_1'][lang(cid)])
            userStep[cid] = 'twitch'
        else:
            bot.send_message( cid, responses['twitch_2'][lang(cid)])
    else:
        bot.send_message( cid, responses['not_user'])
