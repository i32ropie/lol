# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  about.py importado.{/cyan}'))

@bot.message_handler( func=lambda message: message.text=="CRÉDITOS" or message.text=="CREDITS" or message.text=="CREDITI")
@bot.message_handler(commands=['credits'])
def command_credits(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['about'][lang(cid)], parse_mode="Markdown")
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['not_user'])
