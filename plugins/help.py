# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  help.py importado.{/cyan}'))


@bot.message_handler(
    func=lambda m: m.content_type == 'text' and m.text in [
        'AJUDA',
        'ПОМОЩЬ',
        'POMOC',
        'AYUDA',
        'HELP',
        'AIUTO',
        'HILFE',
        'AIDE',
        'YARDIM'])
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('help')
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
        txt = responses['help_1'][lang(cid)]
        for a, b in responses['help_2'][lang(cid)].items():
            txt += '\n/' + a + ': ' + b
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, txt)
    else:
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['not_user'])
