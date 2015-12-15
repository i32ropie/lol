# -*- coding: utf-8 -*-

from config import *

print(Color('{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  patch.py importado.{/cyan}'))

@bot.message_handler( content_types=['text'], func=lambda message: message.text=="PARCHE" or message.text=="PATCH")
@bot.message_handler(commands=['patch'])
def command_patch(m):
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
        with open('extra_data/patch_' + lang(cid) + '.txt', 'rt') as f:
            patch = f.read()
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, patch)
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, responses['not_user'])

@bot.message_handler(commands=['patch_es','patch_en','patch_it','patch_pl'])
def command_update_patch(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message( cid, "Envía el texto para actualizar *patch_" + m.text.split('_')[1] + ".txt* o escribe /cancel", parse_mode="Markdown")
        userStep[cid] = 'patch_' + m.text.split('_')[1]
