# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  name.py importado.{/cyan}'))


@bot.message_handler(commands=['set_name'])
def command_set_name(m):
    cid = m.chat.id
    uid = m.from_user.id
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid) and is_beta(uid):
        if cid > 0:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['name_1'][
                    lang(cid)], reply_markup=markup)
            userStep[cid] = 'name'
        else:
            bot.send_message(cid, responses['private'][lang(cid)])
    else:
        bot.send_message(cid, responses['not_user'])
