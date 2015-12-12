# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  match.py importado.{/cyan}'))

@bot.message_handler( func=lambda message: message.text=="PARTIDA" or message.text=="MATCH" or message.text=="PARTITA" )
@bot.message_handler(commands=['match'])
def command_match(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['match_1'][lang(cid)]
        for region in ['euw','eune','br','na','las','lan','kr','tr','ru','oce']:
            txt += '\n/match_' + region + responses['match_3'][lang(cid)] + '*' + region.upper() + '*'
        txt += responses['match_2'][lang(cid)]
        bot.send_message(cid, txt, parse_mode="Markdown")
    else:
        bot.send_message( cid, responses['not_user'])
