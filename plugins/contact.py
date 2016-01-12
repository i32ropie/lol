# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  contact.py importado.{/cyan}'))


@bot.message_handler(func=lambda message: message.text in [
                     'CONTATO', 'CONTACTO', 'CONTACT', 'CONTATTO', 'KONTAKT'])
@bot.message_handler(commands=['contact'])
def command_contact(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['contact_1'][lang(cid)])
        userStep[cid] = 'contact'
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
