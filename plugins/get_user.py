# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  get_user.py importado.{/cyan}'))


@bot.message_handler(commands=['get_user'], func=lambda m: m.text and len(m.text.split()) == 2)
def command_get_user_info(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('get_user')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_admin(uid):
        try:
            bot.send_message(cid, user_info(m.text.split()[1], lang(cid)), parse_mode="Markdown")
        except:
            pass