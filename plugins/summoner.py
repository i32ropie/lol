# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  summoner.py importado.{/cyan}'))

@bot.message_handler( func=lambda message: message.text=="INVOCADOR" or message.text=="SUMMONER" or message.text=="EVOCATORE" )
@bot.message_handler(commands=['summoner'])
def command_summoner(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['summoner_1'][lang(cid)]
        for region in ['euw','eune','br','na','las','lan','kr','tr','ru','oce']:
            txt += '\n/' + region + responses['summoner_3'][lang(cid)] + '*' + region.upper() + '*'
        txt += '\n' + responses['summoner_2'][lang(cid)]
        bot.send_message(cid, txt, parse_mode="Markdown")
    else:
        bot.send_message( cid, responses['not_user'])


@bot.message_handler( func=lambda message: message.text.lstrip('/').split(' ')[0].split('@')[0] in ['euw','eune','br','na','las','lan','kr','tr','ru','oce'] )
def region(m):
    cid = m.chat.id
    uid = m.from_user.id
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        invocador = ' '.join(m.text.split(' ')[1:])
        if not invocador:
            bot.send_message( cid, responses['no_summoner'][lang(cid)])
        
    else:
        bot.send_message( cid, responses['not_user'])







def region(txt):
    command = txt.lstrip('/')
