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
    aux = dict()
    with open('extra_data/patch_es.txt', 'rt') as f:
        aux['es'] = f.read()
    with open('extra_data/patch_en.txt', 'rt') as f:
        aux['en'] = f.read()
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to( m, responses['banned'])
        return None
    if is_user(cid):
        bot.send_message( cid, aux[lang(cid)])
    else:
        bot.send_message( cid, responses['not_user'])
