# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  help.py importado.{/cyan}'))

@bot.message_handler( func=lambda message: message.text=="AYUDA" or message.text=="HELP" or message.text=="AIUTO")
@bot.message_handler( commands=['help'] )
def command_help(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['help_1'][lang(cid)]
        for a,b in responses['help_2'][lang(cid)].items():
            txt += '\n/' + a + ': ' + b
        bot.send_message( cid, txt)
    else:
        bot.send_message( cid, responses['not_user'])
