# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  00.py importado.{/cyan}'))


@bot.message_handler(commands=['cancel'])
def command_cancel(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('cancel')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_banned(uid) or is_banned(cid):
        if not extra['muted']:
            bot.send_chat_action(cid, 'typing')
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        if next_step_handler(cid) != 0:
            userStep[cid] = 0
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['cancel_1'][
                    lang(cid)], reply_markup=types.ReplyKeyboardRemove(selective=False))
        else:
            bot.send_chat_action(cid, 'typing')
            bot.send_message(
                cid, responses['cancel_2'][
                    lang(cid)], reply_markup=types.ReplyKeyboardRemove(selective=False))
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
