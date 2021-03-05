# -*- coding: utf-8 -*-

from config import *

print(Color(
    '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}  reload.py importado.{/cyan}'))


@bot.message_handler(commands=['reload'])
def command_reload(m):
    cid = m.chat.id
    uid = m.from_user.id
    try:
        send_udp('reload')
    except Exception as e:
        bot.send_message(52033876, send_exception(e), parse_mode="Markdown")
    if not is_recent(m):
        return None
    if is_admin(uid):
        bot.send_chat_action(cid, 'typing')
        bot.send_message(cid, responses['reload'], parse_mode="Markdown")
        print(Color(
            '{autored}[{/red}{autoyellow}+{/yellow}{autored}]{/red} {autocyan}Reiniciando @LoL_bot{/cyan}'))
        restart_process()
