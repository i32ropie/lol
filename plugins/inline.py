# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  inline.py importado.{/cyan}'))


@bot.message_handler(commands=['inline'])
def command_COMANDO(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('inline')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_banned(uid):
        if not extra['muted']:
            bot.reply_to(m, responses['banned'])
        return None
    if is_user(cid):
        txt = responses['inline_help_1'][lang(cid)]
        for x, y in responses['inline_help_2'][lang(cid)].items():
            txt += '\n`@LoL_bot ' + x + y
        bot.send_message(cid, txt, parse_mode="Markdown")
    else:
        bot.send_message(cid, responses['not_user'])
